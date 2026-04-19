# Simple Calculator

#Objective: Create a basic calculator that can perform addition, subtraction, 
# multiplication, and division.

# Welcome

print("=====================================")
print("          SIMPLE CALCULATOR          ")
print("=====================================")

def add(numberOne,numberTwo):
    return numberOne + numberTwo

def subtract(numberOne,numberTwo):
    return numberOne - numberTwo

def multiply(numberOne,numberTwo):
    return numberOne * numberTwo

def divide(numberOne,numberTwo):
    return round(numberOne / numberTwo,2)


# User Input - two numbers and operator
while True:
    try:
        numberOne = int(input("Enter the first number: "))
        numberTwo = int(input("Enter the second number: "))
        operator = input("Enter the operator: ")
        if operator == "":
            print("Please enter the operator")
        else:
            # call the appropriate function based on the operator.
            if operator == "+":
                print(f"{numberOne} {operator} {numberTwo} = {add(numberOne,numberTwo)}")
            elif operator == "-":
                print(f"{numberOne} {operator} {numberTwo} = {subtract(numberOne,numberTwo)}")
            elif operator == "*":
                print(f"{numberOne} x {numberTwo} = {multiply(numberOne,numberTwo)}")
            elif operator == "/":
                try:
                    print(f"{numberOne} {operator} {numberTwo} = {divide(numberOne,numberTwo)}")
                except ZeroDivisionError:
                    print("Cannot divide by zero!")       
            else:
                print("Invalid operator")    
    except ValueError:
        print("Please enter valid number")    

    






