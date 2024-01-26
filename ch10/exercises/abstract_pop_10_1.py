"""
Give a concrete implementation of the pop method in the context of the
MutableMapping class, relying only on the five primary abstract methods
of that class: __getitem__, __setitem__, __delitem__, __iter__, __len__
"""

from collections.abc import MutableMapping

class PoppedMapping(MutableMapping):

    def pop(self, k, d=None):
        try:
            value = self[k]
            del self[k]
            return value
        except KeyError as e:
            if d is not None:
                return d
            raise e from e