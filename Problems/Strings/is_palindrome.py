def palindrome(s):
    s = s.lower()
    s = s.replace(" ", "")
    c = s[::-1]

    if c == s:
        return True
    return False

print(palindrome("dada d"))