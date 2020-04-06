from random import randint
import time

class Graph:
    # create a graph with n vertices numbered from 0 to n-1
    def __init__(self, n):
        self._n = n
        self._inboundEdges = {}
        self._outboundEdges = {}
        for vertex in range(self._n):
            self._inboundEdges[vertex] = []
            self._outboundEdges[vertex] = []

    # creates an edge between two already-exiting vertices
    # verifies if the edge already exists and if the vertices exist
    # input: the two vertices (x and y)
    # output: False if the edge already exists. True otherwise
    def addEdge(self, x, y):
        if self.isEdge(x,y):
            return False
        self._inboundEdges[y].append(x)
        self._outboundEdges[x].append(y)
        return True

    # verifies if the edge we want to add already exists
    # input: the startpoint (x) of the edge and its endpoint (y)
    # output: True if the edge exists. False otherwise
    def isEdge(self, x, y):
        return y in self._outboundEdges[x]

    # output: an enumerable containing the outbound neighbours of the vertex (which (hopefully) already exists)
    def parseOutbound(self, vertex):
        return self._outboundEdges[vertex][:]

    # output: an enumerable containing the inbound neighbours of the vertex (which (hopefully) already exists)
    def parseInbound(self, x):
        l = []
        for vertex in self.parseAll():
            if x in self._outboundEdges[vertex]:
                l.append(vertex)
        return l


    # output: an enumerable containing the neighbours of the vertex (which (hopefully) already exists)
    def parseAll(self):
        return [x for x in self._outboundEdges.keys()]

def createDemoGraph():
    graph = Graph(5)
    graph.addEdge(0,1)
    graph.addEdge(0, 1)
    graph.addEdge(0, 2)
    graph.addEdge(0, 4)
    graph.addEdge(1, 2)
    graph.addEdge(1, 1)
    graph.addEdge(4, 0)
    return graph

# creates a random graph with n vertices and m edges
def createRandomGraph(n,m):
    graph = Graph(n)
    for i in range(m):
        x = randint(0,n-1)
        y = randint(0,n-1)
        while not graph.addEdge(x,y):
            x = randint(0, n-1)
            y = randint(0, n-1)
        graph.addEdge(x,y)
    return graph

# def prettyPrint(graph):
#     for vertex in graph.parseAll():
#         string = str(vertex)+" -> "
#         for neigh in graph.parseOutbound(vertex):
#             string+=str(neigh)+" "
#         print(string)
#
#     for vertex in graph.parseAll():
#         string = str(vertex)+" -> "
#         for neigh in graph.parseInbound(vertex):
#             string+=str(neigh)+" "
#         print(string)

def measureTime(graph):
    time1 = time.time()
    for vertex in graph.parseAll():
        for neigh in graph.parseOutbound(vertex):
            pass
    time2 = time.time()
    # for vertex in graph.parseAll():
    #     for neigh in graph.parseInbound(vertex):
    #         pass
    # time3 = time.time()
    print(time2-time1)#)


def main():
    graph = createRandomGraph(1000000,1000000)
    measureTime(graph)
    # for vertex in graph.parseAll():
    #     string = str(vertex)+" -> "
    #     for neigh in graph.parseOutbound(vertex):
    #         string+=str(neigh)+" "
    #     print(string)
    #
    # for vertex in graph.parseAll():
    #     string = str(vertex)+" -> "
    #     for neigh in graph.parseInbound(vertex):
    #         string+=str(neigh)+" "
    #     print(string)

main()