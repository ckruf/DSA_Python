from typing import Sequence
import math

def p_norm(vector: Sequence[int | float], p: int = 2):
    """
    Given a vector in n-dimensional space, and a value for p, calculate the vector's p-norm.
    For example, if p is 3, then we would sum the cubes of each component of the vector,
    and then take the cube root.

    :param vector: sequence of numbers representing a vector in n-dimensional space
    :param p: specifies the norm
    """
    sum_of_exponentiated = sum(map(lambda component: math.pow(component, p), vector))
    return n_th_root(sum_of_exponentiated, p)


def n_th_root(number: int | float, root: int):
    """
    Find the nth root of a number

    :param number: number for which to find root
    :param root: which root to find (2 for square root, 3 for cube root etc...)
    """
    return math.pow(number, (1 / root))


if __name__ == "__main__":
    print(p_norm([3, 4]))