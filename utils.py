"""
utils.py - Utility functions module for common algorithmic operations.
"""

from typing import List, Any, Union
import math


def is_prime(n: int) -> bool:
    """
    Checks if a given integer is a prime number.
    Uses time complexity O(sqrt(n)).
    """
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False

    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6

    return True


def fibonacci(count: int, first_num: int = 0, second_num: int = 1):
    for _ in range(count):
        yield first_num
        first_num, second_num = second_num, first_num + second_num


def sort_list(items: List[Any], reverse: bool = False, key: Any = None) -> List[Any]:
    """
    Returns a new sorted list from the items in iterable.

    :param items: The list to be sorted.
    :param reverse: If True, sorts in descending order.
    :param key: A function to specify a custom sorting criteria.
    :return: A new sorted list.
    """
    return sorted(items, key=key, reverse=reverse)


def find_gcd(a: int, b: int) -> int:
    """
    Finds the Greatest Common Divisor (GCD) of two integers using the Euclidean algorithm.
    """
    return math.gcd(a, b)


if __name__ == "__main__":
    # Example usage / Sanity tests
    print("Is 29 prime?:", is_prime(29))  # Output: True
    print("Is 10 prime?:", is_prime(10))  # Output: False

    sample_list = [42, 7, 19, 1, 88, 3]
    print("Sorted list:", sort_list(sample_list))  # Output: [1, 3, 7, 19, 42, 88]

    print("GCD of 48 and 18:", find_gcd(48, 18))  # Output: 6

    # Usage:
    sequence = list(fibonacci(10))
    print(sequence)

