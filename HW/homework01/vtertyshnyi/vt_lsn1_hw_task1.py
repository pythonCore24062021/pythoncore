'''
Define variables a and b. Read values a and b from console and calculate:
    - a + b
    - a - b
    - a * b
    - a / b

Output obtained results
'''

print("Enter values for \"a\" and \"b\" (numers are allowed only)");
while True:
    try:
        a = float(input());
        break;
    except ValueError:
        print("Ops.. That's not allowed value for \"a\". Please try again:");

while True:
    try:
        b = float(input());
        break;
    except ValueError:
        print("Ops.. That's not allowed value for \"b\". Please try again:");

print("Thanks for your inputs! Results are:");
print("a + b = ", a + b);
print("a - b = ", a - b);
print("a * b = ", a * b);

try:
    print("a / b = ", a / b)
except ZeroDivisionError:
        print("a / b = unable to devide by 0")
