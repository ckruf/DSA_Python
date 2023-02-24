from __future__ import annotations
import ctypes
import sys
from time import perf_counter_ns
import random
from typing import Sequence, Optional, Iterable, List, Tuple, Any, Protocol, TypeVar, Callable
from dataclasses import dataclass
import math
from abc import abstractmethod


# 5.2
def find_list_resize_boundaries_grow(n: int) -> None:
  data = []
  prev_size = sys.getsizeof(data)
  for _ in range(n):
    length = len(data)
    current_size = sys.getsizeof(data)
    if current_size != prev_size:
      print(f"List changed size at length {length - 1}")
      prev_size = current_size
    data.append(None)


# 5.3
def dynamic_array_resizing_experiment_shrink(n: int = 60, measure_pops: bool = False) -> None:
  data = [None, ] * n

  for _ in range(n):
    length = len(data)
    size = sys.getsizeof(data)
    print(f"Length: {length}, size in bytes: {size}")
    start_time = perf_counter_ns()
    data.pop()
    end_time = perf_counter_ns()
    elapsed_microseconds = (end_time - start_time) / 1_000
    if measure_pops:
      print(f"Pop operation took {elapsed_microseconds} microseconds")


class DynamicArray:
  """A dynamic array class akin to a simplified Python list."""

  def __init__(self):
    """Create an empty array."""
    self._n = 0                                    # count actual elements
    self._capacity = 1                             # default array capacity
    self._A = self._make_array(self._capacity)     # low-level array
    
  @classmethod
  def from_iterable(cls, seq: Iterable):
    """
    Constructor to create instance from iterable sequence.
    """
    dyn_arr = cls()

    # create low-level array of sufficient length in advance,
    # so we don't have to resize like we potentially would with repeated append()
    length = len(seq)
    ceilinged_power = math.ceil(math.log(length, 2))
    capacity = int(math.pow(2, ceilinged_power))
    B = cls._make_array(capacity)

    for i, val in enumerate(seq):
      B[i] = val
    dyn_arr._A = B
    dyn_arr._capacity = capacity
    dyn_arr._n = length

    return dyn_arr
  
  def __len__(self):
    """Return number of elements stored in the array."""
    return self._n
    
  def __getitem__(self, k):
    """Return element at index k."""
    # handle negative indices
    if k < 0:
      k = k + self._n
    if not 0 <= k < self._n:
      raise IndexError('invalid index')
    return self._A[k]                              # retrieve from array

  def __iter__(self):
    self.__index = 0
    return self
  
  def __next__(self):
    if self.__index >= self._n:
      raise StopIteration
    current_item = self._A[self.__index]
    self.__index += 1
    return current_item
  
  def append(self, obj):
    """Add object to end of the array."""
    if self._n == self._capacity:                  # not enough room
      self._resize(2 * self._capacity)             # so double capacity
    self._A[self._n] = obj
    self._n += 1

  def _resize(self, c):                            # nonpublic utitity
    """Resize internal array to capacity c."""
    B = self._make_array(c)                        # new (bigger) array
    for k in range(self._n):                       # for each existing value
      B[k] = self._A[k]
    self._A = B                                    # use the bigger array
    self._capacity = c

  @staticmethod
  def _make_array(c):                        # nonpublic utitity
     """Return new array with capacity c."""   
     return (c * ctypes.py_object)()               # see ctypes documentation

  def insert(self, k, value):
    """Insert value at index k, shifting subsequent values rightward."""
    # (for simplicity, we assume 0 <= k <= n in this verion)
    if self._n == self._capacity:                  # not enough room
      self._insert_when_full(k, value)
      return
    for j in range(self._n, k, -1):                # shift rightmost first
      self._A[j] = self._A[j-1]
    self._A[k] = value                             # store newest element
    self._n += 1

  # 5.6
  def _insert_when_full(self, k: int, value):
    """
    Improved insertion of value at index k. When we reach capacity, instead of copying and then shifting,
    we straight away copy the items into their correct new positions. 
    """
    print(f"inserting when full, self._n = {self._n}, current capacity = {self._capacity}, new capacity = {self._capacity * 2}")
    B = self._make_array(2 * self._capacity)
    for i in range(k):
      B[i] = self._A[i]
    B[k] = value
    for i in range(k, self._n):
      B[i + 1] = self._A[i]
    self._A = B
    self._capacity *= 2
    self._n += 1

  # 5.16
  def pop(self, k: Optional[int] = None):
    """
    Remove value at index k, and shrink array if it reaches quarter of capacity.
    If k is not given, removes last element in array by default.
    """
    if k is None:
      k = self._n - 1
    if (self._n - 1) == self._capacity // 4:
      print(f"self._n = {self._n}, self._capacity = {self._capacity}")
      self._pop_and_shrink(k)
      return
  
    self._A[k] = None
    for i in range(k, self._n - 1):
      self._A[i] = self._A[i + 1]
    self._n -= 1

  def _pop_and_shrink(self, k: int):
    """Remove item at index k and shrink array at once, so we avoid copying AND shifting"""
    print("poppin' and shrinkin'")
    B = self._make_array(self._capacity // 2)
    for i in range(k):
      B[i] = self._A[i]
    for i in range(k, self._n - 1):
      B[i] = self._A[i + 1]
    self._A = B
    self._n -= 1
    self._capacity = self._capacity // 2

  def remove(self, value):
    """Remove first occurrence of value (or raise ValueError)."""
    # note: we do not consider shrinking the dynamic array in this version
    for k in range(self._n):
      if self._A[k] == value:              # found a match!
        for j in range(k, self._n - 1):    # shift others to fill gap
          self._A[j] = self._A[j+1]
        self._A[self._n - 1] = None        # help garbage collection
        self._n -= 1                       # we have one less item
        return                             # exit immediately
    raise ValueError('value not found')    # only reached if no match

  def remove_all(self, value):
    """
    Remove all occurences of value (or raise ValueError).
    
    The idea is to do one full iteration of the array, to record all the indices at which the value occurs,
    so for example for array ["b", "a", "c", "g", "a", "x", "y", "h"] if we were removing "a", we would
    record 1 and 4, "a" occurs at those indices.

    Then we would like to do loops for the values between consecutive occurences of "a". So we would like
    to iterate over indices 2 and 3 (since those are between 1 and 4) and then shift those by one to the left.
    Then we would iterate over indices 5 to 7 and then shift those by two to the left.
    """
    occurence_indices = []
    for k in range(self._n):
      if self._A[k] == value:
        occurence_indices.append(k)

    if not occurence_indices:
      raise ValueError("Value not found")

    occurence_count = len(occurence_indices)

    if self._n - occurence_count < self._capacity // 4:
      self._remove_all_and_shrink(occurence_indices)
      return

    for i in range(occurence_count - 1):
      shift = i + 1
      for j in range(occurence_indices[i] + 1, occurence_indices[i + 1]):
        self._A[j - shift] = self._A[j]

    if occurence_indices[-1] != self._n - 1:
      shift += 1
      for i in range(occurence_indices[-1] + 1, self._n):
        self._A[i - shift] = self._A[i]
    
    for i in range(self._n - occurence_count, self._n):
      self._A[i] = None

    self._n -= occurence_count

  def alt_remove_all(self, val):
    i = 0
    occurences = 0
    while i < self._n:
      if self._A[i] == val:
        occurences += 1
        i += 1
        continue

      self._A[i - occurences] = self._A[i]
      i += 1

    # take out the garbage
    for i in range(self._n - occurences, self._n):
      self._A[i] = None

    self._n -= occurences

  def _remove_all_and_shrink(self, occurence_indices: list):
    B = self._make_array(self._capacity // 2)
    occurence_count = len(occurence_indices)

    for i in range(occurence_count - 1):
      shift = i + 1
      for j in range(occurence_indices[i] + 1, occurence_indices[i + 1]):
        B[j - shift] = self._A[j]

    if occurence_indices[-1] != self._n - 1:
      shift += 1
      for i in range(occurence_indices[-1] + 1, self._n):
        B[i - shift] = self._A[i]
    else:
      B[self._n - 1] = None

    self._A = B
    self._n -= occurence_count
    self._capacity = self._capacity // 2

  def __str__(self):
    return "[" + ", ".join(str(self._A[i]) for i in range(self._n)) + "]"


#5.7
def missing(A: list) -> int:
  found = [False] * len(A)

  for val in A:
    if found[val]:
      return val
    else:
      found[val] = True

@dataclass
class ExperimentResult:
  time_taken_start: float = 0
  time_taken_mid: float = 0
  time_taken_end: float = 0

  def __add__(self, another_result: ExperimentResult) -> ExperimentResult:
    return ExperimentResult(
      self.time_taken_start + another_result.time_taken_start,
      self.time_taken_mid + another_result.time_taken_mid,
      self.time_taken_end + another_result.time_taken_end
    )

  def __truediv__(self, other: int):
    return ExperimentResult(
      self.time_taken_start / other,
      self.time_taken_mid / other,
      self.time_taken_end / other
    )

# 5.8
def list_pop_experiments(repetitions: int = 10) -> None:
  def single_experiment(list_size: int) -> ExperimentResult:
    my_lst = [None] * list_size

    start = perf_counter_ns()
    my_lst.pop()
    end = perf_counter_ns()
    time_taken_pop_end = end - start

    my_lst.append(None)
    mid = list_size // 2

    
    start = perf_counter_ns()
    my_lst.pop(mid)
    end = perf_counter_ns()
    time_taken_pop_mid = end - start 

    my_lst.append(None)

    start = perf_counter_ns()
    my_lst.pop(0)
    end = perf_counter_ns()
    time_taken_pop_start = end - start

    return ExperimentResult(time_taken_pop_start, time_taken_pop_mid, time_taken_pop_end)

  
  list_sizes = (
    100,
    1_000,
    10_000,
    100_000,
    1_000_000,
    10_000_000
  )
  results = dict.fromkeys(list_sizes)

  for size in list_sizes:
    total_result = ExperimentResult()
    for _ in range(repetitions):
      single_result = single_experiment(size)
      total_result += single_result
    average_result = total_result / repetitions
    results[size] = average_result

  print("results:")
  print(results)
  for key, value in results.items():
    print(f"List of size {key}")
    print(value) 

# 5.14
def shuffle_sequence(seq: Sequence) -> None:
  """Shuffle sequence in place, using random module for RNG"""
  seq_len = len(seq)
  for index in range(seq_len):
    random_index = random.randrange(seq_len)
    seq[index], seq[random_index] = seq[random_index], seq[index]


def test_array_meths():
  """Function which tests that implementations of pop and insert are correct."""
  my_lst = DynamicArray()
  length = 30
  for i in range(length):
    my_lst.insert(i, i)
  print(", ".join(str(my_lst[i]) for i in range(length)))
  inserts = 10
  for _ in range(inserts):
    my_lst.insert(10, "a")
  print(", ".join(str(my_lst[i]) for i in range(length)))
  pops = round(length * 0.9)
  print(f"pops = {pops}") 
  for _ in range(pops):
    my_lst.pop(3)
  length -= pops
  print(", ".join(str(my_lst[i]) for i in range(length)))


# 5.21 
def string_composition_experiment(repetitions: int = 10):
  """
  Run an experiment comparing the time it takes to compose a string using the following methods:
  - repeated concatenation (+=)
  - appending to temporary list and then joining
  - list comprehension syntax and then joining
  - generator syntax w/o list and then joining
  """
  str_length = 1_000_000

  total_repeated_concat_time = 0
  total_repeated_append_time = 0
  total_list_comprehension_time = 0
  total_generator_syntax_time = 0

  for _ in range(repetitions):
    alphabet_string = ""
    start = perf_counter_ns()
    for i in range(str_length):
      alphabet_string += chr((i % 26) + 65)
    stop = perf_counter_ns()
    repeated_concat_time = stop - start
    total_repeated_concat_time += repeated_concat_time
    # print(f"Repeated concatenation took {repeated_concat_time}")

    alphabet_list = []
    start = perf_counter_ns()
    for i in range(str_length):
      alphabet_list.append(chr((i % 26) + 65))
    alphabet_string_2 = "".join(alphabet_list)
    stop = perf_counter_ns()
    repeated_append_time = stop - start
    total_repeated_append_time += repeated_append_time
    # print(f"Repeated appending to list took {repeated_append_time}")

    start = perf_counter_ns()
    alphabet_string_3 = "".join([chr((i % 26) + 65) for i in range(str_length)])
    stop = perf_counter_ns()
    list_comprehension_time = stop - start
    total_list_comprehension_time += list_comprehension_time
    # print(f"List comprehension syntax took {list_comprehension_time}")

    start = perf_counter_ns()
    alphabet_string_4 = "".join(chr((i % 26) + 65) for i in range(str_length))
    stop = perf_counter_ns()
    generator_syntax_time = stop - start
    total_generator_syntax_time += generator_syntax_time
    # print(f"Generator syntax took {generator_syntax_time}")

  print(f"Repeated concatenation on average took {total_repeated_concat_time / repetitions:,}")
  print(f"Repeated appends on average took {total_repeated_append_time / repetitions:,}")
  print(f"List comprehension on average took {total_list_comprehension_time / repetitions:,}")
  print(f"Generator syntax on average took {total_generator_syntax_time / repetitions:,}")


# 5.22
def append_vs_extend_experiment(repetitions: int = 30):
  """
  Compare the speed of the built in extend method vs repeated appends.
  """


  first_list_size = 10_000
  second_list_size = 100_000

  total_extend_time = 0
  total_append_time = 0

  for _ in range(repetitions):
    first_list = [i for i in range(first_list_size)]
    second_list = [i for i in range(second_list_size)]

    start = perf_counter_ns()
    first_list.extend(second_list)
    stop = perf_counter_ns()
    extend_time = stop - start
    total_extend_time += extend_time

    first_list = [i for i in range(first_list_size)]
    start = perf_counter_ns()
    for val in second_list:
      first_list.append(val)
    stop = perf_counter_ns()
    append_time = stop - start
    total_append_time += append_time

  print(f"extend took on average {total_extend_time / repetitions:,}")
  print(f"append took on average {total_append_time / repetitions:,}")


# 5.23 
def list_comprehension_vs_append_experiment(repetitions: int = 50):
  """
  Experiment to compare time taken to construct list using list comprehension syntax,
  compared to repeated calls to .append()
  """
  total_append_time = 0
  total_comprehension_time = 0
  list_size = 100_000

  for _ in range(repetitions):
    squares_append = []
    start = perf_counter_ns()
    for i in range(list_size):
      squares_append.append(i*i)
    stop = perf_counter_ns()
    append_time = stop - start
    total_append_time += append_time

    start = perf_counter_ns()
    squares_comprehension = [i*i for i in range(list_size)]
    stop = perf_counter_ns()
    comprehension_time = stop - start
    total_comprehension_time += comprehension_time

  print(f"append took on average {total_append_time / repetitions:,}")
  print(f"comprehension took on average {total_comprehension_time / repetitions:,}")


# 5.24
def remove_experiment(repetitions: int = 20):
  """
  Experiment to compare performance of .remove() method when the value to be removed is at the
  beginning of the list, middle of the list, or end of the list
  """
  def single_experiment(list_size: int) -> ExperimentResult:
    numbers = [i for i in range(list_size)]

    start = perf_counter_ns()
    numbers.remove(0)
    stop = perf_counter_ns()
    time_remove_start = stop - start

    start = perf_counter_ns()
    numbers.remove(list_size // 2)
    stop = perf_counter_ns()
    time_remove_middle = stop - start

    start = perf_counter_ns()
    numbers.remove(list_size - 1)
    stop = perf_counter_ns()
    time_remove_end = stop - start

    return ExperimentResult(
      time_taken_start=time_remove_start,
      time_taken_mid=time_remove_middle,
      time_taken_end=time_remove_end
    )

  list_sizes = (
    100,
    1_000,
    10_000,
    100_000,
  )
  results = dict.fromkeys(list_sizes)

  for size in list_sizes:
    total_result = ExperimentResult()
    for _ in range(repetitions):
      single_result = single_experiment(size)
      total_result += single_result
    average_result = total_result / repetitions
    results[size] = average_result

  print("results:")
  for key, value in results.items():
    print(f"List of size {key}")
    print(value) 

def test_remove_all():
  my_lst = DynamicArray()
  counts = dict()
  for i in range(33):
    val = i % 3
    counts[val] = counts.get(val, 0) + 1
    my_lst.append(i % 3)
  print(my_lst)
  print(f"capacity: {my_lst._capacity}")
  print(f"length: {len(my_lst)}")
  print(f"counts: ")
  print(counts)
  print("=" * 50)
  my_lst.remove_all(1)
  counts = dict()
  for val in my_lst:
    counts[val] = counts.get(val, 0) + 1
  print(my_lst)
  print(f"capacity: {my_lst._capacity}")
  print(f"length: {len(my_lst)}")
  print(f"counts: ")
  print(counts)

def second_test_remove_all():
  original_lst = [1, 2, 3, 2, 5, 7, 9, 10, 2, 3, 4, 2, 8, 9, ]
  filtered_lst = [1, 3, 5, 7, 9, 10, 3, 4, 8, 9]
  my_lst = DynamicArray.from_iterable(original_lst)
  print(my_lst)
  my_lst.remove_all(2)
  print(my_lst)
  print("=" * 50)
  original_lst = [1, 2, 3, 2, 5, 7, 9, 10, 2, 3, 4, 2, 8, 9, 2]
  filtered_lst = [1, 3, 5, 7, 9, 10, 3, 4, 8, 9]
  my_lst = DynamicArray.from_iterable(original_lst)
  print(my_lst)
  my_lst.alt_remove_all(2)
  print(my_lst)
  i = 0
  while True:
    try:
      print(my_lst._A[i])
      i += 1
    except ValueError:
      break 


# 5.26
def find_repeated(seq: Sequence[int]):
  """
  Given an array of integers of length n, with values from 1 to n - 5, where exactly
  5 values are repeated, find the repeated values.
  """
  matches = [False] * len(seq)
  repeated = []
  for val in seq:
    if matches[val] is False:
      matches[val] = True
    else:
      repeated.append(val)
  return repeated


# 5.26
def alt_find_repeated(seq: Sequence[int]):
  """
  Given an array of integers of length n, with values from 1 to n - 5, where exactly
  5 values are repeated, find the repeated values - using sorting.
  """
  seq = sorted(seq)
  repeated = []
  for i in range(len(seq) - 1):
    if seq[i] == seq[i + 1]:
      repeated.append(seq[i])

  return repeated

def test_find_repeated():
  length = 50
  test_arr = [i for i in range(length - 5)]
  repeated = set()
  
  while len(repeated) < 5:
    repeated.add(random.randrange(length - 5))
  random_indices = set()
  
  while len(random_indices) < 5:
    random_indices.add(random.randrange(length - 5))

  print(f"repeated: {repeated}")
  print(f"random indices: {random_indices}")

  for repeated_val, random_index in zip(repeated, random_indices):
    print(f"inserting {repeated_val} at {random_index}")
    test_arr.insert(random_index, repeated_val)

  repeated_result = find_repeated(test_arr)
  print(f"repeated found by my function: {repeated_result}")

  alt_repeated_result = alt_find_repeated(test_arr)
  print(f"repeated found by alternative function: {alt_repeated_result}")


# 5.27
def find_not_present(seq: Sequence[int]) -> int:
  """
  Given a list of n positive integers, each represented with k = ceil(log(n)) + 1 bits, find
  a k-bit integer that's not in the list.
  """
  length = len(seq)
  max_power = math.ceil(math.log(length, 2)) + 1
  max_value = math.pow(2, max_power)
  present = [False] * max_value
  for val in seq:
    present[val] = True
  for index, value in enumerate(present):
    if value is False:
      return index


class Equalable(Protocol):
  """Protocol for annotating types which define equality"""

  @abstractmethod
  def __eq__(self: ET, other: ET) -> bool:
    pass


ET = TypeVar("ET", bound=Equalable)


# 5.29
def natural_join(A: List[Tuple[Any, ET]], B: List[Tuple[ET, Any]]):
  """
  Given lists A and B, containing tuples (x, y) and (y, z), produce the natural join
  of the two lists - a list of tuples(x, y, z), joined on y as a key.
  """
  locations_A = dict()
  for index, pair in enumerate(A):
    _, key = pair
    indices_list = locations_A.get(key)
    if indices_list is None:
      locations_A[key] = [index, ]
    else:
      indices_list.append(index)

  locations_B = dict()
  for index, pair in enumerate(B):
    key, _ = pair
    indices_list = locations_B.get(key)
    if indices_list is None:
      locations_B[key] = [index, ]
    else:
      indices_list.append(index)

  results = []
  for key, indices_list_A in locations_A.items():
    if indices_list_B := locations_B.get(key):
      for index_A in indices_list_A:
        for index_B in indices_list_B:
          pair_A = A[index_A]
          pair_B = B[index_B]
          result = pair_A[0], pair_A[1], pair_B[1]
          results.append(result)

  return results


# 5.29 sorting optimization
def sort_then_natural_join(A: List[Tuple[Any, ET]], B: List[Tuple[ET, Any]]):
  A.sort(key=lambda x: x[1])
  B.sort(key=lambda x: x[0])

  i = 0
  j = 0
  results = []

  while i < len(A) and j < len(B):
    if A[i][1] == B[j][0]:
      results.append(A[i][0], A[i][1], B[j][1])
      j += 1
    elif A[i][1] < B[j][0]:
      i += 1
    else:
      j += 1

  return results


def test_natural_join():
  A = [
    ("a", 1),
    ("b", 1),
    ("c", 1),
    ("g", 3),
    ("h", 4),
    ("q", 7),
    ("w", 7),
    ("i", 11),
    ("k", 12),
    ("r", 15),
    ("t", 42),
    ("y", 60),
    ("j", 61)
  ]
  random.shuffle(A)

  B = [
    (1, "chris"),
    (1, "benjamin"),
    (3, "george"),
    (11, "douglas"),
    (42, "robert"),
    (42, "joanne"),
    (42, "martin"),
    (43, "barbara"),
    (120, "charles")
  ]
  random.shuffle(B)

  correct_join = [
    ("a", 1, "chris"),
    ("a", 1, "benjamin"),
    ("b", 1, "chris"),
    ("b", 1, "benjamin"),
    ("c", 1, "chris"),
    ("c", 1, "benjamin"),
    ("g", 3, "george"),
    ("i", 11, "douglas"),
    ("t", 42, "robert"),
    ("t", 42, "joanne"),
    ("t", 42, "martin")
  ]

  result = natural_join(A, B)

  assert len(correct_join) == len(result)
  for triple in correct_join:
    assert triple in result


def recursive_sum(A: list[int | float]) -> int:
  if len(A) == 1:
    return A[0]
  else:
    return A[0] + recursive_sum(A[1:])


def test_recursive_sum(recursive_fn: Callable[[Sequence[int]], int], initial_input_size: int = 10_000, repetitions: int = 10):
  def single_rep(input_size: int) -> int:
    test_seq = [i for i in range(input_size)]
    start = perf_counter_ns()
    result = recursive_fn(test_seq)
    stop = perf_counter_ns()
    time_elapsed_initial = stop - start
    total_time_initial += time_elapsed_initial
    assert result == sum(test_seq)


  
  total_time_initial = 0
  total_time_double = 0
  total_time_quadruple = 0
  
  for _ in range(repetitions):
    test_seq = [i for i in range(initial_input_size)]
    start = perf_counter_ns()
    result = recursive_fn(test_seq)
    stop = perf_counter_ns()
    time_elapsed_initial = stop - start
    total_time_initial += time_elapsed_initial
    assert result == sum(test_seq)

    test_seq = [i for i in range(2 * initial_input_size)]
    start = perf_counter_ns()
    result = recursive_fn(test_seq)
    stop = perf_counter_ns()
    time_elapsed_double = stop - start
    total_time_double += time_elapsed_double
    assert result == sum(test_seq)



# 5.10
def init(self, shift):
    """Construct Caesar cipher using given integer shift for rotation."""
    self._forward = ''.join(chr((k + shift) % 26 + ord('A')) for k in range(26))                # will store as string
    self._backward = ''.join(chr((k - shift) % 26 + ord('A')) for k in range(26))  


# 5.11
def add_two_dimensional(two_dimensional: list[list[float]]) -> float:
  total = 0
  for seq in two_dimensional:
    for elem in seq:
      total += elem
  
  return total

# 5.12
def sum_add_two_dimensional(two_dimensional: list[list[float]]) -> float:
  return sum(sum(seq) for seq in two_dimensional)

# 5.13
def find_list_resize_boundaries_grow_initial_size(initial_size: int, additions: int) -> None:
  data = [None] * initial_size
  print(f"initial length of list: {len(data)}")
  prev_size = sys.getsizeof(data)
  for _ in range(additions):
    length = len(data)
    current_size = sys.getsizeof(data)
    if current_size != prev_size:
      print(f"List changed size at length {length - 1}")
      prev_size = current_size
    data.append(None)

  
  print(f"final length of list: {len(data)}")
  print("========================")


if __name__ == "__main__":
  my_lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
  print(recursive_sum(my_lst))
