cached_data = {}


def solution(A):
    if type(A) != list:
        return 0
    if A == []:
        return 0
    # value = A.count(n)%2
    for n in A:
        if n in cached_data:
            cached_data[n] += 1
        else:
            cached_data[n] = 1

    for n in cached_data:
        if cached_data[n] == 1:
            return n
        # print(cached_data[n])
    return


# try large list
# l=[]
# for i in range(0, 1000000):
#     l.append(i)
# print(solution(l))

print(solution([2,2,3,3,4]))