# creating Circular queue

class CirQu():
    def __init__(self, maxSiz):
        self.items = maxSiz * [None]
        self.maxSiz = maxSiz
        self.front = -1
        self.rear = -1
    
    def __str__(self):
        values = [str(x) for x in self.items]
        return ' '.join(values)

    def isFull(self):
        if self.rear + 1 == self.front:
            return True
        elif self.front == 0 and self.rear + 1  == self.maxSiz:
            return True
        else:
            False
     
    def isEmpty(self):
        if self.rear == -1:
            return True
        else:
            False
    
    def enQue(self,value):
        if self.isFull():
            return "there is no data"
        else:
            if self.rear +1 == self.maxSiz:
                self.rear = 0
            else:
                self.rear += 1
                if self.front == - 1:
                    self.front = 0
            self.items[self.rear] = value
            return "the element enterted"

    def deQue(self):
        if self.isEmpty():
            return "there is no node"
        else:
            firstEle = self.items[self.front]
            start = self.front
            if self.front == self.rear:
                self.front = -1
                self.rear = -1
            elif self.front +1 == self.maxSiz:
                self.front = 0
            else:
                self.front += 1
            self.items[start] = None
            return firstEle
    def peek(self):
        if self.isEmpty():
            return "there is no list"
        else:
            return self.items[self.front]






cirq = CirQu(3)
#print(cirq.isFull())
cirq.enQue(1)
cirq.enQue(2)
cirq.enQue(3)
#print(cirq)
##print(cirq.isFull())
#print(cirq)
cirq.deQue()
#print(cirq)

print(cirq.peek())




