# Змінній var_int надайте значення 10, var_float - значення 8.4, var_str - "No".
# Змініть значення, збережене в змінній var_int, збільшивши його в 3.5 рази, результат надайте змінній var_big.
# Змініть значення, збережене в змінній var_float, зменшивши його на одиницю, результат надайте тій же змінній.
# Розділіть var_int на var_float, а потім var_big на var_float. Результат запишіть у змінні var_div1 та var_div2 відповідно.
# Змініть значення змінної var_str на "NoNoYesYesYes". При формуванні нового значення використовуйте операції конкатенації (+) і повторення рядка (*).
# Виведіть значення всіх змінних.
var_int = 10
var_float = 8.4
var_str = "No"

var_big = var_int*3.5
var_float = var_float-1
var_div1 = var_int / var_float
var_div2 = var_big / var_float
print(var_div1, var_div2)
var_str = var_str*2+'Yes'*3
print('var_str =', var_str, "\n",
      "var_int=", var_int, "\n",
      "var_float=", var_float, "\n",
      "var_big=", var_big, "\n",
      "var_div1=", var_div1, "\n",
      "var_div2=", var_div2, "\n",
      )


