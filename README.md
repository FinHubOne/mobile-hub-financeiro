# Mobile Hub Financeiro 🏦

A modern financial hub MVP built with Python and Flet for the Hackathon project. This interactive application provides an intuitive interface to manage and track financial transactions with smart personalized recommendations.

## Project Structure

```
mobile-hub-financeiro/
├── data/
│   └── extrato.json          # Mock transaction data
├── src/
│   ├── app.py                # Flet GUI application (MVP)
│   └── main.py               # CLI application (legacy)
├── requirements.txt          # Python dependencies
└── README.md                 # This file
```

## Features

### MVP Features (Flet GUI Application)

- **💰 Balance Display**: Real-time total balance calculation with visual color coding
- **⚡ Quick Actions**: Instant access to common operations:
  - 💸 **Pix**: Quick PIX transfers
  - 📱 **Recarga**: Mobile top-up
  - 🛡️ **Seguros**: Insurance services
- **📊 Intelligent Transaction List**: 
  - Color-coded transactions (🔴 red for expenses, 🟢 green for income)
  - Detailed view with category, date, and amount
  - Icon indicators for transaction direction
- **🎯 Personalized Offers**: Smart recommendations based on spending patterns
  - Auto insurance offer when transport expenses exceed R$ 100

### CLI Features (Legacy)

- **Transaction Management**: Load and display financial transactions from JSON data
- **Balance Calculation**: Automatically calculate total balance from all transactions
- **Category Tracking**: Organize transactions by category (Alimentação, Transporte, Lazer, etc.)
- **Transaction Types**: Support for different transaction types (PIX, compra, recarga)

## Requirements

- Python 3.7 or higher
- Flet 0.21.0 or higher (for GUI application)

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

### MVP - Flet GUI Application (Recommended)

Run the interactive Flet application:

```bash
flet run src/app.py
```

Or alternatively:

```bash
python3 src/app.py
```

This will launch the modern GUI interface with all MVP features.

### CLI Application (Legacy)

Run the command-line interface:

```bash
python3 src/main.py
```

## Testing

Run the comprehensive test suite to verify all functionality:

```bash
python3 test_app.py
```

This will validate:
- Transaction loading
- Balance calculation
- Category totals
- Personalization logic
- Color coding
- Quick action buttons

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