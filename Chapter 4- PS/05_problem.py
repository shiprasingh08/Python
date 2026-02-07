#Write a program to count the number of zeroz in the following tuples
a = (7, 0, 8, 0, 0, 9)
print(a.count(0))

# Create a list of your 5 faourite movies and print the list
movie = ["Pk", "Bahubali", "Dangal", "3 Idiots", "Sholay"]
print(movie)

#Add a new movie to the list using method
movie.append('Uri')
print(movie)

#Remove the second movie from the list
movie.remove("Dangal")
print(movie)

movie.pop(1) # pop removes the element at the given index and returns it

#Print the length of the list
print(len(movie))

#Print first and last fruit in the list
print(movie[0]) # first element of the list
print(movie[-1]) # last element of the list

#Revers the list and print it
movie.reverse()
print(movie)

#Sort the list alphabetically and print it
movie.sort()
print(movie)

#Check if "Uri" is in the list or not
print("Uri" in movie)
    

#Combine two lists of nunbers [1, 2, 3] and [4, 5, 6]
l1 = [1, 2, 3]

l2 = [4, 5, 6]
l1.extend(l2)
print(l1)

#find the sum of number in the list[10,20,30 40]
l3 = [10, 20, 30, 40]
print(sum(l3))