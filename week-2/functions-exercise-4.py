# Write a Python function that takes a number as a parameter and check the number is prime or not. Note : A prime number (or a prime) is a natural number greater than 1 and that has no positive divisors other than 1 and itself.

import random


def check_primality(number):
    for i in range(1, number):
        if (i != 1) and (i != number) and (number % i == 0):
            return False

    return True


for i in range(10):
    number = random.randint(1, 10)
    print(number, 'is prime?', check_primality(number))
