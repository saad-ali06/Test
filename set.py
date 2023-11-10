# Create a set
my_set = {1, 2, 3, 4, 5}

# Add an element
my_set.add(6)

# Remove an element
my_set.remove(3)

# Update a set (Union)
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1.union(set2)

# Update a set (Intersection)
intersection_set = set1.intersection(set2)

# Update a set (Difference)
difference_set = set1.difference(set2)

# Clear the set
my_set.clear()

# Delete a set
del my_set

# Print the results
print(union_set)
print(intersection_set)
print(difference_set)
