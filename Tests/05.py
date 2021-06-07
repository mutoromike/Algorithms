def solution(blocks):
    start = min(blocks)
    index = blocks.index(start)

    end = len(blocks) - 1
    beg = 0
    right = index
    left = index
    while right < end:
        if blocks[right] <= blocks[right+1]:
            right += 1
        else:
            break
    while left > beg:
        if blocks[left] <= blocks[left-1]:
            left -= 1
        else:
            break

    dist = right - left + 1

    return dist
    

print(solution([1, 5, 5, 2, 6]))
