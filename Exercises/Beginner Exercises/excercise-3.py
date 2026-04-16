# String Indexing and Even Slicing

# Display only those characters which are present 
# at an even index number in given string.

text = "pynative"

print(text[0:len(text):2])

print("Original String is",text)
print("Printig only even index chars")
for i in range(0,len(text),2):
    print(text[i])

