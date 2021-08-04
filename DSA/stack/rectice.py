#creating stck with linked list

class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
    
    def __iter__(self):
        nod = self.head
        while nod:
            yield nod
            nod = nod.next

class Stack:
    def __init__(self):
        self.linked = LinkedList()

    def __str__(self):
        
        values = [str(x.value) for x in self.linked]
        return '\n'.join(values)
        
    def isEmpty(self):
        if self.linked.head == None:
            return True

        else:
            False
    
    def pushh(self, value):
        newNode = Node(value)
        newNode.next = self.linked.head
        self.linked.head = newNode

    def popp(self):
        if self.linked.head == None:
            return "there is no node"
        else:
            nodVal = self.linked.head.value
            self.linked.head = self.linked.head.next.value
            return nodVal



stc = Stack()
stc.pushh(1)
stc.pushh(2)
stc.pushh(3)

print(stc)
#print(stc.isEmpty())

stc.popp()
print(stc)

