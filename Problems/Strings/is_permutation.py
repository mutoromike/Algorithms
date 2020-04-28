def is_permutation(s, st):
    if len(s) != len(st):
        return False

    if sort_s(s) == sort_s(st):
        return True

    return False


def sort_s(s):
    s = sorted(s)
    return "".join(s)


print(is_permutation("mine", "mine"))