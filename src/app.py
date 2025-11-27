#!/usr/bin/env python3
"""
Mobile Financial Hub MVP - Flet Application
A mobile-first financial hub with personalized insurance offers.
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
    except FileNotFoundError:
        print(f"Error: File '{filepath}' not found.")
        return []
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON format in '{filepath}'.")
        return []


def calculate_balance(transactions):
    """Calculate the total balance from transactions."""
    return sum(t.get('amount', 0) for t in transactions)


def calculate_category_totals(transactions):
    """Calculate total spending per category."""
    categories = {}
    for t in transactions:
        category = t.get('category', 'Uncategorized')
        amount = t.get('amount', 0)
        if amount < 0:  # Only count expenses
            categories[category] = categories.get(category, 0) + abs(amount)
    return categories


def should_show_insurance_offer(transactions):
    """
    Heuristic logic: Show car insurance offer if transport spending > 30% of total expenses.
    """
    category_totals = calculate_category_totals(transactions)
    total_expenses = sum(category_totals.values())
    
    if total_expenses == 0:
        return False
    
    transport_expenses = category_totals.get('Transporte', 0)
    transport_percentage = (transport_expenses / total_expenses) * 100
    
    return transport_percentage > 30


def show_success_modal(page, title, message):
    """Show a success modal dialog."""
    def close_dialog(e):
        dialog.open = False
        page.update()
    
    dialog = ft.AlertDialog(
        modal=True,
        title=ft.Text(title),
        content=ft.Text(message),
        actions=[
            ft.TextButton("OK", on_click=close_dialog),
        ],
        actions_alignment=ft.MainAxisAlignment.END,
    )
    
    page.dialog = dialog
    dialog.open = True
    page.update()


def main(page: ft.Page):
    """Main application entry point."""
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
    show_insurance = should_show_insurance_offer(transactions)
    
    # Header
    header = ft.Container(
        content=ft.Column([
            ft.Text("🏦 Mobile Hub Financeiro", size=24, weight=ft.FontWeight.BOLD),
            ft.Text("Seu assistente financeiro pessoal", size=14, color=ft.colors.GREY_700),
        ]),
        padding=ft.padding.only(bottom=20),
    )
    
    # Balance Card
    balance_color = ft.colors.GREEN if balance >= 0 else ft.colors.RED
    balance_card = ft.Container(
        content=ft.Column([
            ft.Text("Saldo Total", size=16, color=ft.colors.GREY_700),
            ft.Text(
                f"R$ {balance:.2f}",
                size=32,
                weight=ft.FontWeight.BOLD,
                color=balance_color
            ),
        ]),
        bgcolor=ft.colors.BLUE_50,
        border_radius=10,
        padding=20,
        margin=ft.margin.only(bottom=20),
    )
    
    # Action Buttons
    def on_pix_click(e):
        show_success_modal(page, "Pix", "Transferência Pix realizada com sucesso!")
    
    def on_recarga_click(e):
        show_success_modal(page, "Recarga", "Recarga realizada com sucesso!")
    
    def on_seguros_click(e):
        show_success_modal(page, "Seguros", "Seguro contratado com sucesso!")
    
    action_buttons = ft.Row(
        [
            ft.ElevatedButton(
                "Pix",
                icon=ft.Icons.ATTACH_MONEY,
                on_click=on_pix_click,
                bgcolor=ft.colors.BLUE_400,
                color=ft.colors.WHITE,
            ),
            ft.ElevatedButton(
                "Recarga",
                icon=ft.Icons.PHONE_ANDROID,
                on_click=on_recarga_click,
                bgcolor=ft.colors.GREEN_400,
                color=ft.colors.WHITE,
            ),
            ft.ElevatedButton(
                "Seguros",
                icon=ft.Icons.SECURITY,
                on_click=on_seguros_click,
                bgcolor=ft.colors.ORANGE_400,
                color=ft.colors.WHITE,
            ),
        ],
        alignment=ft.MainAxisAlignment.SPACE_AROUND,
    )
    
    action_buttons_container = ft.Container(
        content=action_buttons,
        margin=ft.margin.only(bottom=20),
    )
    
    # Insurance Offer Banner (conditional)
    insurance_banner = None
    if show_insurance:
        insurance_banner = ft.Container(
            content=ft.Row([
                ft.Icon(ft.Icons.DIRECTIONS_CAR, color=ft.colors.WHITE, size=40),
                ft.Column([
                    ft.Text(
                        "🎯 Oferta Especial: Seguro Auto",
                        size=18,
                        weight=ft.FontWeight.BOLD,
                        color=ft.colors.WHITE,
                    ),
                    ft.Text(
                        "Seus gastos com transporte estão altos! Proteja seu veículo com até 30% de desconto.",
                        size=12,
                        color=ft.colors.WHITE,
                    ),
                ], expand=True),
            ]),
            bgcolor=ft.colors.ORANGE_600,
            border_radius=10,
            padding=15,
            margin=ft.margin.only(bottom=20),
        )
    
    # Transactions List
    transaction_items = []
    for t in sorted(transactions, key=lambda x: x.get('date', ''), reverse=True):
        transaction_id = t.get('id', 'N/A')
        transaction_type = t.get('type', 'N/A')
        category = t.get('category', 'N/A')
        amount = t.get('amount', 0)
        date = t.get('date', 'N/A')
        description = t.get('description', 'N/A')
        
        # Icon based on category
        icon_map = {
            'Alimentação': ft.Icons.RESTAURANT,
            'Transporte': ft.Icons.DIRECTIONS_CAR,
            'Lazer': ft.Icons.MOVIE,
            'Saúde': ft.Icons.MEDICAL_SERVICES,
            'Educação': ft.Icons.SCHOOL,
            'Serviços': ft.Icons.BUILD,
            'Transferência': ft.Icons.ATTACH_MONEY,
        }
        icon = icon_map.get(category, ft.Icons.PAYMENT)
        
        # Color based on amount
        amount_color = ft.colors.GREEN if amount >= 0 else ft.colors.RED
        amount_text = f"+R$ {amount:.2f}" if amount >= 0 else f"-R$ {abs(amount):.2f}"
        
        transaction_card = ft.Container(
            content=ft.Row([
                ft.Icon(icon, color=ft.colors.BLUE_400, size=30),
                ft.Column([
                    ft.Text(description, weight=ft.FontWeight.BOLD, size=14),
                    ft.Text(f"{category} • {date}", size=12, color=ft.colors.GREY_600),
                ], expand=True),
                ft.Text(
                    amount_text,
                    size=16,
                    weight=ft.FontWeight.BOLD,
                    color=amount_color
                ),
            ]),
            bgcolor=ft.colors.WHITE,
            border=ft.border.all(1, ft.colors.GREY_300),
            border_radius=8,
            padding=15,
            margin=ft.margin.only(bottom=10),
        )
        transaction_items.append(transaction_card)
    
    transactions_header = ft.Text(
        "Extrato",
        size=20,
        weight=ft.FontWeight.BOLD,
        margin=ft.margin.only(bottom=10),
    )
    
    # Assemble the page
    page_content = [
        header,
        balance_card,
        action_buttons_container,
    ]
    
    if insurance_banner:
        page_content.append(insurance_banner)
    
    page_content.extend([
        transactions_header,
        *transaction_items,
    ])
    
    page.add(ft.Column(page_content, scroll=ft.ScrollMode.AUTO))


if __name__ == "__main__":
    ft.app(target=main)
