import sys
from time import perf_counter_ns


def dynamic_array_resizing_experiment_grow(n: int = 30, measure_appends: bool = False) -> None:
  data = []

  for _ in range(n):
    length = len(data)
    size = sys.getsizeof(data)
    print(f"Length: {length}, size in bytes: {size}")
    start_time = perf_counter_ns()
    data.append(None)
    end_time = perf_counter_ns()
    elapsed_microseconds = (end_time - start_time) / 1_000
    if measure_appends:
      print(f"Append operation took {elapsed_microseconds} microseconds")
