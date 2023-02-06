from typing import Sequence
import math


def max_recursive(numbers: Sequence[int | float]) -> int | float:
  """
  Exercise R-4.1
  Find the maximum value in a sequence of numbers using recursion.
  """
  if len(numbers) == 0:
    raise ValueError("cannot find maximum value in empty sequence")
  elif len(numbers) == 1:
    return numbers[0]
  else:
    max_in_rest = max_recursive(numbers[1:])
    if numbers[0] > max_in_rest:
      return numbers[0]
    else:
      return max_in_rest


def nth_harmonic_number(n: int) -> int | float:
  """
  Exercise R-4.6

  Find the nth harmonic number using recursion
  """
  if n == 1:
    return 1
  else:
    return (1 / n) + nth_harmonic_number(n - 1)


def str_to_int_recursive(numeric_string: str) -> int:
  """
  Exercise R-4.7

  Convert a string representing an integer into an integer using recursion
  """
  if len(numeric_string) == 0:
    return 0
  else:
    return (int(numeric_string[0]) * (10 ** (len(numeric_string) - 1))) + str_to_int_recursive(numeric_string[1:])


def min_max_recursive(numbers: Sequence[int | float]) -> tuple[int | float, int | float]:
  if len(numbers) == 0:
    raise ValueError("cannot find minimum and maximum values in empty sequence")
  elif len(numbers) == 1:
    return numbers[0], numbers[0]
  else:
    min_in_rest, max_in_rest = min_max_recursive(numbers[1:])
    true_min = min_in_rest
    true_max = max_in_rest
    if numbers[0] > max_in_rest:
      true_max = numbers[0]
    if numbers[0] < min_in_rest:
      true_min = numbers[0]
    return true_min, true_max


def log_2_n(n: int) -> int:
  if n == 1:
    return 0
  else:
    return 1 + log_2_n(n // 2)

def is_unique(seq: Sequence) -> bool:
  if len(seq) == 1:
    return True
  elif seq[0] in seq[1:]:
    return False
  else:
    return is_unique(seq[1:])

def multiply(x: int, y: int) -> int:
  if x == 1:
    return y
  else:
    return y + multiply(x - 1, y)


def towers_of_hanoi(n: int, from_rod: str, to_rod: str, aux_rod: str) -> None:
  """
  Solve the towers of hanoi puzzle, moving n disks from the from_rod to the to_rod.

  :param n: number of disks
  :param from_rod: label/name of rod from which we want to move disks
  :param to_rod: label/name of rod to which we want to move disks
  :param aux_rod: label/name of auxiliary rod
  """
  if n == 1:
    print(f"Move disk from rod {from_rod} to rod {to_rod}")
  else:
    towers_of_hanoi(n - 1, from_rod=from_rod, to_rod=aux_rod, aux_rod=to_rod)
    towers_of_hanoi(1, from_rod=from_rod, to_rod=to_rod, aux_rod=aux_rod)
    towers_of_hanoi(n - 1, from_rod=aux_rod, to_rod=to_rod, aux_rod=from_rod)


def subsets(elements: list):
  def backtrack(first: int, sub_set: list, full_set: list, perm_len: int):
    if len(sub_set) == perm_len:
      output.append(sub_set.copy())
      return
    for i in range(first, len(full_set)):
      sub_set.append(full_set[i])
      backtrack(i + 1, sub_set, full_set, perm_len)
      sub_set.pop()

  output = []
  for k in range(len(elements) + 1):
    backtrack(0, [], elements, k)
  return output


def reverse_string(s: str) -> str:
  def recursive_reversion(letter_list: list[str], start: int, stop: int) -> None:
    if stop - start > 0:
      letter_list[start], letter_list[stop] = letter_list[stop], letter_list[start]
      recursive_reversion(letter_list, start + 1, stop - 1)

  letter_list = list(s)
  recursive_reversion(letter_list, 0, len(s) - 1)
  return "".join(letter_list)


def is_palindrome(s: str) -> bool:
  def recursive_palindromic_determination(letter_list: list[str], start: int, stop: int) -> bool:
    if stop - start > 0:
      return (letter_list[start] == letter_list[stop]) and recursive_palindromic_determination(letter_list, start + 1, stop - 1)
    else:
      return True
  
  letter_list = list(s)
  return recursive_palindromic_determination(letter_list, 0, len(s) - 1)


def has_more_vowels_than_consonants(word: str) -> bool:  
  def count_consonants(s: str) -> int:
    if len(s) == 0:
      return 0
    else:
      return int(is_vowel(s[0])) + count_consonants(s[1:])

  def is_vowel(letter: str) -> bool:
    return (letter.lower() in {"a", "e", "i", "o", "u"})

  return count_consonants(word) > (len(word) / 2)

def even_before_odd(nums: Sequence[int]) -> Sequence[int]:
  def _even_before_odd_recurse(numbers: Sequence[int], low: int, high: int) -> None:
    if low < high:
      if numbers[high] % 2 == 0:
        numbers[high], numbers[low] = numbers[low], numbers[high]
        _even_before_odd_recurse(numbers, low + 1, high)
      else:
        _even_before_odd_recurse(numbers, low, high - 1)

  _even_before_odd_recurse(nums, 0, len(nums) - 1)
  return nums


def pivot_rearrange(numbers: Sequence[int], k: int) -> Sequence[int]:
  """
  Given a sequence of integers, rearrange the sequence such that all numbers
  in the sequence which are less than or equal to k come before numbers which
  are greater than k.

  :param nums: sequence of numbers
  :param k: pivot value according to which to rearrange the sequence
  """
  def _pivot_rearrange_recurse(numbers: Sequence[int], k: int, low: int, high: int) -> None:
    if low >= high:
      return
    
    if numbers[high] <= k:
      numbers[high], numbers[low] = numbers[low], numbers[high]
      _pivot_rearrange_recurse(numbers, k, low + 1, high)
    else:
      _pivot_rearrange_recurse(numbers, k, low, high - 1)

  _pivot_rearrange_recurse(numbers, k, 0, len(numbers) - 1)
  return numbers


def sorted_two_sum(numbers: Sequence[int], k: int) -> tuple[int, int] | None:
  """
  Given a sequence of distinct integers, listed in increasing order, and a number k,
  find two integers in the sequence which sum to k, if such a pair exists.
  Iterates over the array and then uses binary search to look for the complement/difference.

  :param numbers: sequence of distinct integers in increasing order
  :param k: number to which the integers have to sum
  :return: tuple of the two integers, or None if no such integers exist
  """
  def bin_search(seq: Sequence[int], target: int) -> bool:
    def _recurse_bin_search(s: Sequence[int], n: int, low: int, high: int) -> bool:
      if low > high:
        return False
      mid = (low + high) // 2
      if s[mid] == n:
        return True
      elif s[mid] > n:
        return _recurse_bin_search(s, n, low, mid - 1)
      else:
        return _recurse_bin_search(s, n, mid + 1, high)

    return _recurse_bin_search(seq, target, 0, len(seq) - 1)

  middle = len(numbers) // 2

  for i in range(middle):
    difference = k - numbers[i]
    if bin_search(numbers, difference):
      return difference, numbers[i]

  return None


def find_pair(numbers: Sequence[int], n: int) -> bool:
  def _recurse_find_pair(nums: Sequence[int], k: int, low: int, high: int) -> None:
    if low == high:
      return False
    
    if nums[low] + nums[high] < k:
      return _recurse_find_pair(nums, k, low + 1, high)
    elif nums[low] + nums[high] > k:
      return _recurse_find_pair(nums, k, low, high - 1)
    else:  # nums[low] + nums[high] == k
      return True

  return _recurse_find_pair(numbers, n, 0, len(numbers) - 1) 


def power_iterative(x: int, n: int) -> int:
  """Compute x^n (x to the power of n) by repeated squaring"""
  result = 1
  while n > 0:
    if n % 2 == 1:
      result = result * x
    x = x * x
    n = n // 2

  return result






if __name__ == "__main__":
  test_sequence = [1, 3, 8, 2, 12, 18, 3, 4, 0, 9, 3]
  print(max_recursive(test_sequence))
  print(nth_harmonic_number(5))
  print(str_to_int_recursive("13531"))
  print(min_max_recursive(test_sequence))
  print(log_2_n(15))
  print("\nis_unique\n")
  print(is_unique([1, 2, 3, 4, 5, 6,]))
  print(is_unique([1, 2, 3, 4, 5, 6, 7, 8, 2]))
  print("\nmultiply\n")
  print(multiply(5, 3))
  print(multiply(5, 3))
  print(multiply(7, 1))
  print(multiply(1, 7))
  print(multiply(9, 9))
  # towers_of_hanoi(3, "'from'", "'to'", "'aux'")
  print("\nsubsets\n")
  print(subsets(["a", "b", "c", "d"]))
  print("\nreverse_string\n")
  print(reverse_string("pots&pans"))
  print(reverse_string("sn"))
  print("\nis_palindrome\n")
  print(is_palindrome("racecar")) # True
  print(is_palindrome("gohangasalamiimalasagnahog")) # True
  print(is_palindrome("coca-cola")) # False
  print("\nhas_more_vowels_than_consonants\n")
  print(has_more_vowels_than_consonants("alphabet")) # False
  print(has_more_vowels_than_consonants("cocacola")) # False
  print(has_more_vowels_than_consonants("s")) # False
  print(has_more_vowels_than_consonants("australia")) # True
  print(has_more_vowels_than_consonants("hoe")) # True
  print("\neven_before_odd \n")
  print(even_before_odd([1, 3, 4, 5, 8]))
  print("\nless_than_k_first \n")
  print(pivot_rearrange([2, 8, 9, 1, 3, 4, 5, 6, 0], 5))
  print("\nsorted_two_sum \n")
  print(sorted_two_sum([1, 3, 8, 12, 17, 20, 21, 24, 27, 28, 30], 44))
  print("\nfind_pair \n")
  print(find_pair([1, 3, 8, 12, 17, 20, 21, 24, 27, 28, 30], 44))
  print("\npower_iterative \n")
  print(power_iterative(2, 10))
  print(power_iterative(2, 11))
