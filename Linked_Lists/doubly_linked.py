class Node():

    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinked():

    def __init__(self):
        self.head = None

    def append(self, data):

        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        last_node = self.head
        while last_node.next:

            last_node = last_node.next
        new_node.prev = last_node.data
        last_node.next = new_node

    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            print(current_node.prev)
            current_node = current_node.next

new = DoublyLinked()
new.append("A")
new.append("B")
new.append("C")
new.append("D")

new.print_list()