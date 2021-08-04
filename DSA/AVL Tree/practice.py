
import linkedQue as que
class AvlTre:
    def __init__(self, data = None):
        self.data = data
        self.leftChild = None
        self.rightChild = None
        self.height = 1

def preOrderTav(rootNode):
    if not rootNode:
        return
    else: 
        print(rootNode.data)
        preOrderTav(rootNode.leftChild)
        preOrderTav(rootNode.rightChild)



def inOrderTav(rootNode):
    if not rootNode:
        return
    else: 
        
        preOrderTav(rootNode.leftChild)
        print(rootNode.data)
        preOrderTav(rootNode.rightChild)



def postOrderTav(rootNode):
    if not rootNode:
        return
    else: 
        
        preOrderTav(rootNode.leftChild)
       
        preOrderTav(rootNode.rightChild)
        print(rootNode.data)

def levOrderTav(rootNode):
    if not rootNode:
        return
    else:
        Que = que.QueU()
        Que.enqq(rootNode)
        while not(Que.isEm()):
            root = Que.dequ()
            print(root.value.data)
        if(root.value.leftChild is not None):
            Que.enqq(root.value.leftChild)
        if(root.value.rightChild is not None):
            Que.enqq(root.value.rightChild)

def searchNode(rootNode, nodVa):
    if val == rootNode.data:
        print("the not found")
    elif nodva < rootNode.data:
        if rootNode.leftChild.data == nodVa:
            print("Node found")
        else:
            searchNode(rootNode.leftChild , nodVa)
    else:
        if rootNode.rightChild.data == nodVa:
            print("node found")
        else:
            searchNode(rootNode.rightChild , nodVa)


def getHeight(rootNode):
    if not rootNode:
        return 0
    else:
        return rootNode.height

def blncNod(rootNode):
    if not rootNode:
        return 0
    else:
        return getHeight(rootNode.leftChild) - getHeight(rootNode.rightChild)

def rightRot(disBlnced):
    newRoot = disBlnced.leftChild
    disBlnced.leftChild = disBlnced.leftChild.rightChild
    newRoot.rightChild = disBlnced
    disBlnced.height = 1+ max(getHeight(disBlnced.leftChild) , getHeight(disBlnced.rightChild))
    newRoot.height = 1 + max(getHeight(newRoot.leftChild), getHeight(newRoot.rightChild))
    return newRoot


def leftRot(disBlnced):
    newRoot = disBlnced.rightChild
    disBlnced.leftChild = disBlnced.rightChild.leftChild
    newRoot.leftChild = disBlnced
    disBlnced.height = 1+ max(getHeight(disBlnced.leftChild) , getHeight(disBlnced.rightChild))
    newRoot.height = 1 + max(getHeight(newRoot.leftChild), getHeight(newRoot.rightChild))
    return newRoot

def inserted(rootNode, nodVal):
    if not rootNode:
        return AvlTre(nodVal)
    elif nodVal < rootNode.data:
        rootNode.leftChild = inserted(rootNode.leftChild , nodVal)
    else:
        rootNode.rightChild = inserted(rootNode.rightChild , nodVal)

    rootNode.height = 1 + max(getHeight(rootNode.leftChild) ,  getHeight(rootNode.rightChild))
    blc = blncNod(rootNode)
    if blc > 1 and nodVal < rootNode.leftChild.data:
        return rightRot(rootNode)
    if blc > 1 and nodVal > rootNode.leftChild.data:
        rootNode.leftChild = leftRot(rootNode.leftChild)
        return rightRot(rootNode)
    if blc < -1 and nodVal > rootNode.rightChild.data:
        return leftRot(rootNode)
    if blc < -1 and nodVal < rootNode.rightChild.data:
        rootNode.rightChild = rightRot(rootNode.rightChild)
        return leftRot(rootNode)

    return rootNode


newAv = AvlTre(30)
newAv = inserted(newAv , 5)
newAv = inserted(newAv , 10)

inOrderTav(newAv)
