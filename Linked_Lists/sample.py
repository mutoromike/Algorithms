class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList():
    def __init__(self):
        self.head = None

    def my_list(self):
        cur = self.head
        while cur:
            print(cur.data)
            cur = cur.next

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        last_node = self.head

        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def prepend(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return
        
        new_node.next = self.head
        self.head = new_node

    def insert_after(self, prev, data):
        if not prev:
            print("Previous node does not exist")
            return

        new_node = Node(data)
        new_node.next = prev.next
        prev.next = new_node
        
l = LinkedList()

l.append("A")
l.append("b")
l.append("C")

l.prepend("First")
l.insert_after("Te", "Pa")
l.my_list()