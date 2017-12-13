import matplotlib.pyplot as plt
import networkx as nx
import sys
from PyQt4 import QtGui, QtCore

try:
    import pygraphviz
    from networkx.drawing.nx_agraph import graphviz_layout
except ImportError:
    try:
        import pydot
        from networkx.drawing.nx_pydot import graphviz_layout
    except ImportError:
        raise ImportError("This example needs Graphviz and either "
                          "PyGraphviz or pydot")


class CircularTree(QtGui.QWidget):

    plt2 = plt

    def __init__(self, parent=None):
        super(CircularTree, self).__init__()
        # self.other_plt = plt
        print("reached in init?")
        G = nx.balanced_tree(3, 5)
        pos = graphviz_layout(G, prog='twopi', args='')
        self.plt2.figure(figsize=(8, 8))
        nx.draw(G, pos, node_size=100, alpha=0.5,
                node_color="blue", with_labels=False)
        self.plt2.axis('equal')
        print("done with init?")
        self.plt2.show()
        # return self

    def dummyFunc(self):
        print("inside dummy")


# app = QtGui.QApplication(sys.argv)
# d = CircularTree(QtGui.QWidget())
# d.plt2.show()
# d.dummyFunc()
# d.du
