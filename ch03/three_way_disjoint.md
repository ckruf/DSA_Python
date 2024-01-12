# Three way disjointness

Given three sets of integers - A, B and C - we want to determine whether their intersection is empty, meaning that there is no number which can be found in all three sets.

## Naive, cubic approach

```
def disjoint1(A, B, C):
    for a in A:
        for b in B:
            for c in C:
                if a == b == c:
                    return False

    return True
```

Assuming each of the three sets contains n elements, the above algorithm is O(n^3). 

Using a simple observation, we can do better

## Improved, quadratic approach

```
def disjoint2(A, B, C):
    for a in A:
        for b in B:
            if a == b:
                for c in C:
                    if c == b:
                        return False
    return True
```

The algorithm above is a significant improvement, because it only checks the third set if the number is found in the first two sets. 

This algorithm is O(n^2). The checking of the condition `if a == b` will run O(n^2) times. The checking of the condition `if c == b` can run at most O(n^2) times, under our assumption that each of the sets does not have duplicates. Why? Think about the worst case, where A and B are identical sets, for example A = {1, 2, 3, 4, 5} and B = {1, 2, 3, 4, 5}. In this case, we will have n matches. And for each of the n matches, we check n elements in C. Therefore, the `if c == b` condition will run at most n^2 times.

