#double linked list
class Node():
    def __init__(self, value=None):
        self.value = value
        self.prev = None
        self.next = None

class Dlinkedlist():
    def __init__(self):
        self.head = None
        self.tail = None
    

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

#creating empty node
    def creat(self, value):
        newNode = Node(value)
        newNode.prev = None
        newNode.next = None
        self.head = newNode
        self.tail = newNode
        return "Created your double linked list"

    def inser(self, value, location):
        if self.head == None:
            return "there is no such linked list"
        else:
            newNod = Node(value)
            if location == 0:
                newNod.prev = None
                newNod.next = self.head
                self.head.prev = newNod
                self.head = newNod
            elif location == 1:
                newNod.next = None
                newNod.prev = self.tail
                self.tail.next = newNod
                self.tail = newNod

            else:
                temNod = self.head
                i = 0
                while i < location - 1:
                    temNod = temNod.next
                    i += 1
                newNod.next = temNod.next
                newNod.prev = temNod
                newNod.next.prev = newNod
                temNod.next = newNod

     #traversal the doubly linked list
    def trave(self):
        if self.head is None:
            return "there si not list"
        else:
            tav = self.head
            while tav is not None:
                print(tav.value)
                tav = tav.next
     # Reverse Traversal the doubly linked list

    def re_trav(self):
        trav = self.tail
        while trav is not None:
            print(trav.value)
            trav = trav.prev

 #searching element in doubly loinked list 
    def searc(self,value):
        if self.head is None:
            return "there is no linked list"
        else:
            val = self.head
            while val:
                if val.value == value:
                    return val.value
                val = val.next
            return "your value is here"

    #deleting elements form doublye linked  list
    def dele(self, location):
        if self.head is None:
            return "there is no list"
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
                    self.head.prev = None
            elif location == 1:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.tail = self.tail.prev
                    self.tail.next = None
            els
                teNod = self.head
                index = 0
                while index < location -1:
                    teNode = teNod.next
                    index += 1
                teNod.next = teNod.next.next
                teNod.next.prev = teNod
            print('The element deleted')

    #delete entire doubly linked list
    def doubleDel(self):
        if self.head is None:
            return "there is no element"
        else:
            dele = self.head
            while dele:
                dele.prev = None
                dele = dele.next
            self.head = None
            self.tail = None
        print("your double linked list deleted")


    
    
dlinkL = Dlinkedlist()
dlinkL.creat(5)
print([node.value for node in dlinkL])
dlinkL.inser(6, 0)
dlinkL.inser(7, 1)
dlinkL.inser(8, 2)
dlinkL.inser(9, 1)
print([node.value for node in dlinkL])
#dlinkL.trave()
#dlinkL.re_trav()
#print(dlinkL.searc(7))
#dlinkL.dele(1)
dlinkL.doubleDel()
print([node.value for node in dlinkL])



