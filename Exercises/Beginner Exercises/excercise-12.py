# List Comparison and Boolean Logic

# Write a function to return True if the first and last number 
# of a given list is the same. If the numbers are different, return False.


def item_comparsion(list):
    if list[0] == list[-1]:
        return True
    else:
        return False
    
numbers_x = [75,65,35,75,30]
numbers_y = [10,20,30,40,10]
result_x = item_comparsion(numbers_x)
print(f"Given list : {numbers_x} | result is {result_x}")
result_y = item_comparsion(numbers_y)
print(f"Given list : {numbers_y} | result is {result_y}")

        
