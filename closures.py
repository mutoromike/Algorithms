# Closures in Python

def counter(n):
    count = 0
    def revs(n):
        nonlocal count
        while count < n:
            print("counter")
            count+=1
        return count
    return revs

c = counter(5)
print(c(5))