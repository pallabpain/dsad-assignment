from __future__ import print_function
"""
Problem 7: The Hamilton cycle problem - Is it possible to traverse each of
the vertices of a graph exactly once, starting and ending at the same vertex?

Algorithm IsValidVertex(v, pos, path):
    if v is adjacent to previously added vertex at path[pos - 1] and not present in path then
        return true
    else
        return false

Algorithm Cycle(path, pos)
    if pos == total no. of vertices (N) then
        if vertex at last position in path has an edge to vertex at first position then
            return true
        else
            return false
    
    for vertex in 1 to N:
        if IsValidVertex(vertex) then
            add vertex to path[pos]
            if Cycle(path, pos + 1) == true then
                return true
            else
                pos = pos - 1
    return false


Algorithm Hamiltonian():
    initialize path array = [-1] * total vertices (N)
    set path[0] = 0
    if Cycle(path, 1) == true then
        print the path
    else
        no solution found
"""


class Graph(object):

    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = [[0 for _ in range(vertices)]
                      for _ in range(vertices)]

    def is_valid_vertex(self, v, pos, path):
        """
        Checks if a vertex is valid to be added to the path
        1. Vertex should be adjacent to the previos vertex in the path
        2. Vertex should not already be in path
        """
        if self.graph[path[pos - 1]][v] == 0:
            return False
        if v in path:
            return False
        return True

    def ham_cycle(self, path, pos):
        if pos == self.vertices:
            # At the last position in the path, check if the cycle
            # is formed, i.e. last vertex has edge to first vertex
            return self.graph[path[pos - 1]][path[0]] == 1

        for v in range(1, self.vertices):
            if self.is_valid_vertex(v, pos, path):
                path[pos] = v
                if self.ham_cycle(path, pos + 1):
                    return True
                # If cycle is not formed, backtrack
                pos -= 1
        return False

    def hamiltonian(self):
        path = [None] * self.vertices
        path[0] = 0
        if not self.ham_cycle(path, 1):
            print("No hamiltonian cycle found.")
        else:
            print("->".join(map(str, path + [path[0]])))


if __name__ == "__main__":
    g = Graph(5)
    g.graph = [[0, 1, 0, 1, 0],
               [1, 0, 1, 1, 1],
               [0, 1, 0, 0, 1],
               [1, 1, 0, 0, 1],
               [0, 1, 1, 1, 0]]
    g.hamiltonian()
