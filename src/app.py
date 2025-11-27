#!/usr/bin/env python3
"""
Mobile Financial Hub MVP - Flet Application
Interactive financial hub with quick actions and intelligent transaction display.
"""

import json
from pathlib import Path
import flet as ft


def load_transactions(filepath):
    """
    Load transactions from a JSON file.
    
    Args:
        filepath (str): Path to the JSON file containing transactions
        
    Returns:
        list: List of transaction dictionaries
    """
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            transactions = json.load(file)
        return transactions
    except FileNotFoundError:
        print(f"Error: File '{filepath}' not found.")
        return []
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON format in '{filepath}'.")
        return []


def calculate_balance(transactions):
    """
    Calculate the total balance from a list of transactions.
    
    Args:
        transactions (list): List of transaction dictionaries
        
    Returns:
        float: Total balance
    """
    total = sum(transaction.get('amount', 0) for transaction in transactions)
    return total


def calculate_category_total(transactions, category):
    """
    Calculate the total amount for a specific category.
    
    Args:
        transactions (list): List of transaction dictionaries
        category (str): Category name to filter by
        
    Returns:
        float: Total amount for the category
    """
    total = sum(
        transaction.get('amount', 0) 
        for transaction in transactions 
        if transaction.get('category') == category
    )
    return total


def main(page: ft.Page):
    """
    Main Flet application entry point.
    
    Args:
        page (ft.Page): Flet page object
    """
    # Configure page
    page.title = "Hub Financeiro Móvel"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = 20
    page.scroll = ft.ScrollMode.AUTO
    
    # Load transaction data
    script_dir = Path(__file__).parent
    data_file = script_dir.parent / 'data' / 'extrato.json'
    transactions = load_transactions(data_file)
    
    # Calculate balance and category totals
    balance = calculate_balance(transactions)
    transport_total = abs(calculate_category_total(transactions, "Transporte"))
    
    # AlertDialog for quick actions
    def show_action_dialog(action_name):
        """Show success dialog for quick actions."""
        dialog = ft.AlertDialog(
            title=ft.Text(f"{action_name}"),
            content=ft.Text("Funcionalidade simulada com sucesso!"),
            actions=[
                ft.TextButton("OK", on_click=lambda e: close_dialog(dialog))
            ],
        )
        page.dialog = dialog
        dialog.open = True
        page.update()
    
    def close_dialog(dialog):
        """Close the dialog."""
        dialog.open = False
        page.update()
    
    # Quick action button handlers
    def on_pix_click(e):
        show_action_dialog("Pix")
    
    def on_recarga_click(e):
        show_action_dialog("Recarga")
    
    def on_seguros_click(e):
        show_action_dialog("Seguros")
    
    # Build UI components
    
    # Header with balance
    balance_color = ft.colors.GREEN if balance >= 0 else ft.colors.RED
    header = ft.Container(
        content=ft.Column([
            ft.Text("💰 Hub Financeiro", size=28, weight=ft.FontWeight.BOLD),
            ft.Text("Saldo Total", size=16, color=ft.colors.GREY_700),
            ft.Text(
                f"R$ {balance:.2f}",
                size=36,
                weight=ft.FontWeight.BOLD,
                color=balance_color
            ),
        ]),
        padding=20,
        border_radius=10,
        bgcolor=ft.colors.BLUE_50,
    )
    
    # Quick action buttons
    quick_actions = ft.Container(
        content=ft.Column([
            ft.Text("Ações Rápidas", size=18, weight=ft.FontWeight.BOLD),
            ft.Row([
                ft.ElevatedButton(
                    "💸 Pix",
                    on_click=on_pix_click,
                    style=ft.ButtonStyle(
                        bgcolor=ft.colors.BLUE_500,
                        color=ft.colors.WHITE,
                        padding=20,
                    ),
                    expand=1,
                ),
                ft.ElevatedButton(
                    "📱 Recarga",
                    on_click=on_recarga_click,
                    style=ft.ButtonStyle(
                        bgcolor=ft.colors.GREEN_500,
                        color=ft.colors.WHITE,
                        padding=20,
                    ),
                    expand=1,
                ),
                ft.ElevatedButton(
                    "🛡️ Seguros",
                    on_click=on_seguros_click,
                    style=ft.ButtonStyle(
                        bgcolor=ft.colors.ORANGE_500,
                        color=ft.colors.WHITE,
                        padding=20,
                    ),
                    expand=1,
                ),
            ], spacing=10),
        ]),
        padding=20,
        border_radius=10,
        bgcolor=ft.colors.WHITE,
        margin=ft.margin.only(top=10),
    )
    
    # Personalized offer card (show if transport > R$ 100)
    offer_card = None
    if transport_total > 100:
        offer_card = ft.Container(
            content=ft.Row([
                ft.Icon(ft.icons.DIRECTIONS_CAR, color=ft.colors.WHITE, size=40),
                ft.Column([
                    ft.Text(
                        "🚗 Oferta Personalizada",
                        size=16,
                        weight=ft.FontWeight.BOLD,
                        color=ft.colors.WHITE
                    ),
                    ft.Text(
                        "Viajando muito? Conheça nosso Seguro Auto!",
                        size=14,
                        color=ft.colors.WHITE
                    ),
                ], expand=1),
            ]),
            padding=20,
            border_radius=10,
            bgcolor=ft.colors.DEEP_ORANGE_700,
            margin=ft.margin.only(top=10),
        )
    
    # Transaction list
    transaction_items = []
    for transaction in transactions:
        amount = transaction.get('amount', 0)
        is_expense = amount < 0
        
        # Color coding: red for expenses, green for income
        amount_color = ft.colors.RED_700 if is_expense else ft.colors.GREEN_700
        icon_name = ft.icons.ARROW_DOWNWARD if is_expense else ft.icons.ARROW_UPWARD
        icon_color = ft.colors.RED_500 if is_expense else ft.colors.GREEN_500
        
        transaction_card = ft.Container(
            content=ft.Row([
                ft.Icon(icon_name, color=icon_color, size=30),
                ft.Column([
                    ft.Text(
                        transaction.get('description', 'N/A'),
                        size=14,
                        weight=ft.FontWeight.BOLD
                    ),
                    ft.Row([
                        ft.Text(
                            transaction.get('category', 'N/A'),
                            size=12,
                            color=ft.colors.GREY_600
                        ),
                        ft.Text(
                            f"• {transaction.get('date', 'N/A')}",
                            size=12,
                            color=ft.colors.GREY_600
                        ),
                    ]),
                ], expand=1),
                ft.Text(
                    f"R$ {abs(amount):.2f}",
                    size=16,
                    weight=ft.FontWeight.BOLD,
                    color=amount_color
                ),
            ]),
            padding=15,
            border_radius=8,
            bgcolor=ft.colors.WHITE,
            border=ft.border.all(1, ft.colors.GREY_300),
            margin=ft.margin.only(bottom=8),
        )
        transaction_items.append(transaction_card)
    
    transactions_section = ft.Container(
        content=ft.Column([
            ft.Text(
                "📊 Extrato Inteligente",
                size=18,
                weight=ft.FontWeight.BOLD
            ),
            ft.Column(transaction_items, spacing=0),
        ]),
        padding=20,
        border_radius=10,
        bgcolor=ft.colors.GREY_50,
        margin=ft.margin.only(top=10),
    )
    
    # Build page layout
    page_content = [
        header,
        quick_actions,
    ]
    
    if offer_card:
        page_content.append(offer_card)
    
    page_content.append(transactions_section)
    
    # Add all components to page
    page.add(ft.Column(page_content, scroll=ft.ScrollMode.AUTO))


if __name__ == "__main__":
    ft.app(target=main)
