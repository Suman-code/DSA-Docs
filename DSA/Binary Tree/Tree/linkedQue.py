class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        nod = self.head
        while nod:
            yield nod
            nod = nod.next

class QueU:
    def __init__(self):
        self.linked = LinkedList()

    def __str__(self):
        values = [str(x) for x in self.linked]
        return ' '.join(values)

    
    def enqq(self, value):
        newNode = Node(value)
        if self.linked.head == None:
            self.linked.head = newNode
            self.linked.tail = newNode
        else:
            self.linked.tail.next = newNode
            self.linked.tail = newNode


    def isEm(self):
        if self.linked.head == None:
            return True
        else:
            return False

    def peek(self):
        if self.linked.head == None:
            return "there is no node"

        else:
            return self.linked.head

    def dequ(self):
        if self.isEm():
            return "there is no node"

        else:
            temNode = self.linked.head
            if self.linked.head == self.linked.tail:
                self.linked.head = None
                self.linked.tail = None

            else:
                self.linked.head = self.linked.head.next
            return temNode

    def dele(self):
        if self.isEm():
            return "there is no node"
        else:
            self.linked.head = None
            self.linked.tail = None

'''qu = QueU()
qu.enqq(1)
qu.enqq(2)
qu.enqq(3)
print(qu)
qu.dequ()
print(qu)
#print(qu.isEm())
qu.dele()
print(qu)'''
