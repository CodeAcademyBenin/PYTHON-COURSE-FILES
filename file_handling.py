#FILE HANDLING

# To read a file in python we first make use of the open() method which helps to open the 
# file for us either for updating or creating a file.

# The open() funtion takes in two arguement; 
# 1. The File path
# 2. The Mode at which you want to open the file.
""" 
FILE MODES:
 r - Reading a file
 r+ -> Reading and Writing to a file
 w -> Writing to a file(creates the file if it does'nt exist before)
 w+ -> Writing and Reading to a file
 a -> Writing to a file(appends the writings to the end of the file)
 a+ -> 
 x -> Creating a file(fails if the file already exists)
"""

# try:
#     lorem_text = open('documents/lorem.txt', 'x')
#     # print(lorem_text)
#     # print(lorem_text.read()) #extract all the data/contents in the file.
#     # print('1st Line', lorem_text.readline()) #collects all the data in the file.
#     # print('2nd Line', lorem_text.readline()) #collects all the data in the file.
#     # print('3rd Line', lorem_text.readline()) #collects all the data in the file.
#     # print('4th Line', lorem_text.readline(25)) #collects all the data in the file.

#     # lines = lorem_text.readlines() # Extract all the lines and appends them to a python list.
#     # print(lines[3])

#     lorem_text.write('\nMy New Text Content')
#     lorem_text.writelines(['\napple', '\nmango', '\nstrawberry'])
#     lorem_text.close()
# except FileNotFoundError as error:
#     print("ERROR: File not found!!!")
# except FileExistsError as error:
#     print("ERROR: File already exist!!!")


# DELETES A FILE FROM THE SYSTEM
import os

if os.path.exists('documents/dummy.py'):
    os.remove('documents/dummy.py')
    print("SUCCESS: File deleted successfully!!!")
else:
    print("ERROR: File does not exist!!!")


# Best Practice for opening a file
"""This method/approach helps us close the file when we are done by default."""
with open('documents/lorem.txt', 'r') as lorem_text:
    print(lorem_text.readline())

