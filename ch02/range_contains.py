import datetime


class Range:
  """A class that mimic's the built-in range class."""

  def __init__(self, start, stop=None, step=1):
    """Initialize a Range instance.

    Semantics is similar to built-in range class.
    """
    if step == 0:
      raise ValueError('step cannot be 0')
      
    if stop is None:                  # special case of range(n)
      start, stop = 0, start          # should be treated as if range(0,n)

    # calculate the effective length once
    self._length = max(0, (stop - start + step - 1) // step)

    # need knowledge of start and step (but not stop) to support __getitem__
    self._start = start
    self._step = step
    # need stop for simple __contains__ 
    self._stop = stop

  def __len__(self):
    """Return number of entries in the range."""
    return self._length

  def __getitem__(self, k):
    """Return entry at index k (using standard interpretation if negative)."""
    if k < 0:
      k += len(self)                  # attempt to convert negative index

    if not 0 <= k < self._length:
      raise IndexError('index out of range')

    return self._start + k * self._step

  def __contains__(self, val):
    print("__contains run__")
    if ((val - self._start) % self._step == 0) and val >= self._start and val < self._stop:
        return True
    else:
        return False


if __name__ == "__main__":
    my_range = Range(2, 12, 3)
    for i in range(2, 30):
        print(f"{i} is in my_range - {i in my_range}")
    


