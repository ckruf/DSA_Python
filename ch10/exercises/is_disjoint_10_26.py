"""
Give a concrete implementation of the isdisjoint method in the context
of the MutableSet abstract base class, relying only on the five primary
abstract methods of that class. Your algorithm should run in O(min(n,m))
where n and m denote the respective cardinalities of the two sets
"""
from collections.abc import MutableSet


class IsDisjointSet(MutableSet):

    def isdisjoint(self, t: MutableSet):
        if len(self) < len(t):
            shorter_set = self
            other_set = t
        else:
            shorter_set = t
            other_set = self
        for e in shorter_set:
            if e in other_set:
                return False
        return True