class TreeNode:
    def __init__(self, data, childern = []):
        self.data = data
        self.childern = childern

    def __str__(self, level = 0):
        ret = " " * level + str(self.data + "\n")
        for child in self.childern:
            ret += child.__str__(level + 1)
        return ret

    def addChild(self, TreeNode):
        self.childern.append(TreeNode)


tree = TreeNode('drinks' , [])
cold = TreeNode('cold' , [])
hot = TreeNode('hot' , [])

tree.addChild(cold)
tree.addChild(hot)
softDrink = TreeNode('softDrink' , [])
tea = TreeNode('tea' , [])
cofee = TreeNode('cofee' , [])
cofee1 = TreeNode('coldCofee' , [])

cold.addChild(softDrink)
hot.addChild(tea)
hot.addChild(cofee)
cofee.addChild(cofee1)

print(tree)