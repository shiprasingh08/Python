# Replace "dog" with "cat" in the string "I have a dog"
from os import remove


string =  "I have a dog"
string = string.replace("dog", "cat")
print(string)

# Count how many times "a" appears in "banan
string = "banana"
print(string.count("a"))

# /Remove space from " Hello World "
string = " Hello World "
print(string.strip())


# Reverse the string "Python"
string = "Python"
print(string[::-1])

# Check if "madam" is a palindrome
string = "madam"
if string == string[::-1]:
    print("Palindrome") 
