# Dictionary
"""
- A Collection of other datatypes.
- It is mutable.
- It is Ordered.
- It is an Hashable datatype.
- It is created using the curly bracket {} or dict method
- Unlike like list and tuple, items in a dictionary are accessed by key
- Dictionary accepts data using a key and value format 
"""

student1 = {'firstname': 'David', 'lastname': 'Onye', 'age': 56, 'complexion': 'dark'}
student2 = dict((
    ('firstname', 'David'), 
    ('lastname', 'Onye'), 
    ('age', 56), 
    ('complexion', 'dark')
))

# print(student1)
# print(student2)


# Accessing items in a dictionary : we make use of the key
# print(student1['firstname'])

# Update items in a dictionary.
# print(student1)
# student1['lastname'] = 'Onyedikachi'
# student1['lasname'] = 'Onyedikachi'
# print(student1)

# Add an item to a dictionary
student1['gender'] = 'Male'

student1['test'] = {'1st-test': 100, '2nd-test': 68, '3rd-test': 100}

# print(student1['test']['2nd-test'])

# Dictionary Method
# print(student1.items(), '\n')
# print(student1.keys(), '\n')
# print(student1.values())

print(student1.pop("test"))