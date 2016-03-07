"""
Module to test for primes.
"""


def is_prime(number):
    "Test if number is prime."

    #if number <= 0:
    #    raise TypeError("is_prime expects natural number argument")

    if number == 1:
        return False

    for factor in range(2, number):
        if number % factor == 0:
            return False
    return True
