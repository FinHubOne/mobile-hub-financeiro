# Mobile Hub Financeiro 🏦

MVP do Hub Financeiro Móvel desenvolvido com Python e Flet para o Hackathon. Uma aplicação desktop/mobile moderna para gestão financeira com extrato inteligente e personalização.

## 📋 Project Structure

```
mobile-hub-financeiro/
├── data/
│   └── extrato.json          # Dados de transações financeiras
├── src/
│   ├── app.py                # Aplicação Flet (GUI)
│   └── main.py               # Script CLI (legado)
├── requirements.txt          # Dependências Python
└── README.md                 # Este arquivo
```

## ✨ Features

### Funcionalidades Principais:
- **💰 Saldo Total**: Exibição do saldo atual (entradas - saídas)
- **⚡ Ações Rápidas**: Menu com botões para Pix, Recarga e Seguros
- **📊 Extrato Inteligente**: Lista de transações com visual moderno
  - Entradas em Verde ⬆️
  - Saídas em Vermelho ⬇️
- **🎯 Personalização com Heurística**: 
  - Análise automática de gastos por categoria
  - Oferta especial de Seguro Auto quando gastos com Transporte > 30%

### Tecnologias:
- Python 3.7+
- Flet (Framework para apps desktop/mobile)
- Interface moderna com cores inspiradas em fintechs (Nubank)

## 🚀 Como Instalar e Executar

### 1. Instalar Dependências

```bash
pip install -r requirements.txt
```

### 2. Executar a Aplicação

```bash
flet run src/app.py
```

Ou com Python:

```bash
python -m flet run src/app.py
```

A aplicação abrirá em uma janela desktop mostrando o Hub Financeiro.

## 📱 Interface

A aplicação possui:

1. **Header com Saldo**: Mostra o saldo total atualizado
2. **Ações Rápidas**: 3 botões para operações comuns (Pix, Recarga, Seguros)
3. **Card de Oferta**: Aparece automaticamente se gastos com Transporte > 30%
4. **Extrato Inteligente**: Lista scrollable de todas as transações

## 📊 Formato dos Dados

O arquivo `data/extrato.json` contém transações no formato:

```json
{
  "id": 1,
  "titulo": "Supermercado Extra",
  "valor": -45.50,
  "data": "2025-11-20",
  "categoria": "Alimentação",
  "tipo": "compra"
}
```

### Campos:
- **id**: Identificador único
- **titulo**: Descrição da transação
- **valor**: Valor (negativo para gastos, positivo para receitas)
- **data**: Data no formato YYYY-MM-DD
- **categoria**: Categoria (Alimentação, Transporte, Lazer, Salário, etc.)
- **tipo**: Tipo da transação (pix, compra, recarga)

## 🎨 Design

- **Cores**: Roxo (#820AD1) como cor principal (inspirado Nubank)
- **Layout**: Cards brancos sobre fundo cinza claro
- **Tipografia**: Hierarquia clara com títulos em bold
- **Responsivo**: Interface adaptável para diferentes tamanhos de tela

## 🏆 Hackathon Requirements

Este MVP atende aos requisitos:
- ✅ Integração de serviços (simulação via botões)
- ✅ Extrato inteligente com visualização clara
- ✅ Personalização básica com heurística de gastos

## 🛠️ Script CLI (Legado)

Ainda é possível executar a versão CLI:

```bash
python3 src/main.py
```

## 📄 License

MIT - Projeto Hackathon