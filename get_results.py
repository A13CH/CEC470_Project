import SortingMethods.Sorting as srt
from timer import timer
from json import load
import matplotlib.pyplot as plt

with open("data.json") as file:
    data = load(file)

bubble_sort_time = timer(lambda: srt.bubblesort(data.copy()), "Bubble Sort")()
selection_sort_time = timer(lambda: srt.selectionsort(data.copy()), "Selection Sort")()
merge_sort_time = timer(lambda: srt.mergesort(data.copy()), "merge Sort")()
quick_data = data.copy() #data format needed for qucksort
quick_sort_time = timer(lambda: srt.quicksort(quick_data, 0, len(quick_data) - 1), "Quick Sort")()
heap_sort_time =  timer(lambda: srt.heapsort(data.copy()), "Heap Sort")()

Time_list1 = []
Time_list2 = []
Time_list1.append(bubble_sort_time)
Time_list1.append(selection_sort_time)
Time_list2.append(merge_sort_time)
Time_list2.append(quick_sort_time)
Time_list2.append(heap_sort_time)
labels1 = ["Bubble sort","Selection sort"]
labels2 = ["Merge sort","Quick sort","Heap sort"]


fig, ax = plt.subplots()
fig, bx = plt.subplots()
ax.bar(labels1,Time_list1)
ax.set_title("Times for Bubble and select sorting algorthims")
ax.set_ylabel("Time (seconds)")
#remaining times
bx.bar(labels2,Time_list2)
bx.set_title("Sorting times")
bx.set_ylabel("Time (seconds)")
plt.show()