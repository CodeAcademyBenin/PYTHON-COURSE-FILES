"""@TODO
Exercise 1
Write a function that can identify if a number is odd or even.

example:
num_identifier(6)
num_identifier(13)

output:
6 is an even number
13 is an odd number
"""
# Solution 1
def number_identifier(number):
    if number % 2 == 0:
        print(f"{number} is an even number")
    elif number % 2 == 1:
        print(f"{number} is an odd number")
    else:
        print('Probably you entered a floating point number.')

number_identifier(6)
number_identifier(13)
number_identifier(22)
'--------------------------------------------------------------------------------------------'

"""@TODO
Exercise 2
Design a structure by which we can store a matrix within our program.
"""