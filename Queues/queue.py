"""
Works in a FiFO structure
Implementing a QUEUE Data Structure
"""

class Queue():
    """
    a destructure that creates the initial Queue
    """

    def __init__(self):
        self.items = []

    def push(self, item):
        """
        Add item to the end of the queue
        """
        return self.items.append(item)

    def remove(self):
        """
        Remove first item on the queue
        """
        return self.items.pop(0)

    def is_empty(self):
        """
        Check if queue is empty
        """
        return self.items == []

    def peek(self):
        """
        Return the top of the queue
        """
        if not self.is_empty():
            return self.items[0]

    def get_queue(self):
        return self.items

q = Queue()
q.push("A")
q.push("B")
q.push("C")
q.push("D")
print(q.get_queue())
print(q.peek())
print(q.remove())
print(q.get_queue())