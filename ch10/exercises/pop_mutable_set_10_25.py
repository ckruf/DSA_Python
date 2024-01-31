"""
Five core methods of MutableSet:
- add, discard, contains , len , and iter 

pop() behavior:
Remove and return an arbitrary element from the set. If the
set is empty, raise a KeyError.

Give a concrete implementation of the pop method, in the context of a
MutableSet abstract base class, that relies only on the five core set 
behaviors described in Section 10.5.2.
"""


from collections.abc import MutableSet


class PoppedSet(MutableSet):

    def pop(self):
        if len(self) == 0:
            raise KeyError()
        element_to_remove = None
        for e in self:
            element_to_remove = e
            break
        self.discard(element_to_remove)
        return element_to_remove