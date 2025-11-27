# Mobile Hub Financeiro 🏦

A mobile financial hub MVP built with the Flet framework for the Hackathon project. This application helps track and categorize financial transactions with a modern, interactive UI.

## Project Structure

```
mobile-hub-financeiro/
├── data/
│   └── extrato.json          # Mock transaction data
├── src/
│   ├── app.py                # Flet UI application
│   └── main.py               # CLI application (legacy)
├── requirements.txt          # Python dependencies
└── README.md                 # This file
```

## Features

- **Interactive UI**: Built with Flet framework for a native mobile-like experience
- **Transaction Management**: Load and display financial transactions from JSON data
- **Balance Calculation**: Automatically calculate total balance (entradas - saidas)
- **Smart Offers**: Personalized offers based on spending patterns (e.g., Auto Insurance offer when transport spending exceeds R$ 500)
- **Quick Actions**: Simulate Pix, Recarga, and Seguros operations with interactive dialogs
- **Color-Coded Transactions**: Green for income (entrada), Red for expenses (saida)
- **Category Tracking**: Organize transactions by category (Alimentação, Transporte, Lazer, etc.)

## Requirements

- Python 3.7 or higher
- Flet framework

## How to Run

1. **Navigate to the project directory:**
   ```bash
   cd mobile-hub-financeiro
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Flet app:**
   ```bash
   flet run src/app.py
   ```

   Or make it executable and run directly:
   ```bash
   chmod +x src/app.py
   ./src/app.py
   ```

## Application Interface

The Flet application provides:

- **Header**: Displays your total balance prominently at the top
- **Action Buttons**: Quick access to Pix, Recarga, and Seguros features
- **Smart Offers**: Personalized offers based on your spending (e.g., "Oferta Especial: Seguro Auto com 20% de desconto!" when transport spending > R$ 500)
- **Statement List**: Complete transaction history with:
  - Transaction title and date
  - Color-coded amounts (Green for income, Red for expenses)
  - Easy-to-read card layout

## Data Format

The `data/extrato.json` file contains a JSON object with a list of transactions:

```json
{
  "transactions": [
    {
      "id": 1,
      "title": "Salário",
      "type": "entrada",
      "category": "Salário",
      "amount": 5000.00,
      "date": "2025-11-27"
    },
    {
      "id": 2,
      "title": "Supermercado Extra",
      "type": "saida",
      "category": "Alimentação",
      "amount": 45.50,
      "date": "2025-11-20"
    }
  ]
}
```

### Transaction Fields:
- **id**: Unique identifier for the transaction
- **title**: Transaction title/description
- **type**: Transaction type (`entrada` for income, `saida` for expenses)
- **category**: Category of the transaction (Salário, Alimentação, Transporte, Lazer, etc.)
- **amount**: Transaction amount (always positive; type determines if it's added or subtracted)
- **date**: Transaction date in YYYY-MM-DD format

## Legacy CLI Tool

The project also includes a legacy command-line tool (`src/main.py`) that displays transactions in the terminal:

```bash
python3 src/main.py
```

## Contributing

This is a Hackathon MVP project. Feel free to expand and improve the functionality!