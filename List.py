# Create a list
my_list = [1, 2, 3, 4, 5]

# Add an element to the end
my_list.append(6)
print("value of list after element append",my_list)

# Remove an element by value
my_list.remove(3)
print("value of list after element remove",my_list)

# Update an element by index
my_list[1] = 20
print("value of list after element update ",my_list)

# Retrieve an element by index
element = my_list[2]
print("retrieve a element: ",my_list)

# Clear the list
my_list.clear()
print("list is clear",my_list)

# Merge lists
list1 = [1, 2, 3]
list2 = [4, 5, 6]
merged_list = list1 + list2
print("list after merged ",merged_list)
# Delete a list
del my_list
print("list is delete")
