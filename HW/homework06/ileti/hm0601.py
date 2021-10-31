import random
randomlist = random.sample(range(10, 30), 5)
print(randomlist)
randomlist_sum = sum(randomlist)
print(f"Sum of the first list: {randomlist_sum} ")

number_list = []
n = int(input("Enter the list size "))

print("\n")
for i in range(0, n):
    print("Enter number at index", i, )
    item = int(input())
    number_list.append(item)
print("User list is ", number_list)

number_list_sum  = sum(number_list)
print(f"Sum of user list: {number_list_sum}")
list_3 = randomlist_sum + number_list_sum
print(f"Sum of random list and user list = {list_3}")
