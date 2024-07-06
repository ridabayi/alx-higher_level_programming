#!/usr/bin/python3
""" Test function find_peak """

from random import randint
from time import time
from 6-peak import find_peak

def test_find_peak():
    # Test cases
    test_cases = [
        [1, 2, 4, 6, 3],
        [4, 2, 1, 2, 3, 1],
        [2, 2, 2],
        [],
        [-2, -4, 2, 1],
        [4, 2, 1, 2, 2, 2, 3, 1],
        [1, 2, 3, 4, 5],
        [5, 4, 3, 2, 1],
        [3, 2, 1, 2, 3],
        [randint(-100, 100) for _ in range(1000)],  # Random large list
    ]

    for idx, nums in enumerate(test_cases):
        start_time = time()
        peak = find_peak(nums)
        exec_time = (time() - start_time) * 1000  # Convert to milliseconds
        print(f"Test case {idx + 1}:")
        print(f"Input: {nums}")
        print(f"Peak found: {peak}")
        print(f"Execution time: {exec_time:.6f} ms")
        print("")

if __name__ == "__main__":
    test_find_peak()
