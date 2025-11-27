# Mobile Hub Financeiro 🏦

A mobile financial hub MVP built with Python and Flet for the Hackathon project. This application provides an intuitive interface for tracking financial transactions with personalized recommendations.

## Project Structure

```
mobile-hub-financeiro/
├── data/
│   └── extrato.json          # Mock transaction data
├── src/
│   ├── app.py                # Flet UI application (MVP)
│   └── main.py               # CLI version (legacy)
├── requirements.txt          # Python dependencies
└── README.md                 # This file
```

## Features

### 🎨 User Interface (Flet-based)
- **Header**: Displays total balance prominently
- **Action Buttons**: Quick access to Pix, Recarga, and Seguros operations
- **Transaction Feed**: Scrollable list of all transactions with color-coded amounts
  - Green for income (positive amounts)
  - Red for expenses (negative amounts)
- **Modal Dialogs**: Success confirmations for each action

### 🤖 Smart Personalization
- **Heuristic Logic**: Automatically analyzes spending patterns
- **Auto Insurance Offer**: When Transporte expenses exceed 30% of total expenses, displays a special offer banner:
  - "Oferta Especial: Seguro Auto com 20% de desconto! Proteja seu veículo."

### 💾 Data Management
- **Transaction Categories**: Alimentação, Transporte, Lazer, Salário, and more
- **Transaction Types**: income (entrada) and outcome (saída)
- **Automatic Balance Calculation**: Real-time balance updates

## Requirements

- Python 3.7 or higher
- Flet library (for UI)

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/FinHubOne/mobile-hub-financeiro.git
   cd mobile-hub-financeiro
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## How to Run

### Mobile/Desktop App (Recommended)

Run the Flet application:
```bash
python3 src/app.py
```

This will launch a native window with the financial hub interface.

### Web Version

Run the app in web mode:
```bash
python3 src/app.py --web --port 8550
```

Then open your browser to `http://localhost:8550`

### CLI Version (Legacy)

For command-line output:
```bash
python3 src/main.py
```

## Data Format

The `data/extrato.json` file contains an array of transaction objects:

```json
{
  "id": 1,
  "type": "income",
  "category": "Salário",
  "amount": 3500.00,
  "date": "2025-11-01",
  "description": "Salário mensal"
}
```

### Transaction Fields:
- **id**: Unique identifier for the transaction
- **type**: Transaction type (`income` for entrada, `outcome` for saída)
- **category**: Category of the transaction (Alimentação, Transporte, Lazer, Salário, etc.)
- **amount**: Transaction amount (positive for income, negative for expenses)
- **date**: Transaction date in YYYY-MM-DD format
- **description**: Description of the transaction

## Demo Features

The MVP includes demonstration data with:
- 18 sample transactions
- High Transporte spending (>70%) to trigger the personalized insurance offer
- Multiple transaction categories for comprehensive testing
- Realistic Brazilian financial scenarios (Uber, Gasolina, Mecânico, etc.)

## Hackathon Requirements

This MVP fulfills all the requirements:
1. ✅ **Mock Data**: `data/extrato.json` with realistic transactions
2. ✅ **Flet Interface**: Modern UI with header, actions, and transaction feed
3. ✅ **Action Buttons**: Pix, Recarga, and Seguros with success modals
4. ✅ **Color-Coded Amounts**: Green for income, red for expenses
5. ✅ **Personalization**: Auto insurance offer when Transporte > 30%
6. ✅ **Dependencies**: `requirements.txt` with flet

## Contributing

This is a Hackathon MVP project. Feel free to expand and improve the functionality!