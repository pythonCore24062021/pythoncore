for i in range(10):
        if i==0 or i==9:
            for j in range(20):
                print("-", end=' ')
        else:
            print('|',end='')
            for j in range(1,19):
                print('*',end=' ')
            print('',end='|')
        print()


w = int(input("Enter the width: "))
h = int(input("Enter the height: "))
for i in range(0, h):
    print("|",end=' ')
    if i == 0 or i == h - 1:
       for i in range(1, w):
        print("-", end = " ")
        if i == 0 or i == w - 1:
                print(" ", end="|")
    else:
       print(" ")
