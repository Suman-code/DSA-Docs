import linkedQue as quee

class Tree:
    def __init__(self, data = None):
        self.data = data
        self.leftChild = None
        self.rightChild = None

newTre = Tree("Drinks")
leftChild = Tree("Hot")
rightChild = Tree("Cold")
Tea = Tree("Tea")
Cofee = Tree("cofee")
Cola = Tree("cola")

newTre.leftChild = leftChild
newTre.rightChild = rightChild
leftChild.rightChild = Tea
leftChild.leftChild = Cofee
rightChild.leftChild = Cola


'''def insertTre(rootNode, Nod):
    queE = quee.QueU()
    queE.enqq(rootNode)
    while not(queE.isEm()):
        root = queE.dequ()
        print(root.value.data)

        if(root.value.leftChild is not None ):
            queE.enqq(root.value.leftChild)
        if(root.value.rightChild is not None):
            queE.enqq(root.value.rightChild)'''

def preOrderTrav(rootNode):
    if not rootNode:
        return "there is no node"
    else:
        print(rootNode.data)
        preOrderTrav(rootNode.leftChild)
        preOrderTrav(rootNode.rightChild)
        
    
#preOrderTrav(newTre)

def inorderTrv(rootNode):
    if not rootNode:
        return
    else:
        inorderTrv(rootNode.leftChild)
        print(rootNode.data)
        inorderTrv(rootNode.rightChild)

#inorderTrv(newTre)

def posOrderTrav(rootNode):
    if not rootNode:
        return
    else:
        posOrderTrav(rootNode.leftChild)
        posOrderTrav(rootNode.rightChild)
        print(rootNode.data)


#posOrderTrav(newTre)

def levlOrderTrav(rootNode):
    if not rootNode:
        return
    else:
        queE = quee.QueU()
        queE.enqq(rootNode)
        while not(queE.isEm()):
            root = queE.dequ()
            print(root.value.data)

            if(root.value.leftChild is not None ):
                queE.enqq(root.value.leftChild)
            if(root.value.rightChild is not None):
                queE.enqq(root.value.rightChild)

#levlOrderTrav(newTre)

def serchNod(rootNode , value):
    queE = quee.QueU()
    queE.enqq(rootNode)
    while not(queE.isEm()):
        root = queE.dequ()
        if root.value.data == value:
            return root.value.data
        else:
            if(root.value.leftChild is not None):
                queE.enqq(root.value.leftChild)
            if(root.value.rightChild is not None):
                queE.enqq(root.value.rightChild)

    return "not found"

#print(serchNod(newTre, "Tea"))

def insertNod(rootNode, val):
    if not rootNode:
        rootNode = val
    else:
        queE = quee.QueU()
        queE.enqq(rootNode)
        while not(queE.isEm()):
            root = queE.dequ()
            if root.value.leftChild is not None:
                queE.enqq(root.value.leftChild)
            else:
                root.value.leftChild = val
                return "the nde succesfull inseted"

            if root.value.rightChild is not None:
                queE.enqq(root.value.rightChild)
                

            else:
                root.value.rightChild = val
                return "inserted the node succesfully"



#val = Tree("Fanta")
#va = Tree("Pepsi")
#insertNod(newTre , val)
#insertNod(newTre , va)

def deleNod(rootNode , valu):
    if not rootNode:
        return
    else:
        queE = quee.QueU()
        queE.enqq(rootNode)
        while not(queE.isEm()):
            root = queE.dequ()
            if root.value.data == valu:
                

        
