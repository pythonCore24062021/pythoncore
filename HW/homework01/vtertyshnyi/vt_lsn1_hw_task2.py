'''
Output question:
    - "What is your name?"
    - "How old are you?"
    - "Where do you live?". 

Read the answer of user and output next information: 
    - "Hello, (answer(name))"
    - "Your age is (answer(age))"
    - "You live in (answer(city))"
'''

print("What is your name?");
while True:
    try:
        name = str(input());
        if not name: raise Exception("Name should have at least 1 charachter, please try again:");
        break;
    except Exception as msg:
        print(msg);

print("How old are you?");
while True:
    try:
        age = int(input());
        if age < 1: raise Exception("Your age definitely must be greater than 0, please try agian:");
        break;
    except ValueError:
        print("Ops... Age could be only a number, please try again:");
    except Exception as msg:
        print(msg);
        
print("Where do you live?")
while True:
    try:
        city = str(input());
        if not city: raise Exception("City should have at least 1 charachter, please try again:");
        break;
    except Exception as msg:
        print(msg);

print("Hello,", name);
print("Your age is", age);
print("You live in", city);
