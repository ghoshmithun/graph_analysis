from collections import defaultdict
class AdjacencyList:
    def __init__(self):
        self.List=defaultdict(list)

    def _addEdge(self,fromvertex,tovertex):
        if fromvertex in self.List.keys():
            if tovertex not in self.List[fromvertex]:
                self.List[fromvertex].append(tovertex)
        else:
            self.List[fromvertex]=[tovertex]

    def addEdge(self,fromvertex,tovertex,directed=False):
        if directed:
            self._addEdge(fromvertex,tovertex)
        else:
            self._addEdge( fromvertex, tovertex)
            self._addEdge(tovertex, fromvertex)


    def addFromListEdges(self,ListEdges,directed=False):
        for fromvertex,tovertex in ListEdges:
            self.addEdge(fromvertex,tovertex,directed=False)

    def isEdge(self,fromvertex,tovertex):
        if fromvertex in self.List.keys():
            if tovertex in self.List[fromvertex]:
                return True
        return False

    def deleteEdge(self,fromvertex,tovertex):
        if fromvertex in self.List.keys():
            if tovertex in self.List[fromvertex]:
                self.List[fromvertex].remove(tovertex)

    def degree(self,vertex):
        if vertex in self.List.keys():
            return len(self.List[vertex])
        return 0

    def degree_of_all_nodes(self):
        node_degree={}
        for k in list(self.List.keys()):
            node_degree[k]=self.degree(k)
        return node_degree

    def adjacent(self,vertex):
        if vertex in self.List.keys():
            return self.List[vertex]
        return []


    def getTrianglePath(self,vertex):
        """
       :param vertex: Takes the input vertex
       :return: returns the triangle through that vertex
       """
        trianglePaths=[]
        if vertex in self.List.keys():
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
        :return: Get all the unique triangles using above function
        """
        allTraingleList = []
        for vertex in self.List.keys():
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
        for i  in self.List:
            print(i,'->',' -> '.join([str(j) for j in self.List[i]]))


if __name__ == '__main__':
    al = AdjacencyList()
    al.addEdge(0, 1)
    al.addEdge(0, 4)
    al.addEdge(4, 1)
    al.addEdge(4, 3)
    al.addEdge(1, 0)
    al.addEdge(1, 4)
    al.addEdge(1, 3)
    al.addEdge(1, 2)
    al.addEdge(2, 3)
    al.addEdge(3, 4)
    al.printGraph()
    print(al.adjacent(2))
    print(al.degree(4))
    print(al.allTraingles())
    print(al.countNumTraingles())
    print(al.getTrianglePath(3))
    print(al.degree_of_all_nodes())