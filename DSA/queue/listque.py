#creating queue by list
class Queue:
    def __init__(self):
        self.item = []

    def __str__(self):
        values = [str(x) for x in self.item]
        return ' '.join(values)

    def isEmpty(self):
        if self.item == []:
            return True
        else:
            False

    def enque(self, value):
        
            self.item.append(value)
            return "the ele entered"
    
    def deque(self):
        if self.isEmpty():
            return "there isnin que"
        else:
            self.item.pop(0)
    
    def peekk(self):
        if self.isEmpty():
            return "no que"
        else:
            return self.item[0]

    def dele(self):
        self.item = None

    
que = Queue()
que.enque(1)
que.enque(2)
que.enque(3)
#print(que.isEmpty())
print(que)
que.deque()
print(que)
print(que.peekk())
