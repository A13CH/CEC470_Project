"""
Author: Isaac Jarrells
Date: March 6, 2025,
Purpose: This will be the collection of sorting methods used for the sorting for our
         project. This includes Bubble, Heap, Insertion, Selection, Quick, Merge Sorting
         Algorithms.
"""

from timer import timer

@timer
def bubblesort(arr):
    """Bubblesort Algorithm"""
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
def selectionsort(arr):
    """Selection Sort Algorithm"""
    size = len(arr)  # Length of the array
    for i in range(size - 1):
        min_idx = i  # Minimum element
        for j in range(i + 1, size):
            if arr[j] < arr[min_idx]:
                min_idx = j  # Update the minimum element
        arr[min_idx], arr[i] = arr[i], arr[min_idx]



if __name__ == '__main__':
    data = [64,34,25,12,22,11,90]
