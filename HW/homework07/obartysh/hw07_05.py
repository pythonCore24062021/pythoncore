def bank(a, years):
    for year in range(years):
        a *= 1.1
    return a

b = float(input("enter $ "))
n = int(input("enter year to calculate % "))
print(bank(b,n))

