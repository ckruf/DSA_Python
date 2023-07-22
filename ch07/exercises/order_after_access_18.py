"""
File containing solution attempt for exercise 7.18.

This solution doesn't actually require any code.

Problem:
Given the set of element {a,b,c,d,e, f } stored in a list, show the final state
of the list, assuming we use the move-to-front heuristic and access the elements 
according to the following sequence: (a,b,c,d,e,f,a,c,f,b,d,e).

Solution:

We can split the access sequence into two halves, and ignore the first one,
since all elements are accessed in both halves of the access sequence.

The final order of the list will just be the second half of the access sequence
backwards, so: e, d, b, f, c, a.
"""