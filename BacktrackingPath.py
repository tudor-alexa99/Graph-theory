from graph_copy import *
# from Ford import  *
def create():
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

    start = int(input("Insert start point: "))
    stop = int(input("Insert stop point: "))
    # print(graph)
    print("The min path is: ", minPath(graph,start, stop, [], 0))

def minPath(graph ,start, stop, checked, cost):
    for n in graph._outside[start]:
        if n not in checked:
            checked.append(n)
            cost+= minPath(graph, n, stop, checked, cost)
    if stop not in checked:
        print("There's no path")
    if n:
        return graph.getCost(start, n)


#
# def test2():
#     graph = DirectedGraph("input1", 7)
#     graph.add_edge(0,1,6)
#     graph.add_edge(0,2,5)
#     graph.add_edge(0,3,5)
#     graph.add_edge(2,1,-2)
#     graph.add_edge(3,2,-2)
#     graph.add_edge(3,5,-1)
#     graph.add_edge(5,6,3)
#     graph.add_edge(4,6,3)
#     graph.add_edge(2,4,1)
#     graph.add_edge(1,4,-1)
#
#     start = int(input("Insert start point: "))
#     stop = int(input("Insert stop point: "))
#
#     for n in graph._goesOut(start):
#         if n:
#             Ford(start, n)

create()