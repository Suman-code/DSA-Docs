import linkedQue as queue

class Tree:
    def __init__(self , data):
        self.data = data
        self.leftNode = None
        self.rightNode = None

    
treeBT = Tree('Drinks')
leftNode = Tree('Hot')
rightNode = Tree('Cold')
Tea = Tree('Tea')
Cola = Tree('Cola')
Fanta = Tree('Fanta')
Cofee = Tree('Cofee')

leftNode.rightNode = Cofee
leftNode.leftNode = Tea
rightNode.leftNode = Cola
rightNode.rightNode = Fanta

treeBT.leftNode = leftNode
treeBT.rightNode = rightNode

#preorder travasal 

def preTrav(rootNode):
    if not rootNode:
        return
    print(rootNode.data)
    preTrav(rootNode.leftNode)
    preTrav(rootNode.rightNode)
#preTrav(treeBT)

#in order travsal

def inOrder(rootNode):
    if not rootNode:
        return
    inOrder(rootNode.leftNode)
    print(rootNode.data)
    inOrder(rootNode.rightNode)

#inOrder(treeBT)

#post travsal

def postOrder(rootNode):
    if not rootNode:
        return
    postOrder(rootNode.leftNode)
    postOrder(rootNode.rightNode)
    print(rootNode.data)

#level order travsal

def levelOrder(rootNode):
    if not rootNode:
        return
    else:
        custQ = queue.QueU()
        custQ.enqq(rootNode)
        while not(custQ.isEm()):
            root = custQ.dequ()
            print(root.value.data)
        
            if (root.value.leftNode is not None):
                custQ.enqq(root.value.leftNode)
            if(root.value.rightNode is not None):
                custQ.enqq(root.value.rightNode)




#searchnng a  node 
def search(rootNode , nodval):
    if not rootNode:
        return "there is no node"
    else:

        customQ = queue.QueU()
        customQ.enqq(rootNode)
        while not(customQ.isEm()):
            root = customQ.dequ()
            if root.value.data == nodval:
                return root.value.data
            if (root.value.leftNode is not None):
                customQ.enqq(root.value.leftNode)
            if (root.value.rightNode is not None):
                customQ.enqq(root.value.rightNode)

        return "not found"

#print(search(treeBT, 'Tea'))


#inserting node in tree 

def insertNod(rootNode, nod):
    if not rootNode:
        rootNode = newNode
    else:
        cusQue = queue.QueU()
        cusQue.enqq(rootNode)
        while not(cusQue.isEm()):
            root = cusQue.dequ()
            if (root.value.leftNode is not None):
                cusQue.enqq(root.value.leftNode)
            else:
                root.value.leftNode = newNode

                return " succescfull inserted"
            if (root.value.rightNode is not None):
                cusQue.enqq(root.value.rightNode)
            else:

                root.value.rightNode = newNode
                return "succesfull"
            
#newNode = Tree('susu')

#print(insertNod(treeBT, newNode))

#levelOrder(treeBT)

#delete the node from binary tree

def deepestNod(rootNode):
    if not rootNode:
        return "there is no Tree"
    else:
        cusQue = queue.QueU()
        cusQue.enqq(rootNode)

        while not(cusQue.isEm()):
            root = cusQue.dequ()
            if (root.value.leftNode is not None):
                cusQue.enqq(root.value.leftNode)
            if (root.value.rightNode is not None):
                cusQue.enqq(root.value.rightNode)

        deepestNode = root.value
        return deepestNode

        
def deletdeepNod(rootNode, dnod):
    if not rootNode:
        return "there is no tree"
    else:
        custQ = queue.QueU()
        custQ.enqq(rootNode)
        while not(custQ.isEm()):
            root = custQ.dequ()
            if root.value == dnod:
                root.value == None
            
            if root.value.leftNode:
                if root.value.leftNode is dnod:
                    root.value.leftNode == None
                    return
                else:
                    custQ.enqq(root.value.leftNode)

            if root.value.rightNode:
                if root.value.rightNode is dnod:
                    root.value.rightNode == None
                    return
                else:
                    custQ.enqq(root.value.rightNode)

   # delete node from tree                 
def deletNod(rootNode ,  dnode):
    if not rootNode:
        return "there is no node"
    else:
        coustQ = queue.QueU()
        coustQ.enqq(rootNode)
        while not(coustQ.isEm()):
            root = coustQ.dequ()
            if root.value.data == dnode:
                dnode = deepestNod(rootNode)
                root.value.data = dnode.data
                deletdeepNod(rootNode , dnode)
                return "the node deleted"
            if(root.value.leftNode is not None):
                coustQ.enqq(root.value.leftNode)
            if(root.value.rightNode is not None):
                coustQ.enqq(root.value.rightNode)
        return " the node not found"

deletNod(treeBT , "Tea")
levelOrder(treeBT)






#newNode = deepestNod(treeBT)
#deletdeepNod(treeBT , newNode)
#levelOrder(treeBT)

#delete entire binary tree
def deledeBT(nood):
    noood.data = None
    nood.leftNode = None
    nood.rightNode = None
    return "deleteed the binary tree"
