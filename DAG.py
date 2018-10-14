from collections import deque

class GRAPH(object):

  def __init__(self):
    self.graph = {}        # creating new graph

  def add_node(self, node, graph=None): # adding node to graph

    graph=self.graph  # create graph

    if node in graph:
      return False  # if node being added is already present in graph, returns False

    graph[node] = []    # add node to the graph

  def add_edge(self, src_node, dest_node, graph=None):  # adding edge between 2 nodes

    graph = self.graph     # if graph does not exist, create graph

    if src_node not in graph:
      return False  # if source node is not present in graph, return False

    if dest_node not in graph:
        return False  # if destination node is not present in graph, return False

    graph[src_node].append(dest_node)  # create an edge between source and destination node.

#def LCA(src_node, dest_node):   #find LCA in DAG
