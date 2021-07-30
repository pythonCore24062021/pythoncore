# Task2

list1 = []
start = 0
end = 5
while start < end:
    list1.append(float(input("Please, enter five floats - ")))
    start += 1
a = 1
for i in range(len(list1)):
    a *= list1[i]
print(f" the list is - {list1}")
print(f" the summa = {sum(list1)}")
print(f" the product = {a}")
