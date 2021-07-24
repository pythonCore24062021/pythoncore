
p = int(input("provide P"))
h = int(input("provide H"))
s = 0
m = 1

for i in range(p,h+1):
    s = s+i
print(s)
while p != h:
    p = int(input("provide P"))
    if p > s:
        print(s)
    elif p ==h:
        break
print(s)

