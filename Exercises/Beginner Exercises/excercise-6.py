# Calculating  Factorial with a loop

# Write a program that calculates the factorial of a given number 
# (e.g., 5!) using a for loop.

n = int(input("Enter the number : "))
factorial = n
for i in range(1,n):
    factorial *= i

print(f"factorial of {n} is {factorial}")    




