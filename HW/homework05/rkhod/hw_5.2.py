# Task2

a=0
for i in range(0,10):
    i = int(input(f"Set any number ... \n"))
    if i%5==0:
        a+=1
print(f"the amount of number aliquot to five = {a}")