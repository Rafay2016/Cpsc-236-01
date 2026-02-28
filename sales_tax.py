# sales_tax.py

TAX_RATE = 0.06

def calculate_tax(total):
    tax = total * TAX_RATE
    return round(tax, 2)

def calculate_total_after_tax(total):
    tax = calculate_tax(total)
    total_after_tax = total + tax
    return round(total_after_tax, 2)