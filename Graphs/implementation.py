"""
Graphs are created using other DS e.g. trees and linked lists
"""

# Implementation
# #1 Using edge lists

e_list = [[0,2],[2,3],[2,1],[1,3]]

# #2 Adjucent List
# Index is the Node and the value is the node's neghbours
a_list = [[2], [2,3], [0,1,3], [1,2]] 
"""
explaining the above code:
    0 is connected to 2
    1 is connected to 2 and 3
    2 is connected to 0,1 and 3
"""

# #Adjacent matrix
# Similar rep as above
m_list = [
    [0,0,1,0],
    [0,0,1,1],
    [1,1,0,1],
    [0,1,1,0]
]

#  Using object to represent the above
l = {
    0: [0,0,1,0],
    1: [0,0,1,1],
    2: [1,1,0,1],
    3: [0,1,1,0]
}

