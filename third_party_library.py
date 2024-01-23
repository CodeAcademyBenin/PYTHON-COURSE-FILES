# DOWNLOADING AND INSTALLING A THIRD PARTY(EXTERNAL) LIBRARY.
"""
To do this, 
* we make use of python's built-in package manager called pip.
* manually download the package online and install locally on our computer.

Example: Lets say we want to download a library to use within our code we simply 
use the command below;

pip install [library name]

""" 

import time
from plyer import notification

import turtle

print(__name__)
if __name__ == "__main__":
    while True:
        notification.notify(
            title = "ALERT!!!",
            message = "Take a break! It has been over a minute!",
            timeout = 10
        )
        time.sleep(60)