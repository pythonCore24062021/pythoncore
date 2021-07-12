import random

# Set the four number integer
int1=(random.randint(1000,9999))
int1=str(int1)
print('The number is ' + int1)

# Searching for a product of numbers
a=int(int1[0])
b=int(int1[1])
c=int(int1[2])
d=int(int1[3])
e=a*b*c*d
print("The product of numbers is equal to " + str(e))

# Creating a list to operate with
f=[a,b,c,d]
f.reverse()
print("The reverce order of the numbers in integer is " + str(f))
f.sort()
print("The ASC sorted order of the numbers in integer is " + str(f))