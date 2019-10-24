# simple function
from typing import Callable


def cube(n: int):
    return n ** 3


assert cube(3) == 27

# function as lambda
cube_lambda = lambda n: n ** 3
assert cube_lambda(3) == 27

# even or odd lambda
even_or_odd = lambda n: 'YES' if n % 2 == 0 else 'NO'
assert even_or_odd(10) == 'YES'

# sum of two numbers (typed lambda)
sum_of_two_numbers: Callable[[int, int], int] = lambda a, b: a + b
assert sum_of_two_numbers(3, 5) == 8
