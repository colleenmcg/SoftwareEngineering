# A binary tree node
class Node:
    # Constructor
    def __init__(self, key):
        self.key =  key
        self.left = None
        self.right = None

# Finds the path from root node to given node
# Stores path in  path[],
# returns true if path is there else returnsfalse
def findPath( root, path, x):

    if root is None:
        return False

    # Store this node in path.
    path.append(root.key)

    # Checking if x matches key of root
    if root.key == x :
        return True

    # Checking if x is found in left or right sub-tree
    if ((root.left != None and findPath(root.left, path, x)) or
            (root.right!= None and findPath(root.right, path, x))):
        return True

    # If x is not in subtree, return False

    path.pop()
    return False

# Returns LCA if node n1 , n2 are present in the given
# binary tre otherwise return -1
def findLCA(root, n1, n2):

    #Creating empty paths
    path1 = []
    path2 = []

# if function findPath returns false, means n1 or n2 is not present in tree hence we return -1
    if (not findPath(root, path1, n1) or not findPath(root, path2, n2)):
        return -1

    # checking what the LCA is of n1 and n2
    i = 0
    while(i < len(path1) and i < len(path2)):
        if path1[i] != path2[i]:
            break
        i += 1
    return path1[i-1]


# loading tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
