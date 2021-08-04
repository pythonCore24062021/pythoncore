i = 0
count_positive = 1
count_negative = 1
count_positive = float()
count_negative = float()
n = float()
while (n != 0):
    n = float(input("Set the number': "))
    i += 1
    if (n > 0) and (n != 0):
        count_positive += 1
    if (n < 0) and (n != 0):
        count_negative += 1
else:
    if count_positive == 0:
        print(count_positive)
    print(count_negative)
    print(count_positive // (count_positive + count_negative) * 100)
    print(count_negative // (count_positive + count_negative) * 100)

