
def solution(S):
    # write your code in Python 3.6
    count = 0
    start = 0
    first = 0
    n = len(S)
    while first <= n-3:
        second = 2
        while second <= n-2:
            part1 = S[start:first+1]
            part2 = S[first+1:second]
            part3 = S[-(len(S) - second):]
            print(part1, part2, part3)
            if part1.count("a") == part2.count("a") == part3.count("a"):
                count += 1
            second += 1
        first += 1
        
    return count




def solution(S, K):
    # write your code in Python 3.6
    n = len(S)
    data = []
    count = 0
    counter = 1
    new_s = ""
    index = 0
    start = 0
    for s in S:
        if start < len(S) and S[start+1]==s:
            counter+=1
        
        if start < len(S) and S[start+1]!=s:
            data.append([counter, s])
            counter=1
        start +=1
        
    print(data)
        
    for s in S:
        if index > 0:
            print(s)
            if s != S[index-1]:
                # if count == 1:
                #     new_s = new_s + s
                
                new_s = new_s + str(count) + s
                print(new_s)
                count = 0
        count+=1
        index += 1
        
    return len(new_s)
