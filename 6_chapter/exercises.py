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
from typing import Optional, Any, Callable, Tuple, Union, List, Sequence

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

  # def __str__(self):
  #   return str([self._data[(i + self._front) % self._size] for i in range(self._size)])
  
  def __str__(self):
    return str(self._data)


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


def number_permutations_recursive(numbers: list[int | float]) -> list[list[int | float]]:
  results = []
  length = len(numbers)
  
  def recurse(seq: list[int | float], curr: int, acc: list[str]):
    if curr == length:
      acc.append(seq.copy())
    else:
      for i in range(curr, length):
        seq[curr], seq[i] = seq[i], seq[curr]
        recurse(seq, curr + 1, acc)
        seq[curr], seq[i] = seq[i], seq[curr]

  recurse(numbers, 0, results)
  return results


# 6.20
def number_permutations_stack(numbers: list[int | float]) -> list[list[int | float]]:
  length = len(numbers)
  results = []
  curr = 0
  stack = ArrayStack()
  stack.push((numbers, curr))

  while not stack.is_empty():
    numbers, curr  = stack.pop()
    if curr == length:
      results.append(numbers)
    else:
      for i in range(curr, length):
        numbers[curr], numbers[i] = numbers[i], numbers[curr]
        stack.push((numbers.copy(), curr + 1))
        numbers[curr], numbers[i] = numbers[i], numbers[curr]

  return results


# 6.21
def generate_subsets(n):
  stack = ArrayStack(n)
  for i in range(n, 0, -1):
    stack.push(i)
  queue = ArrayQueue()
  queue.enqueue(set())

  while not stack.is_empty():
    next_item = stack.pop()
    qlen = len(queue)
    for i in range(qlen):
      subset = queue.dequeue()
      new_subset = set(subset)
      new_subset.add(next_item)
      queue.enqueue(subset)
      queue.enqueue(new_subset)

  results = []
  while not queue.is_empty():
    results.append(queue.dequeue())
  return results


# 6.21
def generate_power_set(T: set) -> list[set]:
  """
  Generate all subsets of a set T, using a stack and a queue.
  Use the stack to store the elements yet to be used to generate
  subsets and the queue to store the subsets generated so far.
  """
  stack = ArrayStack()
  for item in T:
    stack.push(item)
  queue = ArrayQueue()
  queue.enqueue(set())

  while not stack.is_empty():
    next_item = stack.pop()
    qlen = len(queue)
    for i in range(qlen):
      subset = queue.dequeue()
      new_subset = set(subset)
      new_subset.add(next_item)
      queue.enqueue(subset)
      queue.enqueue(new_subset)

  results = []
  while not queue.is_empty():
    results.append(queue.dequeue())
  return results

import operator


def parse_postfix_expression(expr: str) -> list:
  """
  Parse a string containing a post-fix arithmetic expression (made up of integers and operations only - no floats)
  into a list of numbers and operations
  """
  elements = []
  for char in expr:
    if char == " ":
      continue
    elif char.isdigit():
      elements.append(int(char))
    elif char == "+":
      elements.append(operator.add)
    elif char == "-":
      elements.append(operator.sub)
    elif char == "/":
      elements.append(operator.truediv)
    elif char == "*":
      elements.append(operator.mul)
    else:
      raise ValueError(f"Unexpected character: '{char}'")
  return elements


def test_parse_postfix_expression():
  """
  Test the 'parse_postfix_expression function
  """
  expr_1 = "5 2 + 8 3 - * 4 /"

  expr_2 = "1 1 +"

  assert parse_postfix_expression(expr_1) == [5, 2, operator.add, 8, 3, operator.sub, operator.mul, 4, operator.truediv]

  assert parse_postfix_expression(expr_2) == [1, 1, operator.add]

  print("test_parse_postfix_expression - both tests passed")


# 6.22
def evaluate_postfix(expr: list) -> int | float:
  stack = ArrayStack()
  operations = (operator.add, operator.sub, operator.truediv, operator.mul)

  for elem in expr:
    if elem in operations:
      x, y = stack.pop(), stack.pop()
      result = elem(y, x)
      stack.push(result)
    else:
      stack.push(elem)

  return stack.pop()

def test_evaluate_postfix(evaluation_fn: Callable) -> None:
  expr_1 = "5 2 + 8 3 - * 4 /"
  expr_1_list = parse_postfix_expression(expr_1)
  result = evaluation_fn(expr_1_list)
  print(f"result is {result}")
  assert result == 8.75
  print("test passed")


# 6.23
def rearrange_stacks(R: ArrayStack, S: ArrayStack, T: ArrayStack) -> Tuple[ArrayStack, ArrayStack, ArrayStack]:
  """
  Given three non-empty stacks: R, S and T; describe a sequence of operations that will result in S
  storing all the elements originally in T below all of S's original elements.
  For example if R = [1,2,3], S = [4,5] and T = [6,7,8,9] (where the right is the top of the stack),
  the final configuration should have R = [1,2,3] and S = [6,7,8,9,4,5] 
  """
  length_T = len(T)
  for _ in range(length_T):
    R.push(T.pop())
  
  length_S = len(S)
  for _ in range(length_S):
    T.push(S.pop())
  
  for _ in range(length_T):
    S.push(R.pop())
  
  for _ in range(length_S):
    S.push(T.pop())

  return R, S, T

def test_rearrange_stacks():
  R = ArrayStack()
  S = ArrayStack()
  T = ArrayStack()

  R_orig = (1, 2, 3)
  S_origin = (4, 5)
  T_origin = (6, 7, 8, 9)

  for elem in R_orig:
    R.push(elem)

  for elem in S_origin:
    S.push(elem)

  for elem in T_origin:
    T.push(elem)

  R, S, T = rearrange_stacks(R, S, T)

  print(f"R: {R}")
  print(f"S: {S}")
  print(f"T: {T}")

  for elem in reversed(R_orig):
    assert elem == R.pop()

  assert R.is_empty()

  T_S_combined = T_origin + S_origin
 
  for elem in reversed(T_S_combined):
    assert elem == S.pop()

  assert S.is_empty()

  print("test passed")


# 6.24

class StackUsingQueue:

  def __init__(self):
    self._data = ArrayQueue()

  def push(self, element):
    self._data.enqueue(element)

  def pop(self):
    length = len(self)
    for _ in range(length - 1):
      self._data.enqueue(self._data.dequeue())
    return self._data.dequeue()

  def __len__(self):
    return len(self._data)
  
  def is_empty(self):
    return len(self) == 0
  
  def top(self):
    length = len(self)
    for _ in range(length - 1):
      self._data.enqueue(self._data.dequeue())
    result = self._data.first()
    self._data.enqueue(self._data.dequeue())
    return result


def test_stack_using_queue():
  stack = StackUsingQueue()
  stack.push(5)
  stack.push(3)
  stack.push(10)
  assert len(stack) == 3
  assert stack.pop() == 10
  assert stack.pop() == 3
  stack.push(1)
  assert stack.top() == 1
  assert len(stack) == 2
  assert stack.pop() == 1
  assert stack.pop() == 5
  assert stack.is_empty()
  print("test passed")


# 6.25
class QueueUsingStacks:
  inbox: ArrayStack
  outbox: ArrayStack

  def __init__(self):
    self.inbox = ArrayStack()
    self.outbox = ArrayStack()

  def enqueue(self, val) -> None:
    self.inbox.push(val)

  def dequeue(self) -> Any:
    if not len(self):
      raise Empty()
    if self.outbox.is_empty():
      self._move_inbox_to_outbox()
    return self.outbox.pop()

  def first(self) -> Any:
    if self.outbox.is_empty():
      self._move_inbox_to_outbox()
    return self.outbox.top()

  def is_empty(self) -> bool:
    return (len(self.inbox) + len(self.outbox)) == 0
  
  def _move_inbox_to_outbox(self):
    while len(self.inbox):
      self.outbox.push(self.inbox.pop())

  def __len__(self):
    return len(self.inbox) + len(self.outbox)
  

def test_queue_using_stacks():
  queue = QueueUsingStacks()
  queue.enqueue("A")
  queue.enqueue("B")
  queue.enqueue("C")
  assert queue.dequeue() == "A"
  assert len(queue) == 2
  queue.enqueue("D")
  assert queue.dequeue() == "B"
  assert queue.dequeue() == "C"
  assert queue.first() == "D"
  queue.enqueue("E")
  assert queue.dequeue() == "D"
  assert len(queue) == 1
  print("test passed")

# 6.26
class DequeUsingStacks():
  """
  Deque implemented using two stacks, each stack for each end of the deque.
  """
  left: ArrayStack
  right: ArrayStack
  
  def __init__(self, ):
    self.left = ArrayStack()
    self.right = ArrayStack()

  def add_first(self, val: Any) -> None:
    self.left.push(val)

  def add_last(self, val: Any) -> None:
    self.right.push(val)

  def delete_first(self) -> Any:
    if self.is_empty():
      raise Empty()
    if self.left.is_empty():
      self._move_right_to_left()

    return self.left.pop()
  
  def delete_last(self) -> Any:
    if self.is_empty():
      raise Empty()
    if self.right.is_empty():
      self._move_left_to_right()
    
    return self.right.pop()

  def first(self) -> Any:
    if self.is_empty():
      raise Empty()
    if self.left.is_empty():
      self._move_right_to_left()
    
    return self.left.top()

  def last(self) -> Any:
    if self.is_empty():
      raise Empty()
    if self.right.is_empty():
      self._move_left_to_right()
    
    return self.right.top()

  def is_empty(self) -> bool:
    return len(self) == 0

  def __len__(self) -> int:
    return len(self.left) + len(self.right)

  def _move_left_to_right(self) -> None:
    while len(self.left):
      self.right.push(self.left.pop())

  def _move_right_to_left(self) -> None:
    while len(self.right):
      self.left.push(self.right.pop())


# 6.27

def find_in_stack(x: Any, S: ArrayStack) -> Union[bool, int]:
  """
  Use a queue Q to scan a stack S to determine whether a given element (x) is found 
  in the stack. However, the elements in S have to remain in the same order.
  
  Return either the position of the element (considering the top of the stack is index 0),
  or False, if the element is not part of the stack.
  """
  Q = ArrayQueue()
  position: Union[int, bool] = False
  counter = 0
  # first move all elements from stack into queue, while looking for the element
  while len(S):
    elem = S.pop()
    if elem == x:
      position = counter
    Q.enqueue(elem)
    counter += 1
  # then move all elements back into stack, which is now reversed
  while len(Q):
    S.push(Q.dequeue())
  
  # move all elements into queue
  while(len(S)):
    Q.enqueue(S.pop())
  # move all elements back into stack, which will be in the initial order
  while(len(Q)):
    S.push(Q.dequeue())

  return position


def test_find_in_stack_middle():
  S = ArrayStack()
  stack_elems = ["A", "B", "C", "D", "E"]
  for elem in stack_elems:
    S.push(elem)
  
  # check index is correct
  assert find_in_stack("C", S) == 2

  assert len(S) == len(stack_elems)

  # check all items are in the same order 
  for elem in reversed(stack_elems):
    assert S.pop() == elem

def test_find_in_stack_begin():
  S = ArrayStack()
  stack_elems = ["A", "B", "C", "D", "E"]
  for elem in stack_elems:
    S.push(elem)
  
  # check index is correct
  assert find_in_stack("E", S) == 0

  assert len(S) == len(stack_elems)

  # check all items are in the same order 
  for elem in reversed(stack_elems):
    assert S.pop() == elem

def test_find_in_stack_end():
  S = ArrayStack()
  stack_elems = ["A", "B", "C", "D", "E"]
  for elem in stack_elems:
    S.push(elem)
  
  # check index is correct
  assert find_in_stack("A", S) == 4

  assert len(S) == len(stack_elems)

  # check all items are in the same order 
  for elem in reversed(stack_elems):
    assert S.pop() == elem

def test_find_in_stack_absent():
  S = ArrayStack()
  stack_elems = ["A", "B", "C", "D", "E"]
  for elem in stack_elems:
    S.push(elem)
  
  # check index is correct
  assert find_in_stack("Z", S) is False

  assert len(S) == len(stack_elems)

  # check all items are in the same order 
  for elem in reversed(stack_elems):
    assert S.pop() == elem

def run_all_find_in_stack_tests():
  test_find_in_stack_middle()
  test_find_in_stack_begin()
  test_find_in_stack_end()
  test_find_in_stack_absent()
  print("all 'find in stack' tests passed!")


# 6.28
class ArrayQueueMaxLen:
  """
  Array queue implementation with option to limit its capacity.
  """
  DEFAULT_CAPACITY: int = 10
  _data: List[Any]
  _size: int
  _front: int
  max_len: Optional[int]

  def __init__(self, max_len: Optional[int] = None):
    self._data = [None] * self.DEFAULT_CAPACITY
    self._size = 0
    self._front = 0
    self.max_len = max_len

  def enqueue(self, elem: Any) -> None:
    if self._size == self.max_len:
      raise Full("The queue is full")
    if self._size == len(self._data):
      self._resize(self._size * 2)
    position = (self._front + self._size) % len(self._data)
    self._data[position] = elem
    self._size += 1

  def dequeue(self) -> Any:
    if self._size == 0:
      raise Empty("The queue is empty")
    if (self._size - 1) < len(self._data) / 4:
      self._resize(len(self._data) // 2)
    elem = self._data[self._front]
    self._data[self._front] = None
    self._size -= 1
    self._front = (self._front + 1) % len(self._data)
    return elem

  def __len__(self) -> int:
    return self._size

  def is_empty(self) -> bool:
    return len(self) == 0

  def _resize(self, new_capacity: int) -> None:
    new_list = [None, ] * new_capacity
    for i in range(self._size):
      new_list[i] = self._data[(self._front + i) % len(self._data)]
    self._front = 0
    self._data = new_list


  def first(self) -> Any:
    if self._size == 0:
      raise Empty("The queue is empty")
    return self._data[self._front]
  
  # 6.29
  def rotate(self):
    if self.is_empty():
      raise Empty("The queue is empty")
    elem = self._front
    # do something with elem
    self._front = (self._front + 1) % len(self._data)
    available = (self._front + self._size) % len(self._data)
    self._front = None
    self._data[available] = elem


# 6.30
"""
Put one even integer in one of the queues (P), and all the other integers in the other queue (Q).
Then, if queue P is chosen, then Alice will alway win, and if queue Q is chosen, Alice
has 49/100 chance to win. So her overall chance of winning would be 1/2 + (1/2 * 49/99)
"""

# 6.31
"""
1. Take Mazie and Daisy across (4 minutes)
2. Go back with Daisy (4 minutes)
3. Take Lazy and Crazy across (20 minutes)
4. Go back with Mazie (2 minutes)
5. Take Mazie and Daisy across (4 minutes)
"""

# 6.32
class ArrayDeque:
  DEFAULT_CAPACITY: int = 10
  _front: int
  _size: int
  _data: List[Any]

  def __init__(self):
    self._front = 0
    self._size = 0
    self._data = [None] * self.DEFAULT_CAPACITY

  def add_first(self, elem: Any) -> None:
    if self._size == len(self._data):
      self._resize(2 * len(self._data))
    index = (self._front - 1) % len(self._data)
    self._data[index] = elem
    self._size += 1
    self._front = index


  def add_last(self, elem: Any) -> None:
    if self._size == len(self._data):
      self._resize(2 * len(self._data))
    index = (self._front + self._size) % len(self._data)
    self._data[index] = elem
    self._size += 1
    

  def delete_first(self) -> Any:
    if self.is_empty():
      raise Empty("The deque is empty")
    elem = self._data[self._front]
    self._data[self._front] = None
    self._front = (self._front + 1) % len(self._data)
    self._size -= 1
    return elem
    

  def delete_last(self) -> Any:
    if self.is_empty():
      raise Empty("The deque is empty")
    index = (self._front + self._size - 1) % len(self._data)
    elem = self._data[index]
    self._data[index] = None
    self._size -= 1
    return elem

  def first(self) -> Any:
    if self._size == 0:
      raise Empty("The deque is empty")
    return self._data[self._front]

  def last(self) -> Any:
    if self._size == 0:
      raise Empty("The deque is empty")
    index = (self._front + self._size - 1) % len(self._data)
    return self._data[index]

  def __len__(self) -> int:
    return self._size


  def is_empty(self) -> bool:
    return self._size == 0
  

  def _resize(self, new_capacity: int) -> None:
    if new_capacity < self._size:
      raise ValueError(f"Cannot resize deque to size {new_capacity} when it has {self._size} elements")
    new_data = [None] * new_capacity
    original_size = len(self._data)
    for i in range(self._size):
      new_data[i] = self._data[(self._front + i) % original_size]
    self._front = 0
    self._data = new_data


class ArrayDequeRich:
  DEFAULT_CAPACITY = 10
  _front: int
  _size: int
  _data: List[Any]
  max_len: Optional[int]

  def __init__(self, iterable: Optional[Sequence] = None, max_len: Optional[int] = None):
    if iterable:
      if max_len is not None and max_len < len(iterable):
        raise ValueError("Given iterable exceeds given maximal length")
      if len(iterable) < self.DEFAULT_CAPACITY:
        diff = self.DEFAULT_CAPACITY - len(iterable)
        self._data = list(iterable) + [None] * diff
      else:
        self._data = list(iterable)
      self._size = len(iterable)
      self.max_len = max_len
      self._front = 0
    else:
      self._data = [None] * self.DEFAULT_CAPACITY
      self._front = 0
      self._size = 0
      self.max_len = max_len

  def add_first(self, elem: Any) -> None:
    """
    Add an item to the front of the deque. If maxlen is specified and the deque 
    is full, the last item of the deque is removed, so as not to exceed maxlen.
    """
    full = self._size == len(self._data)
    if full and self.max_len is None:
      self._resize(2* len(self._data))
    index = (self._front - 1) % len(self._data)
    self._data[index] = elem
    self._front = index
    if full and self.max_len is not None:
      return
    self._size += 1


  def add_last(self, elem: Any) -> None:
    """
    Add an item to the end of the deque. If maxlen is specified and the deque is full,
    the first item of the deque is removed, so as to not exceed maxlen.
    """
    full = self._size == len(self._data)
    if full and self.max_len is None:
      self._resize(2 * len(self._data))
    index = (self._front + self._size) % len(self._data)
    self._data[index] = elem
    if full and self.max_len is not None:
      self._front = (self._front + 1) % len(self._data)
      return
    self._size += 1

  def delete_first(self) -> Any:
    """
    Remove an item from the front of the deque.
    """
    if self._size == 0:
      raise Empty("The deque is empty, cannot remove element")
    if self._size - 1 < len(self._data) / 4:
      self._resize(len(self._data) // 2)
    elem = self._data[self._front]
    self._data[self._front] = None
    self._front = (self._front + 1) % len(self._data)
    self._size -= 1
    return elem
    

  def delete_last(self) -> Any:
    """
    Remove an item from the end of the deque.
    """
    if self._size == 0:
      raise Empty("The deque is empty, cannot remove element")
    if self._size - 1 < len(self._data) / 4:
      self._resize(len(self._data) // 2)
    index = (self._front + self._size - 1) % len(self._data)
    elem = self._data[index]
    self._data[index] = None
    self._size -= 1
    return elem

  def first(self) -> Any:
    if self._size == 0:
      raise Empty("The deque is empty")
    return self._data[self._front]

  def last(self) -> Any:
    if self._size == 0:
      raise Empty("The deque is empty")
    index = (self._front + self._size - 1) % len(self._data)
    return self._data[index]

  def clear(self) -> None:
    """
    Remove all elements from the deque.
    """
    self._data = [None] * self.DEFAULT_CAPACITY
    self._front = 0
    self._size = 0

  def rotate(self, k: int) -> None:
    """
    Rotate the deque k steps to the right. If k is negative, rotate to the left.
    Realigns the list such that the first item (after rotating) is at index 0
    of the underlying list. 
    """
    shift = k % self._size
    rotated_list = [None] * len(self._data)
    for i in range(self._size):
      current_pos = (self._front + i) % len(self._data)
      # position if we were to realign the list (such that first item is at index 0 etc)
      realigned_pos = (current_pos + len(self._data) - self._front) % len(self._data)
      rotated_pos = (realigned_pos + shift) % self._size
      rotated_list[rotated_pos] = self._data[current_pos]
    self._data = rotated_list
    self._front = 0


  def remove(self, elem: Any) -> None:
    """Remove first matching element in the deque."""
    target_index = None
    position = None
    for i in range(self._size):
      index = (self._front + i) % len(self._data)
      if self._data[index] == elem:
        target_index = index
        position = i
        break
    if target_index is not None:
      for i in range(position, self._size - 1):
        index = (self._front + i) % len(self._data)
        next_index = (self._front + i + 1) % len(self._data)
        self._data[index] = self._data[next_index]
      self._size -= 1
      if target_index == self._front:
        self._front = (self._front + 1) % len(self._data)

  def count(self, elem: Any) -> int:
    count = 0
    for i in range(len(self._data)):
      if self._data[i] == elem:
        count += 1

    return count

  def _resize(self, new_capacity: int) -> None:
    new_data = [None] * new_capacity
    for i in range(self._size):
      new_data[i] = self._data[(self._front + i) % len(self._data)]
    self._data = new_data
    self._front = 0

  def __len__(self) -> int:
    return self._size

  def __getitem__(self, index: int) -> int:
    if not isinstance(index, int):
      raise ValueError("Index must be integer")
    if index < -self._size or index >= self._size:
      raise IndexError("Index is out of range")
    if index >= 0:
      return self._data[(index + self._front) % len(self._data)]
    else:
      return self._data[(self._front + self._size - index) % len(self._data)]
    

  def __setitem__(self, index: int, elem: Any) -> None:
    if not isinstance(index, int):
      raise ValueError("Index must be integer")
    if index < -self._size or index >= self._size:
      raise IndexError("Index is out of range")
    if index >= 0:
      self._data[(index + self._front) % len(self._data)] = elem
    else:
      self._data[(self._front + self._size - index) % len(self._data)] = elem


def builtin_deque_experiment():
  from collections import deque
  d = deque(["A", "B", "C", "D", "E"])
  print(d)
  d.append(5)
  print(d)
  d.rotate(1)
  print(d)


def deque_test():
  letter_list = [chr(i) for i in range(65, 71)]
  d = ArrayDequeRich(iterable=letter_list)
  print(d._data)
  assert d.delete_first() == "A"
  print(d._data)
  d.rotate(1)
  print(d._data)
  d.rotate(2)
  print(d._data)
  for i in range(6):
    d.add_last(i)
  print(d._data)
  for i in range(6):
    print(d.delete_first())
  d.delete_last()
  print(d._data)
  print(d._front)
  


if __name__ == "__main__":
  deque_test()