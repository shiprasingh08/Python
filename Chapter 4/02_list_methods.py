friends = ["Apple", "Orange",5, 345.06, False, "Akash","Rohan"]
print(friends)
friends.append("Aditya") # append means add element at the end of the list

print(friends)


l1 = [1, 34, 64,2,6,11]
#l1.sort() # sort the list in ascending order
#l1.reverse() # reverse the list in descending order
#l1.insert(3, 33333) # insert 33333 such that its index in the list is 3

value = l1.pop(3)
print(value)
print(l1)

value = l1.remove(64) # remove the element 64 from the list
print(value) # remove does not return the removed value, it returns None