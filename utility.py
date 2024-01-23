import random

def generate_10_digit():
    lowest = 0000000000
    highest = 9999999999

    digit = random.randint(lowest, highest)

    return digit

def generate_digit(N):
    lowest = pow(10, N-1)
    highest = pow(10,N) - 1

    digit = random.randint(lowest, highest)

    return digit
