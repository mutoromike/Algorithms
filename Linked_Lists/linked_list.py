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

    def delete_node(self, data):
        """
        Case 1: Node to be deleted is head
        """
        current_node = self.head
        if current_node and current_node.data == data:
            self.head = current_node.next
            current_node = None
            return
        """
        Case 2: Node to be deleted is not head
        """
        prev = None
        while current_node and current_node.data != data:
            prev = current_node
            current_node = current_node.next
        if current_node is None:
            return
        prev.next = current_node.next
        current_node = None
        # current_node = Node(data)

    """
    Deleting a node at a given position
        : Assume elements in the list are unique
    """
    def delete_node_at_pos(self, pos):
        current_node = self.head
        if pos == 0:
            self.head = current_node.next
            current_node = None
            return

        prev = None
        count = 1
        if current_node and count != pos:
            prev = current_node
            current_node = current_node.next
            count += 1
        if current_node is None:
            """
            position given is greater than the number of elements
            """
            return
        prev.next = current_node.next
        current_node = None

    # def reverse_nodes(self):
    #     prev = None
    #     cur = self.head
        

        



llist = LinkedList()
llist.append("A")
llist.append("B")
llist.append("C")
llist.append("D")
llist.delete_node("C")
# llist.insert_after_node(llist.head.next, "E")
llist.print_list()






"""
New method for running linked list:

this does append for O(1) instead of O(n)
"""



class Node():
  def __init__(self, data):
    self.data = data
    self.next = None


class LinkedList():
  def __init__(self):
    self.head = None
    self.tail = None

  def append(self, data):
    cur = Node(data)

    if self.head is None:
      self.head = cur
      self.tail = cur
      return

    self.tail.next = cur
    self.tail = cur

    return
    
  def get_list(self):
    cur = self.head
    li = []
    while cur:
      li.append(cur.data)
      cur = cur.next
    print(li)
    return

  def prepend(self, data):
    cur = Node(data)

    if self.head is None:
      self.head = cur
      return
    
    cur.next = self.head
    self.head = cur
    return


c = LinkedList()
c.append("a")
c.append("b")
c.append("c")
c.append("d")
c.prepend("we")
c.get_list()