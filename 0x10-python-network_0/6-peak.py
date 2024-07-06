def find_peak(list_of_integers):
    """Finds a peak in a list of unsorted integers."""
    if not list_of_integers:
        return None

    def binary_search_peak(nums, low, high):
        mid = (low + high) // 2
        if (mid == 0 or nums[mid] >= nums[mid - 1]) and (mid == len(nums) - 1 or nums[mid] >= nums[mid + 1]):
            return nums[mid]
        elif mid > 0 and nums[mid - 1] > nums[mid]:
            return binary_search_peak(nums, low, mid - 1)
        else:
            return binary_search_peak(nums, mid + 1, high)

    return binary_search_peak(list_of_integers, 0, len(list_of_integers) - 1)
