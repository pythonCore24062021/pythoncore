# Task 5

def bank(n, years):
    for i in range(years):
        n = n + (n / 100 * 10)
    return n


n = int(input("enter the deposit amount \n"))
years = int(input("enter the deposit period in years \n"))
print(f"The resulting sum is equal to {bank(n, years)}")
