# String Slicing and Substring Removal

# Write a function to remove characters from a string starting from 
# index 0 up to n and return a new string.


def remove_chars(text,index):
    print(f"Original String : {text}")
    return text[index:]


text = input("Enter the text: ")
index = int(input("Enter the index: "))
print("Removing characters from a string")
result = remove_chars(text,index)
print(result)

