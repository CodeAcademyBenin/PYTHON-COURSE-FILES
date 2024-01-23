# LIST
"""
1. It a collection of other datatypes.
2. It is mutable and ordered.
3. It can either be homogenous or heterogenous.
4. It is created and identified with the square bracket [].
5. Data in a list are accessed by an INDEX which can either be positive or negative.
6. Data in the list are seperated with a comma.
7. A list can also be created with the list() method.
"""

students = "Jeff"
students = ["Wealth","Emmanuel","Frank","Austin","Destny"]

# Accessing items in a list.
# print(students[0])  # First Item.
# print(students[-1])  # Last Item.
# print(students[::-1])  # Reverse a list.

# These are the same 
# print(students[2]) 
# print(students[-3])

# Mutability
# print('Before: ', students)
students[-1] = "Destiny"
# print('After: ', students)

# Slicing items in a list.
# students[startIndex:startIndex + NumberOfItems]
# print(students[0:4])
# print(students[1:4])

# List Methods
# print(students)
# ADD to the list
students.append("Joshua")  # Add an item to the end of a list.
students.insert(3,"Susan")  # Add an item to any postion in the list.
# print(students)


# REMOVE from the list
# print(students.pop() + " was removed!!!") # Removes an item from the end/any position of a list.
# students.pop(1)  # Removes an item from the any position of the list with an INDEX.
# students.remove("Destiny")  # Removes an item from any position of the list with the item itself.
# print(students)

# Changes the position of an already existing item in the list.
# students.insert(0, students.pop(1))
# print(students)


# Accessing item in a Complex List Structure
Num = [
    1,
    2,
    3,
    [4,5,6],
    [
        7,
        8,
        [10,11]
    ]
]
# print(Num[3][2])
# print(Num[4][2][0])

a = ['Apple','Banana']
b = ['Milk', 'Bread']

b.extend(a)
# print(a)
# print(b)

# SOrting items in a list
# print(sorted(b)) # Returns the sorted value of b withour altering b itself.

# b.sort() # Just sorts b out for life.
# print(b)


# len Method: is used count the number of items on iterable datatypes such as strings and all complex datatypes
number_of_students = len(students)
print(number_of_students)
