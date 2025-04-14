"""
This is the file that will generate all animated graphs. The data is used is the first 50 entries from our data file.
To see the next animation, you have to close the current figure window. Currently There is not
an animation for quick sort due to its complexity, if I can get it working I will add on to this file.
"""
import animated_sorts as ap
import animated_graphing as ga
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from json import load

with open("data.json") as file:
    data = load(file)
sample_data = data[:50]

bubble_generator = ap.ani_bubblesort(sample_data.copy())
ga.gen_animated_graph(bubble_generator,sample_data,"Bubble sort")

select_generator = ap.ani_selectionsort(sample_data.copy())
ga.gen_animated_graph(select_generator, sample_data, "Selection Sort")

merge_generator = ap.ani_mergesort(sample_data.copy())
ga.gen_animated_graph(merge_generator,sample_data,"Merge sort")


heap_generator = ap.ani_heapsort(sample_data.copy())
ga.gen_animated_graph(heap_generator,sample_data,"Heap sort")