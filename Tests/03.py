"""
An array consisting of N integers is given. We are looking for
pairs of elements of the array that are equal but occupy different
positions in the array. 
Calculate the number of indices of pairs

e.g. the array [3,5,6,3,3,5] will return 4. The pairs (0,3), (0,4), (1,5)
and (3,4) being counted and returned.
"""

# def get_values(li):
#     if type(li) is not list:
#         return
#     if len(li) == 0 or len(li) == 1:
#         return 0
#     else:
#         data = {}
#         count = 0
#         index = 0
#         for l in li:
#             # print("here", l)
#             if l in data:
#                 if data[l] < index:
#                     count += 1
#             data[l] = index
#             index += 1

#     return count

def countPairs(li): 
  
    data = dict() 
    n = len(li)
    i = 0
    # Finding frequency of each number. 
    while i < n:
        # print(i)
        if li[i] in data.keys(): 
            data[li[i]] += 1
        else: 
            data[li[i]] = 1
        i += 1
              
    # Calculating pairs of each value. 
    ans = 0
    for d in data: 
        count = data[d] 
        ans += (count * (count - 1)) // 2
    return ans

print(countPairs([3,5,6,3,3,3,3,5]))
