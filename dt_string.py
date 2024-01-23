# STRINGS

name = 'Jack'

program = "backend"

words = """
this is a text added on the 10th of October 2023.
the python backend class started on the 9th.
"""

# String Methods:
print('Uppercase: ', name.upper())
print('Lowercase: ', name.lower())
print('Capitalize: ', program.capitalize())
print('Replace: ', words.replace('started', 'commenced'))
print('Count: ', words.count("the")) # Return the number of occurrence of a substring.
print('isnumeric: ', name.isnumeric()) 
print('Split: ', words.split('.'))

print('\nlength of name: ', len(name))
print('length of words: ', len(words))

