# ITERATION
"""
It simply means the repitition of a particular task.

Forms of Iteration:
1. For Loop
****Use Cases
a. It is used to iterate through items in an iterable datatype
such as string, list, tuple, dictionary and set.
    SYNTAX>>>
    for variable in datatype:
        block_of_code...

b. It is used to repeat a specific task for a limited or known amount of time.
    SYNTAX>>>
    for variable in range(start,stop,increment/step):
        block_of_code...

2. While Loop
****Use Case
a. It is used to repeat a specific task based on the truth value of a condition.
    SYNTAX>>>
    while condition:
        block_of_code...
b. It is used to run an infinite iteration/loop.
    SYNTAX>>>
    while True:
        block_of_code...
"""

# Use Case 1
# 
test_score = [1, 34, 45, 100, 0, 80, 90]
extra_mark = 15

new_test_score = []

for score in test_score:
    if score + extra_mark > 100:
        new_test_score.append(score)
        continue
    new_test_score.append(score + extra_mark)


# print(test_score)
# print(new_test_score)

# Accessing both the value and index/key of an iterable
# for index,score in enumerate(test_score):
#     print(f"index: {index}, score: {score}")

credentials = {'username': 'maxwell', 'password': 'max345', 'is_admin': False, 'darkMode': True}
# Method 1
# for key,value in enumerate(credentials):
#     print(f"key: {key}, value: {value}")

# Method 2
for key,value in credentials.items():
    print(f"key: {key}, value: {value}")

# Use Case 2
# for i in range(2,5):
#     print('\t',i)

# for i in range(1,11,2):
#     print('\t',i)


# Use Case 3
# user_input = int(input('Enter a number>>> '))
# while user_input <= 3:
#     user_input = int(input('Enter a number>>> '))


# Functions like the For Loop but increases time and space complexity.
# trials = 1
# while trials <= 3:
#     print("Game Started!")
#     trials += 1

# print('Code end')


# Nested Loop
# for i in range(3):
#     for j in range(3):
#         print(f'\t i = {i}, j = {j}')


"""
ASSIGNMENT
Perform the operation 256 * 98999 wihtout making use of the * operator.
Hint: Make use of the concept of iteration.
"""

def mul(*args):
    value = 0
    for key,num in enumerate(args):
        print(key,num)
        next = key + 1

        if next <= (len(args) - 1):
            for i in range(args[next]):
                value += num
        else:
            pass
        print(value)

    return value


print(256 * 98999)
print(mul(2,6,3))


