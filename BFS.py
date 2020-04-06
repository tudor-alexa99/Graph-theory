from graph_copy import *
import queue

def BFS():
    # This is an epty graph
    graph = DirectedGraph("input1", 8)
    # graph.add_edge(0,1,2)
    # graph.add_edge(1,2,1)
    # graph.add_edge(1,4,1)
    # graph.add_edge(1,3,1)
    # graph.add_edge(3,5,2)
    # graph.add_edge(3,6,6)
    # graph.add_edge(6,7,1)

    s = int(input("Insert a STARTING vertex: "))
    y = int(input("Insert a ENDING vertex: "))

    '''Have a list of visited vertices and a list of current heads'''


    q = queue.Queue()
    visited = []
    dist = {}
    prev = {}

    q.put(s)
    # visited.append(y)
    dist[s] = 0
    prev[s] = []
    while (not q.empty()):
        x = q.get()
        for y in graph._goesOut(x):
            prev[y]=[x]
            if y not in visited:
                q.put(y)
                visited.append(y)
                dist[y] = dist[x] + 1
                prev[y].extend(prev[x])

    print("\nThe visited vertices are:  ")
    print(visited)

    print("\nFor each vertex, the path accessed was:")
    print(prev)

    print("\nThe path accessed from start to end was:")
    for i in reversed(prev[y]):
        print(i, "-->",end="")
    print(y)

    print("\nHaving the lenght:")
    print(dist[y]+1)


BFS()