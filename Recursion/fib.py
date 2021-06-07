"""
Fibonacci without memoization
"""
mem_cache = {}
def fibonacci(i):
    # if 
    if i <= 1:
        return i
    else:
        return fibonacci(i - 1) + fibonacci(i - 2)

def count(s): 
    return fibonacci(s + 1)

print(count(5))
