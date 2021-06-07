"""
Given 2 sorted arrays,
return one large array combining the 2
"""

def sort_list(l1, l2):
    if len(l1) == 0:
        return l2
    if len(l2) == 0:
        return l1
    i = 0
    j = 0
    final_list = []
    while i < len(l1) and j < len(l2):
        if l1[i] < l2[j]:
            final_list.append(l1[i])
            i += 1
        else:
            final_list.append(l2[j])
            j += 1
    
    return final_list + l1[i:] + l2[j:]

def sort_list2(l1, l2):
    if len(l1) == 0:
        return l2
    if len(l2) == 0:
        return l1
    l = l1 + l2
    return sorted(l)

print(sort_list([1,2,3,5,6,9], [4,5,7,12,34]))