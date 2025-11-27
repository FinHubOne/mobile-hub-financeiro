# Financial Hub MVP - UI Documentation

## Application Screenshot

While the app couldn't fully render in the test environment due to network restrictions (external Flutter resources blocked), the application logic has been fully tested and verified.

## Expected UI Layout

When you run `flet run src/app.py` or `python3 src/app.py`, you will see:

### 1. Header Section (Blue Background)
```
┌─────────────────────────────────┐
│        Saldo Total              │
│      R$ 3926.80                 │
└─────────────────────────────────┘
```
- Displays the total balance prominently
- Blue background (#BLUE_700)
- Large, bold text for the amount

### 2. Action Buttons Row
```
[Pix 💳]  [Recarga 📱]  [Seguros 🛡️]
```
- Three buttons evenly spaced
- Colors: Green (Pix), Orange (Recarga), Purple (Seguros)
- Each button opens an AlertDialog with "Funcionalidade simulada com sucesso!"

### 3. Personalization Card (Conditional)
**✓ DISPLAYED** (because Transporte spending = R$ 520.50 > R$ 500.00)
```
┌─────────────────────────────────────────────────┐
│ 🚗  Oferta Especial: Seguro Auto com 20%       │
│     de desconto!                                │
└─────────────────────────────────────────────────┘
```
- Orange background (#ORANGE_700)
- White text
- Car icon
- Only shown when transport spending exceeds R$ 500.00

### 4. Statement List (Extrato)
```
Extrato

┌─────────────────────────────────────────┐
│ Salário                  +R$ 5000.00 ✓  │
│ 2025-11-27                              │
└─────────────────────────────────────────┘

┌─────────────────────────────────────────┐
│ Supermercado Extra       -R$ 45.50 ✗    │
│ 2025-11-20                              │
└─────────────────────────────────────────┘

... (16 more transactions)
```
- Each transaction in a card layout
- **GREEN** (+) for entrada (income)
- **RED** (-) for saida (expenses)
- Shows: Title, Date, Amount
- Scrollable list

## Verification Results

### ✅ Logic Tests Passed
- ✓ Loaded 18 transactions from JSON
- ✓ Total Balance calculated correctly: R$ 3926.80
  - Entrada: R$ 5000.00
  - Saidas: R$ 1073.20
- ✓ Transporte category total: R$ 520.50
- ✓ Heuristic triggered correctly (> R$ 500.00)
- ✓ Auto Insurance offer displayed: YES

### Transaction Breakdown
- Entradas (Green): 1 transaction
- Saídas (Red): 17 transactions

### Categories with Spending
- Transporte: R$ 520.50 (Uber x3, Gasolina, Metrô, Mecânico, 99)
- Alimentação: R$ 167.70
- Lazer: R$ 140.00
- Saúde: R$ 120.00
- Educação: R$ 95.00
- Serviços: R$ 30.00

## How to Run Locally

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the app:
   ```bash
   flet run src/app.py
   ```
   
   Or directly with Python:
   ```bash
   python3 src/app.py
   ```

The app will open in a native window or web browser depending on your system configuration.

## Features Implemented

- ✅ Load transactions from `data/extrato.json`
- ✅ Calculate total balance (entradas - saidas)
- ✅ Heuristic for Transporte spending > R$ 500.00
- ✅ Header with prominent balance display
- ✅ Action buttons (Pix, Recarga, Seguros) with AlertDialog
- ✅ Personalized Auto Insurance offer card
- ✅ Color-coded transaction list (Green/Red)
- ✅ Scrollable statement view
- ✅ Clean, modern UI with Flet framework
