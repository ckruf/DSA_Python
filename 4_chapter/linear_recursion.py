from typing import Sequence, Optional

"""
Examples of linear recursion - during each call the recursive function
calls itself once. However, this does not mean that the running time of 
the function is necessarily O(n). For example, if n is divided by two on
each call (like in binary search), the running time is not O(n).
It also does not necessarily mean that the function body only contains
one call to the recursive function. For example, if we have an if/else, 
there can be a recursive call in both, as long as the function can only
call itself once per call.
"""

def recursive_sequence_sum(seq: Sequence[int | float]):
  if len(seq) == 0:
    return 0
  else:
    return seq[0] + recursive_sequence_sum(seq[1:])

def reverse_sequence(seq: Sequence, start: int = 0, stop: Optional[int] = None) -> Sequence:
  if stop is None:
    stop = len(seq) - 1
  
  if stop - start > 1:
    seq[start], seq[stop] = seq[stop], seq[start]
    return reverse_sequence(seq, start + 1, stop - 1)
  else:
    return seq


def power(x: int, n: int) -> int:
  """
  Compute x ** n. Has O(n) running time, as there are n calls until we get from n to 0.
  """
  if n == 0:
    return 1
  else:
    return x * power(x, n - 1)


def power_improved(x: int, n: int) -> int:
  """
  Compute x ** n. Has O(log(n)) running time, as it divided n by 2 on each call.
  """
  if n == 0:
    return 1
  else:
    partial = power_improved(x, n // 2)
    result = partial * partial
    if n % 2 == 1:
      result = result * x
    return result







if __name__ == "__main__":
  print(recursive_sequence_sum([1, 2, 3, 4, 5]))
  print(reverse_sequence([1, 2, 3, 4, 5]))  
  print(power(2, 0))
  print(power(2, 1))
  print(power(2, 2))
  print(power(2, 3))
