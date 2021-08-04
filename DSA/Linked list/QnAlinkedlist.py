from random import randint

class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.prev = None

    def __str__(self):
        return str(self.value)

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def __str__(self):
        values = [str(x.value) for x in self]
        return ' -> '.join(values)

    def __len__(self):
        result = 0
        nod = self.head
        while nod:
            nod = nod.next
            result += 1
        return result
   
    def addEnd(self,value):
        if self.head is None:
            newNode = Node(value)
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = Node(value)
            self.tail = self.tail.next
        return self.tail

    def generate(self, n , min, max):
        self.head = None
        self.tail = None
        for i in range(n):
            self.addEnd(randint(min ,max))
        return self

coust = LinkedList()
coust.generate(10, 10, 20)
print(coust)


