"""
For an ideal compression function, the capacity of the bucket array for a
hash table should be a prime number. Therefore, we consider the problem
of locating a prime number in a range [M,2M]. Implement a method for
finding such a prime by using the sieve algorithm. In this algorithm, we
allocate a 2M cell Boolean array A, such that cell i is associated with the
integer i. We then initialize the array cells to all be “true” and we “mark
off” all the cells that are multiples of 2, 3, 5, 7, and so on. This process
can stop after it reaches a number larger than √2M. (Hint: Consider a
bootstrapping method for finding the primes up to √2M.)
"""
from math import pow


def sieve_of_erastothenes(n: int) -> list[int]:
    """
    Find all prime numbers up to n using the sieve of Erastothenes algorithm.
    """
    primes = [True for _ in range(n + 1)]
    p = 2
    sqrt = int(pow(n, 0.5))
    while p <= sqrt:
        if primes[p]:
            for i in range(p * p, n + 1, p):
                primes[p] = False
        p += 1
    return [p for p in range(2, n + 1) if primes[p]]


def prime_in_range(M: int) -> int:
    """
    Given M, find a prime in the range [M, 2M].
    """
    upper_limit = 2 * M
    primes_up_to_sqrt = sieve_of_erastothenes(int(pow(upper_limit, 0.5)))
    A = [True for _ in range(upper_limit + 1)]

    # Mark non-primes in A using the primes up to sqrt(2M)
    for p in primes_up_to_sqrt:
        start = max(p * p, M + (p - M % p) % p)  # Start marking from the first multiple of p within [M, 2M]
        for multiple in range(start, upper_limit + 1, p):
            A[multiple] = False

    # Find the prime in the range [M, 2M]
    for i in range(M, upper_limit + 1):
        if A[i]:
            return i

    return None  # In case no prime is found in the range, which is unlikely

"""
The method used to find primes up to n is the sieve of Erastothenes. This algorithm
starts with 2, and 
"""