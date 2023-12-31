#task1

class __Node:
    def __init__(self, value):
        self.value = value
        self.nxt = None
class LinkedList:
    def __init__(self, *args):
        length = len(args)
        self.__length = length
        self.__head = self.__Node(args[0]) if length > 0 else None
        self.__tail = self.__head
        for i in range(1, length):
            self.__tail.nxt = self.__Node(args[i])
            self.__tail = self.__tail.nxt
 
    def __iter__(self):
        current = self.__head
        while current is not None:
            yield current.value
            current = current.nxt
 
    def __str__(self):
        return f"[{' '.join(str(i) for i in self)}]"
 
    def __len__(self):
        return self.__length
 
    def __index_check(self, index):
        if not 0 <= index < self.__length:
            raise IndexError
 
    def append(self, value):
        if self.__length > 0:
            self.__tail.nxt = self.__Node(value)
            self.__tail = self.__tail.nxt
        else:
            self.__head = self.__tail = self.__Node(value)
        self.__length += 1
 
    def get(self, index):
        self.__index_check(index)
        current = self.__head
        for _ in range(index):
            current = current.nxt
        return current.value
 
    def remove(self, index):
        self.__index_check(index)
        if self.__length == 1:
            self.__head = self.__tail = None
        elif index == 0:
            self.__head = self.__head.nxt
        else:
            current = self.__head
            for _ in range(index - 1):
                current = current.nxt
            current.nxt = current.nxt.nxt
            if index == self.__length - 1:
                self.__tail = current
        self.__length -= 1
    def insert(self, n, val):
        if n < 1 or n > len(self):
            return "Invalid index"

        new_val_node = Node(val)

        prev_node = None
        for i in range(1, n):
            prev_node = prev_node.next
            
        new_val_node.next = prev_node.next 
        prev_node.next = new_val_node 
