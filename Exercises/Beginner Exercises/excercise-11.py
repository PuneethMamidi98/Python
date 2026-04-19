# Removing Duplicates from a List

# Write a script that takes a list containing duplicate items and 
# returns a new list with only unique elements

data = [1,2,2,3,4,4,4,5,5]
print(f"Original List: {data}")

# 1. using dict.fromkeys
# result = list(dict.fromkeys(data))
# print(f"Unique List: {result}")

# # 2. using OrderedDict.fromkeys
# from collections import OrderedDict
# result = list(OrderedDict.fromkeys(data))
# print(f"Unique List: {result}")

# # 3. using sets
# result = list(set(data))
# print(f"Unique List : {result}")

# 4. for loop - good for short list 
unique_list = []
for item in data:
    if item not in unique_list:
        unique_list.append(item)
    
print(f"Unique List : {unique_list}" )
