"""
Exercise 6.1

These are the values returned:
3, 8, 2, 1, 6, 7, 4, 9

Exercise 6.2

The current size is 18. We has 25 push operations and 10 pops, of which 7 were successful. 25- 7 = 18


"""
 
 # Implementations of stack and queue, not an exercise itself, but needed
 # for other exercises.

class Empty(Exception):
  pass

class ArrayStack:

  def __init__(self):
    self._data = []

  def push(self, value):
    self._data.append(value)

  def pop(self):
    if len(self._data) > 0:
      return self._data.pop()
    else:
      raise Empty("Can't pop from empty stack")
    
  def top(self):
    if len(self._data) > 0:
      return self._data[-1]
    else:
      raise Empty("Stack is empty")
    
  def is_empty(self):
    return len(self._data) == 0
  
  def __len__(self):
    return len(self._data)
  

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

# 6.3

def transfer(S: ArrayStack, T: ArrayStack):
  """
  Transfer all elements from queue S to queue T, such that
  the element that starts at the top of S is the first to be 
  inserted onto T, and the element at the bottom of S ends up at 
  the top of T.
  """
  for _ in range(len(S)):
    T.push(S.pop())

# 6.5 
  
def reverse_with_stack(lst: list):
  stack = ArrayStack()
  length = len(lst)
  for element in lst:
    stack.push(element)
  for i in range(length):
    lst[i] = stack.pop()

if __name__ == "__main__":
  my_lst = [i for i in range(6)]
  reverse_with_stack(my_lst)
  print(my_lst)