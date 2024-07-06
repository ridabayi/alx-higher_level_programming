def find_peak(list_of_integers):
    if not list_of_integers:
        return None
    
    left, right = 0, len(list_of_integers) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if (mid == 0 or list_of_integers[mid] >= list_of_integers[mid - 1]) and \
           (mid == len(list_of_integers) - 1 or list_of_integers[mid] >= list_of_integers[mid + 1]):
            return list_of_integers[mid]
        elif mid > 0 and list_of_integers[mid] < list_of_integers[mid - 1]:
            right = mid - 1
        else:
            left = mid + 1
    
    return None
