"""
Exercise 6.1

These are the values returned:
3, 8, 2, 1, 6, 7, 4, 9

Exercise 6.2

The current size is 18. We has 25 push operations and 10 pops, of which 7 were successful. 25- 7 = 18

Exercise 6.7

These are the values returned:

5, 3, 2, 8, 9, 1, 7, 6

Exercise 6.8

Current size is 22, because there were 32 enqueue operations and 10 successful dequeue operations

Exercise 6.9

10, because the front value increases by one each time we dequeue

Exercise 6.10

If the queue is wrapped around the end, and we just copy the items to the same positions, while changing the 
size of the underlying list, then the items will end up in the wrong positions, because their
positions were calculated using modular arithmetic, which changes when the list size changes.

Exercise 6.12

back() 9
delete_first() 5
delete_last() 9
first() 4
last() 7
delete_first() 4
delete_first() 8

9, 5, 9, 4, 7, 4, 8
"""

from collections import deque
from typing import Optional, Any

 # Implementations of stack and queue, not an exercise itself, but needed
 # for other exercises.

class Empty(Exception):
  pass

class Full(Exception):
  pass

class ArrayStack:

  def __init__(self, maxlen: Optional[int] = None):
    # 6.16, 6.17
    self.maxlen = maxlen
    if maxlen is not None:
      # pre allocate list of maxlen size
      self._data = [None] * maxlen
    else:
      self._data = [None,]
      self._capacity = 1
    self._size = 0
    

  def push(self, value) -> None:
    if self._size == self.maxlen:
      raise Full(f"Maximal length {self.maxlen} reached")
    elif self._size == self._capacity:
      self._resize(2 * self._capacity)
    self._data[self._size] = value
    self._size += 1 

  def pop(self) -> Any:
    if self._size == 0:
      raise Empty("Can't pop from empty stack")

    if self._capacity and self._size == self._capacity // 4:
      self._resize(self._capacity // 2)
    answer = self._data[self._size - 1]
    self._data[self._size - 1] = None
    self._size -= 1
    return answer
    
  def top(self) -> Any:
    if self._size > 0:
      return self._data[self._size - 1]
    else:
      raise Empty("Stack is empty")
    
  def is_empty(self) -> bool:
    return self._size == 0

  def _resize(self, capacity: int) -> None:
    new = [None] * capacity
    for i in range(self._size):
      new[i] = self._data[i]
    self._data = new
    self._capacity = capacity
  
  def __len__(self):
    return self._size

  def __str__(self):
    return str([i for i in self._data if i is not None])
  

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

  def __str__(self):
    return str([self._data[(i + self._front)] % self._size for i in range(self._size)])


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


# 6.4
def remove_recursively(S: ArrayStack):
  if len(S) == 0:
    return
  else:
    S.pop()
    remove_recursively(S)


# 6.5   
def reverse_with_stack(lst: list):
  stack = ArrayStack()
  length = len(lst)
  for element in lst:
    stack.push(element)
  for i in range(length):
    lst[i] = stack.pop()


# 6.11
class DequeQueue:
  """
  Implementing the queue ADT using collections.deque
  """

  def __init__(self):
    self._data = deque()

  def enqueue(self, val) -> None:
    self._data.appendleft(val)

  def dequeue(self):
    return self._data.pop()

  def __len__(self):
    return len(self._data)

  def is_empty(self):
    return len(self) == 0

  def first(self):
    return self._data[-1]

def change_order_queue():
  """
  Given a deque containing numbers (1, 2, 3, 4, 5, 6, 7, 8),
  use an initially empty queue to change the order in the deque
  to (1, 2, 3, 5, 4, 6, 7, 8). You may not use any other variables.
  """
  Q = ArrayQueue()
  D = deque((1, 2, 3, 4, 5, 6, 7, 8))
  D.appendleft(D.pop())
  D.appendleft(D.pop())
  D.appendleft(D.pop())
  D.appendleft(D.pop())
  # 5, 6, 7, 8, 1, 2, 3, 4
  print(D)


  Q.enqueue(D.pop())
  D.append(D.popleft())
  # 6, 7, 8, 1, 2, 3, 5 in deque
  # 4 in queue

  Q.enqueue(D.popleft())
  Q.enqueue(D.popleft())
  Q.enqueue(D.popleft())
  # 1, 2, 3, 5 in deque
  # 4, 6, 7, 8 in queue


  D.append(Q.dequeue())
  D.append(Q.dequeue())
  D.append(Q.dequeue())
  D.append(Q.dequeue())
  # 1, 2, 3, 5, 4, 6, 7, 8 in deque
  # queue empty
  print(D)


def change_order_stack():
  """
  Given a deque containing numbers (1, 2, 3, 4, 5, 6, 7, 8),
  use an initially empty stack to change the order in the deque
  to (1, 2, 3, 5, 4, 6, 7, 8). You may not use any other variables.
  """
  D = deque((1, 2, 3, 4, 5, 6, 7, 8))
  S = ArrayStack()
  S.push(D.pop())
  S.push(D.popleft())
  S.push(D.pop())
  S.push(D.popleft())
  S.push(D.pop())
  S.push(D.popleft())
  D.appendleft(D.pop())
  # deque 5, 4
  # stack 8, 1, 7, 2, 6, 3 <- TOP
  D.appendleft(S.pop())
  D.append(S.pop())
  D.appendleft(S.pop())
  D.append(S.pop())
  D.appendleft(S.pop())
  D.append(S.pop())

  print(f"deque: {D}")


# 6.15
def choose_largest():
  """
  Suppose a stack contains three randomly chosen distinct integers. Write a short function
  which uses one variable and one comparison to find the largest of the three integers
  with probability 2/3.
  """
  S = ArrayStack()
  S.push(7)
  S.push(5)
  S.push(3)

  x = S.pop()
  if x < S.top():
    x = S.top()
  # if the largest integer is either in the first or in the second position,
  # we will choose it, therefore 2/3 probability


#6.18
def reverse_stack():
  """
  Show how you can use the transfer() function and two temporary stacks to 
  reverse the items in stack S.
  """
  A = ArrayStack()
  B = ArrayStack()
  S = ArrayStack()
  for i in range(5):
    S.push(i)
  print(f"S is {S}")
  transfer(S, A)
  transfer(A, B)
  transfer(B, S)
  print(f"S is {S}")


# 6.19
def is_matched_html(raw: str) -> bool:
  """
  Use a stack to determine whether all tags in given HTML strings are matched.
  Return True for valid HTML, and False otherwise.
  """
  tags = ArrayStack()

  opening_tag_index = raw.find("<")
  while opening_tag_index != -1:

    closing_tag_index = raw.find(">", opening_tag_index)
    
    if closing_tag_index == -1:
      return False
    
    space_index = raw.find(" ", opening_tag_index, closing_tag_index)
    
    if space_index == -1:
      end = closing_tag_index
    else:
      end = space_index
    tag = raw[opening_tag_index + 1:end]

    if tag.startswith("/"):
      tag = tag[1:]
      if tags.is_empty():
        return False
      if tag != tags.pop():
        return False
    else:
      tags.push(tag)
    
    opening_tag_index = raw.find("<", closing_tag_index)


  return tags.is_empty()

class TestIsMatchedHTML:
  
  @classmethod
  def run_all(cls):
    cls.test_is_matched_html_pass()
    cls.test_is_matched_html_fail_missing_matching()
    cls.test_is_matched_html_fail_non_matching()
    cls.test_is_matched_html_fail_tag_unclosed()
    cls.test_is_matched_html_fail_tag_unclosed_no_space()
    cls.test_is_matched_html_with_attributes_pass()


  @staticmethod
  def test_is_matched_html_pass():
    """
    Test function for is_matched_html(), with a valid HTML string
    """
    matched_html = """
    <html>
      <body>
        <h1>Hello, world</h1>
        <p>Lorem ipsum doloraes</p>
      </body>
    </html>
    """
    assert is_matched_html(matched_html)
    print("test passed")

  @staticmethod
  def test_is_matched_html_fail_non_matching():
    """
    Test function for is_matched_html(), with HTML string which is invalid
    because opening and closing tags do not match (<h1></h2>)
    """
    mismatched_html = """
    <html>
      <body>
        <h1>Hello, world</h2>
        <p>Lorem ipsum doloraes</p>
      </body>
    </html>
    """
    assert is_matched_html(mismatched_html) is False
    print("test passed")

  @staticmethod
  def test_is_matched_html_fail_missing_matching():
    """
    Test with HTML string which is invalid because of a missing closing HTML tag (<html>)
    """
    missing_matching_html = """
    <html>
      <body>
        <h1>Hello, world</h2>
        <p>Lorem ipsum doloraes</p>
      </body>
    """
    assert is_matched_html(missing_matching_html) is False
    print("test passed")

  @staticmethod
  def test_is_matched_html_fail_tag_unclosed():
    """
    Test with HTML string which is invalid because of an unclosed HTML tag(<p ).
    """
    missing_matching_html = """
    <html>
      <body>
        <h1>Hello, world</h2>
        <p Lorem ipsum doloraes</p>
      </body>
    """
    assert is_matched_html(missing_matching_html) is False
    print("test passed")

  @staticmethod
  def test_is_matched_html_fail_tag_unclosed_no_space():
    """Same as test above, but no space after p"""
    missing_matching_html = """
    <html>
      <body>
        <h1>Hello, world</h2>
        <pLorem ipsum doloraes</p>
      </body>
    """
    assert is_matched_html(missing_matching_html) is False
    print("test passed")

  @staticmethod
  def test_is_matched_html_with_attributes_pass():
    """
    Test function for is_matched_html(), with a valid HTML string
    """
    matched_html = """
    <html>
      <body color="red">
        <h1 font-size="11px" color="blue">Hello, world</h1>
        <p text-align="center">Lorem ipsum doloraes</p>
      </body>
    </html>
    """
    assert is_matched_html(matched_html)
    print("test passed")




if __name__ == "__main__":
  TestIsMatchedHTML.run_all()