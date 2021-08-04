class TrieNod:
    def __init__(self):
        self.childern = {}
        self.endString = False

class Trie:
    def __init__(self):
        self.root = TrieNod()


    def insertNod(self, word):
        root = self.root
        for i in word:
            ch = i
            node = root.childern.get(ch)
            if node == None:
                node = TrieNod()
                root.childern.update({ch:node})
            root = node
        root.endString = True
        print("successfully inserted")

    def searchNode(self, word):
        root = self.root
        for i in word:
            node = root.childern.get(i)
            if node == None:
                return False
            root = node
        if root.endString == True:
            return True
        else:
            return False
        

newTre = Trie()
newTre.insertNod("dog")
newTre.insertNod("doom")
print(newTre.searchNode("dog"))


