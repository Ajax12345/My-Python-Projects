def what_type():
    while True:
        ans = raw_input("Enter the type of operation you would like to use i.e add, subtract, multiply, or divide: ")
        if ans == "add":
            add()
        elif ans == "subtract":
            subtract()

        elif ans == "multiply":
            multiply()

        elif ans == "divide":
            divide()

        answer = raw_input("Do you want to run again? ")
        if answer == 'y' or answer == 'yes':
            continue

        else:
            print "Thank you for trying our new calculator"
            break

def add():
    x = input()
    y = input()
    sum = x + y
    print sum

def subtract():
    x = input()
    y = input()
    remainder = x - y
    print remainder

def multiply():
    x = input()
    y = input()
    product = x*y
    print product

def divide():
    x = input()
    y = input()
    quotient = round(x/y, 5)
    print quotient


what_type()
