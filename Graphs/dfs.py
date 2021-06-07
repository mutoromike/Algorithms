"""
Write a graph's dfs traversal algorithm
video link: https://www.youtube.com/watch?v=FvGCzzfdOLw
"""

adj_list = { # Vertices
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["B", "F"],
    "D": [],
    "E": ["F"],
    "F": []
}

color = {} # shows node state (W-not visited, G-first explored, B-all vertices explored)
parent = {} # to check node's parent (for explanation)
trav_time = {} # to check node traversal time (for explanation)
dfs_traversal_output = [] # to hold final graph traversal

# Initialize
for node in adj_list.keys():
    color[node] = "W"
    parent[node] = None
    trav_time[node] = [-1,-1]

time = 0

def dfs(n):
    global time
    color[n] = "G"
    trav_time[n][0] = time
    dfs_traversal_output.append(n)
    time += 1
    for vertex in adj_list[n]:
        if color[vertex] == "W":
            parent[vertex] = n
            dfs(vertex)

    color[n] = "B"
    trav_time[n][1] = time
    time+=1


dfs("A")
print(dfs_traversal_output)
print(trav_time)
print(parent)
