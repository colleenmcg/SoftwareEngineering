import LCA

def test_LCA_1() :
    assert  LCA.findLCA(LCA.root,2,3) == 1
    assert  LCA.findLCA(LCA.root,4,5) == 2
    assert  LCA.findLCA(LCA.root,4,6) == 1
    assert  LCA.findLCA(LCA.root,3,4) == 1
    assert  LCA.findLCA(LCA.root,2,4) == 2
