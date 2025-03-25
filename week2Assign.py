# Create an empty list called my_list.
# Append the following elements to my_list: 10, 20, 30, 40.
# Insert the value 15 at the second position in the list.
# Extend my_list with another list: [50, 60, 70].
# Remove the last element from my_list.
# Sort my_list in ascending order.
# Find and print the index of the value 30 in my_list.

my_list = [] # Empty list

print("Empty list:", my_list)
# Append the following elements to my_list
elements = [10, 20, 30, 40]

#Using the extend() to append elements to list
my_list.extend(elements)
print("my_list after append:", my_list)

#Insert value 15 at second position in the list; here the second position is index 1
#Use insert operator
my_list.insert(1, 15)
print("my_list after inserting 15 at second position:", my_list)

# Extend my_list with another list: [50, 60, 70]

list = [50, 60, 70]

 #use extend operator
my_list.extend(list)
print("my_list after extending with [50, 60, 70] list:", my_list)

# Remove the last element from my_list.
 #use delete operator
del my_list[-1]
print("my_list after deleting last element:", my_list)

# Sort my_list in ascending order.
 #use sort() operator, To sort descending, use the keyword argument reverse = True:
my_list.sort()
print("my_list after sorting:", my_list)

# Find and print the index of the value 30 in my_list.
index_element30 = my_list.index(30)
print("Index of the value 30 in my_list is:", index_element30)
