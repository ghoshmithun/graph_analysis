import sys
from graph_builders.adjacency_list_graph import AdjacencyList
from graph_builders.edgelist import EdgeListGraph
from graph_builders.adjacency_matrix import AdjacencyMatrixGraph

space_taken=[]
for clsName in [AdjacencyList,EdgeListGraph,AdjacencyMatrixGraph]:
    try:
        g = clsName()
    except:
        g = clsName(5)
    g.addEdge(0, 1)
    g.addEdge(0, 4)
    g.addEdge(4, 1)
    g.addEdge(4, 3)
    g.addEdge(1, 0)
    g.addEdge(1, 4)
    g.addEdge(1, 3)
    g.addEdge(1, 2)
    g.addEdge(2, 3)
    g.addEdge(3, 4)
    print(g.printGraph())
    print()
    print(f"Size {sys.getsizeof(g)} and Location {id(g)}")
    space_taken.append(sys.getsizeof(g))

min_space = min(space_taken)
print(f"Minimum space taken by {space_taken.index(min_space)} object")
print(space_taken)
print(list(map(lambda x: x/min_space,space_taken)))