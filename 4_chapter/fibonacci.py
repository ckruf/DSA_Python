fibonacci_calls: dict[int, int] = dict()

def bad_fibonacci(n: int) -> int:
  # print(f"bad_fibonacci({n})")
  fibonacci_calls[n] = fibonacci_calls.get(n, 0) + 1
  if n == 0:
    return 0
  elif n == 1:
    return 1
  else:
    return bad_fibonacci(n - 1) + bad_fibonacci(n - 2)


def fibonacci_sum(n: int) -> int:
  return bad_fibonacci(n + 2) - 1


def fibonacci_total_calls(n: int) -> int:
  return fibonacci_sum(n) + bad_fibonacci(n - 1)


def good_fibonacci(n: int) -> tuple[int, int]:
  if n == 1:
    return 1, 0
  else:
    n_minus_one, n_minus_two = good_fibonacci(n - 1)
    return n_minus_one + n_minus_two, n_minus_one



if __name__ == "__main__":
  n = 7
  print(bad_fibonacci(n))
  print(good_fibonacci(n))