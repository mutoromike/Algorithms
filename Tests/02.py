"""
A non-negative integer variable V is given. There are 2 actions
available to modify its value:

        V is odd: Subtract 1 from it
        V is even: divide V by 2

These are performed till V's value is 0.
e.e. if V = 28, it'll become 0 after 7 steps

func:
    input: binary string
    return: number of steps to reduce it to 0

    e.g. if S="011100"
    should return & since S=28
"""

# def perm(s):
#     c = int(s, 2)
    # if c == 0:
    #     return 0
    # if c == 1:
    #     return 1
#     else:
#         return numbers(c, num=0)

# def numbers(c, num):
#     if c > 0:
        # if c%2 == 0:
        #     c = c/2
        #     num += 1
        #     return numbers(c, num)
        # else:
        #     c -= 1
        #     num += 1
        #     return numbers(c, num)
#     else:
#         return num
# print(perm("011100"))


def get_num(s):
    c = int(s, 2)
    num = 0
    if c == 0:
        return 0
    if c == 1:
        return 1
    while c > 0:
        if c%2 == 0:
            c = c/2
            num += 1
        else:
            c -= 1
            num += 1


    return num

print(get_num("011100"))
