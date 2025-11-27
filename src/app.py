#!/usr/bin/env python3
"""
FinHub - Mobile Financial Hub MVP
A Flet-based financial application with personalized insurance offers.
"""

import json
from pathlib import Path
import flet as ft


def load_transactions(filepath):
    """Load transactions from JSON file."""
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error loading transactions: {e}")
        return []


def calculate_balance(transactions):
    """Calculate total balance from transactions."""
    balance = 0
    for transaction in transactions:
        if transaction['tipo'] == 'entrada':
            balance += transaction['valor']
        else:  # saida
            balance -= transaction['valor']
    return balance


def check_transport_heuristic(transactions, threshold=1000):
    """Check if transport expenses exceed threshold."""
    transport_total = 0
    for transaction in transactions:
        if transaction['tipo'] == 'saida' and transaction['categoria'] == 'Transporte':
            transport_total += transaction['valor']
    return transport_total > threshold


def main(page: ft.Page):
    """Main Flet application."""
    page.title = "FinHub"
    page.padding = 20
    page.scroll = "adaptive"
    
    # Load data
    script_dir = Path(__file__).parent
    data_file = script_dir.parent / 'data' / 'extrato.json'
    transactions = load_transactions(data_file)
    
    # Calculate totals
    balance = calculate_balance(transactions)
    
    # Check heuristic
    show_insurance_offer = check_transport_heuristic(transactions)
    
    # AlertDialog for actions
    def show_success_dialog(action_name):
        dlg = ft.AlertDialog(
            title=ft.Text(f"{action_name}"),
            content=ft.Text("Operação realizada com sucesso!"),
            actions=[
                ft.TextButton("OK", on_click=lambda e: close_dialog(dlg))
            ],
        )
        page.dialog = dlg
        dlg.open = True
        page.update()
    
    def close_dialog(dialog):
        dialog.open = False
        page.update()
    
    # Header Section
    header = ft.Container(
        content=ft.Column([
            ft.Text("FinHub", size=32, weight=ft.FontWeight.BOLD, color=ft.colors.BLUE_700),
            ft.Text(f"Saldo Total: R$ {balance:.2f}", size=24, weight=ft.FontWeight.W_500, color=ft.colors.GREEN_700 if balance >= 0 else ft.colors.RED_700),
        ]),
        padding=20,
        bgcolor=ft.colors.BLUE_50,
        border_radius=10,
    )
    
    # Actions Row
    actions_row = ft.Row(
        [
            ft.ElevatedButton(
                "Pix",
                icon=ft.icons.PIX,
                on_click=lambda e: show_success_dialog("Pix"),
                style=ft.ButtonStyle(
                    color=ft.colors.WHITE,
                    bgcolor=ft.colors.BLUE_700,
                ),
            ),
            ft.ElevatedButton(
                "Recarga",
                icon=ft.icons.PHONE_ANDROID,
                on_click=lambda e: show_success_dialog("Recarga"),
                style=ft.ButtonStyle(
                    color=ft.colors.WHITE,
                    bgcolor=ft.colors.GREEN_700,
                ),
            ),
            ft.ElevatedButton(
                "Seguros",
                icon=ft.icons.SECURITY,
                on_click=lambda e: show_success_dialog("Seguros"),
                style=ft.ButtonStyle(
                    color=ft.colors.WHITE,
                    bgcolor=ft.colors.ORANGE_700,
                ),
            ),
        ],
        alignment=ft.MainAxisAlignment.SPACE_AROUND,
    )
    
    # Personalization Section (Insurance Offer)
    personalization_section = None
    if show_insurance_offer:
        personalization_section = ft.Container(
            content=ft.Row([
                ft.Icon(ft.icons.LOCAL_OFFER, color=ft.colors.WHITE, size=30),
                ft.Text(
                    "Oferta Especial: Seguro Auto com 20% de desconto!",
                    size=16,
                    weight=ft.FontWeight.BOLD,
                    color=ft.colors.WHITE,
                ),
            ]),
            padding=15,
            bgcolor=ft.colors.DEEP_ORANGE_600,
            border_radius=10,
            margin=ft.margin.only(top=10, bottom=10),
        )
    
    # Transaction List
    transaction_items = []
    for transaction in transactions:
        is_income = transaction['tipo'] == 'entrada'
        icon = ft.icons.ARROW_DOWNWARD if is_income else ft.icons.ARROW_UPWARD
        icon_color = ft.colors.GREEN_700 if is_income else ft.colors.RED_700
        amount_color = ft.colors.GREEN_700 if is_income else ft.colors.RED_700
        amount_prefix = "+" if is_income else "-"
        
        transaction_item = ft.Container(
            content=ft.Row([
                ft.Icon(icon, color=icon_color, size=24),
                ft.Column([
                    ft.Text(transaction['titulo'], size=16, weight=ft.FontWeight.W_500),
                    ft.Row([
                        ft.Text(transaction['categoria'], size=12, color=ft.colors.GREY_700),
                        ft.Text("•", size=12, color=ft.colors.GREY_700),
                        ft.Text(transaction['data'], size=12, color=ft.colors.GREY_700),
                    ]),
                ], spacing=2, expand=True),
                ft.Text(
                    f"{amount_prefix}R$ {transaction['valor']:.2f}",
                    size=16,
                    weight=ft.FontWeight.BOLD,
                    color=amount_color,
                ),
            ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
            padding=15,
            bgcolor=ft.colors.WHITE,
            border=ft.border.all(1, ft.colors.GREY_300),
            border_radius=8,
            margin=ft.margin.only(bottom=8),
        )
        transaction_items.append(transaction_item)
    
    transaction_list_section = ft.Column([
        ft.Text("Transações", size=20, weight=ft.FontWeight.BOLD, color=ft.colors.BLUE_700),
        ft.Column(transaction_items, spacing=0),
    ])
    
    # Build page layout
    page_content = [
        header,
        ft.Container(height=20),  # Spacer
        actions_row,
    ]
    
    if personalization_section:
        page_content.append(personalization_section)
    
    page_content.extend([
        ft.Container(height=20),  # Spacer
        transaction_list_section,
    ])
    
    page.add(ft.Column(page_content, scroll=ft.ScrollMode.AUTO))


if __name__ == "__main__":
    ft.app(target=main)
