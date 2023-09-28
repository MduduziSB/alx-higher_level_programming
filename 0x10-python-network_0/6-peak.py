#!/usr/bin/python3
"""finds a peak in a list of unsorted integers"""


def find_peak(list_of_integers):
    """This function finds a peak in an unsorted list of integers"""
    if not list_of_integers:
        return None

    i_start = 0
    i_end = len(list_of_integers) - 1
    while i_start < i_end:
        mid = i_start + (i_end - i_start) // 2
        if (list_of_integers[mid] > list_of_integers[mid - 1]
                and list_of_integers[mid] > list_of_integers[mid + 1]):
            return list_of_integers[mid]
        if list_of_integers[mid - 1] > list_of_integers[mid + 1]:
            i_end = mid
        else:
            i_start = mid + 1
    return list_of_integers[i_start]
