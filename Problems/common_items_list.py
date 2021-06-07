"""
Check if two arrays have any common items
"""

# BRUTE SOLN O(n^2) or O(a*b) if the lists have diff lengths

def comp_lists(l1, l2):
    for item1 in l1:
        for item2 in l2:
            if item1 == item2:
                return True

    return False

l1 = [1,2,3,4,5]
l2 = [6,7,8,9,4]


# OPTIMIZED SOLN : USING DICTIONARY

def comp_lists2(l1, l2):
    data = {}
    for item in l1:
        if item not in data:
            data[item] = "true"
    for item in l2:
        if item in data:
            return True
    return False

print(comp_lists2(l1, l2))
