
#creating heap on list

class Heaplist:
    def __init__(self, size):
        self.list = (size+1) * [None]
        self.heapSize = 0
        self.maxSiz = size + 1


def heapsize(rootNode):
    if not rootNode:
        return 
    else:
        return rootNode.heapSize

def peek(rootNode):
    if not rootNode:
        return
    else:
        rootNode.list[1]


def levelOrderTrav(rootNode):
    if not rootNode:
        return
    else:
        for i in range(1 , rootNode.heapSize +1):
            print(rootNode.list[i])


def heapifyInsert(rootNode ,  index , heapType):
    parentIndex = int(index/2)
    if index <= 1:
        return
    if heapType == "Min":
        if rootNode.list[index] < rootNode.list[parentIndex]:
            tem = rootNode.list[index]
            rootNode.list[index] = rootNode.list[parentIndex]
            rootNode.list[parentIndex] = tem
        heapifyInsert(rootNode, parentIndex ,  heapType)

    elif heapType == "Max":
        if rootNode.list[index] > rootNode.list[parentIndex]:
            tem = rootNode.list[index]
            
            rootNode.list[index] = rootNode.list[parentIndex]
            rootNode.list[parentIndex] = tem
        heapifyInsert(rootNode , parentIndex , heapType)

def inserttNode(rootNode , nodVal , heapType):
    if rootNode.heapSize +1 == rootNode.maxSiz:
        return "the heap size is full"

    rootNode.list[rootNode.heapSize +1] = nodVal
    rootNode.heapSize += 1
    heapifyInsert(rootNode , rootNode.heapSize , heapType)
    return "the node has been added"




def heapifyExtrac(rootNode, index, heapType):
    leftNode = index *2
    rightNode = index *2 +1
    swapNode = 0
    if rootNode.heapSize < leftNode:
        return
    elif rootNode.heapSize == leftNode:
        if heapType == "Min":
            if rootNode.list[index] > rootNode.list[leftNode]:
                tem = rootNode.list[index]
                rootNode.list[index] = rootNode.list[leftNode]
                rootNode.list[leftNode] = tem
            return
        else:
            if rootNode.list[index] < rootNode.list[leftNode]:
                tem = rootNode.list[index]
                rootNode.list[index] = rootNode.list[leftNode]
                rootNode.list[leftNode] = tem
            return

    else:
        if heapType == "Min":
            if rootNode.list[leftNode] < rootNode.list[rightNode]:
                swapNode = leftNode
            else: 
                swapNode = rightNode

            if rootNode.list[index] > rootNode.list[swapNode]:
                tem = rootNode.list[index]
                rootNode.list[index] = rootNode.list[swapNode]
                rootNode.list[swapNode] = tem

        else:
            if rootNode.list[leftNode] > rootNode.list[rightNode]:
                swapNode = leftNode
            else:
                swapNode = rightNode
            if rootNode.list[index] < rootNode.list[swapNode]:
                tem = rootNode.list[index]
                rootNode.list[index] = rootNode.list[swapNode]
                rootNode.list[swapNode] = tem

    heapifyExtrac(rootNode , swapNode, heapType)

def deleNode(rootNode , heapType):
    if heapsize == 0:
        return
    else:
        deleNod = rootNode.list[1]
        rootNode.list[1] = rootNode.list[rootNode.heapSize]
        rootNode.list[rootNode.heapSize] = None
        rootNode.heapSize -= 1
        heapifyExtrac(rootNode , 1 , heapType)
        return deleNod

def deleteEntore(rootNode):
    rootNode.list = None
    


newHeap = Heaplist(5)
inserttNode(newHeap ,  10 , "Min")
inserttNode(newHeap ,  15 , "Min")
inserttNode(newHeap ,  18 , "Min")
inserttNode(newHeap ,  2 , "Min")
inserttNode(newHeap ,  1 , "Min")
levelOrderTrav(newHeap)
#deleNode(newHeap , "Min")
#levelOrderTrav(newHeap)



