"""
Given a list (array)
return the first recurring character
e.g [2,1,1,3,2,4,6] should return 1
"""

def recur(l):
    data = set()
    for li in l:
        if li in data:
            return li
        data.add(li)
    return "No recurring element"

print(recur([2,1,1,3,2,4,6]))
    