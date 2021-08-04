# circular single linked list
class Node():
    def __init__(self, value=None):
        self.value = value
        self.next = None

class CircularSLL():
    def __init__(self):
        self.head = None
        self.tail = None
    
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
            if node.next == self.head:
                break

    #cirvular Linked list
    def creat(self, value):
        newNode = Node(value)
        newNode.next = newNode
        self.head = newNode
        self.tail = newNode
        return "Node has been created"

    def inser(self, value, location):
        if self.head is None:
            return 'there si no Linked list'
        
        else:
            neNode = Node(value)
            if location == 0:
                neNode.next = self.head
                self.head = neNode
                self.tail.next = neNode
            elif location == 1:
                #neNode = Node(value)
                
                neNode.next = self.tail.next
                self.tail.next = neNode
                self.tail = neNode
                
            else:
                #neNode = Node(value)
                temNod = self.head
                i = 0

                while i < location - 1:
                    temNod = temNod.next
                    i += 1
                nextNod = temNod.next
                temNod.next = neNode
                neNode.next = nextNod
            return 'Node has inserted'
    # traverse function

    def trav(self):
        if self.head is None:
            return "There is no linked list"
        else:
            tav = self.head
            while tav:
                print(tav.value)
                tav = tav.next
                if tav == self.tail.next:
                    break
    #searching Node
    def search(self, valu):
        if self.head is None:
            return "there is no node"
        else:
            seaNode = self.head
            while seaNode:
                if seaNode.value == valu:
                    return seaNode.value
                seaNode = seaNode.next
                if seaNode == self.tail.next:
                    return "there is no nade value"

    # deleting node
    def dele(self, loca):
        if self.head is None:
            return "There is no node"
        else:
            if loca == 0:
                if self.head == self.tail:
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
                    self.tail.next = self.head
            elif loca == 1:
                if self.head == self.tail:
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else:
                    nod = self.head
                    while nod is not None:
                        if nod.next == self.tail:
                            break
                        nod = nod.next
                    nod.next = self.head
                    self.tail = nod

            else:
                temNode = self.head
                i = 0
                while i < loca - 1:
                    temNode = temNode.next
                    i += 1
                nextNode = temNode.next
                temNode.next = nextNode.next
     #delete entire linked list
    def deleEn(self):
        self.head = None
        
        self.tail.next = None
        self.tail = None
         


            



cList = CircularSLL()
print(cList.creat(1))

cList.inser(2,1)
cList.inser(3,1)
cList.inser(4,1)
cList.inser(5,1)

print([node.value for node in cList])

#cList.trav()
#print(cList.search(1))

#cList.dele(1)
cList.deleEn()

print([node.value for node in cList])