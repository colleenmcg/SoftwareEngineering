
from DAG import GRAPH
import pytest


Graph = None
Graph=GRAPH()

#def test_DAG_initialize() :

# testing initilize function

def test_DAG_add_node() :

# testing add_node function

    Graph.add_node('A') #adding node
    Graph.add_node('B') #adding node
    Graph.add_node('C') #adding node
    assert (Graph.graph == {'A': [],'B': [],'C': []}) # test passes if graph has all nodes added

    assert Graph.add_node('C') == False # function should return false if node that is already present in graph is added.


def test_DAG_add_edge() :

# testing add_edge function

    Graph.add_edge('A', 'B')
    Graph.add_edge('A', 'C')
    assert (Graph.graph == {'A': ['B','C'],'B': [],'C': []})


    assert Graph.add_edge('A', 'D') == False # function should return false if destination node is not present in graph.

    assert Graph.add_edge('E', 'B') == False # function should return false if source node is not present in graph.

    assert Graph.add_edge('E', 'D') == False # function should return false if both source and destination node are not present in graph.


def test_DAG_BFS() :
    
    Graph.add_node('D') #adding node
    Graph.add_node('E') #adding node
    Graph.add_node('F') #adding node
    
    Graph.add_edge('C', 'D')
    Graph.add_edge('B', 'D')
    Graph.add_edge('C', 'E')
    Graph.add_edge('D', 'F')
    
  
    assert  Graph.bfs('A', 'C') == {'A','B','C'}
    assert  Graph.bfs('A', 'D') == {'A','B','C','D'}
    assert  Graph.bfs('A', 'E') == {'A','B','C','D','E'}
    assert  Graph.bfs('A', 'F') == {'A','B','C','D','E','F'}
