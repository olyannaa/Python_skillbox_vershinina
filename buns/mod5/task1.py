class Node:
    def __init__(self, data):
        self.data = data  
        self.pref = None  


class Stack:
    def __init__(self):
        self.end = None  

    def pop(self):
        if self.end is None:
            raise IndexError("Stack is empty")

        val = self.end.data
        self.end = self.end.pref
        return val

    def push(self, val):
        new_node = Node(val)
        if self.end is None:
            self.end = new_node
        else:
            new_node.pref = self.end
            self.end = new_node

    def print(self):
        if self.end is None:
            print("Stack is empty")
            return

        current = self.end
        while current is not None:
            print(current.data)
            current = current.pref
