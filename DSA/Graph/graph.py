from collections import defaultdict



'''#creating grapf
class Graph:
    def __init__(self, gdict = None):
        if gdict is None:
            gdict = {}
        self.gdict = gdict

    def addEdge(self, vertix , edge):
        self.gdict[vertix].append(edge)



    # grapf travasal

    def bfs(self, vertix):
        visited = [vertix]
        enque = [vertix]

        while enque:
            deQue = enque.pop(0)
            print(deQue)

            for adjucen in self.gdict[deQue]:
                if adjucen not in visited:
                    visited.append(adjucen)
                    enque.append(adjucen)


    def dfs(self, vertex):
        visited = [vertex]
        stack = [vertex]
        while stack:
            deStc = stack.pop()
            print(deStc)
            for adjucen in self.gdict[deStc]:
                if adjucen not in visited:
                    visited.append(adjucen)
                    stack.append(adjucen)


    def topologyUtil(self, v , visited, stack):
        visited.append(v)
        for i in self.gdict[v]:
            if i not in visited:
                self.topologyUtil(i , visited, stack)


        stack.insert(0, v)


    def topologysort(self):
        visited = []
        stack = []


        for k in list[self.gdict]:
            if k not in visited:
                topologyUtil(k, visited , stack)

        print (stack)


rout = { 'a' : ['b' , 'c'],
        'b' : ['d' , 'e', 'a'],
        'c' : ['a' , 'e'],
        'd' : ['b' , 'e' , 'f'],
        'e' : ['d' , 'c' ],
        'f' : ['e' , 'e']
}

class Graph:
    def __init__(self, numberOfvertx):
        self.graph = defaultdict(list)
        self.numberOfvertx = numberOfvertx


    def addEdge(self, vertex , edge):
        self.graph[vertex].append(edge)



    def topologyUtil(self, v , visited , stack):
        visited.append(v)
        for i in self.graph:
            if i not in visited:
                self.topologyUtil(i , visited, stack)

        stack.insert(0 , v)

    def topologysort(self):
        visited = []
        stack = []

        for k in list(self.graph):
            if k not in visited:
                self.topologyUtil(k , visited , stack)

        print(stack)






graph = Graph(9)
graph.addEdge('A' , 'c')
graph.addEdge('c' , 'e')
graph.addEdge('e' , 'f')
graph.addEdge('f' , 'h')
graph.addEdge('h' , 'i')
graph.addEdge('c' , 'd')

graph.addEdge('d' , 'k')

graph.topologysort()'''


