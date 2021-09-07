# Write a Python function to check whether a number is in a given range.

import random


def is_in_range(number, minimum, maximum):
    if (number >= minimum) and (number <= maximum):
        return True
    else:
        return False


number = random.randint(0, 10)
minimum = random.randint(0, 10)
maximum = random.randint(minimum + 1, minimum + 11)

print(number, 'in range', minimum, '-', maximum,
      '?', is_in_range(number, minimum, maximum))
