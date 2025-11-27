#!/usr/bin/env python3
"""
Script principal para o Hub Financeiro
Lê dados de transações financeiras e exibe o extrato inteligente
"""

import json
import os
from typing import List, Dict, Any


def carregar_extrato(caminho_arquivo: str) -> List[Dict[str, Any]]:
    """
    Carrega os dados do extrato a partir de um arquivo JSON
    
    Args:
        caminho_arquivo: Caminho para o arquivo JSON
        
    Returns:
        Lista de transações financeiras
    """
    try:
        with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        print(f"Erro: Arquivo não encontrado - {caminho_arquivo}")
        return []
    except json.JSONDecodeError:
        print(f"Erro: Arquivo JSON inválido - {caminho_arquivo}")
        return []


def calcular_saldo(transacoes: List[Dict[str, Any]]) -> Dict[str, float]:
    """
    Calcula o saldo total e os totais de entradas e saídas
    
    Args:
        transacoes: Lista de transações financeiras
        
    Returns:
        Dicionário com total de entradas, saídas e saldo
    """
    total_entradas = 0.0
    total_saidas = 0.0
    
    for transacao in transacoes:
        valor = transacao.get('valor', 0.0)
        tipo = transacao.get('tipo', '').lower()
        
        if tipo == 'entrada':
            total_entradas += valor
        elif tipo == 'saida':
            total_saidas += valor
    
    saldo = total_entradas - total_saidas
    
    return {
        'entradas': total_entradas,
        'saidas': total_saidas,
        'saldo': saldo
    }


def formatar_valor(valor: float) -> str:
    """
    Formata um valor monetário para exibição
    
    Args:
        valor: Valor a ser formatado
        
    Returns:
        String formatada com o valor
    """
    return f"R$ {valor:,.2f}".replace(',', '_').replace('.', ',').replace('_', '.')


def exibir_extrato(transacoes: List[Dict[str, Any]]) -> None:
    """
    Exibe o extrato formatado no console
    
    Args:
        transacoes: Lista de transações financeiras
    """
    print("\n" + "="*80)
    print(" "*25 + "EXTRATO INTELIGENTE")
    print("="*80)
    print()
    
    if not transacoes:
        print("Nenhuma transação encontrada.")
        return
    
    # Ordenar transações por data
    transacoes_ordenadas = sorted(transacoes, key=lambda x: x.get('data', ''))
    
    # Exibir cabeçalho
    print(f"{'ID':<5} {'Data':<12} {'Descrição':<25} {'Categoria':<15} {'Tipo':<10} {'Valor':>15}")
    print("-"*80)
    
    # Exibir transações
    for transacao in transacoes_ordenadas:
        id_trans = transacao.get('id', '-')
        data = transacao.get('data', '-')
        descricao = transacao.get('descricao', '-')[:25]
        categoria = transacao.get('categoria', '-')[:15]
        tipo = transacao.get('tipo', '-').capitalize()
        valor = transacao.get('valor', 0.0)
        
        valor_formatado = formatar_valor(valor)
        
        print(f"{id_trans:<5} {data:<12} {descricao:<25} {categoria:<15} {tipo:<10} {valor_formatado:>15}")
    
    print("-"*80)
    
    # Calcular e exibir resumo
    resumo = calcular_saldo(transacoes)
    print()
    print(" "*50 + f"Total de Entradas: {formatar_valor(resumo['entradas']):>15}")
    print(" "*50 + f"Total de Saídas:   {formatar_valor(resumo['saidas']):>15}")
    print(" "*50 + "-"*31)
    
    saldo_cor = resumo['saldo']
    saldo_texto = f"Saldo Final:       {formatar_valor(saldo_cor):>15}"
    
    print(" "*50 + saldo_texto)
    print()
    print("="*80)
    print()


def main() -> None:
    """
    Função principal do script
    """
    # Determinar o caminho do arquivo de dados
    diretorio_atual = os.path.dirname(os.path.abspath(__file__))
    diretorio_projeto = os.path.dirname(diretorio_atual)
    caminho_extrato = os.path.join(diretorio_projeto, 'data', 'extrato.json')
    
    print("Hub Financeiro - MVP")
    print(f"Carregando dados de: {caminho_extrato}")
    
    # Carregar transações
    transacoes = carregar_extrato(caminho_extrato)
    
    if not transacoes:
        print("Não foi possível carregar as transações.")
        return
    
    print(f"Total de transações carregadas: {len(transacoes)}")
    
    # Exibir extrato
    exibir_extrato(transacoes)


if __name__ == "__main__":
    main()
