"""
Author: Isaac Jarrells
Date: March 6, 2025,
File: test_sorts.py
Purpose: This is the bubblesort algorithm which works by swapping adjacent elements in an unsorted array.
"""
from timer import timer
import pytest

@pytest.fixture
def arr():
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    return data

@timer
def test_bubblesort(arr):
    """Testing of the Bubblesort Algorithm"""
    size = len(arr) # Defines the length of the array

    for i in range(size-1):
        swapped = False # Keep searching for number larger than values to be swapped
        for j in range(i+1,size):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
                swapped = True # If a number is larger swapped has happened
            if not swapped: # If there is no swap break the for loop
                break

@timer
def test_selectionsort(arr):
    """Testing of Selection Sort Algorithm"""
    size = len(arr)  # Length of the array
    for i in range(size - 1):
        min_idx = i  # Minimum element
        for j in range(i + 1, size):
            if arr[j] < arr[min_idx]:
                min_idx = j  # Update the minimum element
        arr[min_idx], arr[i] = arr[i], arr[min_idx]