# creating stck with linked list
class Node:
    def __init__(self,value=None):
        self.value = value
        self.next = None
    
class Linkedlist:
    def __init__(self):
        self.head = None

    def __iter__(self):
        tav = self.head
        while tav:
            yield tav
            tav = tav.next

class Stack:
    def __init__(self):
        self.linkedlist = Linkedlist()

    def __str__(self):
        
        values = [str(x.value) for x in self.linkedlist]
        return '\n'.join(values)

# chekcing the empty
    def isEmpty(self):
        if self.linkedlist.head == None:
            return True

        else:
            False
# push in stack by linked list

    def pushList(self, value):
        newNode = Node(value)
        newNode.next = self.linkedlist.head
        self.linkedlist.head = newNode


# pop form linked list
    def pop(self):
        if self.isEmpty():
            return "there is no no node"

        else:
            nodeVal = self.linkedlist.head.value
            self.linkedlist.head = self.linkedlist.head.next
            return nodeVal

# Peek function
    def peekk():
        if self.iseEmpty():
            return "there is no node"
        else:
            nodeVal = self.linkedlist.head.value
            return nodeVal
    
# delete the stack linked list
    def dele():
        self.linkedlist.head = None



stck = Stack()
stck.pushList(1)
stck.pushList(2)
stck.pushList(3)
print(stck)
#print(stck.isEmpty())
stck.pop()
print('_____')
print(stck)


