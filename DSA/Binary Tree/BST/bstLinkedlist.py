import linkedQue as que


# create binary search tree

class Bstree:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None


#inserting a node

def insertNod(rootNode , nodValu):
    if rootNode.data == None:
        rootNode.data = nodValu

    elif nodValu <= rootNode.data:
        if rootNode.leftChild is None:
            rootNode.leftChild = Bstree(nodValu)
        else:
            insertNod(rootNode.leftChild , nodValu)
    else:
        if rootNode.rightChild is None:
            rootNode.rightChild = Bstree(nodValu)
        else:
            insertNod(rootNode.rightChild , nodValu)

    return "the node has been inserted"
    
#pre order travasal

def preOrderTrav(rootNode):
    if not rootNode:
        return
    else:
        print(rootNode.data)
        preOrderTrav(rootNode.leftChild)
        preOrderTrav(rootNode.rightChild)

# inorder Travasal

def inOrderTrav(rootNode):
    if not rootNode:
        return
    else:
        inOrderTrav(rootNode.leftChild)
        print(rootNode.data)
        inOrderTrav(rootNode.rightChild)
# post order travsal

def postOrderTav(rootNode):
    if not rootNode:
        return
    else:
        postOrderTav(rootNode.leftChild)
        postOrderTav(rootNode.rightChild)
        print(rootNode.data)
    return "travasal done"



#level order travasal of binary search tree

def levOrderTrav(rootNode):
    if not rootNode:
        return
    else:
        coustomQ = que.QueU()
        coustomQ.enqq(rootNode)
        while not(coustomQ.isEm()):
            root = coustomQ.dequ()
            print(root.value.data)
            if root.value.leftChild is not None:
                coustomQ.enqq(root.value.leftChild)

            if root.value.rightChild is not None:
                coustomQ.enqq(root.value.rightChild)
        return "node inserted"
        

#searching a node

def searchNod(rootNode , val):
    if rootNode.data == val:
        print("found the node")

    elif val < rootNode.data:
        if rootNode.leftChild.data == val:
            print("the node found")
        else:
            searchNod(rootNode.leftChild, val)
    
    else:
        if rootNode.rightChild.data == val:
            print("found the node")
        else: 
            searchNod(rootNode.rightChild, val)
        
        
#deleting the node from BST

#minimum value

def minimumVal(bsTr):
    current = bsTr
    while(current.leftChild is not None):
        current = current.leftChild
    return current

def delNode(rootNode, nodValue):
    if rootNode is None:
        return rootNode

    if nodValue < rootNode.data:
        rootNode.leftChild = delNode(rootNode.leftChild , nodValue)

    elif nodValue > rootNode.data:
        rootNode.rightChild = delNode(rootNode.rightChild , nodValue)
    else:
        if rootNode.leftChild is None:
            tem = rootNode.rightChild
            rootNode = None
            return tem
        if rootNode.rightChild is None:
            tem = rootNode.leftChild
            rootNode = None
            return tem

        temNod = minimumVal(rootNode.rightChild)
        rootNode.data = temNod.data
        rootNode.rightChild = delNode(rootNode.rightChild , temNod.data)
    return rootNode
 

    

newBST = Bstree(None)
insertNod(newBST , 50)
insertNod(newBST , 40)
insertNod(newBST , 60)
insertNod(newBST , 80)
insertNod(newBST , 85)
insertNod(newBST , 90)
insertNod(newBST , 30)
insertNod(newBST , 35)
insertNod(newBST , 45)
#preOrderTrav(newBST)
#inOrderTrav(newBST)
#postOrderTav(newBST)
#levOrderTrav(newBST)
#searchNod(newBST , 80)
delNode(newBST, 85)
levOrderTrav(newBST)
    