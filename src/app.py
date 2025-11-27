#!/usr/bin/env python3
"""
Mobile Hub Financeiro - Flet UI Application
A financial hub MVP with personalized offers based on spending patterns.
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
    """Calculate the total balance from transactions."""
    return sum(t.get('amount', 0) for t in transactions)


def calculate_transporte_percentage(transactions):
    """Calculate percentage of expenses spent on Transporte."""
    total_expenses = sum(t['amount'] for t in transactions if t['amount'] < 0)
    transporte_expenses = sum(
        t['amount'] for t in transactions 
        if t.get('category') == 'Transporte' and t['amount'] < 0
    )
    
    if total_expenses == 0:
        return 0
    
    return (abs(transporte_expenses) / abs(total_expenses)) * 100


def main(page: ft.Page):
    """Main Flet application."""
    page.title = "Mobile Hub Financeiro"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = 20
    page.scroll = ft.ScrollMode.AUTO
    
    # Load transactions
    script_dir = Path(__file__).parent
    data_file = script_dir.parent / 'data' / 'extrato.json'
    transactions = load_transactions(data_file)
    
    # Calculate metrics
    balance = calculate_balance(transactions)
    transporte_percentage = calculate_transporte_percentage(transactions)
    
    # Function to show alert dialog
    def show_alert(e, feature_name):
        dlg = ft.AlertDialog(
            title=ft.Text(feature_name),
            content=ft.Text("Funcionalidade simulada com sucesso!"),
            actions=[
                ft.TextButton("OK", on_click=lambda _: close_dialog(dlg))
            ],
        )
        page.dialog = dlg
        dlg.open = True
        page.update()
    
    def close_dialog(dlg):
        dlg.open = False
        page.update()
    
    # Action buttons
    action_buttons = ft.Row(
        [
            ft.ElevatedButton(
                "Pix",
                icon=ft.icons.PIX,
                on_click=lambda e: show_alert(e, "Pix"),
                style=ft.ButtonStyle(
                    color=ft.colors.WHITE,
                    bgcolor=ft.colors.BLUE_700,
                ),
            ),
            ft.ElevatedButton(
                "Recarga",
                icon=ft.icons.PHONE_ANDROID,
                on_click=lambda e: show_alert(e, "Recarga"),
                style=ft.ButtonStyle(
                    color=ft.colors.WHITE,
                    bgcolor=ft.colors.GREEN_700,
                ),
            ),
            ft.ElevatedButton(
                "Seguros",
                icon=ft.icons.SECURITY,
                on_click=lambda e: show_alert(e, "Seguros"),
                style=ft.ButtonStyle(
                    color=ft.colors.WHITE,
                    bgcolor=ft.colors.ORANGE_700,
                ),
            ),
        ],
        alignment=ft.MainAxisAlignment.SPACE_EVENLY,
    )
    
    # Balance card
    balance_card = ft.Card(
        content=ft.Container(
            content=ft.Column(
                [
                    ft.Text(
                        "Saldo Total",
                        size=16,
                        weight=ft.FontWeight.W_500,
                        color=ft.colors.GREY_700,
                    ),
                    ft.Text(
                        f"R$ {balance:.2f}",
                        size=32,
                        weight=ft.FontWeight.BOLD,
                        color=ft.colors.GREEN if balance >= 0 else ft.colors.RED,
                    ),
                ],
                spacing=5,
            ),
            padding=20,
        ),
        elevation=2,
    )
    
    # Special offer card (only if Transporte > 30%)
    special_offer = None
    if transporte_percentage > 30:
        special_offer = ft.Card(
            content=ft.Container(
                content=ft.Column(
                    [
                        ft.Row(
                            [
                                ft.Icon(ft.icons.LOCAL_OFFER, color=ft.colors.ORANGE),
                                ft.Text(
                                    "Oferta Especial",
                                    size=18,
                                    weight=ft.FontWeight.BOLD,
                                    color=ft.colors.ORANGE,
                                ),
                            ],
                            spacing=10,
                        ),
                        ft.Text(
                            "Seguro Auto com 20% de desconto!",
                            size=16,
                            color=ft.colors.BLACK87,
                        ),
                    ],
                    spacing=10,
                ),
                padding=20,
                bgcolor=ft.colors.ORANGE_50,
            ),
            elevation=4,
        )
    
    # Transaction list
    transaction_items = []
    for t in transactions:
        amount = t.get('amount', 0)
        is_income = amount >= 0
        
        transaction_items.append(
            ft.Card(
                content=ft.Container(
                    content=ft.Row(
                        [
                            ft.Column(
                                [
                                    ft.Text(
                                        t.get('description', 'N/A'),
                                        size=14,
                                        weight=ft.FontWeight.W_500,
                                    ),
                                    ft.Text(
                                        f"{t.get('category', 'N/A')} • {t.get('date', 'N/A')}",
                                        size=12,
                                        color=ft.colors.GREY_600,
                                    ),
                                ],
                                spacing=2,
                                expand=True,
                            ),
                            ft.Text(
                                f"R$ {amount:.2f}",
                                size=16,
                                weight=ft.FontWeight.BOLD,
                                color=ft.colors.GREEN if is_income else ft.colors.RED,
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    ),
                    padding=15,
                ),
                elevation=1,
            )
        )
    
    # Build the page
    page_content = [
        ft.Text(
            "🏦 Mobile Hub Financeiro",
            size=28,
            weight=ft.FontWeight.BOLD,
            text_align=ft.TextAlign.CENTER,
        ),
        ft.Divider(height=20, color=ft.colors.TRANSPARENT),
        action_buttons,
        ft.Divider(height=20, color=ft.colors.TRANSPARENT),
        balance_card,
        ft.Divider(height=20, color=ft.colors.TRANSPARENT),
    ]
    
    # Add special offer if applicable
    if special_offer:
        page_content.append(special_offer)
        page_content.append(ft.Divider(height=20, color=ft.colors.TRANSPARENT))
    
    # Add transactions section
    page_content.extend([
        ft.Text(
            "Transações",
            size=20,
            weight=ft.FontWeight.BOLD,
        ),
        ft.Divider(height=10, color=ft.colors.TRANSPARENT),
    ])
    
    page_content.extend(transaction_items)
    
    # Add all content to page
    page.add(ft.Column(page_content, spacing=10))


if __name__ == "__main__":
    ft.app(target=main)
