import sys
import os
import random
from PyQt4 import QtGui, QtCore

from numpy import arange, sin, pi
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import networkx as nx

from scipy.cluster import hierarchy
import numpy as np


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

progname = os.path.basename(sys.argv[0])
progversion = "0.1"


class MyMplCanvas(FigureCanvas):
    """Ultimately, this is a QWidget (as well as a FigureCanvasAgg, etc.)."""

    def __init__(self, G=None, parent=None, width=5, height=4, dpi=100):
        # def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        # We want the axes cleared every time plot() is called
        self.axes.hold(False)

        self.compute_initial_figure(G)

        FigureCanvas.__init__(self, fig)
        self.setParent(parent)

        FigureCanvas.setSizePolicy(self,
                                   QtGui.QSizePolicy.Expanding,
                                   QtGui.QSizePolicy.Expanding)
        #    figsize=(8, 8))
        FigureCanvas.updateGeometry(self)

    def compute_initial_figure(self):
        pass


class MyStaticMplCanvas(MyMplCanvas):
    """Simple canvas with a sine plot."""

    def compute_initial_figure(self, G):
        # G = nx.path_graph(10)
        # pos = nx.spring_layout(G)
        # nx.draw(G, pos, ax=self.axes)

        # G = nx.balanced_tree(3, 5)
        pos = graphviz_layout(G, prog='twopi', args='')
        # plt.figure(figsize=(8, 8))
        if G is None:
            print("I'll do nothing")
        else:
            nx.draw(G, pos, node_size=100, alpha=0.5,
                    node_color="blue", with_labels=False, ax=self.axes)
        # ax = self.axes('equal'))
        # plt.axis('equal')
        # plt.show()

    def __init__(self, G=None, parent=None, width=5, height=4, dpi=100):
        # do nothing
        print("G in mystaticmplcanvas", G)
        super(MyStaticMplCanvas, self).__init__(
            G, parent=None, width=5, height=4, dpi=100)


qApp = QtGui.QApplication(sys.argv)

G = nx.balanced_tree(3, 5)

# # aw = ApplicationWindow()
aw = MyStaticMplCanvas(G, QtGui.QWidget(),  width=5,
                       height=4, dpi=100)
# aw.setWindowTitle("%s" % progname)
# aw.show()
# sys.exit(qApp.exec_())
# qApp.exec_()
