"""
Given a list, return it rotated k times
"""

def rotate(list_, k):
    if len(list_) == 1:
        return list_
    if k > len(list_):
        k = k % len(list_)
    
    return list_[-k:] + list_[:-k]


print(rotate([1,2,3,4], 18))