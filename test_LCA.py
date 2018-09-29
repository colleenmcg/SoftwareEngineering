import LCA
import pytest
from LCA import Node


def test_LCA_initialize() :

# testing initilize function by
# inserting Node with val 1 into tree.

    x = Node(1);
    assert x.key == 1

def test_LCA_no_values() :

# if a function is called with no parameters
# we must output an exception.

    with pytest.raises(Exception) as e_info:
        y = Node()

    with pytest.raises(Exception) as e_info:
        y = findPath()

    with pytest.raises(Exception) as e_info:
        y = findLCA()

def test_LCA_find_path() :

    path = []

# Function should output a False statement if
# we dont input a root Node.

    root = Node(None)
    assert LCA.findPath(root,path,2) == False

# Function outputs the path if we have
# a one node tree that matches the key we are looking for.

    root = Node(5)
    assert LCA.findPath(root,path,5) == [5]

# Function outputs the path that it has found from root to the
# key we are looking for.

    path=[]
    root.left = Node(2)
    root.right = Node(3)
    assert LCA.findPath(root,path,3) == [5,3]

    path=[]
    root.right.right = Node(7)
    assert LCA.findPath(root,path,7) == [5,3,7]

# Function outputs a False statement if we are looking
# for a key that is not in the tree.


    assert LCA.findPath(root,path,9) == False

    assert LCA.findPath(root,path,-7) == False


    root.right.right = None

    assert LCA.findPath(root,path,7) == False


    root.left = Node(6)
    root.right = Node(7)
    assert LCA.findPath(root,path,0) == False



def test_LCA_find_LCA() :

#inserting values into tree.

    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)

# Function outputs -1 if we try to find the LCA of
# 2 nodes and one or both nodes are not in the tree.

    assert LCA.findLCA(root, 11, 17) == -1

# Function outputs the LCA of 2 nodes present in the tree.

    assert  LCA.findLCA(root,2,3) == 1

    assert  LCA.findLCA(root,4,5) == 2

    assert  LCA.findLCA(root,4,6) == 1

    assert  LCA.findLCA(root,3,4) == 1

    assert  LCA.findLCA(root,2,4) == 2
