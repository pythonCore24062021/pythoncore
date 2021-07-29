P = 6
H = 7
i = 0
n = int()
sum = 0
product = 1
count = 0
while (n != P) and (n != H):
    n = int(input("Enter the number: "))
    i += 1
    if n < P:
        sum += n
    if n > H:
        product *= n
    if n >= P and n <= H:
        count +=1
else:
   print(sum)
   print(product)
   print(count)
