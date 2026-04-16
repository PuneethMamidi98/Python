# Arithmetic Product and Conditional Logic

# Write a Python function that accepts two integer numbers.
#  If the product of the two numbers is less than or equal to 1000, 
# return their product; otherwise, return their sum.

def arthimetic(numberOne,numberTwo):
    product = numberOne * numberTwo
    if product <= 1000:
        return product
    else:
        return numberOne + numberTwo


numberOne = int(input("Enter the first number: "))
numberTwo = int(input("Enter the second number: "))

result = arthimetic(numberOne,numberTwo)
print("The result is", result)

