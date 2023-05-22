from typing import Any, List

class Empty(ValueError):
  pass
  

class ArrayStack:
  
  def __init__(self):
    self._data = []

  def push(self, elem: Any) -> None:
    self._data.append(elem)

  def pop(self) -> Any:
    if len(self) == 0:
      raise Empty("The stack is empty")
    return self._data.pop()
  
  def top(self) -> Any:
    if len(self) == 0:
      raise Empty("The stack is empty")
    return self._data[-1]
  
  def is_empty(self) -> bool:
    return len(self) == 0
  
  def __len__(self) -> int:
    return len(self._data)

def stack_test():
  S = ArrayStack()
  stack_elems = ["A", "B", "C", "D"]

  for elem in stack_elems:
    print(elem)
    S.push(elem)

  for elem in reversed(stack_elems):
    print(S.top())
    assert S.pop() == elem


class ArrayQueue:
  DEFAULT_CAPACITY = 10
  _data: List[Any]
  _size: int
  _front: int
  
  def __init__(self):
    self._data = [None] * self.DEFAULT_CAPACITY
    self._size = 0
    self._front = 0

  def enqueue(self, elem: Any) -> None:
    if self._size == len(self._data):
      self._resize(2 * self._size)
    index = (self._front + self._size) % len(self._data)
    self._data[index] = elem
    self._size += 1

  def dequeue(self) -> Any:
    if self._size == 0:
      raise Empty("The queue is empty")
    if (self._size - 1) < (len(self._data) / 4):
      new_size = round(len(self._data) / 2)
      self._resize(new_size)
    elem = self._data[self._front]
    self._data[self._front] = None
    self._front = (self._front + 1) % len(self._data)
    self._size -= 1
    return elem

  def is_empty(self) -> bool:
    return len(self) == 0

  def __len__(self) -> int:
    return self._size
  
  def _resize(self, new_capacity: int) -> None:
    new_list: List[Any] = [None] * new_capacity
    for i in range(self._size):
      new_list[i] = self._data[(self._front + i) % len(self._data)]
    self._front = 0
    self._data = new_list

  def first(self) -> Any:
    if self._size == 0:
      raise Empty("The queue is empty")
    return self._data[self._front]
  

def basic_queue_test() -> None:
  """Test the basic functionality of the queue - the enqueuing and dequeuing of elements in the right order."""
  Q = ArrayQueue()
  Q.enqueue("A")
  Q.enqueue("B")
  Q.enqueue("C")
  assert Q.dequeue() == "A"
  assert Q.dequeue() == "B"
  assert Q.dequeue() == "C"

def wrap_around_queue_test() -> None:
  """Test that the queue wraps around properly"""
  Q = ArrayQueue()
  # fill up queue with 0-9
  for i in range(10):
    Q.enqueue(i)
  # dequeue 0,1; so that the next items we enqueue wrap around without resizing
  assert Q.dequeue() == 0
  assert Q.dequeue() == 1

  Q.enqueue(10)
  Q.enqueue(11)

  assert Q._data == [10, 11] + [i for i in range(2, 10)]

  # dequeue elements such that 3 are left (so we avoid resizing again, as going below 2
  # would cause the queue to shrink the underlying array
  for i in range(2, 9):
    assert Q.dequeue() == i

  assert Q._data == [10, 11] + (7 * [None]) + [9,]

  # enqueue 12, 13, 14, 15, 16

  for i in range(12, 17):
    Q.enqueue(i)

  assert Q._data == [10, 11] + [i for i in range(12, 17)] + [None, None] + [9,]

  # finally, test that wrapped around items 10, 11, 12 dequeue when they should

  for i in range(9, 13):
    assert Q.dequeue() == i

  print("wrap around queue test passed")


def resize_when_full_queue_test() -> None:
  """Test that the queue doubles in size when full, and keeps elements in proper order"""
  Q = ArrayQueue()

  for i in range(10):
    Q.enqueue(i)

  assert len(Q._data) == Q.DEFAULT_CAPACITY

  Q.enqueue(10)

  assert len(Q._data) == 2 * Q.DEFAULT_CAPACITY

  for i in range(11):
    assert Q.dequeue() == i

  print("resize queue when full test passed")


def resize_when_quarter_full_queue_test() -> None:
  """Test that the queue halves in size when quarter full, and keeps elements in proper order"""
  Q = ArrayQueue()
  for i in range(3):
    Q.enqueue(i)

  assert len(Q._data) == Q.DEFAULT_CAPACITY

  assert Q.dequeue() == 0

  assert len(Q._data) == round(Q.DEFAULT_CAPACITY / 2) == 5

  print("resize queue when quarter full test passed")


def throws_exception_when_empty_test() -> None:
  """Test that the queue throws an exception when we attempt to dequeue() or first() on an empty queue"""
  Q = ArrayQueue()

  try:
    Q.dequeue()
    # make sure this is not reached, as the above line should throw an exception
    assert False
  except Exception as e:
    assert isinstance(e, Empty)

  print("throws exception when empty test passed")

def run_all_queue_tests() -> None:
  wrap_around_queue_test()
  resize_when_full_queue_test()
  resize_when_quarter_full_queue_test()
  throws_exception_when_empty_test()


if __name__ == "__main__":
  run_all_queue_tests()