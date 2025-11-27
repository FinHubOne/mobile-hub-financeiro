#!/usr/bin/env python3
"""
Financial Hub MVP - Main Script
Loads transaction data and displays balance information.
"""

import json
import os
from pathlib import Path


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


def display_transactions(transactions):
    """
    Display transactions in a formatted manner.
    
    Args:
        transactions (list): List of transaction dictionaries
    """
    if not transactions:
        print("No transactions to display.")
        return
    
    print("\n" + "="*80)
    print(" " * 25 + "FINANCIAL HUB - TRANSACTIONS")
    print("="*80)
    
    for transaction in transactions:
        transaction_id = transaction.get('id', 'N/A')
        transaction_type = transaction.get('type', 'N/A')
        category = transaction.get('category', 'N/A')
        amount = transaction.get('amount', 0)
        date = transaction.get('date', 'N/A')
        description = transaction.get('description', 'N/A')
        
        # Format amount with color indicator (positive/negative)
        amount_str = f"R$ {amount:>8.2f}"
        if amount < 0:
            amount_indicator = "[-]"
        else:
            amount_indicator = "[+]"
        
        print(f"\nID: {transaction_id:>3} | {date} | {transaction_type:>10}")
        print(f"Category: {category:>15} | {amount_indicator} {amount_str}")
        print(f"Description: {description}")
        print("-" * 80)
    
    print("="*80)


def main():
    """
    Main function to run the financial hub application.
    """
    # Get the path to the data file
    script_dir = Path(__file__).parent
    data_file = script_dir.parent / 'data' / 'extrato.json'
    
    print("\n🏦 Welcome to Financial Hub MVP 🏦\n")
    print(f"Loading transactions from: {data_file}")
    
    # Load transactions
    transactions = load_transactions(data_file)
    
    if not transactions:
        print("No transactions loaded. Exiting.")
        return
    
    print(f"Successfully loaded {len(transactions)} transactions.\n")
    
    # Display all transactions
    display_transactions(transactions)
    
    # Calculate and display balance
    balance = calculate_balance(transactions)
    print(f"\n{'='*80}")
    print(f"TOTAL BALANCE: R$ {balance:.2f}")
    print(f"{'='*80}\n")
    
    # Display summary by category
    categories = {}
    for transaction in transactions:
        category = transaction.get('category', 'Uncategorized')
        amount = transaction.get('amount', 0)
        categories[category] = categories.get(category, 0) + amount
    
    print("SUMMARY BY CATEGORY:")
    print("-" * 40)
    for category, total in sorted(categories.items()):
        print(f"{category:>20}: R$ {total:>8.2f}")
    print("-" * 40)


if __name__ == "__main__":
    main()
