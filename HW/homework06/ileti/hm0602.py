number_list = []
x = int(input("Enter number at index: "))

print("\n")
for i in range(0, x):
    print("Enter number at index", i, )
    item = float(input())
    number_list.append(item)
print("User list is ", number_list)
suma  = sum(number_list)
print(f"Sum  = {suma}")

def multiplyList(number_list):
    result  = 1
    for item in number_list:
        result  = result * item
    return result
print("multiplying:")
print(multiplyList(number_list))