"""
Works in a LIFO structure
Implementing a STACK Data Structure
"""

class Stack():
    """
    a destructure that creates the initial Stack
    """

    def __init__(self):
        self.items = []

    def push(self, item):
        """
        Add item to stack
        """
        return self.items.append(item)

    def pop(self):
        """
        Remove last item on stack
        """
        return self.items.pop()

    def is_empty(self):
        """
        Check if stack is empty
        """
        return self.items == []

    def peek(self):
        """
        Return the last item in the stack
        """
        if not self.is_empty():
            return self.items[-1]
    def get_stack(self):
        return self.items
