#creation of stack
class Stack:
    def __init__(self):
        self.list = []
    

    def __str__(self):
        values = self.list.reverse()
        values = [str(x) for x in self.list]
        return '\n'.join(values)

    #checking the empty list

    def empty(self):
        if self.list == []:
            return True
        else:
            False
    #push the list
    def pushEle(self, value):
        self.list.append(value)
        return "the list enterted"

    #pop the element
    def poop(self):
        if self.empty():
            return "The list is empty"
        else:
            self.list.pop()

   #peek method 
    def peeek(self):
        if self.empty():
            return 'there is no list'
        else:
            return self.list[len(self.list) - 1]

#delete
    def dele(self):
        self.list = None
    

        

stc = Stack()
stc.empty()
stc.pushEle(1)
stc.pushEle(2)
stc.pushEle(3)
print(stc)

stc.dele()


