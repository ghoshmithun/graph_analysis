# graph_analysis
Graph analysisfrom scratch with python

Learning Objectives:

 

    Understand the space complexity of Graph Representations and the performance of operations under each representation.

    Choose the right representation for specific datasets and high-level operations.

    Implement, efficiently, operations on large graphs.

 

 

    Implement a Graph data type with three different representations: adjacency matrix, adjacency list, and edge list. The Graph ADT should include the following operations:
          boolean isEdge(i,j); // returns true if and only if (i,j) is an edge.
        void addEdge(i,j);  // add an edge (i,j)
        void deleteEdgE(i,j); // remove an edge(i,j)
        int degree(i); // returns degree of vertex i 
        int[] adjacent(i); // returns the list of vertices adjacent to vertex i
    Using the Graph ADT,  write a program – in any language of your choice to implement the  following: 

    a) Compute the degree distribution p(d) for any given graph.
    b) Count the number of triangles in any given graph. [A triangle is a set of three edges (i,j) , (j,k) and (i,k) for vertices i,j, and k. 

You must not use any libraries or built-in data structures other than arrays and (linked)lists.

    go to the Google folder:

https://drive.google.com/drive/folders/1psRIEL65sQCTA7pG6uF8yw5ElVB7vwq3?usp=sharing (Links to an external site.). 

Choose one of the small-to-medium-sized graph datasets from the datasets sub-folder.  [Enter your BITS ID against the set you have chosen in the spreadsheet:


 Each data set may be chosen by at most three students.

    a) Run your program to output the degree distribution and triangle count on your graph.

    For Degree Distribution 20 mins and 2 mins. Counting of traingles is taking too long

    b)  Measure the time taken for each of the two computations under each of the three representations. 
    c) Plot the degree distribution curve and do curve fitting to a power-law distribution and determine the constant. You may use any tool to do curve fitting.
    Go to the subfolder named large within the datasets Google folder. Choose one of the large datasets from the large subfolder. Add and entry in the spreadsheet with folder chosen and your BITS ID.     

https://docs.google.com/spreadsheets/d/1bh2LzeJhgwUNDscTkOA_RHBXhyf7auB352CjyLpfmE4/edit?usp=sharing (Links to an external site.) 
