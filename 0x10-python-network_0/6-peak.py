#!/usr/bin/python3
"""Finds a peak in a list of unsorted integers"""

def find_peak(list_of_integers):
    """Find a peak element in the list of unsorted integers."""
    if not list_of_integers:
        return None

    return find_peak_helper(list_of_integers, 0, len(list_of_integers) - 1)

def find_peak_helper(arr, low, high):
    """Helper function to find the peak element using binary search."""
    mid = (low + high) // 2

    # If mid is a peak
    if (mid == 0 or arr[mid - 1] <= arr[mid]) and (mid == len(arr) - 1 or arr[mid + 1] <= arr[mid]):
        return arr[mid]
    # If the left neighbor is greater, then the peak must be on the left side
    elif mid > 0 and arr[mid - 1] > arr[mid]:
        return find_peak_helper(arr, low, mid - 1)
    # If the right neighbor is greater, then the peak must be on the right side
    else:
        return find_peak_helper(arr, mid + 1, high)
