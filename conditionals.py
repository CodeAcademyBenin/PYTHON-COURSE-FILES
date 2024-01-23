# CONDITIONALS
"""
Conditionals in programming is a process of altering flow/execution
of a program. 
A conditional statement executes a block of code depending on
whether a condition is true of false.

SYNTAX: 
if condition statement:
    block_of_code...
elif condition statement: [optional...]
    block_of_code...
else: [optional...]
    block_of_code...
"""

age = 25
has_pvc = False

# Using only the if statement
# if age > 18:
#     print("You can place your vote!")

# Using the if and else statemen
# if age >= 18 and has_pvc:
#     print("You can place your vote!")
# elif age >= 90:
#     print("You cannot place your vote!")
#     print("You have exceed the age.")
# else:
#     print("You cannot place your vote!")
#     print("Grow Up Kid!")

print('\n')

# Nested if statement
# if age >= 18:
#     if has_pvc:
#         print("You can place your vote!")
#     else:
#         print("Go get your PVC!")
# elif age >= 90:
#     print("You cannot place your vote!")
#     print("You have exceed the age.")
# else:
#     print("You cannot place your vote!")


# Short-hand for if and else statement
#SYNTAX:
# on_true_statement if condition else on_false_statement

# if has_pvc:
#     print("You can place your vote!")
# else:
#     print("Go get your PVC!")

print("You can place your vote!") if has_pvc else print("Go get your PVC!")



"""Assignment

1. Learn how to use python input() method.
2. Simulate the behaviour of an ATM.

"""