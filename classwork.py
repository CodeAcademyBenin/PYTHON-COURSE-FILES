"""@TODO
>>> Question 1

Given a list of strings, write a program to identify the longest and shortest
string in the list.

Example:
['Bird','Hippopotamus','Father','Abomination','Missisipi']

'Longest String: Hippopotamus, Shortest String: Bird'

>>> Question 2

Design a function to identify a palindrome. 
A palindrome is a string which when reversed stays the same.
Example:
original strings: 'ababa', '19091', 'oGgo'
reversed strings: 'ababa', '19091', 'ogGo'

is_palindrome('19091') >>> True
is_palindrome('10991') >>> False

>>> Question 3

Write a function to eliminate duplicates from a sorted iterable datatype.
Example: 
a = [1,4,6,4,0,3,2,1,9]
b = ('v','c','b','c','a','a','s','k')

duplicates_removal(a) >>> [0,1,2,3,4,6,9]
duplicates_removal(b) >>> ('a','b','c','k','s','v')
"""

# QUESTION 1
words = ['Bird','Hippopotamus', 'Father', 'Fish', 'Abomination','Missisipi']

# METHOD 1
# length_of_words = len(words)  # Get the length of string.
# longest_string = []
# shortest_string = []

# longest_string.append(words[0])
# shortest_string.append(words[0])

# for index,string in enumerate(words,1):
#     length_of_string = len(string)  # Get the length of string.

#     #  Compare the lenth of current longest string with the string.
#     if length_of_string > len(longest_string[0]):
#         longest_string.append(string)  # replace current longest string if greater than.
#     elif length_of_string == len(longest_string[0]):
#         longest_string.append(string)  # append to the longest string if equal.

#     if index ==length_of_words:
#         break
#     if length_of_string < len(words[index]):
#         shortest_string[0] = string  # replace current shortest string if greater than.
#     elif length_of_string == len(words[index]):
#         shortest_string.append(string)
# print(longest_string)
# print(shortest_string)


# QUESTION 2
def reverse_string(string):
    b = []
    for i in range(1,len(string)+1):
        b.append(string[-i])

    return ''.join(b)

def is_palindrome(string:str) -> bool:
    original_string = string.lower()
    # Using python built in feature for reversing string.
    # reversed_string = string[::-1].lower()

    reversed_string = reverse_string(string).lower()

    if original_string == reversed_string:
        print(f"{string} is a palindrome")
        return True
    else:
        print(f"{string} is not a palindrome")
        return False

# is_palindrome('19091')
# is_palindrome('10991')
# is_palindrome('oGgo')


# QUESTION 3
a = [1,4,6,1,9,1,1,4,4,4,0,3,2,1,9,4]
b = ('v','c','b','c','a','a','s','k','c','c')

def duplicates_removal(iter):
    iter = sorted(iter)
    print("Old Data", iter)
    for num in iter:
        while iter.count(num) > 1:
            iter.remove(num)

    print("New Data", iter)

# duplicates_removal(a)
# duplicates_removal(b)


# QUESTION 4
c = [24,6,10,2]
hold = 0

# SPACE COMPLEXITY: UTILIZES THE COMPUTER MEMORY
# for num in c:
#     hold = hold + num

# # TIME COMPLEXITY: UTILIZES TIME OVER THE COMPUTER MEMORY
# for index,num in enumerate(c):
#     if c[index] != c[0]:
#         c[0] = c[0] + num
#         print(c[0])

# print(c[0])