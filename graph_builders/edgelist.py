from collections import Counter

class EdgeListGraph:
    class Edge:
        slots = '_origin', '_destination'

        def __init__(self, u, v):
            self._origin = u
            self._destination = v

        def endpoints(self):
            return (self._origin, self._destination)

        def opposite(self, u):
            return self._destination if u in self._origin else self._origin

        def pointBelongsEdge(self, v):
            return v == self._origin or v == self._destination

        def is_connected(self, other):
            if self != other:
                if self._origin == other._destination or self._destination == other._origin \
                        or self._origin == other._origin or self._destination == other._destination:
                    return True
            return False

        def two_adjacent_edge_vertices(self, other):
            if self.is_connected(other):
                return dict(Counter([self._origin, self._destination, other._origin, other._destination]))
            return {0: 0}

        def __str__(self):
            return str(self._origin) + '<->' + str(self._destination)

        def __eq__(self, other):
            if self._origin == other._origin and self._destination == other._destination:
                return True
            return False

    def __init__(self):
        self.e_list = []
        self.v_list = []

    def addEdge(self, fromvertex, tovertex):
        edge = self.Edge(fromvertex, tovertex)
        if edge not in self.e_list:
            self.e_list.append(edge)
        if fromvertex not in self.v_list:
            self.v_list.append(fromvertex)
        if tovertex not in self.v_list:
            self.v_list.append(tovertex)

    def isEdge(self, fromvertex, tovertex):
        edge1 = self.Edge(fromvertex, tovertex)
        edge2 = self.Edge(tovertex, fromvertex)
        for e in self.e_list:
            if edge1 == e or edge2 == e:
                return True
        return False

    def deleteEdge(self, fromvertex, tovertex):
        edge = self.Edge(fromvertex, tovertex)
        if edge in self.e_list:
            self.e_list.remove(edge)
        if fromvertex in self.v_list:
            if not all(map(lambda x: x.pointBelongsEdge(fromvertex), self.e_list)):
                self.v_list.remove(fromvertex)
        if tovertex in self.v_list:
            if not all(map(lambda x: x.pointBelongsEdge(tovertex), self.e_list)):
                self.v_list.remove(tovertex)

    def adjacent(self, vertex):
        adj = []
        if vertex in self.v_list:
            for edge in self.e_list:
                if vertex == edge._origin:
                    if edge._destination not in adj:
                        adj.append(edge._destination)
                if vertex == edge._destination:
                    if edge._origin not in adj:
                        adj.append(edge._origin)
        return adj

    def degree(self, vertex):
        return len(self.adjacent(vertex))

    def degree_of_all_nodes(self):
        node_degree={}
        for k in self.v_list:
            node_degree[k]=self.degree(k)
        return node_degree

    def ifTriangle(self, u, v, w):
        """
        :param u: vertex 1
        :param v: vertex 2
        :param w: vertex 3
        :return: whether they form triangle
        """
        if u in self.v_list and v in self.v_list and w in self.v_list:
            if self.isEdge(u, v) and self.isEdge(v, w) and self.isEdge(w, u):
                e1 = self.Edge(u, v)
                e2 = self.Edge(v, w)
                e3 = self.Edge(w, u)
                if e1.is_connected(e2) and e2.is_connected(e3) and e3.is_connected(e1):
                    return True
        return False

    def countNumTraingles(self):
        cnt = 0
        n = len(self.v_list)
        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                for k in range(j + 1, n):
                    v1 = self.v_list[i]
                    v2 = self.v_list[j]
                    v3 = self.v_list[k]
                    if self.ifTriangle(v1, v2, v3):
                        cnt += 1
        return cnt

    def printGraph(self):
        print("EdgeList edges ")
        for edge in self.e_list:
            print(edge)
        print("EdgeList Vertices ")
        for l in self.v_list:
            print(l, end=" ")


if __name__ == '__main__':
    elg = EdgeListGraph()
    elg.addEdge(0, 1)
    elg.addEdge(0, 4)
    elg.addEdge(4, 1)
    elg.addEdge(4, 3)
    elg.addEdge(1, 0)
    elg.addEdge(1, 4)
    elg.addEdge(1, 3)
    elg.addEdge(1, 2)
    elg.addEdge(2, 3)
    elg.addEdge(3, 4)
    elg.printGraph()
    print('\n', "-" * 50)
    print(elg.adjacent(2))
    print(elg.degree(1))
    print(elg.countNumTraingles())