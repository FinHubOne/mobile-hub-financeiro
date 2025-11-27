# Mobile Hub Financeiro 🏦

A simple financial hub MVP for the Hackathon project. This application helps track and categorize financial transactions.

## Project Structure

```
mobile-hub-financeiro/
├── data/
│   └── extrato.json          # Mock transaction data
├── src/
│   └── main.py               # Main application logic
└── README.md                 # This file
```

## Features

- **Transaction Management**: Load and display financial transactions from JSON data
- **Balance Calculation**: Automatically calculate total balance from all transactions
- **Category Tracking**: Organize transactions by category (Alimentação, Transporte, Lazer, etc.)
- **Transaction Types**: Support for different transaction types (PIX, compra, recarga)

## Requirements

- Python 3.7 or higher
- No external dependencies required (uses only Python standard library)

## How to Run

1. **Navigate to the project directory:**
   ```bash
   cd mobile-hub-financeiro
   ```

2. **Run the main script:**
   ```bash
   python3 src/main.py
   ```

   Or make it executable and run directly:
   ```bash
   chmod +x src/main.py
   ./src/main.py
   ```

## Sample Output

The application will:
1. Load transactions from `data/extrato.json`
2. Display all transactions with details (ID, date, type, category, amount, description)
3. Calculate and show the total balance
4. Provide a summary of expenses/income by category

## Data Format

The `data/extrato.json` file contains an array of transaction objects with the following structure:

```json
{
  "id": 1,
  "type": "compra",
  "category": "Alimentação",
  "amount": -45.50,
  "date": "2025-11-20",
  "description": "Supermercado Extra"
}
```

### Transaction Fields:
- **id**: Unique identifier for the transaction
- **type**: Transaction type (pix, compra, recarga)
- **category**: Category of the expense/income (Alimentação, Transporte, Lazer, etc.)
- **amount**: Transaction amount (negative for expenses, positive for income)
- **date**: Transaction date in YYYY-MM-DD format
- **description**: Description of the transaction

## Related Issues

This implementation addresses:
- Issue #1: Basic project structure
- Issue #2: Transaction categorization demonstration

## Contributing

This is a Hackathon MVP project. Feel free to expand and improve the functionality!