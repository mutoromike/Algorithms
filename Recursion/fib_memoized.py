"""
    Given a number N, return the index value of the 
    fibonacci sequence, i.e. where the sequence is:
"""


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
    if n < 2:
        value = n
    elif n == 2:
        value = 1
    else:
        value = fibonacci(n-1) + fibonacci(n-2)
    fibonacci_cache[n] = value
    return value


# print(fibonacci(999))
for n in range(1, 10001):
    print(n, ":", fibonacci(n))

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


# for n in range(1, 10000):
#     print(n, ":", fib(n))


# Without recursion

def fibs(n):
    li = [0,1]
    i = 2
    while i < n+1:
        li.append(li[i-2] + li[i-1])
        i += 1
    return li[n]

# print(fibs(100000))