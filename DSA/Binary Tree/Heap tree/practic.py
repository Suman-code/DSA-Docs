class HeapNode:
    def __init__(self, size):
        self.maxSize = size
        self.heapSize = 0
        self.list = (size+1)*[None]


def heapSize(rootNode):
    if not rootNode:
        return 0
    else:
        return rootNode.heapSize


def peek(rootNode):
    if not rootNode:
        return 
    else:
        return rootNode.list[1]
    

def levelOrderTrav(rootNode):
    if not rootNode:
        return
    else:
        for i in range(1 , rootNode.heapSize +1):
            print(rootNode.list[i])
        
    

def heapifyInsert(rootNode, index , heapType):
    parentIndex = int(index/2)
    if index <= 1:
        return
    if heapType == "Min":
        if rootNode.list[index] < rootNode.list[parentIndex]:
            tem = rootNode.list[index]
            rootNode.list[index] = rootNode.list[parentIndex]
            rootNode.list[parentIndex] = tem
        heapifyInsert(rootNode , parentIndex , heapType)

    
    elif heapType == "Max":
        if rootNode.list[index] > rootNode.list[parentIndex]:
            tem = rootNode.list[index]
            rootNode.list[index] = rootNode.list[parentIndex]
            rootNode.list[parentIndex] = tem
        heapifyInsert(rootNode , parentIndex , heapType)



def insertNode(rootNode , nodVal  , heapType):
    if rootNode.heapSize + 1 == rootNode.maxSize:
        return "the heap is full"
    else: 
        rootNode.list[rootNode.heapSize +1] = nodVal
        rootNode.heapSize += 1
        heapifyInsert(rootNode ,  rootNode.heapSize , heapType)


def heapifyExtrac(rootNode , index , heapType):
    leftNode = index * 2
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
            if rootNode.list[index] < rootNode.list[swapNode]:
                rootNode.list[index] = rootNode.list[swapNode]
                rootNode.list[swapNode] = tem
    heapifyExtrac(rootNode , swapNode , heapType)


def delNode(rootNode , heapType):
    if not rootNode:
        return
    else:
        delNod = rootNode.list[1]
        rootNode.list[1] = rootNode.list[rootNode.heapSize]
        rootNode.list[rootNode.heapSize] = None
        rootNode.heapSize -= 1
        heapifyExtrac(rootNode , 1 , heapType)
        return delNod



newHeap = HeapNode(5)
insertNode(newHeap , 5 , "Min")
insertNode(newHeap , 7 , "Min")
insertNode(newHeap , 6 , "Min")
insertNode(newHeap , 3 , "Min")
#levelOrderTrav(newHeap)
delNode(newHeap , "Min")
levelOrderTrav(newHeap)