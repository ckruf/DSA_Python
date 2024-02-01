## 10.4

What is the worst-case running time for inserting n key-value pairs into an initially empty map M that is implemented with the UnsortedTableMap class?

Worst case of inserting n key-value pairs into UnsortedTableMap is O(n^2), because `__setitem__` searches the entire list each time (ie O(n)), since it has to check whether we are overwriting an existing value, or adding a new one.

## 10.6

Which of the hash table collision-handling schemes could tolerate a load factor above 1 and which could not?

Only separate chaining can deal with a load factor above 1. Other collision-handling schemes rely on there being empty slots in the bucket array into which it can store key-value pairs in case of collision.

## 10.7

Our Position classes for lists and trees support the eq method so that
two distinct position instances are considered equivalent if they refer to the same underlying node in a structure. For positions to be allowed as keys in a hash table, there must be a definition for the hash method that is consistent with this notion of equivalence. Provide such a hash method.

The hash method must be based on the node alone. So make a hash based on the node's `id()`:

```
def __hash__(self):
    return id(self._node)

```

## 10.8

What would be a good hash code for a vehicle identification number that is a string of numbers and letters of the form “9X9XX99X9XX999999,” where a “9” represents a digit and an “X” represents a letter?

Either polynomial hash code, or cyclic bit shift. Definitely not a sum or XOR based hash code, since we want order to matter.

## 10.9

<img src="./ex_10_9.png" >

## 10.10

<img src="./ex_10_10.png" >

## 10.11

<img src="./ex_10_11.png" >

## 10.12

<img src="./ex_10_12.png" >

## 10.13

What is the worst-case time for putting n entries in an initially empty hash table, with collisions resolved by chaining? What is the best case?

The worst case is that all the keys hash to the same value. Therefore, when adding the first key, there would be 0 collisions, second key would be 1 collision, third key would be 2 collisions, and so on. And all the entries which hash to the same value have to be iterated, to check whether we are adding a new key, or overwriting an existing one. This sum is esentially from 1 to n, which equals n*((n+1)/2), which is O(n^2). The best case for n insertions is O(n), since in the best case, each insertion is O(1).

## 10.14

<img src="./ex_10_14.png" >

## 10.18

Because a hash map scatters keys randomly throughout the underlying array

## 10.19

Compared to using an array-based structure for a sorted map, the main differences are that a doubly linked list does not support binary search, and insertions and deletions anywhere in the list are O(1). The array based sorted map can use binary search to find an item (or an insertion position) in log(n) time. So reads are O(log(n)), but insertion of new keys and deletion of keys requires all the items after to be shifted, which is O(n). On the other hand, a linked structure would require linear search to find the item, which is O(n). But subsequently inserting or deleting a key-value pair is O(1). So in a linked-list based sorted map, reads, writes and deletions would all be O(n) in the worst case. 

## 10.20

The worst case for performing n deletions from a SortedTableMap is O(n^2). Items can be found using log(n) steps. But deletion takes O(n-k) steps, where k is the index of the item being deleted, since all the items in front of the deleted item need to be shifted. So each deletion is O(n) worst case, therefore n of them is O(n^2) worst case.


## 10.22

Consider the following variant of the `_find_index` method, implementing binary search:

```
def _find_index(self, k, low, high):
    if high < low:
        return high + 1
    else:
        mid = (low + high) // 2
        if self._table[mid]. key < k:
            return self._find_index(k, mid + 1, high)
        else:
            return self._find_index(k, low, mid − 1)
```

Does this always produce the same result as the original version below? Justify your answer.

```
def _find_index(self, k, low, high):
    if high < low:
        return high + 1
    else:
        mid = (low + high) // 2
        if self._table[mid] == k:
            return mid
        elif self. table[mid]. key < k:
            return self._find_index(k, mid + 1, high)
        else:
            return self._find_index(k, low, mid − 1)
```

In terms of the results returned, the algorithms return the same results when the key is not found in the array, and also when the item is in the array, but it only occurs once. 

The difference between the algorithms is the results that it gives when the key occurs multiple times. And also the general behavior. The new version of the algorithm never terminates 'early'. For example, let's say we were looking for 5 in the list below. The original algorithm will return the answer using a single function call, since we immediately find the key at the 'mid' index. On the other hand, the newer version, will have the following function calls

[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

`_find_index(5, 0, 10)`
`_find_index(5, 0, 4)`
`_find_index(5, 3, 4)`
`_find_index(5, 4, 4)`
`_find_index(5, 5, 4)` -> returns 5

It uses the same case whether the element at the mid index is equal to the key, or greater than the key. It looks in the left half of the array. So it will look in the left half, then drift all the way to the rightmost element, and return the index that's one greater than that.

When the key occurs in the list multiple times, then the new version of the algorithm will always return the leftmost occurence, whereas the original algorithm provides no such guarantee.



## 10.22

What is the expected running time of the methods for maintaining a maxima set if we insert n pairs such that each pair has lower cost and performance than one before it? What is contained in the sorted map at the end of this series of operations? What if each pair had a lower cost and higher performance than the one before it?

If each pair has lower cost and performance than the one before it, then all the pairs will be added to the map, and remain in it after the series of operations, because it means that no pair dominates another pair. 

The expected running time for each `add` call would be O(log(n)) if the maxima set is implemented using a skip list, and O(n) if it is implemented using a sorted table map. That's because the item is being inserted into first position each time, so all the items in front of it need to be shifted. Therefore the total running time would be O(nlog(n)) for the skip list and O(n^2) for the sorted table map.


On the other hand, if each pair had a lower cost and higher performance than the one before it, then the map would always remain at size 1, since the newly added pair would remove the one existing pair. Therefore, for both a skip list and a sorted table map, the complexity would be O(n).

## 10.23

<img src="./ex_10_23.png">

The height of the 'towers' of the newly inserted items, 24 and 48, depends on the number of 'consecutive coin tosses which come up heads'.


## 10.24

Give a pseudo-code description of the delitem map operation when
using a skip list

```
p = skip_search(k)
if not p:
    raise KeyError
while above(p) is not None:
    unlink left and right neighbours
    p = above(p)
decrement n
```

## 10.27

What abstraction would you use to manage a database of friends’ birthdays in order to support efficient queries such as “find all friends whose birthday is today” and “find the friend who will be the next to celebrate a birthday”?

A sorted map, ideally implemented using a skip list.

## 10.31

The sieve of Erastothenes algorithm works by marking multiples of numbers as non-prime, leaving us with only prime numbers. For example, if we wanted to look for all prime numbers up to 100. We would initially set p to 2, and then mark all multiples of p in the range p^2 up to 100. We then increment p to 3, check that it has not been crossed off, and again mark all multiples of 3 in the range of 9 (p^2) to 100. We then increment to 4, but it has been crossed off already, so we continue to 5, then skip 6, go to 7, and so on. Note that we always start at p^2, because smaller multiples of p would have been marked previously. For example, when looking at mulitples of 3, we start with 9. But 6 would have already been marked when going over multiples of 2.

Now, let's look at an example to see how the bootstrapping step, in which we first find the primes up to sqrt(2M) helps. Let M = 100, such that we are looking for primes in the range 100 to 200. 

### Wihtout bootstrapping

- generate a boolean array of length 200
- mark all multiples of 2 in range 4, 200
- mark all multiples of 3 in range 9, 200
- mark all multiples of 5 in range 25, 200
- mark all multiples of 7 in range 49, 200
- mark all multiples of 11 in range 121, 200
- mark all multiples of 13 in range 169, 200 

### With bootstrapping

Bootstrapping

- generate boolean array of size 14 (square root of 200, rounded)
- mark all multiples of 2 in range 4, 14
- mark all multiples of 3 in range 9, 14
- At this point, all non-primes have been marked in the range, return list of primes [2, 3, 5, 7, 11, 13]

Generation

- generate boolean array of length 200
- mark all multiples of 2 in range 100, 200
- mark all multiples of 3 in range 102, 200
- mark all multiples of 5 in range 100, 200
- mark all multiples of 7 in range 105, 200
- mark all multiples of 11 in range 121, 200
- mark all mutliples of 13 in range 169, 200

So for numbers where p^2 is much smaller than the beginning of the range, we saved a bunch of iterations. For example for 2, rather than marking all multiples of 2 in the range 4 to 200, we marked just in the range 100 to 200

## 10.35

Describe how to perform a removal from a hash table that uses linear probing to resolve collisions where we do not use a special marker to represent deleted elements. That is, we must rearrange the contents so that it appears that the removed entry was never inserted in the first place.


[None, "A", None, "B", "C", "D", "E", None, "G"]

Let's say in the above example that "B", "C", "D" and "E" all hashed to the same value, and so "C", "D", and "E" had to probe to find an available slot. 

With special marker values, if we wanted to remove "D", we would just replace it's value with the marker, so the outcome would be:

[None, "A", None, "B", "C", _AVAIL, "E", None, "G"]

If we then queried for "E", the hash code would lead us to "B", and we would then keep checking subsequent positions, until "E" or None are found.

Without special marker values, we might be tempted to simply set "D" to None:

[None, "A", None, "B", "C", None, "E", None, "G"]

But then querying for "E" would raise KeyError, even though "E" is in the hash table.

One strategy to avoid this would be to shift all the consecutive values in front of "D"/None one to the left.

Therefore, if we wish to remove an item whose key hashes to index j, which is found at some index k = j + n, then we find the nearest None value in front of k, let's say at index i, and we shift all items between k and i by one to the left.

## 10.38

The version of binary search from exercise 10.21 can be used to find the leftmost occurence of the key from the table. It is then trivial.

## 10.39

See answer to 10.21

## 10.40

We do a 'double binary search'. We start by searching in the first array, S, by examining the element at the index k/2. This is analogous to binary search. Since we are looking for the kth smallest element, we only need to consider the elements up to k, so our 'mid' is at k/2. We then do a binary search on the second array, T, to find the greatest element which is less than or equal to the 'mid' element in S. This helps us determine how many elements there are in T which are smaller than the initial candidate from S. We then sum the indices of the two elements that we found. This sum is equal to the number of elements in S and T which are smaller than our current candidate. Indeed, the goal is to get this sum to equal to k. If the sum is equal to the k, then we can just return the greater of the two elements at the given indices. If it is smaller, then we set k = k/2 and repeat the process. This takes log(n) probes in S, and for each of them, we need to doo a log(n) search in T, hence the complexity is log(n)^2

## 10.41

Notes based on [this](https://www.youtube.com/watch?v=l5siJgontlE) explanation

An alternative way to think about this problem from 10.40 and 10.41 is that we would like to find a partitioning of the two arrays which leaves us with the k smallest elements, and then we can just return the greatest element from this partitioning.

For example, if we have have the following two arrays

1 3 5 7 20 25 40  
3 4 8 9 12 15 22 35 60 70

And we would like to find the 5th smallest element, then we first want to create partitions in the two arrays, such that we have the five smallest elements. For demonstration, let's say we picked our initial partitions like so:

1 | 3 5 7 20 25 40  
3 4 8 9 | 12 15 22 35 6 70

To check whether we really have the five smallest elements, we need to do a cross-check. Since the arrays are sorted, it's obvious that we cannot find a smaller item within a given aray to the left of the current partition. Instead, we want to compare the last element of the partition of array 1 to the first element outside the partition of array 2, and vice versa. So in this case, we compare the 9 in the second array with the 3 in the first array. The 3 is smaller, so we need to adjust our partitioning:

1 3 | 5 7 20 25 40  
3 4 8 | 9 12 15 22 35 6 70

Now we compare the 8 in the second array, to the 5 in the first array, and again we see that we need to adjust the partitioning

1 3 5 | 7 20 25 40  
3 4 | 8 9 12 15 22 35 6 70

When we check now, we see that we do indeed have the right partitioning containing the five smallest elements. We can now just return the greater of the last elements of each partition, which in this case is 5, and we are done.

The challenge is to now implement this in O(log(n)) complexity, using binary search.

First, let's assume our arguments are called arr1 and arr2, and that arr2 is the bigger array.

Let's see what we want to set our `low` and `high` to for our binary search.

For `low`, we want the max of 0 and (k - arr2.length - 1). The second expression is there in case that k is greater than length of arr2. For example, if arr2 has 10 elements, and k is 12, then we will always want at least 2 elements from arr1. The -1 is in the expression to adjust for 0 based indexing (ie if we want at least two elements from arr1, then the index of the second item is 1, rather than 2).

For `high`, we want the min of k and arr1.length. This makes sense, because the greatest number of elements we could have in a partition is k, in the case where we take no elements from one array.

For `mid`, which is the index of the partitioning of array1, we choose `low + (high - low) / 2`, like in typical binary search.

Looking at our example, if we set k = 6, then we would have

- low = 0, since k is not greater than the length of the bigger array
- high = 6, since k is not greater than the length of the smaller high
- mid would then be 3, so our partitioning would be:

1 3 5 7 | 20 25 40  
3 4 8 9 12 15 22 35 60 70

We also want to choose a `mid2`, which is the index of the partitioning of array2, which will be `k - mid - 2`, because we want the index of the last item in the partition of the second array:

1 3 5 7 | 20 25 40  
3 4 | 8 9 12 15 22 35 60 70  

Then, we want to do the comparisons. Let's label the 4 compared values like so:

```
      l1  r1
1 3 5 7 | 20 25 40
  l2  r2  
3 4 | 8 9 12 15 22 35 60 70
```

Such that l1, r1 and l2, r2 are the elements just to the left and just to the right of the partitions.

We set the variables to the following values:

```
l1 = arr1[mid]
# mid2 could be negative, if we are not taking any value from the second array
l2 = arr2[mid2] if mid2 >= 0 else float('-inf')
r1 = arr1[mid+1] if mid+1 < len(arr1) else float('inf')
r2 = arr2[mid2+1] if mid2+1 < len(arr2) else float('inf')
```

Now we can do our checks

```
if l1 <= r2 and l2 <= r1:
    # we have the correct partitioning, return the greater of the two elements
    return max(l1, l2)
if l1 > r2:
    # we need to decrease partition of arr1 and increase partition of arr2
    high = mid
if l2 > r1:
    # we need to decrease partittion of arr2 and increase partition of arr1
    low = mid + 1
```

Since only our `mid` is based on `high` and `low` (`mid2` is just `k - mid - 2`), we are only really searching for the correct partition index in arr1. Therefore, when l1 is greater than r2, and we need to decrease the partition of arr1, we look to the left, by setting high = mid. And if l2 is greater than r1, and we need to increase the partition of arr1, we look to the right, so we set low = mid + 1.

So the complete code ends up being:

```
def kth_smallest(arr1: list[int], arr2: list[int], k: int) -> int:
    # assume arr1 is the smaller array, which is the one we want to search on
    if len(arr1) > len(arr2):
        return kth_smallest(arr2, arr1, k)
    low = min(0, k - len(arr2) - 1)
    high = max(k, len(arr1))

    while low < high:
        mid = low + ((high - low) / 2)
        mid2 = k - mid - 2

        l1 = arr1[mid]
        # mid2 could be negative, if we are not taking any value from the second array
        l2 = arr2[mid2] if mid2 >= 0 else float('-inf')
        r1 = arr1[mid+1] if mid+1 < len(arr1) else float('inf')
        r2 = arr2[mid2+1] if mid2+1 < len(arr2) else float('inf')

        if l1 <= r2 and l2 <= r1:
            # we have the correct partitioning, return the greater of the two elements
            return max(l1, l2)
        if l1 > r2:
            # we need to decrease partition of arr1 and increase partition of arr2
            high = mid
        if l2 > r1:
            # we need to decrease partittion of arr2 and increase partition of arr1
            low = mid + 1

    # if we take no items from arr1
    return arr2[k-1]
```