# FUNCTIONS
"""Functions are simply a block of statement or a block of code which performs a
specific task/operation.

SYNTAX: 
>>> Function Definition : Defines how the function should work/behave.
def name_of_function([...parameters]):
    block_of_code / statements
    return

>>> Function Call : Puts the function to work.
name_of_function([...arguments])

:: Global Variable : Varibles outside a block(function definition), hence they can be
accessed at any point in our code.

:: Local Variable : Variables inside a block(function definition), hence they can only be
accessed within the block/function.

"""

# Global variables
# val1 = 5
# val2 = 6
# val3 = 7

# Function Definition
def sum_test_score(score1=0, score2=0, score3=0):
    # value here is a local variable declared within a block.
    value = score1 + score2 + score3
    return value

# print(value) : This would result to a name error, because value was declared local.

# INFO: The return helps the function sends a value back to the main program,
# or you can say it makes the value stored on the local variable accessible
# outside of the function.

exam_score = 50
total_test_score = sum_test_score(5,7,6)
total = exam_score + total_test_score
# print(total)

# 
def sum_grade(*args, **kwargs):
    # *args here is used to specify an unknown amount of parameters.
    value = 0
    for grade in args:
        value = value + grade

    return value

sum_grade(20,40,12,50,76)
sum_grade(16,22,21)
sum_grade()

# EXAMPLE
def area_of_circle(radius):
    """Returns the area of a circle,
    It accepts the radius as a parameter
    """
    PI = 22/7
    area = PI * (radius ** 2)
    print(f'\t The area of the circle with radius {radius} is {area}cm2')
    return  area

area_of_circle(7)
# area_of_circle(8.98)
