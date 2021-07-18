#Згенерувати 20 випадкових цілих чисел в діапазоні від -5 до 4, записати їх в список. Порахувати кількість додатних, від’ємних
#і нульових елементів. Вивести на екран елементи списку і пораховані кількості.
count_positive= 0
count_negative = 0
count_null = 0
import random
randomlist = random.sample(range(-5, 20), 20)
print(randomlist)
for x in randomlist:
    if x > 0:
        count_positive +=1
    if x < 0:
        count_negative +=1
    if x == 0:
        count_null += 1
print(count_positive, count_negative, count_null)
