# High scores example

```
class GameEntry:
  """Represents one entry of a list of high scores."""

  def __init__(self, name, score):
    """Create an entry with given name and score."""
    self._name = name
    self._score = score

  def get_name(self):
    """Return the name of the person for this entry."""
    return self._name
    
  def get_score(self):
    """Return the score of this entry."""
    return self._score

  def __str__(self):
    """Return string representation of the entry."""
    return '({0}, {1})'.format(self._name, self._score) # e.g., '(Bob, 98)'

class Scoreboard:
  """Fixed-length sequence of high scores in nondecreasing order."""

  def __init__(self, capacity=10):
    """Initialize scoreboard with given maximum capacity.

    All entries are initially None.
    """
    self._board = [None] * capacity        # reserve space for future scores
    self._n = 0                            # number of actual entries

  def __getitem__(self, k):
    """Return entry at index k."""
    return self._board[k]

  def __str__(self):
    """Return string representation of the high score list."""
    return '\n'.join(str(self._board[j]) for j in range(self._n))

  def add(self, entry):
    """Consider adding entry to high scores."""
    score = entry.get_score()

    # Does new entry qualify as a high score?
    # answer is yes if board not full or score is higher than last entry
    good = self._n < len(self._board) or score > self._board[-1].get_score()

    if good:
      if self._n < len(self._board):        # no score drops from list
        self._n += 1                        # so overall number increases

      # shift lower scores rightward to make room for new entry
      j = self._n - 1
      while j > 0 and self._board[j-1].get_score() < score:
        self._board[j] = self._board[j-1]   # shift entry from j-1 to j
        j -= 1                              # and decrement j
      self._board[j] = entry                # when done, add new entry
```

## Adding an entry

Let's look at the `add` method of the Scoreboard class, and go through two examples.

### Adding a score which is greater than all other scores currently in the list

Let's say that we have a list of length 10, and it is completely full, so it has 10 entries

`j` gets initialized to a value of 9. The while loop first sets the value of `board[9]` to `board[8]`, effectively shifting the values to the right. This will continue until the last iteration, which will occur when `j` has a value of 1. `board[1]` will get the value of `board[0]`, and j will be decremented to 0. The entry will then be placed to `board[0]`

### Adding a score which is greater than the lowest score on the list (but not greater than any other score on the list)\

Let's say again that we have a list of length 10, and it is completely full, so it has 10 entries.

`j` gets initialized to 9. The while loop will not even execute once though, because one of its conditions is that the score has to be greater than `board[j-1]`, in this case `board[8]`. However if the score is only greater than the last entry in the list, `board[9]`, it is not greater than `board[8]`. The entry will still be added thanks to the line after the while loop though.

