# creating grapf
'''
class Graph:
    def __init__(self, gdict = None):
        if gdict is None:
            gdict = {}
        self.gdict = gdict


    def bfs(self, start , end):
        queue = []
        queue.append([start])
        while queue:
            path = queue.pop(0)
            node = path[-1]
            if node == end:
                return path

            for adjacen in self.gdict.get(node, []):
                new_path = list(path)
                new_path.append(adjacen)
                queue.append(new_path)


costm = { 'a' : ['b' , 'c'],

        'b' : ['d' , 'e'],

        'c' : ['f' , 'h'],
         'e' : ['k' , 'r'],

}

g = Graph(costm)
print(g.bfs('b' , 'r'))'''

# BFS for singal source sort path

# creating Graph

class Graph():
    def __init__(self , gdict = None):
        if gdict is None:
            gdict = {}
        self.gdict = gdict
    
    def bfsPath(self, start , end):
        queue = []
        queue.append([start])
        while queue:
            path = queue[0]
            node = path[-1]
            if node == end:
                return path

            for adjacen in self.gdict.get(node , []):
                new_path = list(path)
                new_path.append(adjacen)
                queue.append(new_path)


costm = { 'a' : ['b' , 'c'],
'b' : ['c' , 'd'] , 
'c' : ['e' , 'f'],
'e' : ['g' , 'f']


}

g = Graph(costm)
print(g.bfsPath('a' , 'd'))
