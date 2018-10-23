
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
    Graph.add_node('G') #adding node
    Graph.add_node('H') #adding node
    Graph.add_node('I') #adding node
    
    Graph.add_edge('B', 'H') #adding edge
    Graph.add_edge('C', 'I') #adding edge
    Graph.add_edge('D', 'H') #adding edge
    Graph.add_edge('D', 'I') #adding edge
    Graph.add_edge('D', 'E') #adding edge
    Graph.add_edge('E', 'F') #adding edge
    Graph.add_edge('E', 'G') #adding edge
    Graph.add_edge('F', 'H') #adding edge
    Graph.add_edge('G', 'I') #adding edge

    
  
    assert  list(Graph.bfs('A', 'C')) == [['A','C']]
    assert  list(Graph.bfs('D', 'H')) == [['D','H'],['D','E','F','H']]
    assert  list(Graph.bfs('A', 'H')) == [['A','B','H']]




def test_to_Flat_List() :
    temp = list(Graph.bfs('D', 'H'))
    assert list(Graph.toFlatList(temp)) == ['D','H','D','E','F','H']

def test_common_Ancestor() :
    
    assert list(Graph.commonAncestor([['A','E'],['A','B','E','F']],[['A','C','F']])) == ['F']


def test_LCA() :

    assert list(Graph.LCA('D','F','G')) == ['E']
    assert list(Graph.LCA('A','H','I')) == ['A']
    assert list(Graph.LCA('D','H','I')) == ['E']


