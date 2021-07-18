P = 5
H = 8
i = 0
n = int()
suma = 0
dobutok = 1
while (n != P) and (n != H):
    n = int(input("Set the number': "))
    i += 1
    if n < P:
        suma += n
#        print("suma = ",  n + P)
    if n > H:
        dobutok *= n
else:
   print(suma)
   print(dobutok)
