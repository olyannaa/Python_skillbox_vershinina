class Node:
    def __init__(self, data):
        self.data = data  
        self.nref = None  
        self.pref = None  


class Queue:

    def __init__(self):
        self.start = None  
        self.end = None  

    def pop(self):
        if self.start is None:
            raise IndexError("Queue is empty")

        val = self.start.data
        self.start = self.start.nref
        if self.start is None:
            self.end = None
        else:
            self.start.pref = None
        return val

    def push(self, val):
        new_node = Node(val)
        if self.end is None:
            self.start = new_node
            self.end = new_node
        else:
            new_node.pref = self.end
            self.end.nref = new_node
            self.end = new_node

    def insert(self, n, val):
        if self.start is None:
            raise IndexError("Queue is empty")

        new_node = Node(val)

        if n == 0:
            new_node.nref = self.start
            self.start.pref = new_node
            self.start = new_node
        else:
            current = self.start
            i = 0
            while current is not None and i < n:
                current = current.nref
                i += 1

            if current is None:
                raise IndexError("Index out of range")

            prev_node = current.pref
            prev_node.nref = new_node
            new_node.pref = prev_node
            new_node.nref = current
            current.pref = new_node

    def print(self):
        if self.start is None:
            print("Queue is empty")
            return

        current = self.start
        while current is not None:
            print(current.data)
            current = current.nref
