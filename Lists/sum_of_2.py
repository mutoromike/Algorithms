"""
Given a list of positive numbers, find
if there exists a combination of 2 numbers
that add to a given number:
    i.e. [2,5,3,1] and 6. 5 and 1 should be returned
"""

def find_sum(values, target):
    if values == []:
        return "No Values"
    data = set()
    
    for v in values:
        # Check if compliment exists in the set
        print(v)
        compliment = target - v
        if v in data:
            return "Values: {} and {}".format(v, compliment)
        # Add compliment in the set
        data.add(compliment)

    return "None"


print(find_sum([5,3,7,11,8,10,13], 24))


"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
"""

def twoSum(nums, target):
    if nums == []:
        return []
    data = dict()
    index = 0
    for num in nums:
        compliment = target - num
        if num in data.keys():
            return [data[num], index]
        data[compliment] = index
        index += 1
    return []