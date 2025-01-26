######################################################
# Quick Sort - 2025
# Complexity: O(n log n)
######################################################
"""
Quick sort is a divide-and-conquer algorithm.
It works by selecting a 'pivot' element from the array
and partitioning the array such that all elements on the left
are less than the pivot and all elements on the right are 
greater. The pivot is placed in right position in the array.

Termination condition: If the array has only one element.
"""

from typing import List
import pytest


def quick_sort(arr: List[int])-> List[int]:
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        smaller = filter(lambda x: x<pivot, arr[1:])
        greater = filter(lambda x: x>=pivot, arr[1:])
        return quick_sort(list(smaller)) + [pivot] + quick_sort(list(greater))  
