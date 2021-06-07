#!/bin/python3

import math
import os
import random
import re
import sys
from operator import itemgetter

from natsort import natsorted


#
# Complete the 'numberOfTokens' function below.

# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER expiryLimit
#  2. 2D_INTEGER_ARRAY commands
#

def numberOfTokens(expiryLimit, commands):
    # Write your code here
    freq = {}
    for item in commands:
        if item[0]==0:
            freq[item[1]] = item[2] + expiryLimit
        else:
            if item[1] in freq.keys():
                expiry = freq[item[1]]
                if expiry <= item[2]:
                    freq.pop(item[1])
                else:
                    freq[item[1]] = item[2] + expiryLimit

    return len(freq)


# if __name__ == '__main__':



def numberOfTokenss(expiryLimit, commands):
    # Write your code here
    values = dict()
    time = 0

    for c in commands:
        #  extraction values
        action = c[0]
        token_id = c[1]
        time = c[2]

        #  set token
        if action == 0:
            values[token_id] = expiryLimit + time

        #  reset token
        elif action == 1:
            # check if token exists
            if token_id in values:
                expiry_time = values[token_id]
                print(values)
                if expiry_time >= time:
                    values[token_id] = time + expiryLimit
                    # values[token_id] = values[token_id] + expiryLimit - (expiry_time - time)

    # counting values alive after reading all the values
    count = sum(1 for i in values.values() if i >= time)
    return count

# print(numberOfTokenss(4, [[0,1,1],[0,2,2],[0,3,1],[1,1,5],[1,2,7],[1,3,8]]))


def solution(items, sortOrder, pageNumber, sortParameter, itemsPerPage):

    if sortOrder == 0:
        order = False
    elif sortOrder == 1:
        order = True

    if sortParameter == 1:
        sort = sorted(items, key=lambda x: x[1], reverse=order)
    elif sortParameter == 2:
        sort = sorted(items, key=lambda x: x[2], reverse=order)
    elif sortParameter == 0:
        sort = natsorted(items, key=lambda x: x[0], reverse=order)
    slicer = pageNumber*itemsPerPage
    sliced = slice(slicer, slicer + itemsPerPage)
    print(sort)
    return sort[sliced]

print(solution([["item4",7,1],["item1",2,2],["item90",3,1],["item7",6,5],["item33",2,7],["item3",28,8]], 0, 1, 0, 2))



# def numberOfTokens(expiryLimit, commands):
#     # Write your code here
#     values = {}

#     for cur in commands:
#         #  extraction values
#         token = cur[1]
#         time = cur[2]

#         if cur[0] == 0:
#             values[token] = expiryLimit + time

#         elif cur[0] == 1:
#             # check if token exists
#             if token in values:
#                 expiry_time = values[token]
#                 if expiry_time >= time:
#                     values[token] = time + expiryLimit

#     return sum(1 for i in values.values() if i >= time)

#     select 
#     d.Name, 
#     count(e.ID) as empCount
# from 
#     Department d
# left outer join 
#     Employee e on d.ID = e.DEPT_ID
# group by 
#     d.Name
# order by 
#     empCount desc, 
#     d.Name