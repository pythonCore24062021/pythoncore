#Task4

n = int(input('Please specify N - '))
m = int(input('Please specify N - '))
char = input('Please specify symbol for borders - ')
char2 = input('Please specify symbol for background - ')
for i in range(n):
    if i == 0 or i == n - 1:
        for j in range(m):
            print(char, end='')
    else:
        print(char, end='')
        for j in range(1, m - 1):
            print(char2, end='')
        print(char, end='')
    print()