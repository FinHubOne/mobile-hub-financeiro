# Mobile Hub Financeiro

A financial hub MVP with intelligent transaction tracking and balance calculation.

## Project Structure

```
mobile-hub-financeiro/
├── data/
│   └── extrato.json          # Mock financial transaction data
├── src/
│   └── main.py               # Main application script
└── README.md                 # This file
```

## Features

- **Extrato Inteligente**: View all your financial transactions with detailed information
- **Balance Calculation**: Automatic calculation of current balance based on income and expenses
- **Transaction Categorization**: Transactions organized by categories (Alimentação, Transporte, Salário, etc.)

## Mock Data

The `data/extrato.json` file contains simulated financial transactions with the following fields:
- `id`: Unique transaction identifier
- `date`: Transaction date (YYYY-MM-DD format)
- `description`: Description of the transaction
- `value`: Transaction amount (float)
- `type`: Transaction type ("entrada" for income, "saida" for expenses)
- `category`: Transaction category (e.g., "Alimentação", "Transporte", "Salário")

## How to Run

### Prerequisites

- Python 3.x installed on your system

### Running the Application

1. Navigate to the project directory:
```bash
cd mobile-hub-financeiro
```

2. Run the main script:
```bash
python3 src/main.py
```

Or make it executable and run directly:
```bash
chmod +x src/main.py
./src/main.py
```

### Expected Output

The script will display:
1. All transactions from the `data/extrato.json` file with formatted details
2. The current balance calculated as: (total income - total expenses)

## Example Output

```
================================================================================
EXTRATO INTELIGENTE - TRANSAÇÕES FINANCEIRAS
================================================================================

ID: 1
Data: 2024-01-15
Descrição: Salário
Categoria: Salário
Valor: + R$ 5000.00
Tipo: ENTRADA
--------------------------------------------------------------------------------
...

================================================================================
SALDO ATUAL: R$ 5333.70
================================================================================
```

## Development

This is the base MVP structure for Issue #2, establishing:
- Mock data for the "Extrato Inteligente" feature
- Core logic for loading transactions and calculating balances
- Simple command-line interface for viewing financial data