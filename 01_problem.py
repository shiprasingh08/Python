#Write a program to create a dictionary of hindi words with values as their english translation . Provide user with an option to look it up

words = {
 "namaste" : "hello",
    "duniya" : "world",
    "kaise" : "how",
}

word = input("Enter a hindi word to look up: ")
print(words[word])
 