"""
    Functionality that implements stacks in checking whether
    a string of parentheses, brackets and/or braces are
    a perfect match, i.e. opening and closing pairs
"""
from stacks import Stack


def is_match(p1, p2):
    """
    Check if the parens are a match
    """
    if p1 == "(" and p2 == ")":
        return True
    elif p1 == "[" and p2 == "]":
        return True
    elif p1 == "{" and p2 == "}":
        return True
    else:
        return False    



def is_parens_balanced(parens_string):
    s = Stack()
    is_balanced = True
    index = 0

    while index < len(parens_string) and is_balanced:
        paren = parens_string[index]
        if paren in "({[":
            s.push(paren)
        else:
            if s.is_empty():
                is_balanced = False
            else:
                top = s.pop()
                if not is_match(top, paren):
                    is_balanced = False
        index += 1

    if s.is_empty() and is_balanced:
        return True
    else:
        return False

print(is_parens_balanced("{([])}"))