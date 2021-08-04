#Заповнити список дійсними числами введенням з клавіатури. Порахувати суму і добуток елементів списку.
#Вивести на екран сам список, отримані суму і добуток його елементів.
product = 1
mylist = [5, 6, 7 , 8, 10]
Sum = sum(mylist)
sum(mylist)
print(Sum)

lst = []
num = int(input('How many numbers: '))
for n in range(num):
    numbers = int(input('Enter number '))
    lst.append(numbers)
print("Sum of elements in given list is :", sum(lst))
for x in mylist:
    product *=x
    print(product)