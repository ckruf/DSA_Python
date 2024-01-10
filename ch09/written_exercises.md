# Exercises

## 9.1

Each remove_min operation takes log(n) time, so removing the log(n) smallest elements would take log(n) * log(n) = (log(n))^2 time.

## 9.2

In a preorder traversal, children are always visited after their parents, so the ranks (and therefore also keys) of children would always be greater than those of parents. Therefore, the heap order property would always be satisified. So in order for the binary tree to be a heap, it would also have to satisfy the complete binary tree property.

## 9.3

1, D

3, J
4, B

5, A

2, H
6, L


## 9.4

A priority queue implemented using a heap. A priority queue is well-suited, because we want to remove items with the lowest priority, and add items with arbitrary priority (ie not necessarily to the end). And a heap implementation offers the best possible running times for these two operations, with logarithmic time for both adding and removing the minimum item. 

## 9.5

