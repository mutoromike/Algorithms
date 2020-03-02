"""
A binary gap within a positive integer N is any maximal sequence of consecutive zeros that
is surrounded by ones at both ends in the binary representation of N.

For example, number 9 has binary representation 1001 and contains a binary gap of length 2.
The number 529 has binary representation 1000010001 and contains two binary gaps: one of length
4 and one of length 3. The number 20 has binary representation 10100 and contains one binary gap of
length 1. The number 15 has binary representation 1111 and has no binary gaps. The number 32 has binary
representation 100000 and has no binary gaps.

Write a function:

def solution(N)

that, given a positive integer N, returns the length of its longest binary gap. The function
should return 0 if N doesn't contain a binary gap.
"""
import math

def binary_gap(n, longest=0, count=0, gap=False):
    if type(n) is not int:
        raise TypeError("The number should be an integer")
    rem = n%2
    nxt = math.floor(n/2)
    if rem == 1:
        if count > longest:
            longest = count
        count = 0
        gap = True
    else:
        if gap:
            count += 1
    
    if nxt != 0:
        return binary_gap(nxt, longest, count, gap)

    return longest


def solution(A=[], K=0):
    # write your code in Python 3.6
    if K <= 0 or A == []:
        return "The array cannot be empty and the integer should be greater than 0"
    while K > 0:
        i = A.pop()
        A.insert(0, i)
        K -= 1
    if K > 0:
        return solution(A, K)
    return A



def get_odd():
    


