"""
Check if a string is a substring of another,
the method checking this should be called once!
"""

def is_rotation(s1, s2):
    _len = len(s1)
    if _len == len(s2) and _len > 0:
        return is_substring(s1+s1, s2)

    return False


def is_substring(s1, s2):
    print("s1 is {} and s2 is {}".format(s1, s2))
    if (s2 in s1):
        return True
    return False

print(is_rotation("waterbottle", "erbottlewat"))