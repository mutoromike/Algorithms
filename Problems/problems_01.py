"""
Given a list of numbers and a number k, return
whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, 
return true since 10 + 7 is 17.
"""

def get_sum(n, nums=[]):
    if nums == []:
        return "The list is empty"
    i=0
    j = len(nums)
    k = 0
    while i < j:
        k = nums[i]
        if n in list(map(lambda x: x+k, nums)):
            return True
        i+=1
    return False

print(get_sum(17, [10, 15, 3, 7]))

"""
This solution has a BIG O of O(n)
"""


"""Sum of numbers from 1 to n"""
def get_sums(n):
    return n * (n+1)/2

"""Binary search O(logn)"""
def binary_search(lst, elem):
    start = 0
    end = elem
    middle = math.floor((start + elem)/2)
    while middle != elem:
        if elem < lst[middle]:
            end = middle - 1
        else:
            start = middle + 1
        if start >= end:
            return -1
        middle = math.floor((start + end)/2)
    return middle

k = [1,2,3,4,5,6]
m = [2,5,6,7,8,9]
x = [[i,j] for i,j in zip(k,m)]
print(x)