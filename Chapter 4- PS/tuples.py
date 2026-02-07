#Create a tuple of 4 of your favourites colours

colors = "red", "blue", "green", "yellow"
print(colors)

# Print the first and last colour in the tuple
print(colors[0]) # first element of the tuple
print(colors[3]) # last element of the tuple

#Check if "blue" is in the tuple or not
print("blue" in colors)

#Count how many times "red appear in the tuples ("red", "blue", "red", "yellow", "red").

t = ("red", "blue", "red", "yellow", "red")
print(t.count("red"))

#find the length of the tuple.
print(len(t))

#Create a tuple from a list of numbers [1, 2, 3, 4, 5]
l = [1, 2, 3, 4, 5]
t = tuple(l)
print(t)

#Concatenate two tuples (1, 2, 3) and (4, 5, 6)
t1 = (1, 2, 3)
t2 = (4, 5, 6)
t3 = t1 + t2
print(t3)

#Try changing the first element of the tuple (10,20,30) (and explain what happened)
# t = (10, 20, 30)
# t[0] = 100 # this will give an error because tuples are immutable, which means that once a tuple is created, its elements cannot be changed.

#Slice the tuple (10, 20, 30, 40, 50) to get (20, 30, 40)

t = (10, 20, 30, 40, 50)
print(t[1:4]) # slicing the tuple from index 1 to index 3 (index 4 is not included)


#Convert the tuple (1, 2, 3, 4, ) to a list and append 5 to it.


t = (1, 2, 3, 4, )
l1 = list(t)
l1.append(5)
print(l1)