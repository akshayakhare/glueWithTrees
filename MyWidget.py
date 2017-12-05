'''import sys
from PyQt4 import QtGui
import matplotlib.pyplot as plt

from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT as NavigationToolbar

import networkx as nx

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


class PrettyWidget(QtGui.QWidget):

    def __init__(self):
        super(PrettyWidget, self).__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(600, 300, 1000, 600)
        self.center()
        self.setWindowTitle('GUI Plotting')

        grid = QtGui.QGridLayout()
        self.setLayout(grid)

        btn1 = QtGui.QPushButton('Plot 1', self)
        btn1.resize(btn1.sizeHint())
        btn1.clicked.connect(self.plot1)
        grid.addWidget(btn1, 2, 0)

        btn2 = QtGui.QPushButton('Plot 2', self)
        btn2.resize(btn2.sizeHint())
        btn2.clicked.connect(self.plot2)
        grid.addWidget(btn2, 2, 1)

        self.figure = plt.figure(figsize=(15, 5))
        self.canvas = FigureCanvas(self.figure)
        self.toolbar = NavigationToolbar(self.canvas, self)
        grid.addWidget(self.canvas, 1, 0, 1, 2)
        grid.addWidget(self.toolbar, 0, 0, 1, 2)

        self.show()

    def plot1(self):
        plt.cla()
        ax = self.figure.add_subplot(111)
        # x = [i for i in range(100)]
        # y = [i**2 for i in x]
        # ax.plot(x, y, 'b.-')
        G = nx.balanced_tree(3, 5)
        pos = graphviz_layout(G, prog='twopi', args='')
        plt.figure(figsize=(8, 8))
        plt.axis('equal')
        ax.plot(nx.draw(G, pos, node_size=100, alpha=0.5,
                        node_color="blue", with_labels=False))
        ax.set_title('Quadratic Plot')
        self.canvas.draw()
        # plt.show()

    def plot2(self):
        plt.cla()
        ax = self.figure.add_subplot(111)
        x = [i for i in range(100)]
        y = [i**0.5 for i in x]
        ax.plot(x, y, 'r.-')
        ax.set_title('Square Root Plot')
        self.canvas.draw()

    def center(self):
        qr = self.frameGeometry()
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


def main():
    app = QtGui.QApplication(sys.argv)
    w = PrettyWidget()
    app.exec_()


if __name__ == '__main__':
    main()
'''

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

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        # We want the axes cleared every time plot() is called
        self.axes.hold(False)

        self.compute_initial_figure()

        #
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

    def compute_initial_figure(self):
        # G = nx.path_graph(10)
        # pos = nx.spring_layout(G)
        # nx.draw(G, pos, ax=self.axes)

        G = nx.balanced_tree(3, 5)
        pos = graphviz_layout(G, prog='twopi', args='')
        # plt.figure(figsize=(8, 8))
        nx.draw(G, pos, node_size=100, alpha=0.5,
                node_color="blue", with_labels=False, ax=self.axes)
        # ax = self.axes('equal'))
        # plt.axis('equal')
        # plt.show()


class ApplicationWindow(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.setWindowTitle("application main window")

        self.file_menu = QtGui.QMenu('&File', self)
        self.file_menu.addAction('&Quit', self.fileQuit,
                                 QtCore.Qt.CTRL + QtCore.Qt.Key_Q)
        self.menuBar().addMenu(self.file_menu)

        self.help_menu = QtGui.QMenu('&Help', self)
        self.menuBar().addSeparator()
        self.menuBar().addMenu(self.help_menu)

        self.help_menu.addAction('&About', self.about)

        self.main_widget = QtGui.QWidget(self)

        l = QtGui.QVBoxLayout(self.main_widget)
        sc = MyStaticMplCanvas(self.main_widget, width=5,
                               height=4, dpi=100)
        l.addWidget(sc)

        self.main_widget.setFocus()
        self.setCentralWidget(self.main_widget)

        self.statusBar().showMessage("All hail matplotlib!", 2000)

    def fileQuit(self):
        self.close()

    def closeEvent(self, ce):
        self.fileQuit()

    def about(self):
        QtGui.QMessageBox.about(self, "About %s" % progname)


qApp = QtGui.QApplication(sys.argv)

aw = ApplicationWindow()
aw.setWindowTitle("%s" % progname)
aw.show()
sys.exit(qApp.exec_())
# qApp.exec_()
