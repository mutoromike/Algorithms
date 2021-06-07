class Graph(object):

    def __init__(self):
        self.no_of_nodes = 0
        self.adjacent_list = {}

    def add_vertex(self, node):
        self.adjacent_list[node] = []
        self.no_of_nodes += 1
        return self.adjacent_list

    def add_node(self, node1, node2):
        if node1 in self.adjacent_list:
            self.adjacent_list[node1].append(node2)
            self.adjacent_list[node2].append(node1)
            return self.adjacent_list
        else:
            return "vertex not available"

    def print_graph(self):
        return self.adjacent_list

    def show_connections(self):
        for k in self.adjacent_list.keys():
            print(k, self.adjacent_list[k])

g = Graph()
g.add_vertex(1)
g.add_vertex(2)
g.add_vertex(3)
g.add_vertex(4)
g.add_node(1,2)
g.add_node(2,3)
g.add_node(2,4)
g.add_node(4,3)
g.add_node(3,1)
print(g.print_graph())
g.show_connections()