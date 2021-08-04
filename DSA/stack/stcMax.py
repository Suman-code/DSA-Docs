# creating a stack with limited element

class StackMa:
    def __init__(self, maxVal):
        self.list = []
        self.maxVal = maxVal
    
    def __str__(self):
        values = self.list.reverse()
        values = [str(x) for x in self.list]
        return '\n'.join(values)

    #check list is or not

    def isFull(self):
        if len(self.list) == self.maxVal:
            return True
        else:
            False

    #checking is empty or not
    def isEmpty(self):
        if self.list == []:
            return True
        else:
            False

    # push the list

    def pushList(self, value):
        if self.isFull():
            return "there is no place"

        else:
            self.list.append(value)
            return "the element has been entered"

    def poopp(self):
        if self.isEmpty():
            return "there is no list"
        else:
            return self.list.pop()

    #peek function 
    
    def peeek(self):
        if self.iseEmpty():
            return "there si no element"
        else:

            return self.list[len(self.list) -1]


    def deke(self):
        self.list = None
    

 
limted = StackMa(4)

#print(limted.isEmpty())
#print(limted.isFull())
limted.pushList(1)
limted.pushList(2)

limted.pushList(3)
#print(limted)
print(limted.poopp())
print(limted)