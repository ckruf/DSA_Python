# Sorting with a priority queue

We can use a very simple algorithm to sort a collection using a priority queue. First, we iterate over the collection, adding each element to the priority queue. Then we iterate over the priority queue, successively calling `remove_min`. The order in which the elements are removed from the priority queue is a non-decreasing order.


```
def pq_sort(C):
    n = len(C)
    P = PriorityQueue()
    for j in range(n):
        element = C.delete(C.first())
        P.add(element, element)
    for j in range(n):
        k, v = P.remove_min()
        C.add_last(v)
```

The running time of this algorithm depends on the implementation of the priority queue, particularly the complexity of the `add` and `remove_min` operations.

## Unsorted list implementation - selection sort

When the priority queue is implemented using an unsorted list, the `add` operation has `O(1)` complexity, as new elements are simply appended to the end of the underlying list. However, the `remove_min` operation has `O(n)` complexity, as we need to scan the entire list in order to find the element with the lowest key. The bottleneck of the algorithm is the repeated 'selection' of the minimum element. This is known as selection sort. In the second loop, in each successive iteration, we must scan n elements, then n-1 elements, then n-2 elements, until finally only a single element. The running time is therefore `O(n^2)`. It is also noteworthy that even the best case running time is still `O(n^2)`, because we need to scan the entire remainder of the list during each iteration, in order to make sure that we have selected the minimum element.


## Sorted list implementation - insertion sort


When the priority queue is implemented using a sorted list, the `add` operation has `O(n)` complexity, as we need to scan the sorted list until we find the position where the new element fits, which could be at the end of the list in the worst case. On the other hand, the `remove_min` operation has `O(1)` complexity, as we simply remove the first element in the list. The worst case running time is again `O(n^2)`, since we are dealing with the equivalent sum of (1 + 2 + ... + n-1 + n). However, the best case running time (when dealing with an already sorted collection) is O(n), since insertion terminates as soon as the correct position is found. Unlike selection, which has to scan the entire list every time.


## Heap implementation - heap sort

When the priority queue is implemented using a heap, both the first phase and the second phase have `O(nlog(n))` complexity, since both the `add` and `remove_min` operations have `log(n)` complexity, and they are applied to all n elements. The first phase can be improved to `O(n)` by using bottom-up heap construction, though it still leaves the overall algorithm at `O(nlog(n))`.  

### heap sort in-place

If the collection to be sorted is implemented as an array-based sequence, we can speed up heap-sort and reduce its space requirement by using a portion of the list itself to store the heap, thereby avoiding the auxiliary heap data strucutre. To accomplish this, we use a maximum-oriented heap.