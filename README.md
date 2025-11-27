# Mobile Hub Financeiro 🏦

A mobile financial hub MVP for the Hackathon project with a modern UI built with Flet. This application helps track and categorize financial transactions with personalized offers based on spending patterns.

## Project Structure

```
mobile-hub-financeiro/
├── data/
│   └── extrato.json          # Mock transaction data
├── src/
│   ├── app.py                # Flet UI application (Main MVP)
│   └── main.py               # CLI application
├── requirements.txt          # Python dependencies
└── README.md                 # This file
```

## Features

- **Transaction Management**: Load and display financial transactions from JSON data
- **Balance Calculation**: Automatically calculate total balance from all transactions
- **Category Tracking**: Organize transactions by category (Alimentação, Transporte, Lazer, etc.)
- **Interactive UI**: Modern mobile-like interface built with Flet
- **Action Buttons**: Quick access to Pix, Recarga, and Seguros features
- **Smart Personalization**: Display special offers based on spending patterns (e.g., auto insurance discount when transport expenses exceed 30%)

## Requirements

- Python 3.7 or higher
- Flet (for the UI application)

## How to Run

### Flet UI Application (Recommended)

1. **Navigate to the project directory:**
   ```bash
   cd mobile-hub-financeiro
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Flet application:**
   ```bash
   flet run src/app.py
   ```

   Or:
   ```bash
   python3 src/app.py
   ```

### CLI Application (Legacy)

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

### Flet UI Application

The Flet app provides a modern mobile interface with:
- Total balance display with color-coded values (green for positive, red for negative)
- Three action buttons (Pix, Recarga, Seguros) that show success dialogs when clicked
- List of all transactions with color-coded amounts
- Smart personalization: Special offer card for auto insurance discount when transport expenses exceed 30%

### CLI Application

The CLI application will:
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
- Issue #1: Basic project structure and data model
- Issue #2: Transaction categorization and UI implementation
- Issue #3: Personalized offers based on spending heuristics

## Contributing

This is a Hackathon MVP project. Feel free to expand and improve the functionality!