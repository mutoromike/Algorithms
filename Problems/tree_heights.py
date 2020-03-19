def min_tree_cuts(n):
    if not n or len(n) <=1:
        return 0

    count = 0 #count of cuts from front
    count1 = 0 # count of cuts from back
    i = 0 #front pointer, moves to end of array.
    j = len(n)-1 #back pointer, moves to start of array

    if n[0] >= n[1]:
        i = 1
    if n[-1] >= n[-2]:
        j = j-1
    elements = []
    elements1 = []

    while i <= len(n) or j >= 0:

        if (i-1>=0 and i<=len(n)-1 and n[i-1]<=n[i])\
        or (i+1 <= len(n)-1 and n[i+1] <= n[i])\
        or (i == len(n)-1 and n[len(n)-2]<= n[i]):
            count +=1

        if (j-1 >= 0 and n[j-1] <= n[j])\
        or (j>=0 and j+1 <= len(n)-1 and n[j+1] <= n[j]):
            count1 +=1
        i +=2
        j -=2


    return min(count, count1)









def solution(m):
    maxN = 0
    #get starting points
    for row in range(0, len(m)):
        for col in range(0, len(m[row])):
            maxN = max(maxN, dfs(row, col, m, 3, set()))
    return maxN
def dfs(row, col, m, depth, visited=set()):
  if row < 0 or row >= len(m) or col < 0 or col >= len(m[row]) or (row,col) in visited:
    return -2**32
  if depth == 0:
    return m[row][col]
  visited.add((row,col))
  rest = max(
    dfs(row-1, col, m, depth-1, visited),
    dfs(row+1, col, m, depth-1, visited),
    dfs(row, col-1, m, depth-1, visited),
    dfs(row, col+1, m, depth-1, visited)
  )
  visited.remove((row,col))
  return (m[row][col] * (10**depth)) + rest