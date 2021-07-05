''' Output question “What is your name?“,“How old are you?“, Where do you live?“.
Read the answer of user and output next information: “Hello,
(answer(name))“,“Your age is  (answer(age))“, “You live in  (answer(city))“ '''

name = str(input("What is your name?\n"))
age = int(input("How old are you?\n")) 
city = str(input("Where do you live?\n")) 
print("\n"+"Hello,"+ name.title() +"\n"+"Your age is "
    + str(age) +"\n"+"You live in "+ city.title() + "\n")