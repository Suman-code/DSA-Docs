import linkedQue as que

#creating AVL tree
class Avltree:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None
        self.height = 1



#preOrder Travsal

def preOrderTav(rootNode):
    if not rootNode:
        return
    
    else:
        print(rootNode.data)
        preOrderTav(rootNode.leftChild)
        preOrderTav(rootNode.rightChild)

    return "nood inserted"

def inOrderTra(rootNode):
    if not rootNode:
        return
    else:
        inOrderTra(rootNode.leftChild)
        print(rootNode.data)
        inOrderTra(rootNode.rightChild)
    return "inserted"
def postOrderTrav(rootNode):
    if not rootNode:
        return
    else:
        postOrderTrav(rootNode.leftChild)
        postOrderTrav(rootNode.rightChild)
        print(rootNode.data)



def levOrderTav(rootNode):
    if not rootNode:
        return
    else:
        coustQ = que.QueU()
        coustQ.enqq(rootNode)
        while not(coustQ.isEm()):
            root = coustQ.dequ()
            print(root.value.data)

            if (root.value.leftChild is not None):
                coustQ.enqq(root.value.leftChild)
            if (root.value.rightChild is not None):
                coustQ.enqq(root.value.rightChild)

def searchNod(rootNode , nodVal):
    if nodVal == rootNode.data:
        return "the nide found"

    elif nodVal < rootNode.data:
        if rootNode.leftChild.data == nodVal:
            print ("the Node found")
        else:
            searchNod(rootNode.leftChild, nodVal)
    else:
        
        if rootNode.rightChild.data == nodVal:
            print("the node is found")
        else:
            searchNod(rootNode.rightChild , nodVal)


def getHeight(rootNode):
    if not rootNode:
        return 0
    else:
        return rootNode.height

def rightRotate(disBlnNod):
    newRoot = disBlnNod.leftChild
    disBlnNod.leftChild = disBlnNod.leftChild.rightChild
    newRoot.rightChild = disBlnNod
    disBlnNod.height = 1 + max(getHeight(disBlnNod.leftChild) , getBlacn(disBlnNod.rightChild))
    newRoot.height = 1 + max(getHeight(newRoot.leftChild) , getHeight(newRoot.rightChild))
    return newRoot 
        

def leftRotete(disBlnNod):
    newRoot = disBlnNod.rightChild
    disBlnNod.rightChild = disBlnNod.rightChild.leftChild
    newRoot.leftChild = disBlnNod
    disBlnNod.height = 1 + max(getHeight(disBlnNod.leftChild) , getHeight(disBlnNod.rightChild))
    newRoot.height = 1 + max(getHeight(newRoot.leftChild) , getHeight(newRoot.rightChild))
    return newRoot


def getBlacn(rootNode):
    if not rootNode:
        return 0
    else:
        return getHeight(rootNode.leftChild) - getHeight(rootNode.rightChild)


def insertNod(rootNode ,nodVal):
    if not rootNode:
        return Avltree(nodVal)
    
    elif nodVal < rootNode.data:
        rootNode.leftChild = insertNod(rootNode.leftChild , nodVal)
    else:
        rootNode.rightChild = insertNod(rootNode.rightChild , nodVal)

    
    rootNode.height = 1 + max (getHeight(rootNode.leftChild), getHeight(rootNode.rightChild))
    blance = getBlacn(rootNode)
    if blance > 1 and nodVal < rootNode.leftChild.data:
        return rightRotate(rootNode)
    if blance > 1 and nodVal > rootNode.leftChild.data:
        rootNode.leftChild = leftRotete(rootNode.leftChild)
        return rightRotate(rootNode)

    if blance < -1 and nodVal > rootNode.rightChild.data:
        return leftRotete(rootNode)
    if blance < - 1 and nodVal < rootNode.rightChild.data:
        rootNode.rightChild = rightRotate(rootNode.rightChild)
        return leftRotete(rootNode)

    return rootNode




def minNod(rootNode):
    if rootNode is None or rootNode.leftChild is None:
        return rootNode
    else:
        return minNod(rootNode.leftChild)

def deleNod(rootNode , nod):
    if not rootNode:
        return rootNode

    elif nod < rootNode.data:
        rootNode.leftChild = deleNod(rootNode.leftChild ,  nod)
    elif nod > rootNode.data:
        rootNode.rightChild = deleNod(rootNode.rightChild , nod)

    else:
        if rootNode.leftChild is None:
            tem = rootNode.rightChild
            rootNode = None
            return tem
        elif rootNode.rightChild is None:
            tem = rootNode.leftChild
            rootNode = None
            return tem
        tem = minNod(rootNode.rightChild)
        rootNode.data = tem.data
        rootNode.rightChild = deleNod(rootNode.rightChild , tem.data)

        blc = getBlacn(rootNode)
        if blc  > 1 and getBlacn(rootNode.leftChild) >= 0:
            return rightRotate(rootNode)
        if blc < -1 and getBlacn(rootNode.rightChild) >= 0:
            return leftRotete(rootNode)
        if blc > 1 and getBlacn(rootNode.leftChild) < 0:
            rootNode.leftChild = leftRotete(rootNode.leftChild)
            return rightRotate (rootNode)
        if blc < -1 and getBlacn(rootNode.rightChild) > 0:
            rootNode.rightChild = rightRotate(rootNode.rightChild)
            return leftChild(rootNode)
        return rootNode

def deleEntire(rootNode):
    rootNode = None
    rootNode.leftChild = None
    rootNode.rightChild = None
    return "deleted"


newAVL = Avltree(50)
newAVL = insertNod(newAVL , 30)
newAVL = insertNod(newAVL , 60)

newAVL = insertNod(newAVL , 40)
newAVL = insertNod(newAVL , 10)
newAVL = insertNod(newAVL , 5)
newAVL = insertNod(newAVL , 4)

levOrderTav(newAVL)
deleNod(newAVL ,  5)
print("aaaaaaaa")

levOrderTav(newAVL)




    
        

    
