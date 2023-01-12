from abc import ABCMeta, abstractmethod


class Sequence(metaclass=ABCMeta):
    
    @abstractmethod
    def __len__(self):
        """Return the length of the sequence"""
    
    @abstractmethod
    def __getitem__(self, j):
        """Return the element at index j of the sequence"""

    def __contains__(self, val):
        """Return True if val is found in sequence, False otherwise"""
        for j in range(len(self)):
            if self[j] == val:
                return True
        return False 
    
    def index(self, val):
        """Return the leftmost index at which val is found, or raise ValueError"""
        for j in range(len(self)):
            if self[j] == val:
                return j
        raise ValueError("value not in sequence")

    def count(self, val):
        """Return the number of elements equal to given value"""
        count = 0
        for j in range(len(self)):
            if self[j] == val:
                count += 1
        return count


class MyBadSequence(Sequence):
    pass


class MyGoodSequence(Sequence):
    def __init__(self, values: list) -> None:
        self.values = values

    
    def __len__(self):
        return len(self.values)


    def __getitem__(self, j):
        return self.values[j]


class WeakSequence:
    @abstractmethod
    def __len__(self):
        """Return the length of the sequence"""
    
    @abstractmethod
    def __getitem__(self, j):
        """Return the element at index j of the sequence"""

    def __contains__(self, val):
        """Return True if val is found in sequence, False otherwise"""
        for j in range(len(self)):
            if self[j] == val:
                return True
        return False 
    
    def index(self, val):
        """Return the leftmost index at which val is found, or raise ValueError"""
        for j in range(len(self)):
            if self[j] == val:
                return j
        raise ValueError("value not in sequence")

    def count(self, val):
        """Return the number of elements equal to given value"""
        count = 0
        for j in range(len(self)):
            if self[j] == val:
                count += 1
        return count


if __name__ == "__main__":
    my_wrapped_list = MyGoodSequence([1, 2, 3, 2, 1])
    print("4 is in list: ", 4 in my_wrapped_list)
    print("1 is in list: ", 1 in my_wrapped_list)
    print("1-count in list: ", my_wrapped_list.count(1))
    try:
        my_bad_list = MyBadSequence()
    except Exception as e:
        print("could not instantiate MyBadSequence: ")
        print(e)

    try:
        my_sequence = Sequence()
    except Exception as e:
        print("could not instantiate Sequence: ")
        print(e)

    try:
        weak_seqeunce = WeakSequence()
        print("success")
    except Exception as e:
        print("Could not instantiate WeakSequence")
        print(e)
