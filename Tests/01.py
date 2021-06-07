"""
Given a number N, return the least number with the
same number of digits, e.g. 125 returns 100, 10 returns 10
1 returns 0
"""

def number(n):
    if type(n) is not int:
        return
    s = len(str(n))
    if s < 1:
        return
    if s == 1:
        return 0
    else:
        num = "1" + "0"*(s-1)
        return int(num)
    

print(number(12324))