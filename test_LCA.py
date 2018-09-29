import LCA
import pytest
from LCA import Node


def test_LCA_initialize() :
    x = Node(1);
    assert x.key == 1

def test_LCA_no_values() :
    with pytest.raises(Exception) as e_info:
        y = Node()

def test_LCA_Initial() :
    assert  LCA.findLCA(LCA.root,2,3) == 1
    assert  LCA.findLCA(LCA.root,4,5) == 2
    assert  LCA.findLCA(LCA.root,4,6) == 1
    assert  LCA.findLCA(LCA.root,3,4) == 1
    assert  LCA.findLCA(LCA.root,2,4) == 2

def test_LCA_Root() :
    assert LCA.findLCA(LCA.root,-1,4) == -1
