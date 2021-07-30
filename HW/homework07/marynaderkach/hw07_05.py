def bank(n, years):
    return round(n * (1 + 0.1) ** years, 2)


print(bank(10000, 6))
