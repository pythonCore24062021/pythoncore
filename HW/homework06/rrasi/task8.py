#У списку випадкових цілих чисел поміняти місцями мінімальний і максимальний елементи.

a = [3, 4, 5, 6, 1]
b = [-5000 if x == min(a) else 5000 if x == max(a) else x for x in a]
print(max(a))
print(min(a))
print(a)
print(b)

def swap(a) :
  max_index=a.index(max(a))
  min_index=a.index(min(a))
  ma=max(a)
  mi=min(a)
  a[max_index]=mi
  a[min_index]=ma
a=[3,4,5,2,1]
swap(a)
print(a)

data=[3,4, 5, 2, 1]
max_va=data.index(max(data))
min_va=data.index(min(data))
data[max_va],data[min_va]=data[min_va],data[max_va]
print(data)