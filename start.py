from edgesIterator import *
from graph_copy import *


def start():
    test_graph()
    test_iterator()
    #testReadFromFile()


def test_graph():
    #create a graph
    graph = DirectedGraph("input1", 8)

    #add some edges with given costs
    graph.add_edge(0,1,2)
    graph.add_edge(1,0,4)
    graph.add_edge(2,0)
    graph.add_edge(2,1)
    graph.add_edge(2,3)
    graph.add_edge(3,4)
    graph.add_edge(4,5)
    graph.add_edge(6,7)
    graph.add_edge(7,0)
    graph.add_edge(6,2)

    #remove a vertex and check if the edges and other vertices were modified
    graph.remove_vertex(2)
    graph.remove_vertex(5)

    #copy the graph
    copy_graph = graph.copyGraph()

    #remove certain elements from the copy to prove that the original does not get modified
    copy_graph.remove_vertex(1)
    copy_graph.remove_vertex(3)

    print("This is the copy: \n",copy_graph, "\nAnd this is the original:\n")


    #move the iterator to the first edge
    #iterE = EdgesIterator(graph)
    #iterE.first()

    #checck if the iterator goes to the first edge added
    #print(iterE.getCurrent())

    # print the final graph:  ||  inbound vertex  || --> ||  outbound vertex  ||  cost of the edge  ||

    print(graph)

    '''Print the list of inbound and outbound vertices on each position'''
    print(graph._outside)
    print(graph._inside)
    return

    '''I still have to work on this'''
    for i in graph._outside[2]:
        print(graph.show_cycle(2,[i],[]))
    print(graph._outside[2])
    # print(graph.show_cycle(2,[2],[]))
    # print(graph.show_cycle(3,[3],[]))


def test_iterator():
    graph = DirectedGraph("input1",4)

    graph.add_edge(0,1,2)
    graph.add_edge(1,0,4)
    graph.add_edge(2,0)
    graph.add_edge(2,1)
    graph.add_edge(2,3)

    iter = EdgesIterator(graph)

    '''
    We'll check the valid() function of the iterator
    If we call the function next() too many times, it should throw a ValueError
    '''
    iter.first()
    iter.next()
    iter.next()
    iter.next()
    iter.next()
    iter.next()
    #   ^^ so far, it's the exact number of edges
    #

    try:
        iter.next()
    except ValueError() as error:
        print("Some error")

def testReadFromFile():
    graph = DirectedGraph("very_large_input")
    print(graph)

start()