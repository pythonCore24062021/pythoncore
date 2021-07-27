n = int(input("enter width: "))
m = int(input("enter height: "))

for i in range(m):
    if i == 0 or i == m - 1:
        for j in range(n):
            print('*', end=' ')
    else:
        print('*', end=' ')
        for j in range(1, n - 1):
            print('#', end=' ')
        print('*', end=' ')
    print()
