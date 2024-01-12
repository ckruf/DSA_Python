class SequenceIterator:
    """An iterator for any of Python s sequence types."""
    def __init__(self, sequence):
        """Create an iterator for the given sequence."""
        self.seq = sequence # keep a reference to the underlying data
        self.k = -1 # will increment to 0 on first call to next

    def __next__(self):
        """Return the next element, or else raise StopIteration error."""
        self.k += 1 # advance to next index
        if self.k < len(self. seq):
            return self.seq[self.k] # return the data element
        else:
            raise StopIteration() # there are no more elements
    
    def __iter__(self):
        """By convention, an iterator must return itself as an iterator."""
        return self


class ReversedSequenceIterator:
    """A reversed iterator for any of Python's sequence types."""
    
    def __init__(self, sequence):
        """Create a reversed iterator for the given sequence."""
        self.seq = sequence
        self.k = len(sequence)

    def __next__(self):
        """Return the next element, or raise StopIteration error."""
        self.k -= 1
        if self.k >= 0:
            return self.seq[self.k]
        else:
            raise StopIteration()

    def __iter__(self):
        """By concention, an iterator must return self as iterator"""
        return self


def main() -> None:
    my_lst = [1, 2, 3, 4]
    itrtr = SequenceIterator(my_lst)
    for val in itrtr:
        print(val)

    rev_itrtr = ReversedSequenceIterator(my_lst)
    for val in rev_itrtr:
        print(val)



if __name__ == "__main__":
    main()