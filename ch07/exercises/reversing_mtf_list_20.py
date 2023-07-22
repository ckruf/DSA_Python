"""
File containing solution attempt for exercise 7.20.

This solution doesn't actually require any code.

Problem:

Let L be a list of n items maintained according to the move-to-front heuristic. 
Describe a series of O(n) accesses that will reverse L.

Solution:

Access the items in the same order in which they are currently. For example,
if the list is currently "A", "B", "C" and we access the items in that same order,
then the order will be "C", "B", "A"
"""