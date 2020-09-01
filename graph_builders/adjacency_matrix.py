# import numpy as np
# If we have to deploy make sure to change all integer to np.uint8(1) rather than only 1 which is 64 bit integer
# Space complexity is too high.May gobble all RAM for considerably large data

class AdjacencyMatrixGraph:
    # constructor
    def __init__(self, num_ofNodes):
        self._n = num_ofNodes
        # initializing each element of the adjacency matrix to zero
        self._g = [[0 for _ in range(self._n)] for _ in range(self._n)]

    def addEdge(self, fromvertex, tovertex):
        # checks if the vertex exists in the graph
        if (fromvertex >= self._n) or (tovertex >= self._n):
            print("Vertex does not exists !")
        # checks if the vertex is connecting to itself
        if (fromvertex == tovertex):
            print("Same Vertex !")
        else:
            # connecting the vertices
            self._g[tovertex][fromvertex] = 1
            self._g[fromvertex][tovertex] = 1

    def addVertex(self):
        # increasing the number of vertices
        self._n = self._n + 1
        # initializing the new elements to 0
        for i in range(0, self._n):
            self._g[i][self._n - 1] = 0
            self._g[self._n - 1][i] = 0

    def removeVertex(self, x):
        # checking if the vertex is present
        if (x > self._n):
            print("Vertex not present !")
        else:
            # removing the vertex
            while (x < self._n):
                # shifting the rows to left side
                for i in range(0, self._n):
                    self._g[i][x] = self._g[i][x + 1]
                    # shifting the columns upwards
                for i in range(0, self._n):
                    self._g[x][i] = self._g[x + 1][i]
                x = x + 1
            # decreasing the number of vertices
            self._n = self._n - 1

    def isEdge(self,fromvertex,tovertex):
        if (fromvertex >= self._n) or (tovertex >= self._n):
            return False
        else:
            if self._g[fromvertex][tovertex]==1:
                return True
        return False

    def deleteEdge(self,fromvertex,tovertex):
        if (fromvertex >= self._n) or (tovertex >= self._n):
            return
        else:
            # Dropping the vertices connection
            self._g[tovertex][fromvertex] = 0
            self._g[fromvertex][tovertex] = 0

    def degree(self,vertex):
        deg = sum(self._g[vertex])
        return deg

    def degree_of_all_nodes(self):
        node_degree = {}
        for i in range(self._n):
            node_degree[i] = self.degree(i)
        return node_degree

    def adjacent(self,vertex):
        """
        :param vertex: input vertex
        :return: list of adjacent vertices
        """
        adj = []
        for i in range(self._n):
            if self._g[vertex][i]==1:
                adj.append(i)
        return adj

    def getTrianglePath(self,vertex):
        """
        :param vertex: Takes the input vertex
        :return: returns the triangle through that vertex
        """
        trianglePaths=[]
        if vertex < self._n:
            visited=[vertex]
            for i in self.adjacent(vertex):
                if i not in visited:
                    visited.append(i)
                    for j in self.adjacent(i):
                        if j not in visited:
                            visited.append(j)
                            for k in self.adjacent(j):
                                if k == vertex:
                                    trianglePaths.append({i,j,k})
        return trianglePaths

    def allTraingles(self):
        """
        :return: Get all the triangles using above function
        """
        allTraingleList = []
        for vertex in range(self._n):
            this_triangles =  self.getTrianglePath(vertex)
            for path in this_triangles:
                if path not in allTraingleList:
                    allTraingleList.append(path)
        return allTraingleList

    def countNumTraingles(self):
        """
        :return: Count the number of unique triangles
        """
        allTraingleList = self.allTraingles()
        return len(allTraingleList)

    def printGraph(self):
        print("\n\n Adjacency Matrix:", end="")
        # displaying the 2D array
        for i in range(0, self._n):
            print()
            for j in range(0, self._n):
                print("", self._g[i][j], end="")



if __name__ == '__main__':
    amg = AdjacencyMatrixGraph(5)
    amg.addEdge(0, 1)
    amg.addEdge(0, 4)
    amg.addEdge(4, 1)
    amg.addEdge(4, 3)
    amg.addEdge(1, 0)
    amg.addEdge(1, 4)
    amg.addEdge(1, 3)
    amg.addEdge(1, 2)
    amg.addEdge(2, 3)
    amg.addEdge(3, 4)
    amg.printGraph()
    print('\n',"-"*50)
    print(amg.adjacent(2))
    print(amg.degree(4))
    print(amg.allTraingles())
    print(amg.countNumTraingles())
    print(amg.getTrianglePath(3))