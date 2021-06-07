# Has O(n^2)

def sort(li):
    i = 0
    n = len(li)-1

    while i <= n:
        j = 0
        while j < n:
            if li[j] > li[j+1]:
                temp = li[j]
                li[j] = li[j+1]
                li[j+1] = temp
            j += 1
        i += 1

    return li


print(sort([3, 456, 56, 78, 1, 0, 34, 90, 81, 100]))