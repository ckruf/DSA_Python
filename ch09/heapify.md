# Bottom-up heap construction of an array-based heap


## Bottom up vs top-down 

If we know the elements from which we want to construct a heap in advance, then we can use bottom-up heap construction to construct a heap with `O(n)` complexity. This is an improvement to the naive way to construct a heap. That would be to succesively keep adding elements to the heap, one by one. This is also know as the top-down approach.

The `add` operation for a heap-based priority queue has complexity `O(log(n))`. The element is added into the last possible position, and then bubbled up using the `upheap` operation. From the bottom level, it can undergo at most h swaps, where h is the height of the heap. The height is equal to log(n), where n is the total number of elements in the heap. 

Therefore, when adding n elements to the heap, where each addition has `log(n)` complexity, the total complexity is `O(nlog(n))`. Bottom-up heap construction allows us to do better than that, at O(n) complexity.


## Bottom up illustration

In bottom up heap construction, we start of with single-node 'heaps', which are the nodes initially occupying the bottom level. We then pair up these heaps and add one more element to each pair, to merge them into three-node heaps, and run a downheap operation on the newly added node, so that the heap-order property is not violated. We then repeat, to create seven-node heaps, and so on, until we finally have a single heap:

<img src="./bottom_up_illustration.png">

## Python implementation 

The implementation of bottom-up heap construction in Python is actually surprisingly simple. Look:

```
def __init__(self, contents: Optional[list[tuple[int, Any]]] = None):
        contents = contents or []
        self._data = [Item(k, v) for k, v in contents]
        if len(self._data) > 1:
            self._heapify()
    
def _heapify(self):
    start = self._parent(len(self)-1)
    for j in range(start, -1, -1):
        self._downheap(j)
```

Now let's explain how this extremely simple code implements the complex illustration above. Let's use the following list as an example: `[44, 11, 13, 35, 5, 8, 43, 41, 26, 33, 39, 14, 2, 29, 2]`. As a binary tree, it would currently look like this:

<img src="./1.png">

when using the standard numbering for a binary tree. Ie we label the root as index 0, and then left children have the index of (2 * parent_index) + 1 and right children have the index of (2 * parent_index) + 2. We consider the bottom level to be 8 single-node heaps. Since single-node heaps are by definition in order, there is no need to do any work.

<img src="./2.png">

In order to merge them into three-node heaps, we just need to call a `downheap` operation on the second level nodes, at indices 3 to 6. 

Before calling `downheap` on indices 3 to 6:

<img src="./3.png">


After calling `downheap` on indices 3 to 6:

<img src="./4.png">

Now, in order to merge these three-node heaps into 7-node heaps, we just call `downheap` on indices 1-2. The current list representation of the heap is `[44, 11, 13, 26, 5, 2, 2, 41, 35, 33, 39, 14, 8, 29, 43]`. The current node representation, before calling `downheap` is:

<img src="./5.png">


After calling `downheap` on 1-2:

<img src="./6.png">

And finally, in order to merge the two 7-node heaps into a single 15-node heap, we just call downheap on index 0:

<img src="./7.png">
