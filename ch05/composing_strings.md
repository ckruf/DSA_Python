# Composing  strings

Suppose that we had a long string, `document` and wanted to create a new string based on this string, such that the new string only contained the alphabetic characters of the original string. A naive approach would be:

```
letters = ""

for c in document:
  if c.isalpha():
    letters += c
```

The problem with this approach is that because strings are immutable, the line `letters += c` will create a new string on each iteration. Therefore, if `letters` ends up having length n, we would have constructed a string of length 1, then a string of length 2, all the way up to n, which would take time proportional to the familiar sum 1 + 2 + 3 + ... n; meaning `O(n^2)` time complexity. An improved approach would be

```
temp = []

for c in document:
  if c.isalpha():
    temp.append(c)

letters = "".join(temp)
```

This would be much faster, because when we are repeatedly appending to a list, we don't have to create a whole new list each time. Of course, we can do even better by using a comprehension, which avoids the repeated calls to `append`:

```
letters = "".join(c for c in document if c.isalpha())
```

