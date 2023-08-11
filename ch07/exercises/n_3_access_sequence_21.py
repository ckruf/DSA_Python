"""
File containing solution attempt for exercise 7.21.

This solution doesn't actually require any code.

Problem:
Suppose we have an n-element list L maintained according to the move-to-front
heuristic. Describe a sequence of n^2 accesses that is guaranteed
to take Ω(n^3) time to perform on L.

Solution:

Each access will have to have Ω(n) complexity. This can be achieved by accessing
the last element each time. This is the same as accessing the elements in 
the opposite of the current order. So if the current list is "A", "B", "C";
then access the elements in order "C", "B", "A".
"""
