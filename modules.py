# A Module is a file that contains code to perform a specific task.
# A module is a file that contains constants,variables,functions or classes
"""
* Built-In Modules : Modules that are offered by the programming language.
* Third Party Modules : Modulels that are created by other programmers.
* Self Created Modules : Modules that are designed/created by the programmer.
"""

#HOW TO USE A MODULE
"""
* Import the module by name
    >>> import math
    >>> import math as mt
    >>> from math import mean
"""

# BUILT-IN MODULES
"""
- math
- statistics
- random
- datetime
- calendar
- smtpd
- urllib
- socket
"""

import math
# print(math.sqrt(64))
# print(math.isqrt(64))
# print(math.sin(60))

import random
# Helps to perform randomization within your program.
numbers = [3,2,98,0,45,23,13,199,302,0]

lucky_number = random.choice(numbers)
lucky_number = random.randint(0,100)
# print(lucky_number)

import datetime
# print(datetime.datetime.now())
# print(datetime.date.today())

import calendar
# print(calendar.month(theyear=2019, themonth=10))
# print(calendar.month(theyear=2023, themonth=10))

# THIRD PARTY MODULES
"""
- requests
- docx
- beautifulsoup
- pypdf
- qrcode

HOW TO USE:
* first download the module from the web.
    >>> pip install [name of module]
    >>> pip install requests
* import the module for use.
"""

# SELF CREATED MODULES
# import utility
from utility import generate_10_digit, generate_digit

# value = generate_10_digit()
value = generate_digit(10)
print(value)