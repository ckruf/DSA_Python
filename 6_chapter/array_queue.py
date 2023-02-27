class Empty(Exception):
  pass


class ArrayQueue:
  """
  A queue implemented using a python list and modular arithmetic (circular queue).
  """
  INITIAL_SIZE = 10

  def __init__(self):
    self._data = [None] * ArrayQueue.INITIAL_SIZE
    self._size = 0
    self._front = 0
    
  def enqueue(self, val) -> None:
    """
    Add element to the end of the queue.
    """
    if self._size == len(self._data):
      self._resize(2*len(self._data))
    avail = (self._front + self._size) % len(self._data)
    self._data[avail] = val
    self._size += 1

  def dequeue(self):
    """
    Remove element from the front of the queue.
    """
    if self.is_empty():
      raise Empty("Queue is empty")
    front_val = self._data[self._front]
    self._data[self._front] = None
    self._front = (self._front + 1) % len(self._data)
    self._size -= 1
    if 0 < self._size < len(self._data) // 4:
      self._resize(len(self._data) // 2)
    return front_val

  def __len__(self):
    return self._size
  
  def is_empty(self):
    return len(self) == 0
  
  def first(self):
    if self.is_empty():
      raise Empty("Queue is empty")
    return self._data[self._front]
  
  def _resize(self, capacity: int):
    if capacity < self._size:
      raise ValueError(f"There are {self._n} items in the queue") 
    old = self._data
    self._data = [None] * capacity
    start = self._front
    for i in range(self._size):
      self._data[i] = old[start]
      start = (1 + start) % len(old)
    self._front = 0
