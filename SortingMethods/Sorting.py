"""
Author: Isaac Jarrells
Date: March 6, 2025,
Purpose: This will be the collection of sorting methods used for the sorting for our
         project. This includes Bubble, Heap, Insertion, Selection, Quick, Merge Sorting
         Algorithms.
"""

from timer import timer


def bubblesort(arr) -> list:
    """Bubble Sort Algorithm"""
    size = len(arr)  # Get the length of the array
    if size > 1:
        # Outer loop to control passes
        for i in range(size - 1):
            swapped = False  # Flag to detect any swap
            # Inner loop to compare and swap elements
            for j in range(i + 1, size):
                if arr[i] > arr[j]:
                    arr[i], arr[j] = arr[j], arr[i]  # Swap if left is greater than right
                    swapped = True
            if not swapped:
                break  # Break early if no swaps occurred (array is sorted)
    return arr


def selectionsort(arr):
    """Selection Sort Algorithm"""
    size = len(arr)  # Get the length of the array
    if size > 1:
        # Loop through each element in the array
        for i in range(size - 1):
            min_idx = i  # Assume current index is the minimum
            # Find the actual minimum element in the rest of the array
            for j in range(i + 1, size):
                if arr[j] < arr[min_idx]:
                    min_idx = j
            # Swap the found minimum with the current element
            arr[min_idx], arr[i] = arr[i], arr[min_idx]
    return arr


def mergesort(arr):
    """Merge Sort Algorithm (Divide and Conquer)"""
    if len(arr) <= 1:
        return arr  # Base case: single element is already sorted

    # Divide the array into left and right halves
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    # Recursively sort both halves
    sorted_left = mergesort(left)
    sorted_right = mergesort(right)

    # Merge the sorted halves
    return merge(sorted_left, sorted_right)


def merge(left, right):
    """Merge two sorted arrays into one sorted array"""
    result = []
    i = j = 0

    # Compare elements from both arrays and merge in sorted order
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Append remaining elements, if any
    result.extend(left[i:])
    result.extend(right[j:])
    return result


def partition(arr, low, high):
    """Partition the array using Lomuto partition scheme"""
    pivot = arr[high]  # Choose the last element as pivot
    i = low - 1  # Index of smaller element

    # Rearranging elements around pivot
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[j], arr[i] = arr[i], arr[j]  # Swap if current element is less than or equal to pivot

    # Place pivot in its correct sorted position
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1  # Return the index of pivot


def quicksort(arr, low, high):
    """Quick Sort Algorithm (Divide and Conquer)"""
    if low < high:
        p = partition(arr, low, high)  # Partition the array
        quicksort(arr, low, p - 1)     # Recursively sort left subarray
        quicksort(arr, p + 1, high)    # Recursively sort right subarray
    return arr


def heapify(arr, n, i):
    """Heapify a subtree rooted at index i"""
    largest = i  # Initialize largest as root
    left = 2 * i + 1  # Left child
    right = 2 * i + 2  # Right child

    # Check if left child exists and is greater than root
    if left < n and arr[i] < arr[left]:
        largest = left

    # Check if right child exists and is greater than current largest
    if right < n and arr[largest] < arr[right]:
        largest = right

    # If largest is not root, swap and continue heapifying
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def heapsort(arr):
    """Heap Sort Algorithm"""
    n = len(arr)

    # Build a max heap
    for i in range(n // 2, -1, -1):
        heapify(arr, n, i)

    # Extract elements from heap one by one
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # Swap current root to end
        heapify(arr, i, 0)  # Heapify the reduced heap
    return arr


# Main block to test sorting algorithms
if __name__ == '__main__':
    data = [5, 9, 7, 1, 2, 4, 3, 8, 6]

    # Note: Each sort mutates `data`, so copy the original list each time
    timer(lambda: bubblesort(data.copy()), "Bubble Sort")()

    timer(lambda: selectionsort(data.copy()), "Selection Sort")()

    # For mergesort, time just the outermost call
    timer(lambda: mergesort(data.copy()), "Merge Sort")()

    # For quicksort, time the outermost call
    quick_data = data.copy()
    timer(lambda: quicksort(quick_data, 0, len(quick_data) - 1), "Quick Sort")()

    timer(lambda: heapsort(data.copy()), "Heap Sort")()
