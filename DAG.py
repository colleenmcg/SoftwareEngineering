from collections import deque
import array as arr
import collections


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


  def bfs(self, src_node, dest_node, graph=None):
    graph = self.graph

    visited = set([src_node])
    queue = collections.deque([src_node])
    while queue:
            vertex = queue.popleft()
            for node in graph[vertex]:
                    if node not in visited:
                        visited.add(node)
                        queue.append(node)

                        if node == dest_node:
                            queue=None
                            return visited


