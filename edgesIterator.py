

class EdgesIterator:
    def __init__(self, graph):
        self.__graph = graph
        self.__current_vertex = 0
        self.__current_neighbour_index = 0

    def first(self):
        '''
        __current_neighbour points to the n-th element in the list of neighbours
        '''
        self.__current_vertex = 0
        self.__current_neighbour = 0

    def valid(self):
        '''
        Checks if the current index didn't surpass the number of vertices in the list
        '''
        return self.__current_vertex < self.__graph._number_of_vertices()

    def next(self):
        if not self.valid():
            raise ValueError\
                ("Index out of range")
        '''
        If the current vertex does not point towards any other vertex, it means that there's no edge starting with it, therefore
        we'll increase the current index
        '''
        if len(self.__graph._outside[self.__current_vertex]) == 0:
            self.__current_vertex +=1
            self.__current_neighbour_index = 0
        elif self.__current_neighbour_index < len(self.__graph._outside[self.__current_vertex])-1 :
            '''If the current_neighbour index did not reach the end of the neighbours list, increases it'''
            self.__current_neighbour_index += 1
        else:
            '''
            If there is no other neighbour to iterate, goes to the next vertex
            '''
            self.__current_vertex += 1
            self.__current_neighbour_index = 0

    def getCurrent(self):
        if not self.valid():
            raise ValueError
        if len(self.__graph._outside[self.__current_vertex]) == 0:
            return 0
        return str(self.__current_vertex) +"-->"+str( self.__graph._outside[self.__current_vertex][self.__current_neighbour_index]) +" cost:"+ str(self.__graph._costs[(self.__current_vertex,  self.__graph._outside[self.__current_vertex][self.__current_neighbour_index])])