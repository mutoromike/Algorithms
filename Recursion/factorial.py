def factorial(n):
    if n == 2:
        return n
    return n * factorial(n-1)
    

# print(factorial(3000))


def fact(n):
    mult = 1
    while n >= 2:
        mult = mult * n
        n -= 1
    return mult

# print(fact(3000))

def sum(n):
    if n == 0:
        return n
    return n + sum(n-1)

print(sum(5))