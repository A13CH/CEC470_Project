"""
This file contains modified sorting algorithms to generate an animated graph for each of the sections.
The functions need to yield the entire array at specific points during execution for the animation process,
which is why they are a seperate function
"""


def ani_bubblesort(arr):
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
                    yield arr
            if not swapped:
                break  # Break early if no swaps occurred (array is sorted)


def ani_selectionsort(arr):
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
            yield arr


#This merge sort has been modified for the purpose of animation
def ani_mergesort(arr):
    yield from _mergesort(arr, 0, len(arr) - 1)

def _mergesort(arr, left, right):
    if left >= right:
        return

    mid = (left + right) // 2

    yield from _mergesort(arr, left, mid)
    yield from _mergesort(arr, mid + 1, right)
    yield from merge(arr, left, mid, right)


def merge(arr, left_start, mid, right_end):
    """Merge two sorted subarrays of arr and yield each update for animation"""
    left = arr[left_start:mid+1]
    right = arr[mid+1:right_end+1]

    i = j = 0
    k = left_start

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1
        yield arr.copy()

    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1
        yield arr.copy()

    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1
        yield arr.copy()

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

def ani_heapsort(arr):
    """Heap Sort Algorithm"""
    n = len(arr)

    # Build a max heap
    for i in range(n // 2, -1, -1):
        heapify(arr, n, i)

    # Extract elements from heap one by one
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # Swap current root to end
        heapify(arr, i, 0)  # Heapify the reduced heap
        yield arr