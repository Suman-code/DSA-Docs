# creating binary tree wiht python list
class ListTree:
    def __init__(self, size):
        self.coustList = size * [None]
        self.maxSiz = size
        self.lastusedindex = 0

#inserting the niode

    def insert(self , value):
        if self.lastusedindex +1 == self.maxSiz:
            return "the list size is full"
        else:
            self.coustList[self.lastusedindex +1] = value
            self.lastusedindex += 1
        return " the node inserted"

# searching for a node

    def searchNode(self, node):
        for i in range(len(self.coustList)):
            if self.coustList[i] == node:
                return i
        return  "not found"

#preOrder  Travasal

    def preOrderTrav(self, index):
        if index > self.lastusedindex:
            return
        else:
            print(self.coustList[index])
            self.preOrderTrav(index*2)
            self.preOrderTrav(index * 2 + 1)

    
    #Inorder Travsal

    def inOrderTrav(self ,  index):
        if index > self.lastusedindex:
            return
        else:
            self.inOrderTrav(index *2)
            print(self.coustList[index])
            self.inOrderTrav(index * 2+1)

# post order travasal

    def postOrderTrav(self, index):
        if index > self.lastusedindex:
            return
        else:
            self.postOrderTrav(index*2)
            self.postOrderTrav(index * 2+1)
            print(self.coustList[index])

#levelOrdertrav

    def levelOrderTrav(self, index):
        for i in range(index, self.lastusedindex+1):
            print(self.coustList[i])


    #delet node from list
    def deleNod(self, value):
        if self.lastusedindex == 0:
            return "there si no node"
        else:
            for i in range(1 , self.lastusedindex +1):
                if self.coustList[i] == value:
                    self.coustList[i] = self.coustList[self.lastusedindex]
                    self.coustList[self.lastusedindex] == None
                    self.lastusedindex -= 1

        
#delete enter list

    def enterList(self):
        self.coustList = None

        return "the list has been deleted"




newBT = ListTree(8)
newBT.insert('Drinks')
newBT.insert('Hot')
newBT.insert('Cold')
newBT.insert('Tea')
newBT.insert('Coffee')
(newBT.searchNode("Tea"))
#newBT.preOrderTrav(1)
#newBT.inOrderTrav(3)
#newBT.postOrderTrav(1)
#newBT.levelOrderTrav(1)
#newBT.deleNod("Cold")
#newBT.levelOrderTrav(1)
