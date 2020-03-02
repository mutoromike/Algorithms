cached_data = {}


def solution(A):
    if type(A) != list:
        return
    if A == []:
        return
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

print(solution(range(1, 202)))