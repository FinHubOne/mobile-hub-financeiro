#!/usr/bin/env python3
"""
Financial Hub MVP - Flet Application
A mobile financial hub built with Flet framework.
"""

import json
from pathlib import Path
import flet as ft


def load_transactions(filepath):
    """Load transactions from JSON file."""
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            data = json.load(file)
        return data.get('transactions', [])
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error loading transactions: {e}")
        return []


def calculate_balance(transactions):
    """Calculate total balance (entradas - saidas)."""
    balance = 0
    for transaction in transactions:
        if transaction['type'] == 'entrada':
            balance += transaction['amount']
        else:  # saida
            balance -= transaction['amount']
    return balance


def calculate_category_total(transactions, category):
    """Calculate total spend in a specific category."""
    total = 0
    for transaction in transactions:
        if transaction.get('category') == category and transaction['type'] == 'saida':
            total += transaction['amount']
    return total


def main(page: ft.Page):
    """Main Flet application."""
    page.title = "Mobile Hub Financeiro"
    page.padding = 20
    page.scroll = ft.ScrollMode.AUTO
    
    # Load data
    script_dir = Path(__file__).parent
    data_file = script_dir.parent / 'data' / 'extrato.json'
    transactions = load_transactions(data_file)
    
    # Calculate metrics
    total_balance = calculate_balance(transactions)
    transporte_total = calculate_category_total(transactions, 'Transporte')
    show_auto_insurance_offer = transporte_total > 500.00
    
    # Dialog for simulated actions
    def show_dialog(action_name):
        def close_dialog(e):
            dialog.open = False
            page.update()
        
        dialog = ft.AlertDialog(
            title=ft.Text(f"{action_name}"),
            content=ft.Text("Funcionalidade simulada com sucesso!"),
            actions=[
                ft.TextButton("OK", on_click=close_dialog)
            ],
            actions_alignment=ft.MainAxisAlignment.END
        )
        page.dialog = dialog
        dialog.open = True
        page.update()
    
    # Header with Total Balance
    header = ft.Container(
        content=ft.Column([
            ft.Text("Saldo Total", size=16, weight=ft.FontWeight.NORMAL),
            ft.Text(f"R$ {total_balance:.2f}", size=32, weight=ft.FontWeight.BOLD),
        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
        bgcolor=ft.colors.BLUE_700,
        padding=20,
        border_radius=10,
        alignment=ft.alignment.center,
    )
    
    # Actions Row
    actions_row = ft.Row([
        ft.ElevatedButton(
            "Pix",
            icon=ft.icons.PIX,
            on_click=lambda _: show_dialog("Pix"),
            style=ft.ButtonStyle(
                bgcolor=ft.colors.GREEN_700,
                color=ft.colors.WHITE,
            )
        ),
        ft.ElevatedButton(
            "Recarga",
            icon=ft.icons.PHONE_ANDROID,
            on_click=lambda _: show_dialog("Recarga"),
            style=ft.ButtonStyle(
                bgcolor=ft.colors.ORANGE_700,
                color=ft.colors.WHITE,
            )
        ),
        ft.ElevatedButton(
            "Seguros",
            icon=ft.icons.SECURITY,
            on_click=lambda _: show_dialog("Seguros"),
            style=ft.ButtonStyle(
                bgcolor=ft.colors.PURPLE_700,
                color=ft.colors.WHITE,
            )
        ),
    ], alignment=ft.MainAxisAlignment.SPACE_EVENLY)
    
    # Personalization Card (Auto Insurance Offer)
    personalization_content = []
    if show_auto_insurance_offer:
        offer_card = ft.Container(
            content=ft.Row([
                ft.Icon(ft.icons.DIRECTIONS_CAR, size=40, color=ft.colors.ORANGE),
                ft.Column([
                    ft.Text(
                        "Oferta Especial: Seguro Auto com 20% de desconto!",
                        size=14,
                        weight=ft.FontWeight.BOLD,
                        color=ft.colors.WHITE,
                    ),
                ], expand=True),
            ]),
            bgcolor=ft.colors.ORANGE_700,
            padding=15,
            border_radius=10,
            margin=ft.margin.only(top=10, bottom=10),
        )
        personalization_content.append(offer_card)
    
    # Statement List
    statement_title = ft.Text("Extrato", size=20, weight=ft.FontWeight.BOLD)
    
    transaction_items = []
    for transaction in transactions:
        # Determine color based on type
        if transaction['type'] == 'entrada':
            amount_color = ft.colors.GREEN
            amount_text = f"+R$ {transaction['amount']:.2f}"
        else:  # saida
            amount_color = ft.colors.RED
            amount_text = f"-R$ {transaction['amount']:.2f}"
        
        transaction_card = ft.Container(
            content=ft.Row([
                ft.Column([
                    ft.Text(transaction['title'], size=14, weight=ft.FontWeight.BOLD),
                    ft.Text(transaction['date'], size=12, color=ft.colors.GREY_700),
                ], expand=True),
                ft.Text(
                    amount_text,
                    size=14,
                    weight=ft.FontWeight.BOLD,
                    color=amount_color,
                ),
            ]),
            bgcolor=ft.colors.WHITE,
            border=ft.border.all(1, ft.colors.GREY_300),
            border_radius=8,
            padding=12,
            margin=ft.margin.only(bottom=8),
        )
        transaction_items.append(transaction_card)
    
    statement_list = ft.Column(transaction_items, scroll=ft.ScrollMode.AUTO)
    
    # Main layout
    page.add(
        ft.Column([
            header,
            ft.Container(height=20),  # Spacer
            actions_row,
            *personalization_content,
            ft.Container(height=20),  # Spacer
            statement_title,
            ft.Container(height=10),  # Spacer
            statement_list,
        ])
    )


if __name__ == "__main__":
    ft.app(target=main)
