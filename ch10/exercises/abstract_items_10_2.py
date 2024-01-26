"""
Give a concrete implementation of the items() method in the context of the 
MutableMapping class, relying only on the five primary abstract methods 
__getitem__, __setitem__, __delitem__, __iter__, __len__. 
What would its running time be if directly applied to the UnsortedTableMap subclass?
"""


from collections.abc import MutableMapping


class ItemsMapping(MutableMapping):

    def items(self):
        """
        Run time using UnsortedTableMap is O(n^2), because each self[k] call
        is O(n)
        """
        for k in self:
            yield k, self[k]