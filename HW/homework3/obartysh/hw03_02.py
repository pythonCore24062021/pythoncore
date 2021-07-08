print("введіть число");
a = input();
res = list(map(int, str(a)));
suma=0;
for n in range(0, len(res)):
    suma = suma + res[n]
print("Sum of all elements in given list: ", suma);
reversed_list = res[::-1];
print('reversed List:', reversed_list);
res.sort();
print(res);

