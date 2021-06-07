"""
This is a demo task.

Write a function:

def solution(A)

that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.

For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.

Given A = [1, 2, 3], the function should return 4.

Given A = [−1, −3], the function should return 1.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
each element of array A is an integer within the range [−1,000,000..1,000,000].
"""

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# def solution(A):
#     # write your code in Python 3.6
#     ints_list = range(min(A), max(A) + 1)
#     missing_list = [x for x in ints_list if x not in A]
#     if missing_list == []:
#         return max(A) + 1
#     elif min(missing_list) < 0:
#         return 1
#     else:
#         return min(missing_list)
[3,4,5,7,8]

def solution(A):
    # write your code in Python 3.6
    if 1 not in A:
        return 1
    a = min(A)
    c = max(A)
    ints_list = range(a, c + 1)
    miss = [x for x in set(ints_list) if x not in set(A)]
    if miss == []:
        if c < 0:
            return 1
        return c + 1
    b = min(miss)
    if b <=0:
        return 1
    return b





def solution(S):
    # write your code in Python 3.6
    n = len(S)
    data = ""
    i = 0
    for i in range(n):
        print("we are here")
        if i+1 <= n-1:
            if (S[i] > S[i+1]):
                for j in range(n):
                    if (i != j):
                        print(j, i)
                        print(data)
                        data += S[j]

                return data
    data = S[0: n-1]
    return data

print(solution("codility"))

