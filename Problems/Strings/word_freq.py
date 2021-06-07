"""
arrange words according to how they appear,
e.g tree should be eert or eetr
"""

def solution(st):
    dict_ = {}
    for s in st:
        if s in dict_:
            dict_[s] += 1
        else:
            dict_[s] = 1
    items = sorted(dict_.items(), key=lambda kv: kv[1], reverse=True)
    string = ""
    for item in items:
        if item[1] != 0:
            string = string + item[0]*item[1]
    return string


print(solution("acacacc"))