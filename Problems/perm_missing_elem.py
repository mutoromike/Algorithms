"""An array A consisting of N different integers is given. The array contains 
integers in the range [1..(N + 1)], which means that exactly one element is missing.

Your goal is to find that missing element.

Write a function:

def solution(A)

that, given an array A, returns the value of the missing element.

For example, given array A such that:

  A[0] = 2
  A[1] = 3
  A[2] = 1
  A[3] = 5
the function should return 4, as it is the missing element.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [0..100,000];
the elements of A are all distinct;
each element of array A is an integer within the range [1..(N + 1)].
"""

def solution(a):
    if type(a) != list:
        return 0
    if a == []:
        return 0
    if len(a) == 1:
        l = [1,2]
        if a[0] == 1:
            return 2
        else:
            return 1
    data = {}
    m = 0
    for n in a:
        data[n] = m
        m += 1
    max_ = max(a)
    i = 1
    while i <= max_:
        if data.get(i) == None:
            return i
        i += 1
    return 0

print(solution([2,3,1,5]))