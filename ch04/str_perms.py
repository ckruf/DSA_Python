import copy

def og_str_perms(letters: list[str], count: int = 0) -> None:
  """
  The well studied OG string permutation algorithm. Proof that ChatGPT doesn't
  know what it's talking about when it comes to mathematical series.
  """
  length = len(letters)
  if count == length:
    print("".join(letters))
  else:
    for i in range(count, length):
      letters[count], letters[i] = letters[i], letters[count]
      og_str_perms(letters, count + 1)
      letters[count], letters[i] = letters[i], letters[count]


def alt_str_perms(perm: list[str], letters: set[str]) -> None:
  perm = perm.copy()
  letters = letters.copy()
  if len(letters) == 0:
    print("".join(perm))
  else:
    for letter in letters:
      perm.append(letter)
      letters.remove(letter)
      alt_str_perms(perm, letters)
      perm.pop()
      letters.add(letter)


def sub_perms(perm: list[str], letters: set, k: int):
  """Produce all k-length permutations from a set of elements"""
  # print(f"perm={perm}, letters={letters}")
  # perm = perm.copy()
  # letters = letters.copy()
  if len(perm) == k:
    print("".join(perm))
  else:
    for letter in letters:
      perm.append(letter)
      letters.remove(letter)
      sub_perms(perm, letters, k)
      perm.pop()
      letters.add(letter)


call_count = 0


def puzzle_solve(k: int, S: list, U: set):
  """Produce all k-length permutations from a set of elements"""
  print(f"puzzle_solve({k}, {S}, {U})")
  U = U.copy()
  global call_count
  call_count += 1
  for element in U:
    S.append(element)
    U.remove(element)
    if k == 1:
      print("".join(S))
    else:
      puzzle_solve(k-1, S, U)
    S.remove(element)
    U.add(element)

def puzzle_solve_list(k: int, S: list, U: list):
  """Produce all k-length permutations from a set of elements"""
  print(f"puzzle_solve({k}, {S}, {U})")
  global call_count
  call_count += 1
  for element in U:
    S.append(element)
    U.remove(element)
    if k == 1:
      print("".join(S))
    else:
      puzzle_solve_list(k-1, S, U)
    S.remove(element)
    U.append(element)


if __name__ == "__main__":
  # og_str_perms(["a", "b", "c"])
  # print("===")
  # alt_str_perms([], {"a", "b", "c"})
  # print("===")
  # sub_perms([], {"a", "b", "c", "d"}, 2)
  # print("========")
  puzzle_solve_list(3, [], ["a", "b", "c", "d"])
  print("========")
  print(f"call count is {call_count}")
  # print("========")
  # puzzle_solve_alt(4, [], {"a", "b", "c", "d"})

