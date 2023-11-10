
my_dict = {'name': 'saad', 'age': 23, 'city': 'Lhr'}
print("value my_dict after creating",my_dict)
# Add 
my_dict['email'] = 'saad@example.com'

# Remove 
del my_dict['age']

# Update 
my_dict['city'] = 'karachi'
print('value of dictionary after updated dictonary',my_dict)
# Retrieve 
name = my_dict.get('name')

name = my_dict.get('number',0)
print("Output of this command: name = my_dict.get('number',0)")
# Clear 
my_dict.clear()
print('value of dictionary after clear',my_dict)

# Merge d
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
merged_dict = {**dict1, **dict2}
merged_dict1 = dict1 | dict2
print('value of dictionary after merging',merged_dict)
print('value of dictionary2 after merging by different technique',merged_dict)

# Delete a dictionary
del my_dict
print("My dictionary is deleted after running this command : del my_dict")