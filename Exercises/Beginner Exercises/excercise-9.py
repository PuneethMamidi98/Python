# Vowel Frequency Counter

# Write a program to count the total number of vowels 
# (a, e, i, o, u) present in a given sentence.

vowels = ['a','e','i','o','u']
sentence = "Learning Python is fun!"
total_vowels = 0
for i in sentence:
    total_vowels += vowels.count(i)
print(f"Number of vowels: {total_vowels}")    