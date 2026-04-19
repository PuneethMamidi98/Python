try:
    numberOne = int(input("Enter the first number: "))
    numberTwo = int(input("Enter the second number: "))
    divide = numberOne / numberTwo
    print(f"The result : {divide}")
except ValueError:
    print("Please enter valid number")
except ZeroDivisionError:
    print("Cannot divide by zero!")
finally:
    print("Calculation Completed")






