#У списку знайти елементи, які в ньому зустрічаються тільки один раз, і вивести їх на екран.

mylist = [8, 3, 15, 6, 4, 2, 15, 8]
unique_num = []
for i in range(len(mylist)):
    if mylist.count(i) < 2:
        unique_num.append(i)
        print(unique_num)


def catch_unique(list_in):
   # intilize an empty list
   unq_list = []

   # Check for elements
   for x in list_in:
      # check if exists in unq_list
      if x not in unq_list:
         unq_list.append(x)
         # print list
   for x in unq_list:
      print(x)

Alist = [8, 3, 15, 6, 4, 2, 15, 8]
print("Unique values from the list is")
catch_unique(Alist)


