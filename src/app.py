"""
Mobile Hub Financeiro - MVP usando Flet
Aplicação desktop/mobile para gestão financeira com extrato inteligente
"""

import json
from pathlib import Path
import flet as ft


def load_transactions():
    """Carrega transações do arquivo JSON"""
    script_dir = Path(__file__).parent
    data_file = script_dir.parent / 'data' / 'extrato.json'
    
    try:
        with open(data_file, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        print(f"Erro ao carregar dados: {e}")
        return []


def calculate_balance(transactions):
    """Calcula o saldo total (entradas - saídas)"""
    total = sum(t['valor'] for t in transactions)
    return total


def calculate_expenses_by_category(transactions):
    """Calcula gastos por categoria"""
    expenses = {}
    for t in transactions:
        if t['valor'] < 0:
            categoria = t['categoria']
            expenses[categoria] = expenses.get(categoria, 0) + abs(t['valor'])
    return expenses


def should_show_auto_insurance(transactions):
    """Verifica se deve mostrar oferta de seguro auto (Transporte > 30%)"""
    expenses = calculate_expenses_by_category(transactions)
    total_expenses = sum(expenses.values())
    
    if total_expenses == 0:
        return False
    
    transporte = expenses.get('Transporte', 0)
    percentage = transporte / total_expenses
    
    return percentage > 0.3


def main(page: ft.Page):
    """Função principal da aplicação Flet"""
    page.title = "Hub Financeiro Móvel"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = 20
    page.bgcolor = "#F5F5F5"
    
    # Cores modernas (roxo inspirado no Nubank)
    PRIMARY_COLOR = "#820AD1"
    SECONDARY_COLOR = "#6A0DAD"
    SUCCESS_COLOR = "#00C853"
    DANGER_COLOR = "#D32F2F"
    CARD_BG = "#FFFFFF"
    
    # Carregar dados
    transactions = load_transactions()
    balance = calculate_balance(transactions)
    show_offer = should_show_auto_insurance(transactions)
    
    # Função para mostrar diálogo de ação rápida
    def show_action_dialog(action_name):
        def close_dialog(e):
            dialog.open = False
            page.update()
        
        dialog = ft.AlertDialog(
            title=ft.Text(f"{action_name}"),
            content=ft.Text(f"Operação de {action_name} simulada com sucesso!"),
            actions=[
                ft.TextButton("OK", on_click=close_dialog)
            ],
            actions_alignment=ft.MainAxisAlignment.END,
        )
        
        page.dialog = dialog
        dialog.open = True
        page.update()
    
    # Header com saldo
    header = ft.Container(
        content=ft.Column([
            ft.Text(
                "💰 Hub Financeiro",
                size=28,
                weight=ft.FontWeight.BOLD,
                color=PRIMARY_COLOR,
            ),
            ft.Container(height=10),
            ft.Text("Saldo Total", size=16, color="#666"),
            ft.Text(
                f"R$ {balance:,.2f}",
                size=36,
                weight=ft.FontWeight.BOLD,
                color=SUCCESS_COLOR if balance >= 0 else DANGER_COLOR,
            ),
        ]),
        padding=20,
        bgcolor=CARD_BG,
        border_radius=10,
    )
    
    # Menu de ações rápidas
    quick_actions = ft.Container(
        content=ft.Column([
            ft.Text(
                "Ações Rápidas",
                size=20,
                weight=ft.FontWeight.BOLD,
                color="#333",
            ),
            ft.Container(height=10),
            ft.Row([
                ft.ElevatedButton(
                    "💸 Pix",
                    icon=ft.icons.PAYMENT,
                    on_click=lambda _: show_action_dialog("Pix"),
                    bgcolor=PRIMARY_COLOR,
                    color="white",
                    style=ft.ButtonStyle(
                        padding=20,
                    ),
                ),
                ft.ElevatedButton(
                    "📱 Recarga",
                    icon=ft.icons.PHONE_ANDROID,
                    on_click=lambda _: show_action_dialog("Recarga"),
                    bgcolor=PRIMARY_COLOR,
                    color="white",
                    style=ft.ButtonStyle(
                        padding=20,
                    ),
                ),
                ft.ElevatedButton(
                    "🛡️ Seguros",
                    icon=ft.icons.SECURITY,
                    on_click=lambda _: show_action_dialog("Seguros"),
                    bgcolor=PRIMARY_COLOR,
                    color="white",
                    style=ft.ButtonStyle(
                        padding=20,
                    ),
                ),
            ],
            alignment=ft.MainAxisAlignment.SPACE_AROUND,
            ),
        ]),
        padding=20,
        bgcolor=CARD_BG,
        border_radius=10,
    )
    
    # Card de oferta especial (se aplicável)
    offer_card = None
    if show_offer:
        offer_card = ft.Container(
            content=ft.Row([
                ft.Icon(ft.icons.DIRECTIONS_CAR, color="white", size=40),
                ft.Column([
                    ft.Text(
                        "🎉 Oferta Especial!",
                        size=18,
                        weight=ft.FontWeight.BOLD,
                        color="white",
                    ),
                    ft.Text(
                        "Seguro Auto com 20% de desconto para você!",
                        size=14,
                        color="white",
                    ),
                ],
                expand=True,
                ),
            ]),
            padding=20,
            bgcolor="#FF6B35",
            border_radius=10,
        )
    
    # Extrato inteligente
    transaction_cards = []
    
    # Ordenar transações por data (mais recentes primeiro)
    sorted_transactions = sorted(transactions, key=lambda x: x['data'], reverse=True)
    
    for t in sorted_transactions:
        is_income = t['valor'] > 0
        color = SUCCESS_COLOR if is_income else DANGER_COLOR
        icon = "⬆️" if is_income else "⬇️"
        
        card = ft.Container(
            content=ft.Row([
                ft.Column([
                    ft.Text(
                        f"{icon} {t['titulo']}",
                        size=16,
                        weight=ft.FontWeight.BOLD,
                        color="#333",
                    ),
                    ft.Text(
                        f"{t['categoria']} • {t['data']}",
                        size=12,
                        color="#666",
                    ),
                ],
                expand=True,
                ),
                ft.Text(
                    f"R$ {abs(t['valor']):,.2f}",
                    size=16,
                    weight=ft.FontWeight.BOLD,
                    color=color,
                ),
            ]),
            padding=15,
            bgcolor=CARD_BG,
            border_radius=8,
            border=ft.border.all(1, "#E0E0E0"),
        )
        transaction_cards.append(card)
    
    # Construir lista de componentes da tela
    content_list = [
        header,
        ft.Container(height=20),
        quick_actions,
    ]
    
    # Adicionar card de oferta se aplicável
    if offer_card:
        content_list.append(ft.Container(height=20))
        content_list.append(offer_card)
    
    # Adicionar extrato
    content_list.append(ft.Container(height=20))
    content_list.append(
        ft.Text(
            "📋 Extrato Inteligente",
            size=20,
            weight=ft.FontWeight.BOLD,
            color="#333",
        )
    )
    content_list.append(ft.Container(height=10))
    
    # Adicionar cards de transações
    for card in transaction_cards:
        content_list.append(card)
        content_list.append(ft.Container(height=10))
    
    # Criar coluna scrollable com todo o conteúdo
    page.add(
        ft.Container(
            content=ft.Column(
                controls=content_list,
                scroll=ft.ScrollMode.AUTO,
            ),
            expand=True,
        )
    )


if __name__ == "__main__":
    ft.app(target=main)
