from array import *
import numpy as np

arr = np.array([1,2,3,5,6,7,8,9,10])
#print(arr)
'''def check(arre):
    for i in range(len(arre)):
        for j in range(len(arre[0])):

            print(arre[i][j])

print(check(new))

def search(arre, col):
    for i in range(len(arre)):
        for j in range(len(arre[0])):
            if arre[i][j] == col:
                return ''

print(search(new,12))

dt = np.delete(new, 1, axis = 1)

print(dt)

def check(list, n):
    su = 10*11/2
    su1 = sum(arr)
    print(su-su1)

check (arr , 10)

li = [1,2,4,5,6,3,10]

def check(ar , su):
    for i in range(len(ar)):
        for k in range(i+1,len(ar)):
            if (ar[i]+ar[k]) == su:
                print(ar[i], ar[k])
check(li,6)

def ser(ar, nu):
    for i in range(len(ar)):
        if ar[i] == nu:
            print(i)

ser(arr,10)
la = [2,4,61,5,45,34,67,65,13,17,65,12,21,3,4,31]
lii = []

def sear(ar):
    for i in range(len(ar)):
        maxv = 0
        for j in range(i+1, len(ar)):
            if ar[i] * ar[j] > maxv:
                maxv = ar[i] * ar[j]
                
                print(maxv)
                
sear(la)

lis = [1,2,3,4,5,6,7,8,9,10,1]

fi = []

def check(li):
    s = []
    for i in range(len(li)):
        if i in s:
            print(i)
            return False
        else:
        
            s.append(i)
        return True

        
print(check(lis))'''

det = {'name' : 'suman' , 'age' : 28, 'home':'assam', 'age' : 28, 'educ' : 'BA'}

'''def check(dic,value):
    for i in dic:
        if dic[i] == value:
            return i, value

print(check(det,28))

del det['name']
print(det)

tu = ('a' , 'b' , 'c' , 'd' , 'e')
def check(te, va):
    for i in te:
        if i == va:
            return te.index(i)

print(check(tu, 'd'))'''

# singlylined list


'''class Node():
    def __init__(self, value=None):
        self.value = value
        self.next = None

class Slinklist:
    def __init__(self):
        self.head = None
        self.tail = None
    

    #insert node

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
        
    def thenod(self, value, location):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            if location == 0:
                newNode.next = self.head
                self.head = newNode

            elif location == 1:

                newNode.next == None
                self.tail.next = newNode

            else:
                tem = self.head
                index = 0
                while index < location - 1:
                    tem = tem.next
                    index += 1
                temNext = tem.next
                tem.next = newNode
                newNode.next = temNext

    def travase(self):
        if self.head is None:
            print('There is no Linked list')

        else:
            node = self.head
            while node is not None:
                print(node.value)
                node  = node.next
    #searching a item
    def search(self, val):
        if self.head is None:
            print('Thiere no linked list')
        else:
            nd = self.head
            while nd is not None:
                if nd.value == val:
                    return nd.value
                nd = nd.next

            return "The mactch does not found"'''

#delete nod from list
    def dele(self, loca):
        if self.head in None:
            print('no node available')
        else:
            if loca == 0:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
            elif loca == 1:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    nod = self.head
                    while nod is not None:
                        if nod.next == self.tail:
                            brake
                    nod = nod.next
                    nod.next = None
                    self.tail = nod
            else:
                temNod = self.head
                i = 0
                while i < loca -1:
                    temNod = temNod.next
                    i += 1
                nextTem = temNod.next
                temNod.next = nextTem.next


singleLink = Slinklist()
singleLink.thenod(2,1)
singleLink.thenod(5,0)
singleLink.thenod(1,3)
singleLink.thenod(3,2)
print([node.value for node in singleLink])
singleLink.travase()
#print(singleLink.search(3))






    
