"""
Implement an algorithm to determine if a
string has all unique characters. What if you
cannot use additional data structures?
"""

# def unique(s):
#     for st in s:
#         c = s.count(st)
#         if c > 1:
#             return False
#     return True

# Approach 2 - without using inbuilt methods

def unique(s):
    if len(s) > 128:
        return False

    for st in s:
        new = s.replace(st, '', 1) # replace the character once
        print(new)
        if st in new:
            return False

    return True

print(unique("mime"))
