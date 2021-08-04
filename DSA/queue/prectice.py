class CirQue:
    def __init__(self, maxSize):
        self.items = maxSize * [None]
        self.maxSize = maxSize
        self.front = -1
        self.rear = -1

    def __str__(self):
        values = [str(x) for x in self.items]
        return ' '.join(values)

    def isFull(self):
        if self.rear + 1 == self.front:
            return True
        elif self.front == 0 and self.rear +1 == self.maxSize:
            return True
        else:
            False

    def isEmpty(self):
        if self.rear == -1:
            return True
        else:
            False
    
    def enQuee(self, value):
        if self.isFull():
            return "there is space for limst"

        else:
            if self.rear + 1 == self.maxSize:
                self.rear = 0
            else:
                self.rear += 1
                if self.front == -1:
                    self.front = 0
            
            self.items[self.rear] = value
            return "the element enterted"

    def dequee(self):
        if self.isEmpty():
            return " there is no list element"
            
        else:
            firstEle = self.items[self.front]
            start = self.front
            if self.front == self.rear:
                self.front = -1
                self.rear = -1
            elif self.front +1 == self.maxSize:
                self.front = 0

            else:
                self.front += 1
            self.items[start] = None
            return firstEle

    def peekk(self):
        if self.isEmpty():
            return "there is no item"
        else:
            return self.items[self.front]


circu = CirQue(3)
circu.enQuee(1)
circu.enQuee(2)
circu.dequee()
print(circu)
print(circu.peekk())