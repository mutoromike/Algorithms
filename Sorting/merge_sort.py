import math

def merge(left=[], right=[], new=[]):
    i, j, k = 0, 0, 0
    """
    Check the lenth of thr left and right
    parts of the new lists
    """
    while(i < len(left) and j < len(right)):
        if left[i] < right[j]:
            new[k] = left[i]
            i += 1
        else:
            new[k] = right[j]
            j += 1
        k += 1
    """
    Check if left part still remains and append 
    to the new list"""
    while i < len(left):
        new[k] = left[i]
        i += 1
        k += 1
    """
    Check if right part still remains and append 
    to the new list"""
    while j < len(right):
        new[k] = right[j]
        j += 1
        k += 1

    return new


def mergesort(new):
    n = len(new)
    # Check if the array has only one item and return
    if n < 2:
        return new
    # Divide the array in half
    mid = math.floor(n/2)
    left, right =[], []
    i=0
    # Arrange left side
    while i < mid:
        left.append(new[i])
        i += 1
    # Arrange right side
    while i >= mid and i < n:
        right.append(new[i])
        i += 1
    # Call mergesort recirsively to sort left and right parts
    a = mergesort(left)
    b = mergesort(right)
    # Return merged left and right
    return merge(a, b, new)

a = [2,9,5,7,1,6,8,3,12]
print(mergesort(a))
