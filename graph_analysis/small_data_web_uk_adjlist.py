import sys
import os

PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))

from graph_builders.adjacency_list_graph import AdjacencyList
from collections import Counter
import os
import time
import pickle
WRITE_FILE='../adj_list_small_web_uk.txt'
DEGREE_FILE_SMALL ='../degree_file_from_adjlist_small.pickle'
SMALL_GRAPH_FILE = '/Users/mghosh2/Downloads/web-uk-2005/web-uk-2005.mtx'


def get_path(path):
    path =os.path.join(os.path.dirname(__file__),path)
    path=os.path.abspath(path)
    return path

# get path for one level above in directory
WRITE_FILE=get_path(WRITE_FILE)
DEGREE_FILE_BIG = get_path(DEGREE_FILE_SMALL)

def save_pickle(obj,path):
    with open(path,'wb') as f:
        pickle.dump(obj,f)

def create_graph(datapath,line_to_skip=0):
    graph_out= AdjacencyList()
    with open(datapath, 'r') as rf:
        for index,line in enumerate(rf):
            if index >= line_to_skip:    #leaving the first row
                i,j = line.split(" ")
                i , j = int(i),int(j.replace('\n',''))
                graph_out.addEdge(i,j)
    return graph_out

if __name__ == '__main__':
    graph = create_graph(SMALL_GRAPH_FILE,line_to_skip=2)
    with open(WRITE_FILE,'w') as wf:
        wf.write("Time started  " + str(time.ctime()))
        wf.write("##"*40)
        start=time.time()
        all_degrees = graph.degree_of_all_nodes()
        degree_values = dict(Counter(all_degrees.values()))
        save_pickle(degree_values,DEGREE_FILE_BIG)
        print("The degree Values are: ", degree_values)
        wf.write("Time taken  " + str(time.time() - start) + " Secs")
        wf.write("--" * 40)
        wf.write( "The degree Values are: " +  str(degree_values) )
        wf.write("--"*40)
        start = time.time()
        total_triangles=graph.countNumTraingles()
        print("The total number of triangles are : ", total_triangles)
        wf.write("The total number of triangles are : " + str(total_triangles))
        wf.write("Time taken  " + str(time.time() - start) + " Secs")
        wf.write("Time Ended  " + str(time.ctime()))
        wf.write("##"*40)



