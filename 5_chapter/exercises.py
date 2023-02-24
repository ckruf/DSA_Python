from __future__ import annotations
import ctypes
import sys
from time import perf_counter_ns
from typing import NamedTuple
from dataclasses import dataclass


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

  def _make_array(self, c):                        # nonpublic utitity
     """Return new array with capacity c."""   
     return (c * ctypes.py_object)()               # see ctypes documentation

  def insert(self, k, value):
    """Insert value at index k, shifting subsequent values rightward."""
    # (for simplicity, we assume 0 <= k <= n in this verion)
    if self._n == self._capacity:                  # not enough room
      #self._resize(2 * self._capacity)             # so double capacity
      self.insert_when_full(k, value)
      return
    for j in range(self._n, k, -1):                # shift rightmost first
      self._A[j] = self._A[j-1]
    self._A[k] = value                             # store newest element
    self._n += 1


  # 5.6
  def insert_when_full(self, k: int, value):
    """
    Improved insertion of value at index k. When we reach capacity, instead of copying and then shifting,
    we straight away copy the items into their correct new positions. 
    """
    print("inserting into full")
    B = self._make_array(2 * self._capacity)
    for i in range(k):
      B[i] = self._A[i]
    B[k] = value
    for i in range(k, self._n):
      B[i + 1] = self._A[i]
    self._A = B
    self._capacity *= 2
    self._n += 1



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


#5.7
def missing(A: list) -> int:
  found = [False] * len(A)

  for val in A:
    if found[val]:
      return val
    else:
      found[val] = True

# 5.8
def list_pop_experiments(repetitions: int = 10) -> None:

  @dataclass
  class ExperimentResult:
    time_taken_pop_start: float = 0
    time_taken_pop_mid: float = 0
    time_taken_pop_end: float = 0

    def __add__(self, another_result: ExperimentResult) -> ExperimentResult:
      return ExperimentResult(
        self.time_taken_pop_start + another_result.time_taken_pop_start,
        self.time_taken_pop_mid + another_result.time_taken_pop_mid,
        self.time_taken_pop_end + another_result.time_taken_pop_end
      )

    def __truediv__(self, other: int):
      return ExperimentResult(
        self.time_taken_pop_start / other,
        self.time_taken_pop_mid / other,
        self.time_taken_pop_end / other
      )
  

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
  for i in range(30):
    find_list_resize_boundaries_grow_initial_size(i, 50 - i)