from collections import deque

class DAG(object):

  def __init__(self):
    self.new_graph()        # creating new graph

  def add_node(self, node, graph=None): # adding node to graph
    if not graph:
      graph=self.graph  # if graph does not exist, create graph
    if node in graph:
      raise KeyError('node %s exists in graph' % node)  # if node being added is already present in graph, output error
    graph[node] = []    # add node to the graph

  def add_edge(self, src_node, dest_node, graph=None):  # adding edge between 2 nodes
    if not graph:
      graph = self.new_graph     # if graph does not exist, create graph
    if src_node not in graph:
      raise KeyError('source node %s does not exist in graph' % src_node)   # if source node is not present in graph, output error
    if dest_node not in graph:
      raise KeyError('dest node %s does not exist in graph' % dest_node)    # if destination node is not present in graph, output error
    graph[src_node].add(dest_node)  # create an edge between source and destination node.

def LCA(src_node, dest_node):   #find LCA in DAG
