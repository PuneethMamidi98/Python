# Variable Swapping (The In-Place Method)
# Write a program to swap the values of two variables, a and b, 
# without using a third temporary variable.


a,b = 5 , 10
print(f"Before Swap: a = {a}, b = {b}")

a,b  = b,a
print(f"After Swap: a = {a}, b = {b}")

