# Tail recursion - by ChatGPT

> What is tail recursion?

Tail recursion is a specific form of recursion where the recursive call is the last operation performed in the function. This means that there is no additional computation that needs to be done after the recursive call returns. Because of this, the call stack does not need to save the current function's state before making the recursive call, which can make tail recursive functions more efficient than non-tail recursive ones.

> Can you give examples of functions which use tail recursion and functions which don't use tail recursion?

Sure, here are some examples of tail recursive functions:
 - A function to calculate the factorial of a number using tail recursion:
 
 ```
  def factorial_tail_recursive(n, acc=1):
      if n == 0:
          return acc
      return factorial_tail_recursive(n-1, acc*n)
 ```

- A function to calculate the nth Fibonacci number using tail recursion:

```
  def fibonacci_tail_recursive(n, a=0, b=1):
      if n == 0:
          return a
      elif n == 1:
          return b
      return fibonacci_tail_recursive(n-1, b, a+b)

```

Here are some examples of non-tail recursive functions:

- A function to calculate the factorial of a number using recursion:

```
def factorial_non_tail_recursive(n):
    if n == 0:
        return 1
    return n * factorial_non_tail_recursive(n-1)
```

- A function to calculate the nth Fibonacci number using recursion:

```
def fibonacci_non_tail_recursive(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci_non_tail_recursive(n-1) + fibonacci_non_tail_recursive(n-2)
```

In both examples above, the recursive call is not the last operation, there's an additional calculation that needs to be done.