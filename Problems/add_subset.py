"""
Given a string, find the longest palindromic contiguous
substring. If there are more than one with the maximum length,
return any one.

For example, the longest palindromic substring of "aabcdcb" is
"bcdcb". The longest palindromic substring of "bananas" is "anana".
"""

def solution(n):
    if n=="" or (type(n) != str):
        return 0
    front = 0
    back = 0
    mid = 0
    n = n.lower()
    m = n
    p = n
    while m != "":
        if m == m[::-1]:
            if len(m) > front:
                front = len(m)
                s = m
        m = m[1:]

    while p != "":
        if p == p[::-1]:
            if len(p) > mid:
                mid = len(p)
                z = p
        p = p[1:]
        p = p[:-1]

    while n != "":
        if n == n[::-1]:
            if len(n) > back:
                back = len(n)
                c = n
        n = n[:-1]

    return max((s, c, z), key=len)
    


print(solution("bananas"))