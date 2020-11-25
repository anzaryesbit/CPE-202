from sys import argv
from stack_array import *
from queue_array import *

class Vertex:
    def __init__(self, ID):
        self.point = ID
        self.push = False
        self.in_deg = 0
        self.adjacent = []

    def __repr__(self):
        return str(self.point) + ": " + str(self.in_deg) + " " + str(self.adjacent)

    def __lt__(self, other):
        return self.in_deg < other.in_deg

    def __eq__(self, other):
        return self.point == other.point

    def adjacent_to(self, adj_list):
        self.adjacent.append(adj_list)

    def inc_deg(self):
        self.in_deg += 1

class Graph:
    '''Add additional helper methods if necessary.'''
    def __init__(self, list1):
        '''reads in the specification of a graph and creates a graph using an adjacency list representation.
           You may assume the graph is not empty and is a correct specification.  E.g. each edge is
           represented by a pair of vertices.  Note that the graph is not directed so each edge specified
           in the input file should appear on the adjacency list of each vertex of the two vertices associated
           with the edge.'''
        dict1 = {}
        self.dict = dict1
        for i in range(len(list1)//2):
            self.add_vertex(vertex_pair[2*i])
            self.add_vertex(current_line[2*i+1])
            self.add_edge(current_line[2*i], current_line[2*i+1])


    def add_vertex(self, key):
        '''Add vertex to graph, only if the vertex is not already in the graph.'''
        vert = Vertex(key)
        if self.dict.get(key) is None:
            self.dict[key] = vert

    def get_vertex(self, key):
        '''Return the Vertex object associated with the id. If id is not in the graph, return None'''
        if self.dict.get(key) is not None:
            return self.dict.get(key)
        else:
            return None

    def add_edge(self, v1, v2):
        '''v1 and v2 are vertex id's. As this is an undirected graph, add an
           edge from v1 to v2 and an edge from v2 to v1.  You can assume that
           v1 and v2 are already in the graph'''
        self.dict[v1].adjacent_to(v2)
        self.dict[v2].adjacent_to(v1)

    def get_vertices(self):
        '''Returns a list of id's representing the vertices in the graph, in ascending order'''
        lists = list(self.dict.keys())
        lists.sort()
        return lists

    def conn_components(self):
        '''Returns a list of lists.  For example, if there are three connected components
           then you will return a list of three lists.  Each sub list will contain the
           vertices (in ascending order) in the connected component represented by that list.
           The overall list will also be in ascending order based on the first item of each sublist.
           This method MUST use Depth First Search logic!'''
        final = []
        already_checked = {}
        stack = Stack(len(self.dict))
        for key in self.dict:
            if key not in already_checked:
                stack.push(key)
                x = key
                already_checked[x] = 0
                while stack.num_items != 0:
                    for i in self.dict[x].adjacent_to:
                        if already_checked.get(i) is None:
                            stack.push(i)
                            already_checked[i] = 0
                    final.append(stack.pop())
        return final


    def is_bipartite(self):
        '''Returns True if the graph is bicolorable and False otherwise.
           This method MUST use Breadth First Search logic!'''
        already_checked = {}
        traversal = []
        que = Queue(len(self.dict))
        for key in self.dict:
            if key not in already_checked:
                que.enqueue(key)
                while que.num_items != 0:
                    current = que.items[que.first]
                    for i in self.dict[current].adjacent:
                        if already_checked.get(i) is None:
                            que.enqueue(i)
                            already_checked[i] = 0
                    traversal.append(que.dequeue())
        return traversal


def tsort(vertices):
    '''
    * Performs a topological sort of the specified directed acyclic graph.  The
    * graph is given as a list of vertices where each pair of vertices represents
    * an edge in the graph.  The resulting string return value will be formatted
    * identically to the Unix utility {@code tsort}.  That is, one vertex per
    * line in topologically sorted order.
    *
    * Raises a ValueError if:
    *   - vertices is emtpy with the message "input contains no edges"
    *   - vertices has an odd number of vertices (incomplete pair) with the
    *     message "input contains an odd number of tokens"
    *   - the graph contains a cycle (isn't acyclic) with the message 
    *     "input contains a cycle"'''
    if vertices == []:
        raise ValueError("input contains no edges")
    if len(vertices) % 2 == 1:
        raise ValueError("input contains an odd number of tokens")
    tsort_stack = Stack(50)
    to_return = []
    adj_list = []
    for vert in vertices:
        vertex = Vertex(vert)
        exist = False
        if vertex in adj_list:
            exist = True
        if not exist:
            adj_list.append(vertex)
    for i in range(len(adj_list)):
        for j in range(len(vertices) - 1):
            if adj_list[i].point == vertices[j] and j % 2 == 0:
                for vert in adj_list:
                    if vert.point == vertices[j + 1]:
                        adj_list[i].adjacent.append(vert)
                        vert.inc_deg()
    for term in adj_list:
        if term.in_deg == 0 and not term.push:
            tsort_stack.push(term)
            term.push = True
    while not tsort_stack.is_empty():
        vertex = tsort_stack.pop()
        to_return.append(vertex.point)
        for adj_point in vertex.adjacent:
            adj_point.in_deg -= 1
            if adj_point.in_deg == 0 and not adj_point.push:
                tsort_stack.push(adj_point)
                adj_point.push = True
    if len(to_return) == len(adj_list):
        return "\n".join(to_return)
    else:
        raise ValueError('input contains a cycle')



def main():
    '''Entry point for the tsort utility allowing the user to specify
       a file containing the edge of the DAG'''
    if len(argv) != 2:
        print("Usage: python3 tsort.py <filename>")
        exit()
    try:
        f = open(argv[1], 'r')
    except FileNotFoundError as e:
        print(argv[1], 'could not be found or opened')
        exit()

    vertices = []
    for line in f:
        vertices += line.split()

    try:
        result = tsort(vertices)
        print(result)
    except Exception as e:
        print(e)

if __name__ == '__main__': 
    main()
