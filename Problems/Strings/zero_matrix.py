"""
Write an algorithm such that if an element in an MxN matrix is 0, its entire row and
column are set to 0.
"""

def _matrix(array):
    indices_pairs = [(row,col) for row in range(len(array)) for col in range(len(array[0])) if array[row][col] == 0]


    for indices_pair in indices_pairs:
        row, col = indices_pair

    for i in range(len(array[0])):
        array[row][i] = 0

    for i in range(len(array)):
        array[i][col] = 0

    return array

    

m = [[1,2,3],[5,8,4],[3,0,9]]
print(_matrix(m))