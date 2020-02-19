"""
Dynamic Programming Solution:
    Fibonacci with memoization: CACHING

Solution 1:
    Implementing memoization explicitly
"""

fibonacci_cache = {}

def fibonacci(n):
    # Check if the first value is in our cache and return it
    if n in fibonacci_cache:
        return fibonacci_cache[n]
    #  Compute n
    if n==1:
        value = 1
    elif n == 2:
        value = 1
    elif n > 2:
        value = fibonacci(n-1) + fibonacci(n-2)
    fibonacci_cache[n] = value
    return value

# for n in range(1, 10001):
#     print(n, ":", fibonacci(n))

"""
Solution 2:
    Implementing memoization using in-built
    Python functionality
"""
from functools import lru_cache

@lru_cache()
def fib(i):
    if type(i) != int:
        raise TypeError("i must be a positive integer")
    if i < 0:
        raise ValueError("i must be a positive integer")
    if i == 0 or i == 1:
        return i
    elif i == 2:
        return 1
    elif i>2:
        return fib(i - 1) + fib(i - 2)


for n in range(1, 10001):
    print(n, ":", fib(n))
