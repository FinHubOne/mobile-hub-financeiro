# Mobile Hub Financeiro 🏦

A mobile financial hub MVP built with Flet for the Hackathon project. This application helps track and categorize financial transactions with personalized insurance offers.

## Project Structure

```
mobile-hub-financeiro/
├── data/
│   └── extrato.json          # Mock transaction data
├── src/
│   ├── app.py                # Flet UI application (NEW)
│   └── main.py               # CLI application (legacy)
├── requirements.txt          # Python dependencies
└── README.md                 # This file
```

## Features

- **Interactive Dashboard**: Modern UI built with Flet framework
- **Transaction Management**: Load and display financial transactions from JSON data
- **Balance Calculation**: Automatically calculate total balance from all transactions
- **Category Tracking**: Organize transactions by category (Alimentação, Transporte, Lazer, etc.)
- **Quick Actions**: Buttons for Pix, Recarga, and Seguros with success modals
- **Smart Recommendations**: Personalized insurance offers based on spending patterns
- **Heuristic Logic**: Displays special car insurance offer when transport spending exceeds 30% of total expenses

## Requirements

- Python 3.7 or higher
- Flet 0.24.1 or higher (see `requirements.txt`)

## Installation

1. **Navigate to the project directory:**
   ```bash
   cd mobile-hub-financeiro
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## How to Run

### Flet UI Application (Recommended)

Run the modern Flet-based UI application:

```bash
python3 src/app.py
```

Or make it executable and run directly:
```bash
chmod +x src/app.py
./src/app.py
```

This will launch a window with the interactive financial dashboard.

### CLI Application (Legacy)

Run the command-line interface version:

```bash
python3 src/main.py
```

## Application Features

The Flet UI application provides:

1. **Balance Overview**: See your total balance at a glance
2. **Transaction History**: Browse all transactions with icons and categories
3. **Quick Actions**:
   - **Pix**: Simulate instant transfers
   - **Recarga**: Simulate phone/transport recharges
   - **Seguros**: Simulate insurance purchases
4. **Smart Recommendations**: 
   - If your transport spending exceeds 30% of total expenses, you'll see a special car insurance offer banner
   - This personalization helps you save money on relevant services

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