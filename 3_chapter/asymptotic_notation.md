# Asymptotic notation

In order to evaluate the performance of an algorithm, we would like to express how the running time of the algorithm grows as the input size grows. In particular, we are interested in the most important factor of the function mapping the input size to the running time. 

For example, suppose the running time of an algorithm varies with input size n according to the function `6n^2 + 100n + 300`. In asymptotic analysis, we are interested in large values of n. For large values of n, the terms `100n + 300` become insignificant compared to the `6n^2` term. We typically also ignore the coefficients of the leading terms, as they are usually not as signficant at large values of n. So this function would be `O(n^2)`

## Functions in asymptomatic notation

There are several functions which we will often encounter in the analysis of algorithms. Here they are, ordered from slowest **growing** to fastest **growing**:

1. `O(1)`
2. `O(log(n))`
3. `O(n)`
4. `O(nlog(n))`
5. `O(n^2)`
6. `O(n^2log(n))`
7. `O(n^3)`
8. `O(2^n)`
9. `O(n!)`

## Big O notation

Big O notation is used to express an upper bound on the running time of an algorithm. It is concerned with the worst case running time of an algorithm. More formally, if an algorithm has running time `O(f(n))`, then for large enough values of n (the asymptotic case), the running time is at most `k*f(n)`.

<img src="./running_time.png">

Slightly more formally, we could say that a function f(n) is O(g(n)) if there is a real constant c > 0 and an integer constant n0 ≥ 1 such that:

`f(n) ≤ c*g(n)` for n ≥ n0.

For example, the function 8n + 5 is O(n). There are many values we could use for c and n0 to show this. For example, c = 9 and n0 = 5. Or c = 13 and n0 = 1.

### Some properties of Big O

If a function is a polynomial of the nth degree, such that:

f(n) = a<sub>0</sub> + a<sub>1</sub>n + ··· + a<sub>d</sub>n<sup>d</sup>

Then f(n) is O(n^d).

Because for n ≥ 1 we have 1 ≤ n ≤ n^2 ≤ n^3 ≤ ... ≤ n^d

Therefore

a<sub>0</sub> + a<sub>1</sub>n + a<sub>2</sub>n<sup>2</sup> ··· + a<sub>d</sub>n<sup>d</sup> ≤ (|a<sub>0</sub>| + |a<sub>1</sub>| + |a<sub>2</sub>| + |a<sub>d</sub>|) * n<sup>d</sup>

Therefore, it is O(n^d), since we can find a coefficient c, such that f(n) < g(n).

### Characterizing accurately

While technically it would be correct that a function like `8n + 5` is O(n^2) or O(n^3) or O(2^n), since we can find quadratic, cubic and exponential functions which act as an upper bound on the function, it would be a bit misleading / inaccurate. We always strive to give the closest possible function as upper bound (ie `O(n)` in this case).

## Big Omega and Big Theta

While Big O provides an upper bound for a function (and for the rate of growth of our algorithm in terms of input size), Big Omega provides a lower bound. 