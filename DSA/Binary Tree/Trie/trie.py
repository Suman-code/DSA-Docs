#creating node for trie
class TriNode:
    def __init__(self ):
        self.childern = {}
        self.endString = False

class Trie:
    def __init__(self):
        self.root = TriNode()

    
    def insertNod(self, val):
        current = self.root
        for i in val:
            cha = i
            
            node = current.childern.get(cha)
            if node == None:
                node = TriNode()
                current.childern.update({cha:node})
            current = node
        current.endString = True
        print("succesfully inserted")
    
    def sarchingNod(self, val):
        current = self.root
        for i in val:
            node = current.childern.get(i)
            if node == None:
                return False
            current = node
        if current.endString == True:
            return True
        else:
            return False
        


        


newTrie = Trie()
#newTrie.insertNod("dog")
#newTrie.insertNod("cat")
print(newTrie.sarchingNod("cat"))
