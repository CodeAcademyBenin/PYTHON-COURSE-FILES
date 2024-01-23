import os 

# file = open("C:/Users/user/Videos/algorithm.mp4", "rb")]
# print(file.readline())

# List the Directories and files under a folder.
dirs = os.listdir("C:/Users/user/Videos/")
# print(dirs)
baymax = os.listdir("C:/Users/user/Videos/Baymax")
# print(baymax)


# Copy or Moving Files in Python
import shutil

fileA = "aaa.html"
fileB = "bbb.html"
destination = "documents/"

# shutil.copy(fileA, destination)
# print("File Copied Successfully!!!")

# shutil.move(fileB, destination)
# print("File Moved Successfully!!!")