class Node():

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList():

    def __init__(self):
        self.head = None

    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next

    def append(self, data):
        """
        Insert at the end of the list
        """
        new_node = Node(data)
        """
        If the list is empty:. 
            Insert the new Node as the Head
        """
        if self.head is None:
            self.head = new_node
            return
        """
        If the list is not empty:. 
            Find the ending of the list
            & insert the new node
        """
        last_node = self.head
        while last_node.next: # While this is not Null
            last_node = last_node.next
        last_node.next = new_node

    def prepend(self, data):
        """
        Insert at the beginning of the list
        """
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_after_node(self, prev_node, data):
        """
        Insert after a specific node
        """
        if not prev_node:
            print("Previous Node is not in the list")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node



llist = LinkedList()
llist.append("A")
llist.append("B")
llist.append("C")
llist.append("D")
llist.insert_after_node(llist.head.next, "E")
llist.print_list()