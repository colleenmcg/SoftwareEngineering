#Colleen McGloin SN: 16325155
from DAG import GRAPH
import pytest


Graph = None
Graph=GRAPH()


def test_DAG_add_node() :

# testing add_node function

    Graph.add_node('A') #adding node
    Graph.add_node('B') #adding node
    Graph.add_node('C') #adding node
    assert (Graph.graph == {'A': [],'B': [],'C': []}) # test passes if graph has all nodes added

    assert Graph.add_node('C') == False # function should return false if node that is already present in graph is added.


def test_DAG_add_edge() :

# testing add_edge function

    Graph.add_edge('A', 'B') #adding edge
    Graph.add_edge('A', 'C') #adding edge
    assert (Graph.graph == {'A': ['B','C'],'B': [],'C': []})  # test passes if graph has all edges added


    assert Graph.add_edge('A', 'D') == False # function should return false if destination node is not present in graph.

    assert Graph.add_edge('E', 'B') == False # function should return false if source node is not present in graph.

    assert Graph.add_edge('E', 'D') == False # function should return false if both source and destination node are not present in graph.


def test_DAG_BFS() :
    
# testing bfs function
    
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

    
  
    assert  list(Graph.bfs('A', 'C')) == [['A','C']] # function should return a list made up of path(s) from A node to C node
    assert  list(Graph.bfs('D', 'H')) == [['D','H'],['D','E','F','H']] #  function should return a list made up of paths from D node to H node
    assert  list(Graph.bfs('A', 'H')) == [['A','B','H']] #  function should return a list made up of path(s) from A node to H node


def test_to_Flat_List() :
    
# testing to_Flat_List function

    temp = list(Graph.bfs('D', 'H')) # getting list made up of multiple paths from D to H and assigning list to temp
    assert list(Graph.toFlatList(temp)) == ['D','H','D','E','F','H'] # this function converts a list that contains multiple lists into just one list

def test_common_Ancestor() :
    
# testing common_Ancestor function
    
    assert list(Graph.commonAncestor([['A','E'],['A','B','E','F']],[['A','C','F']])) == ['F'] #this function returns 'F' which is the Lowest Common Ancestor of the 2 paths i inputted into the function


def test_LCA() :
    
# testing LCA function

    assert list(Graph.LCA('D','F','G')) == ['E'] # this function returns 'E' which is the LCA of the 2 nodes F and G from the root D
    assert list(Graph.LCA('A','H','I')) == ['A'] # this function returns 'A' which is the LCA of the 2 nodes H and I from the root A
    assert list(Graph.LCA('D','H','I')) == ['E'] # this function returns 'E' which is the LCA of the 2 nodes H and I from the root D


