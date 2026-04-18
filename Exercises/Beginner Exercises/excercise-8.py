# String Reversal

# Write a program that takes a string and reverses it 
# (e.g., “Python” becomes “nohtyP”).

text = input("Enter the text: ")
print(f"Original text : {text} ")
reversed_text = text[::-1]
print(f"Reversed text : {reversed_text}")