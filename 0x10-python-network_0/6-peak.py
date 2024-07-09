#!/usr/bin/python3
"""Finds a peak in a list of unsorted integers"""



def find_peak(arr):
    """Find a peak element in the list of unsorted integers."""
    if not arr:
        return None

    return peak_helper(arr, 0, len(arr) - 1)

def peak_helper(arr, low, high):
    """Helper function to find the peak element using binary search."""
    mid = (low + high) // 2

    # If mid is a peak
    if (mid == 0 or arr[mid - 1] <= arr[mid]) and (mid == len(arr) - 1 or arr[mid + 1] <= arr[mid]):
        return arr[mid]
    # If the left neighbor is greater, then the peak must be on the left side
    elif mid > 0 and arr[mid - 1] > arr[mid]:
        return peak_helper(arr, low, mid - 1)
    # If the right neighbor is greater, then the peak must be on the right side
    else:
        return peak_helper(arr, mid + 1, high)
