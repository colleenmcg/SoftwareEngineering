import LCA
import pytest
from LCA import Node


def test_LCA_initialize() :
    x = Node(1);
    assert x.key == 1

def test_LCA_no_values_init() :
    with pytest.raises(Exception) as e_info:
        y = Node()

def test_LCA_no_values_find_path() :
    with pytest.raises(Exception) as e_info:
        y = findPath()

def test_LCA_no_values_find_LCA() :
    with pytest.raises(Exception) as e_info:
        y = findLCA()

def test_LCA_find_path() :
    path = [5,2,3]
    root = Node(None)
    assert LCA.findPath(root,path,2) == False

    root = Node(5)
    assert LCA.findPath(root,path,5) == True

    path = []
    root.left = Node(2)
    root.right = Node(3)
    assert LCA.findPath(root,path,3) == [5,3]

    root.left = None
    assert LCA.findPath(root,path,9) == False

    root.right = None
    assert LCA.findPath(root,path,7) == False

    root.left = Node(2)
    root.right = Node(3)
    assert LCA.findPath(root,path,0) == False


def test_LCA_Initial() :
    assert  LCA.findLCA(LCA.root,2,3) == 1
    assert  LCA.findLCA(LCA.root,4,5) == 2
    assert  LCA.findLCA(LCA.root,4,6) == 1
    assert  LCA.findLCA(LCA.root,3,4) == 1
    assert  LCA.findLCA(LCA.root,2,4) == 2

def test_LCA_Root() :
    assert LCA.findLCA(LCA.root,-1,4) == -1
