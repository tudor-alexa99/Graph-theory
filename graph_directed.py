
from copy import *
import texttable
# from edgesIterator import *
from random import randint
"""
class Iterator
2 iteratori pentru edges si 2 pt vertices

"""
class DirectedGraph:
    def __init__(self, filename, nr = 0):
        #nr will be the number of vertices of the graph
        if nr != 0:
            self._nr = nr
            self._edges = 0
            '''
            for each vertex, we'll keep track of edges that start at the given point
            or end there
            '''
            self._inside = {}
            self._outside = {}
            self._costs = {}
            '''A list (dictionary) of costs. Each edge will be saved as a a dictionary, where the key is the tuple of
             of vertices x and y and the value will be the cost'''
            '''
            Each in/out edge will be saved inside of a dictionary, where the key is 
            the "name"/value attributed to the vertex, and it will point towards all
            the other vertices that are starting / ending points of the given edge
            '''
            #for each of the n vertices, we'll assign an empty list

            for v in range(self._nr):
                self._inside[v] = []
                self._outside[v] = []
                #each vertice will be identified by an integer, going from 0 to n-1

        else:
            self._edges = 0
            self._inside = {}
            self._outside = {}
            self._costs = {}
            self.readFromFile(filename)

    def readFromFile(self, filename):
        try:

            '''The first line is the number of vertices'''
            f = open(filename, 'r')
            line = f.readline().strip()
            l = line.split(' ')
            self._nr = int(l[0])
            self._edges = int(l[1])

            for i in range(0, self._nr):
                self._outside[i] = []
                self._inside[i] = []

            line = f.readline().strip()
            while line != "":
                l = line.split(" ")
                self._outside[int(l[0])].append(int(l[1]))
                self._inside[int(l[1])].append(int(l[0]))
                self._costs[(int(l[0]), int(l[1]))] = int(l[2])
                line = f.readline().strip()
        except IOError as e:
            print("Error loading from file" + str(e))
        return self

    def _number_of_vertices(self):
        return self._nr

    def _number_of_edges(self):
        return self._edges

    def add_vertex(self):
        self._nr += 1
        self._outside[self._nr-1] = []
        self._inside[self._nr-1] = []

    def remove_vertex(self, number):
        '''
        Remove the vertex from the list.
        Go through the lists of in's and out's. For each index in those lists that is
        greater than the vertex that was removed, decrement its value
        exp: if in a graph of 6 vert., the 2nd one is removed, each of the vertices 3,4 and 5
        will get the values 2, 3 and 4
        '''
        if number >= self._nr:
            return None
        # go through the list of vertices that connect to the removed one
        for i in self._outside[number]:
            #remove the element from all the connected vertices vertices
            self._inside[i].remove(number)
        #go through the list of vertices that are pointing towards the removed one
        for i in self._inside[number]:
            self._outside[i].remove(number)

        #go through all the vertices in the list and update their new values
        #according to the removed one
        self._nr -= 1
        self._inside.pop(number)
        self._outside.pop(number)
    def getCost(self, x, y):
        if self._isEdge(x,y):
            return self._costs[(x, y)]

    def add_edge(self, x, y, cost = 0):
        '''
        x = the starting point of the edge
        y = the ending point
        '''
        #first, we'll have to check if the given edge already exists

        if self._isEdge(x, y) == True:
            return False
        '''
        mark that y is the endpoint of an edge starting at x
        and that x is the startpoint of an edge that ends with y
        '''
        self._outside[x].append(y)
        self._inside[y].append(x)
        self._edges += 1

        self._costs[(x, y)] = cost

        return True
    def _isEdge(self, x, y):
        '''
        We have to check if there's an edge that starts with X and ends with Y
        '''
        if y in self._outside[x]:
            return True
        return False

    def _goesOut(self, v):
        '''
        takes as an input a given vertice and returns a list of all the connected edges to it
        '''
        l = []
        # all_edges = self.iterate()

        for e in self._outside[v]:
            # for vertice in self._outside[e]:
            l.append(e)
        return l

    def goesIn(self, v):

        l = []
        # all_edges = self.iterate()

        for e in self._inside[v]:
            # for vertice in self._outside[e]:
            l.append(e)
        return l

    def iterate(self):
        '''
        Goes through all the edges in the graph, copies them to a list and returns it
        '''
        copy_list = []
        for v in self._outside.keys():
            copy_list.append(v)
        return copy_list

    def nrVertices(self):
        return self._nr
    def getEdges(self):
        copyList =[]
        for v in range(self._nr):
            for x in self._goesOut(v):
                copyList.append((v, x))
        return copyList
    def createRandomGraph(self, n):
        '''n = the number of random edges to be generated'''
        for i in range(n):
            x = randint(0, self._nr - 1)
            y = randint(0, self._nr - 1)
            cost = randint(0, 30)
            while x == y or not self.add_edge(x, y, cost) :
                x = randint(0, self._nr - 1)
                y = randint(0, self._nr - 1)
            self.add_edge(x, y, cost)

    def show_cycle(self, v, checked_list, edges):
        '''Goes through the cycle of vertices coming from v
        if type(v) == int:
            if v not in checked_list:
                checked_list.append(self._outside[v])
                return self.show_cycle(self._outside[v], checked_list)
        else:
            for i in v:
                if i not in checked_list:
                    return self.show_cycle(v, checked_list)
        return checked_list
        '''
        for i in self._outside[v]:
            if i not in checked_list:
                checked_list.append(i)
                edges.append(str(v) + "-->" + str(i))
                self.show_cycle(i,checked_list, edges)
        return edges
    def __str__(self):
        t = texttable.Texttable()
        for i in self._outside:
            if len(self._outside[i]) > 0:
                for extra in range(len(self._outside[i])):  #in case a given vertex points towards more vertices
                    t.add_row(["[" + (str(i) +"]"), "-->", "[" + str(self._outside[i][extra]) + "]" , self._costs[(int(i),self._outside[i][extra])]])
        t.header(["in"," ", "out", "cost" ])
        return t.draw()

    def addEdgeUndirected(self, x, y, cost = 0):
        self.add_edge(x,y,cost)
        self.add_edge(y,x,cost)

    def copyGraph(self):
        return deepcopy(self)



def test_random_graph():
    graph = DirectedGraph(6)
    graph.createRandomGraph(8)
    print(graph)


# test_graph()
#test_print()
# test_random_graph()
class UI:
    def __init__(self):
        self.command = []

    def print_command_menu(self):
        print("Choose an action:")
        print("\t1.Get the number of vertices:.")
        print("\t2Iterate vertices.")
        print("\t3Check if two vertices are connected.")
        print("\t4Get in and out degree of a vertex.")
        print("\t5Parse edges.")
        print("\t6.")
        print("\t1.")
