# Cumulative Sum of a Range

# Iterate through the first 10 numbers (0–9). In each iteration, 
# print the current number, the previous number, and their sum

previous_number = 0

for i in range(10):
    print(f"Current Number {i} Previous Number {previous_number} Sum {i+previous_number}")
    previous_number = i
    



