"""
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.
Example:
Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
"""


l = [0,3,4,0,7,9,0,0,45,55,0]


def remove_zero(A):
    if 0 not in A:
        return A
    
    for i in A:
        if i == 0:
            A.remove(i)
            A.append(i)

    return A


print(remove_zero(l))