# COMMENTS: are codes that are not executed by the interpreter.

# Single Line Comment
# This is a single line comment.

"""
Multi Line Comment
This 
is 
a 
multi
line commment
with double quotes.
"""

'''
Multi Line Comment
This 
is 
a 
multi
line commment
with single quotes.
'''

# Constants and Variables
"""constants and variables are like boxes that helps the computer store
values within a program.
constants are boxes whose values are not meant to change.
variables are boxes whose values can are allowed to change within the program.

NOTE: while a variable is the box that stores the value the variable name is the 
identifier/label given to the box.

In python best practices, constants can be identified by names with all upper case letters,
while variable can be identified by names with all lower case letters.
"""

# Datatypes: are formats which the program can store data. 
"""
1. Simple Datatype
    - Numbers
        - integers => 10, 25, 
        - float => 0.2, 11.88,
        - complex numbers => i + 5j
    - Strings: sequence of characters embedded within a quote.
        - single line string : single Quote, double Quote.
        - multi line string : Triple single/double Quotes.
    -Boolean 

2. Complex/Structured Datatype
    - List
    - Tuple
    - Dictionary
    - Set
"""

AGE = 20
age = 50

name1 = 'Emmanuel'
name2 = "Wealth"

text = '''
This is me 
writing my 
first program
'''

text = """
This is me 
writing my 
first program
"""


# Using the print statement
"""
The print statement helps the program return data to whosoever is
interacting with the program. 
"""
print(text)

# String Concantenation: Joining strings together.
# print(name1, 'is', age, 'years old')

# Method 1 : plus symbol/operator
print(name1 + ' is ' + str(age) + ' years old')

# Method 2 : .format() method
print("{} is {} years old".format(name1,age))

# rearranging the varibles given.
print("{1} is {0} years old".format(age, name1))

# Method 3 : f string
print(f"{name1} is {age} years old")

