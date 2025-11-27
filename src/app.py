#!/usr/bin/env python3
"""
Financial Hub MVP - Flet UI Application
Mobile interface for financial transaction management with personalization features.
"""

import json
from pathlib import Path
import flet as ft


def load_transactions(filepath):
    """Load transactions from a JSON file."""
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            transactions = json.load(file)
        return transactions
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error loading transactions: {e}")
        return []


def calculate_balance(transactions):
    """Calculate the total balance from a list of transactions."""
    return sum(transaction.get('amount', 0) for transaction in transactions)


def calculate_transporte_percentage(transactions):
    """Calculate the percentage of expenses spent on Transporte."""
    total_expenses = sum(abs(t['amount']) for t in transactions if t['amount'] < 0)
    transporte_expenses = sum(
        abs(t['amount']) for t in transactions 
        if t['amount'] < 0 and t['category'] == 'Transporte'
    )
    
    if total_expenses == 0:
        return 0
    
    return (transporte_expenses / total_expenses) * 100


def main(page: ft.Page):
    """Main application function."""
    page.title = "Hub Financeiro"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = 20
    page.scroll = ft.ScrollMode.AUTO
    
    # Load transactions
    script_dir = Path(__file__).parent
    data_file = script_dir.parent / 'data' / 'extrato.json'
    transactions = load_transactions(data_file)
    
    # Calculate balance and transporte percentage
    balance = calculate_balance(transactions)
    transporte_pct = calculate_transporte_percentage(transactions)
    
    # Dialog function for action buttons
    def show_success_dialog(e, action_name):
        dialog = ft.AlertDialog(
            title=ft.Text(f"{action_name}"),
            content=ft.Text("Operação realizada com sucesso!"),
            actions=[
                ft.TextButton("OK", on_click=lambda _: close_dialog(dialog))
            ],
        )
        page.dialog = dialog
        dialog.open = True
        page.update()
    
    def close_dialog(dialog):
        dialog.open = False
        page.update()
    
    # Header with balance
    header = ft.Container(
        content=ft.Column([
            ft.Text(
                "💰 Hub Financeiro",
                size=28,
                weight=ft.FontWeight.BOLD,
                color=ft.colors.WHITE
            ),
            ft.Text(
                f"Saldo Total: R$ {balance:,.2f}",
                size=24,
                weight=ft.FontWeight.W_500,
                color=ft.colors.WHITE
            ),
        ], spacing=5),
        padding=20,
        bgcolor=ft.colors.BLUE_700,
        border_radius=10,
        margin=ft.margin.only(bottom=20)
    )
    
    # Action buttons
    action_buttons = ft.Row(
        [
            ft.ElevatedButton(
                "💸 Pix",
                icon=ft.icons.PIX,
                on_click=lambda e: show_success_dialog(e, "Pix"),
                style=ft.ButtonStyle(
                    bgcolor=ft.colors.GREEN_700,
                    color=ft.colors.WHITE,
                    padding=15,
                ),
            ),
            ft.ElevatedButton(
                "📱 Recarga",
                icon=ft.icons.PHONE_ANDROID,
                on_click=lambda e: show_success_dialog(e, "Recarga"),
                style=ft.ButtonStyle(
                    bgcolor=ft.colors.ORANGE_700,
                    color=ft.colors.WHITE,
                    padding=15,
                ),
            ),
            ft.ElevatedButton(
                "🛡️ Seguros",
                icon=ft.icons.SECURITY,
                on_click=lambda e: show_success_dialog(e, "Seguros"),
                style=ft.ButtonStyle(
                    bgcolor=ft.colors.PURPLE_700,
                    color=ft.colors.WHITE,
                    padding=15,
                ),
            ),
        ],
        alignment=ft.MainAxisAlignment.SPACE_AROUND,
        spacing=10,
    )
    
    action_buttons_container = ft.Container(
        content=action_buttons,
        padding=10,
        margin=ft.margin.only(bottom=20)
    )
    
    # Personalized offer banner (shown if Transporte > 30%)
    offer_banner = None
    if transporte_pct > 30:
        offer_banner = ft.Container(
            content=ft.Column([
                ft.Row([
                    ft.Icon(ft.icons.LOCAL_OFFER, color=ft.colors.AMBER_400, size=30),
                    ft.Text(
                        "Oferta Especial!",
                        size=20,
                        weight=ft.FontWeight.BOLD,
                        color=ft.colors.WHITE
                    ),
                ], spacing=10),
                ft.Text(
                    "Seguro Auto com 20% de desconto!",
                    size=16,
                    weight=ft.FontWeight.W_500,
                    color=ft.colors.WHITE
                ),
                ft.Text(
                    "Proteja seu veículo.",
                    size=14,
                    color=ft.colors.WHITE70
                ),
            ], spacing=5),
            padding=20,
            bgcolor=ft.colors.DEEP_ORANGE_700,
            border_radius=10,
            margin=ft.margin.only(bottom=20),
            border=ft.border.all(2, ft.colors.AMBER_400)
        )
    
    # Transaction feed
    transaction_items = []
    for transaction in transactions:
        amount = transaction.get('amount', 0)
        
        # Color code based on income/outcome
        if amount >= 0:
            amount_color = ft.colors.GREEN_700
            amount_text = f"+R$ {amount:,.2f}"
        else:
            amount_color = ft.colors.RED_700
            amount_text = f"-R$ {abs(amount):,.2f}"
        
        transaction_card = ft.Container(
            content=ft.Row(
                [
                    ft.Column(
                        [
                            ft.Text(
                                transaction.get('description', 'N/A'),
                                size=16,
                                weight=ft.FontWeight.W_500
                            ),
                            ft.Text(
                                f"{transaction.get('category', 'N/A')} • {transaction.get('date', 'N/A')}",
                                size=12,
                                color=ft.colors.GREY_700
                            ),
                        ],
                        spacing=5,
                        expand=True
                    ),
                    ft.Text(
                        amount_text,
                        size=16,
                        weight=ft.FontWeight.BOLD,
                        color=amount_color
                    ),
                ],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            ),
            padding=15,
            bgcolor=ft.colors.GREY_100,
            border_radius=8,
            margin=ft.margin.only(bottom=10)
        )
        transaction_items.append(transaction_card)
    
    # Transaction feed header
    feed_header = ft.Container(
        content=ft.Text(
            "📋 Extrato de Transações",
            size=20,
            weight=ft.FontWeight.BOLD,
            color=ft.colors.BLUE_900
        ),
        padding=ft.padding.only(bottom=10)
    )
    
    # Build the main column with all components
    main_column_items = [header, action_buttons_container]
    
    if offer_banner:
        main_column_items.append(offer_banner)
    
    main_column_items.append(feed_header)
    main_column_items.extend(transaction_items)
    
    # Main content
    page.add(
        ft.Column(
            main_column_items,
            scroll=ft.ScrollMode.AUTO,
            expand=True
        )
    )


if __name__ == "__main__":
    ft.app(target=main)
