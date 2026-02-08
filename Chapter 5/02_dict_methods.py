d = {} # to create an empty dictionary

marks = {
    "Shipra" : 100,
    "Prakhar" : 90,
    "Rohit" : 80,
}

# print(marks.items()) # to get a list of tuples containing the key-value pairs in the dictionary
# print(marks.keys()) # to get a list of keys in the dictionary
# print(marks.values()) # to get a list of values in the dictionary
# marks.update({"Shipra": 95, "Ananya": 85}) # to update the dictionary with new key-value pairs
# print(marks) # to print the updated dictionary

# print(marks.get("Shivika")) # to get the value of a key in the dictionary, returns None if the key is not found
# print(marks.get("Shipra")) # to print the value of the key "Shipra"


# print(marks.pop("Rohit")) # to remove a key-value pair from the dictionary and return the value of the removed key
# print(marks) # to print the updated dictionary after removing the key-value pair

print(marks.popitem()) # to remove and return an arbitrary key-value pair from the dictionary
print(marks) # to print the updated dictionary after removing the key-value pair