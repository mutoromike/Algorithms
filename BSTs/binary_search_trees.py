class Node():

    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None


class BST():

    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert(data, self.root)

    def _insert(self, data, cur_node):
        if data < cur_node.data:
            if cur_node.left is None:
                cur_node.left = Node(data)
            else:
                self._insert(data, cur_node.left)
        elif data > cur_node.data:
            if cur_node.right is None:
                cur_node.right = Node(data)
            else:
                self._insert(data, cur_node.right)
        else:
            print("The data is already in the tree")

    def search(self, data):
        if self.root:
            is_found = self._find(data, self.root)
            if is_found:
                return True
            else:
                return False
        else:
            return None

    def _find(self, data, cur_node):
        if data > cur_node.data and cur_node.right:
            return self._find(data, cur_node.right)
        elif data < cur_node.data and cur_node.left:
            return self._find(data, cur_node.left)
        
        elif data == cur_node.data:
            return True


bst = BST()
bst.insert(5)
bst.insert(4)
bst.insert(2)
bst.insert(1)
bst.insert(3)
bst.insert(7)
bst.insert(6)
bst.insert(10)

print(bst.search(23))