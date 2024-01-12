from typing import Sequence, Optional

def binary_sum(numbers: Sequence[int | float], start: int = 0, stop: Optional[int] = None):
  if stop is None:
    stop = len(numbers) - 1

  if stop - start == 0:
    return numbers[stop]
  else:
    mid = (start + stop) // 2
    return binary_sum(numbers, start, mid) + binary_sum(numbers, mid + 1, stop)


if __name__ == "__main__":
  print(binary_sum([1, 2, 3, 4, 5, 6]))  # should print 21
  print(binary_sum([1, 2, 3, 4, 5]))  # should print 15
  print(binary_sum([1, 2, 3]))  # should print 6
  print(binary_sum([1, 2]))  # should print 3
  print(binary_sum([1,])) # should print 1