#!/usr/bin/python3
"""Module to find the peak in a list of integers"""

def find_peak(list_of_integers):
    """
    Finds a peak in a list of unsorted integers.

    A peak is an element that is greater than or equal to its neighbors.

    Returns the first peak found, or None if no peak is found.
    """
    if not list_of_integers:
        return None

    low = 0
    high = len(list_of_integers) - 1

    while low <= high:
        mid = (low + high) // 2
        if mid == 0 or mid == len(list_of_integers) - 1:
            # Edge cases: check if first or last element is a peak
            if list_of_integers[mid] >= list_of_integers[mid - 1]:
                return list_of_integers[mid]
            low = mid + 1
        elif list_of_integers[mid] >= list_of_integers[mid - 1] and list_of_integers[mid] >= list_of_integers[mid + 1]:
            # Found a peak, return it
            return list_of_integers[mid]
        elif list_of_integers[mid] < list_of_integers[mid - 1]:
            # Mid element is smaller than the previous one, move the search range to the left
            high = mid - 1
        else:
            # Mid element is smaller than the next one, move the search range to the right
            low = mid + 1

    return None
