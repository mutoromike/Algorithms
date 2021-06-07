def solution(String):
    # write your code in Python 3.6
    li = []
    for s in String:
        li.append(s)
    data = {
        "A": 0,
        "B": 0
    }
    dropped = 0
    index = 0
    cur = 0
    n = len(li)
    while index < n:
        if li[index] == "A":
            cur += 1
            if index+1 < n and li[index+1] == "B":
                if cur > data["A"]:
                    dropped += data["A"]
                    data["A"] = cur
                else:
                    dropped += cur
                cur = 0
            # elif index+1 < n:
            #     if cur > data["A"]:
            #         dropped += data["A"]
            #         data["A"] = cur
            #     else:
            #         dropped += cur
            #     cur = 0

        if li[index] == "B":
            cur += 1
            if index+1 < n and li[index+1] == "A":
                if cur > data["B"]:
                    dropped += data["B"]
                    data["B"] = cur
                else:
                    dropped += cur
                cur = 0
            # elif index+1 < n:
            #     if cur > data["B"]:
            #         dropped += data["B"]
            #         data["B"] = cur
            #     else:
            #         dropped += cur
            #     cur = 0
        index += 1
    print(data)

    return dropped

print(solution("BAAABAB"))

