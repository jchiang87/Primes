"""
Unit tests for Primes package
"""
import unittest
from desc.primes import is_prime

class PrimesTestCase(unittest.TestCase):
    """
    TestCase class for is_prime function.
    """
    def test_one_is_not_prime(self):
        "Test that one is not prime."
        self.assertFalse(is_prime(1))

    def test_two_is_prime(self):
        "Test that two is prime."
        self.assertTrue(is_prime(2))

    def test_three_is_prime(self):
        "Test that three is prime."
        self.assertTrue(is_prime(3))

    def test_four_is_not_prime(self):
        "Test that four is not prime."
        self.assertFalse(is_prime(4))

    def test_float_raises_type_error(self):
        "Test that a non-integer returns a TypeError."
        self.assertRaises(TypeError, is_prime, 3.14159)

    def test_non_positive_integer_raises_type_error(self):
        "Test that a non-positive integer returns a TypeError."
        self.assertRaises(TypeError, is_prime, 0)
        self.assertRaises(TypeError, is_prime, -1)


if __name__ == '__main__':
    unittest.main()
