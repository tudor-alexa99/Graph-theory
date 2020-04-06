from graph_copy import *

def Ford(graph, start, end):
    '''we'llhave a list of minimum costs from start to all the possible paths'''

    '''this returns a list of all the accessible vertices'''
    distances = graph.iterate()

    distances[start] = 0
    for v in range (1, graph.nrVertices()):
        distances[v] = 999999

    edges = graph.getEdges()

    for index in range (graph.nrVertices()):
        print("\n step number: ", index )
        print("Before:", distances)
        for edg in edges:
            '''the distance from starting point to the end
            point of a given vertex will be saved as the minimum cost from the start to that point'''
            frm = edg[0]
            to = edg[1]
            distances[to] = min(distances[to], distances[frm] + graph.getCost(frm,to))
        print("After: ", distances)
    # print(lst)

    '''check for possible negative cost loops'''
    previous_distances = deepcopy(distances)

    print("\nThe final cost from ", start, "to", end, "is: ", distances[end])

def another_test():
    '''Create a graph with 7 edges'''
    graph = DirectedGraph("input1", 7)
    graph.add_edge(0,1,6)
    graph.add_edge(0,2,5)
    graph.add_edge(0,3,5)
    graph.add_edge(2,1,-2)
    graph.add_edge(3,2,-2)
    graph.add_edge(3,5,-1)
    graph.add_edge(5,6,3)
    graph.add_edge(4,6,3)
    graph.add_edge(2,4,1)
    graph.add_edge(1,4,-1)

    print(graph)
    print("\n")

    Ford(graph, 0, 6)

another_test()