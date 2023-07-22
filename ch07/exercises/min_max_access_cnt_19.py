"""
File containing solution attempt for exercise 7.19.

This solution doesn't actually require any code.

Problem:

Suppose that we have made kn total accesses to the elements in a list L of
n elements, for some integer k ≥ 1. What are the minimum and maximum
number of elements that have been accessed fewer than k times?

Solution:

- We could access a single element kn times, therefore the remaining n-1 elements
would be accessed fewer than k times. So maximum is n - 1.
- We could access each of the n elements k times. Then, no element would be
accessed fewer than k times. So minimum is 0.
"""