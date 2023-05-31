
"""
Python:Lambda Map

The square operation is to be performed on an input
array of arrays. It is to be applied only to the integers which are
greater than 0, ignoring the rest, i.e. the rest are not to be included in the output.
The input is not exactly a 2D array, as all the rows can have different number of elements.

example: input array = [[-1, -2, 1, 2, 3], [4, -5], [6, 7, 8, 9]]

remove all elements less than or equal to 0
square all elements
"""


def lambdaMap(arr):
    result = list(map(lambda row: list(map(lambda num: num ** 2, filter(lambda num: num > 0, row))), arr))
    return result

    """
    a decorator that logs the invocation of the decorated function
    to the provided descriptor. assume that it will only decorate functions that take
    in positional arguments.
    - the log line format is; LOG: ,function_name>(comma separated list of arguments).
    last character should be a newline.
    - The line should be logged prior to the execution of the decorated function's body.

    example:
    @log(descriptor)
    def my_max(a,b,c):
        return max(a,b,c)

    @log(descriptor)
    def my_min(a,b):
        return min(a,b)

    my_max(1,2,3)
    my_min(1,2)
    my_sum(1,2,3)

    writes to the given descriptor the following output:
    LOG: my_max(1,2,3)
    3
    LOG: my_min(1,2)
    1
    LOG: my_sum(1,2,3)
    6
    """


def log(descriptor):
    # Implement the decorator here
    def decorator(func):
        def wrapper(*args, **kwargs):
            log = f"LOG: {func.__name__}({','.join(map(repr, args))})\n"
            descriptor.write(log)
            result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator


"""
given an arbitrary function, return a new function, which, when called, returns the result of
the original function calledwith the arguments reversed order.
"""


def reverse_args(func):
    def wrapper(*args, **kwargs):
        reversed_args = args[::-1]
        return func(*reversed_args, **kwargs)
    return wrapper
