def calculate_total_cost(base_price):
    tourism_levy = base_price * 0.01
    vat = base_price * 0.15
    total = base_price + tourism_levy + vat
    return round(total, 2)
