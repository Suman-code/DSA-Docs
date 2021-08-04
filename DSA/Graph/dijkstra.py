from collections import defaultdict

class Graph:
   def __init__(self):
       self.nodes = set()
       self.edges = defaultdict(list)
       self.distances = {}

    def addNod(self, value):
        self.nodes.append(value)

    def addEdge(self, fromNod , toNod , distance):
        self.edges[fromNod].append(toNod)
        self.distances[(fromNod , toNod)] = distance


def diskstra(graph , initial):
    visited = { initial : 0 }
    path = defaultdict(list)

    nodes = (graph.nodes)
    while nodes:
        minNod = None
        for node in nodes:
            if node in visited:
                if minNod is None:
                    minNod = node
                elif 



