class Graph:
    def __init__(self, nr):
        self._nr = nr
        self._edges = 0
        self._connect = {}
        self._cost = {}
        for v in range(self._nr):
            self._connect[v] = []

    def addEdge(self, x, y, cost):
        if x not in self._connect[y]:
            self._connect[x].append(y)
            self._connect[y].append(x)
            self._cost[(x, y)] = cost
            self._cost[(y, x)] = cost
            self._edges += 1
            return True
        else:
            return False

    def get_edges(self):
        copyList =[]
        for v in range(self._nr):
            for x in self._connect[v]:
                if (v, x) not in copyList and (x, v) not in copyList:
                    copyList.append((v, x))
        return copyList




    def add_vertex(self):
        self._nr += 1
        self._connect[self._nr - 1] = []

    def _number_of_vertices(self):
        return self._nr

    def _number_of_edges(self):
        return self._edges

    def get_cost(self,x,y):
        c = self._cost[(x,y)]
        return c
    def nr_edges(self):
        return self._edges