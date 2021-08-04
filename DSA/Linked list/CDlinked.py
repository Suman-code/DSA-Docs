# circular doubly  linked list
class Node():
    def __init__(self, value= None):
        self.value = value
        self.prev = None
        self.next = None
class cdList():
    def init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
            if node ==  self.tail.next:
                break
            
    
    #create a circular doubly linked list
    def creat(self, value):
        newNode = Node(value)
        self.head =  newNode
        self.tail = newNode
        newNode.next = newNode
        newNode.tail = newNode
        return "Your node is ready"
# insertion a noide in circular doubly loinked list
    def inser(self, value, location):
        if self.head is None:
            return "there is no node"
        else:
            newNode = Node(value)
            if location == 0:
    
                newNode.next = self.head
                newNode.prev = self.tail

                self.head.prev = newNode
                self.head = newNode
                self.tail.next = newNode

            elif location == 1:
                    newNode.next = self.head
                    newNode.prev = self.tail
                    self.head.prev = newNode
                    self.tail.next = newNode
                    self.tail = newNode
            else:
                temNode = self.head
                i = 0
                while i < location - 1:
                    temNode = temNode.next
                    i += 1
                newNode.next = temNode.next
                newNode.prev = temNode
                newNode.next.prev = newNode
                temNode.next = newNode
            return "the node is inserted"
    
    #travesal the doubly circuler linked list
    def trav(self):
        if self.head is None:
            return "There si no list"
        else:
            nod = self.head
            while nod:
                print(nod.value)
                if nod == self.tail:
                    break
                nod =  nod.next
    #reverse the circular linked list
    def reTrav(self):
        rev = self.tail
        while rev:
            print(rev.value)
            if rev == self.head:
                break
            rev = rev.prev
    #searching a node element in circular doubly linked list

    def searchEle(self, value):
        sea = self.head
        while sea:
            if sea.value == value:
                return sea.value 
            if sea == self.tail:
                return "the value is not found"
                    
            sea = sea.next
    # deleting the node form circular diubly  linked list

    def dete(self,location):
        if self.head is None:
            print("There is no node")
        else:
            if location == 0:

                if self.head == self.tail:
                    self.prev = None
                    self.next = None
                    self.head = None
                    self.tail = None
                else:
        
                    self.head = self.head.next
                    self.head.prev = self.tail
                    self.tail.next = self.head
            elif location == 1:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                    self.prev = None
                    self.next = None
                else:
                    self.tail = self.tail.prev
                    self.tail.next= self.head
                    self.tail.prev = self.tail
            else:
                de = self.head
                ind = 0
                while de < loca -1:
                    de = de.next
                    ind += 1
                de.next = de.next.next
                de.next.prev = de
            print('the node deleted')
    def deletEtr(self):
        if self.head is None:
            return "there is no node"
        else:
            self.tail.next = None
            had = self.head
            while had:
                had.prev == None
                had = had.next
            self.head = None
            self.tail = None
            print('the node has been deleted')


cirDlist = cdList()
cirDlist.creat(0)
print([node.value for node in cirDlist])
cirDlist.inser(1, 0)
cirDlist.inser(2, 1)
cirDlist.inser(3, 3)
cirDlist.inser(4, 2)
print([node.value for node in cirDlist])
#cirDlist.reTrav()
#print(cirDlist.searchEle('silpi'))
#cirDlist.dete(1)
cirDlist.deletEtr()

print([node.value for node in cirDlist])