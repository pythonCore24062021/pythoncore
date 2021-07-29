'''
3. Вивести на екран таблицю множення (від 1 до 9).
'''

print ('  |', end='')
for i in range(1, 10):
    print(f"\t{i}", end='')
print('\n' + '=' * 80)

for i in range(1, 10):
    print(f"{i} |", end='')
    for j in range(1, 10):
        # print(f"{i}x{j}\t{i * j}")
        print(f"\t{i * j}", end='')
    print()
