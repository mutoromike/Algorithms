"""
Implement an algorithm to determine if a
string has all unique characters. What if you
cannot use additional data structures?
"""

def unique(s):
    for st in s:
        c = s.count(st)
        if c > 1:
            return False
    return True

print(unique("miminawewe"))