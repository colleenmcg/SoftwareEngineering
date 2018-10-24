#Colleen McGloin SN: 16325155

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



    def bfs(self, src_node, dest_node, graph=None):  # bfs is returning all paths from root to dest node
        
        graph = self.graph  #create graph
        queue = [(src_node, [src_node])] # creates a queue that contains source node and path from source node
        while queue:  #while queue is not empty
                (vertex, path) = queue.pop(0)   # pop of most recent node that was added to queue
                for next in graph[vertex]:
                        if next == dest_node:   # if next node in graph == dest node
                            yield path + [next] # return the path
                        else:
                            queue.append((next, path + [next])) # append the next node onto the queue



    def toFlatList(self,list): # converts my list of lists into just one list
        flat_list = [item for sublist in list for item in sublist]
        return flat_list


    def commonAncestor(self, xList, yList): # calculates the LCA between 2 Lists
        x_Ancest = GRAPH.toFlatList(self, xList) # converts x list to one list
        y_Ancest = GRAPH.toFlatList(self, yList) # converts x list to one list
    
        for x in x_Ancest: # calculates LCA between 2 lists
            for y in y_Ancest:
                if x == y:
                    LCA = x
        return LCA



    def LCA(self,root,x,y): # calls relevant functions and then returns the LCA of 2 nodes
        xList = GRAPH.bfs(self,root,x)
        yList = GRAPH.bfs(self,root,y)
        LCA = GRAPH.commonAncestor(self, xList, yList)
        return LCA

