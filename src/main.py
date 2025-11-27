#!/usr/bin/env python3
"""
Financial Hub MVP - Main Module
This script loads financial transactions and calculates the current balance.
"""

import json
import os


def load_transactions(file_path):
    """
    Load transactions from a JSON file.
    
    Args:
        file_path (str): Path to the JSON file containing transactions
        
    Returns:
        list: List of transaction dictionaries
    
    Raises:
        FileNotFoundError: If the data file is not found
        json.JSONDecodeError: If the file contains invalid JSON
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            transactions = json.load(file)
        return transactions
    except FileNotFoundError:
        print(f"Erro: Arquivo não encontrado: {file_path}")
        print("Certifique-se de que o arquivo data/extrato.json existe.")
        raise
    except json.JSONDecodeError as e:
        print(f"Erro: Arquivo JSON inválido: {file_path}")
        print(f"Detalhes: {e}")
        raise


def calculate_balance(transactions):
    """
    Calculate the total balance from a list of transactions.
    
    Args:
        transactions (list): List of transaction dictionaries
        
    Returns:
        float: Total balance (entrada - saida)
    """
    total_entrada = sum(t['value'] for t in transactions if t['type'] == 'entrada')
    total_saida = sum(t['value'] for t in transactions if t['type'] == 'saida')
    balance = total_entrada - total_saida
    return balance


def print_transactions(transactions):
    """
    Print all transactions in a formatted way.
    
    Args:
        transactions (list): List of transaction dictionaries
    """
    print("\n" + "="*80)
    print("EXTRATO INTELIGENTE - TRANSAÇÕES FINANCEIRAS")
    print("="*80 + "\n")
    
    for transaction in transactions:
        tipo_symbol = "+" if transaction['type'] == 'entrada' else "-"
        print(f"ID: {transaction['id']}")
        print(f"Data: {transaction['date']}")
        print(f"Descrição: {transaction['description']}")
        print(f"Categoria: {transaction['category']}")
        print(f"Valor: {tipo_symbol} R$ {transaction['value']:.2f}")
        print(f"Tipo: {transaction['type'].upper()}")
        print("-" * 80)


def main():
    """Main function to execute the financial hub script."""
    # Get the path to the data file
    script_dir = os.path.dirname(os.path.abspath(__file__))
    data_file = os.path.normpath(os.path.join(script_dir, '..', 'data', 'extrato.json'))
    
    # Load transactions
    transactions = load_transactions(data_file)
    
    # Print transactions
    print_transactions(transactions)
    
    # Calculate and print balance
    balance = calculate_balance(transactions)
    print("\n" + "="*80)
    print(f"SALDO ATUAL: R$ {balance:.2f}")
    print("="*80 + "\n")


if __name__ == '__main__':
    main()
