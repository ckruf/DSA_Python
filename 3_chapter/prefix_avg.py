def prefix_average1(S):
  """Return list such that, for all j, A[j] equals average of S[0], ..., S[j]."""
  n = len(S)
  A = [0] * n                     # create new list of n zeros
  for j in range(n):
    total = 0                     # begin computing S[0] + ... + S[j]
    for i in range(j + 1):
      total += S[i]
    A[j] = total / (j+1)          # record the average
  return A

def prefix_average2(S):
  n = len(S)
  A = [0] * n
  A[0] = S[0]
  for i in range(1, n):
    A[i] = ((A[i - 1] * i) + S[i]) / (i + 1)
  return A

def prefix_average3(S):
  n = len(S)
  A = [0] * n
  total = 0
  for i in range(n):
    total += S[i]
    A[i] = total / (i + 1)
  return A

if __name__ == "__main__":
  my_lst = [18, 10, 12, 25, 20]
  print(prefix_average1(my_lst))
  print(prefix_average2(my_lst))
  print(prefix_average3(my_lst))
