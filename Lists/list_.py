"""
Implement List (Array) features
"""

class myList(object):
    
    def __init__(self):
        self.length = 0
        self.data = {}

    def get(self, index):
        return self.data[index]

    def append(self, item):
        self.data[self.length] = item
        self.length += 1

        return self.length

    def pop(self):
        last_item = self.data[self.length-1]
        del self.data[self.length-1]
        self.length -= 1
        return last_item

    # self delete(index):
    
x = myList()
x.append("mine")
x.append("hers")
print(x.get(0))
print(x.pop())
print(x.get(0))