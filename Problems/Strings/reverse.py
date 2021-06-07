"""
Reverse a string
"""

def reverse(s):
    if type(s) is not str or len(s) < 2:
        return 

    backwards = []

    i = len(s)-1
    while i >= 0:
        backwards.append(s[i])
        i -= 1
    
    print("".join(backwards))
    return "".join(backwards)

def reverse2(s):
    if type(s) is not str or len(s) < 2:
        return s
    return s[::-1]


print(reverse("mimi ni mtu"))