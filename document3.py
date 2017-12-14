"""
Created on Thu Dec 12 08:38:21 2013
 
@author: Sukhbinder Singh
 
Simple QTpy and MatplotLib example with Zoom/Pan
 
Built on the example provided at
How to embed matplotib in pyqt - for Dummies
http://stackoverflow.com/questions/12459811/how-to-embed-matplotib-in-pyqt-for-dummies
 
"""
import sys
from PyQt4 import QtGui

from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt
import networkx as nx

import pygraphviz
from networkx.drawing.nx_agraph import graphviz_layout

import random


class Window(QtGui.QWidget):
    # G2 = nil

    def __init__(self, parent=None):
        super(Window, self).__init__(parent)

        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)

        self.toolbar = NavigationToolbar(self.canvas, self)
        # self.toolbar.hide()

        # Just some button
        self.button = QtGui.QPushButton('Plot')
        self.button.clicked.connect(self.plot)

        self.button1 = QtGui.QPushButton('Zoom')
        self.button1.clicked.connect(self.zoom)

        self.button2 = QtGui.QPushButton('Pan')
        self.button2.clicked.connect(self.pan)

        self.button3 = QtGui.QPushButton('Home')
        self.button3.clicked.connect(self.home)

        self.button4 = QtGui.QPushButton('Home')
        self.button3.clicked.connect(self.home)
        # tabs = QtGui.QTabWidget()
        # tab1 = QtGui.QWidget()
        # tab2 = QtGui.QWidget()

        # set the layout
        layout = QtGui.QVBoxLayout()
        layout.addWidget(self.toolbar)
        layout.addWidget(self.canvas)
        layout.addWidget(self.button)
        layout.addWidget(self.button1)
        layout.addWidget(self.button2)
        layout.addWidget(self.button3)

        self.setLayout(layout)

    def home(self):
        self.toolbar.home()

    def zoom(self):
        self.toolbar.zoom()

    def pan(self):
        self.toolbar.pan()

    def addData(self, G=None):
        self.G2

    def plot(self):
        ''' plot some random stuff '''
        G = nx.balanced_tree(3, 5)
        pos = graphviz_layout(G, prog='twopi', args='')
        # self.plt2.figure(figsize=(8, 8))
        nx.draw(G, pos, node_size=100, alpha=0.5,
                node_color="blue", with_labels=False)
        # data = [random.random() for i in range(25)]
        # ax = self.figure.add_subplot(111)
        # ax.hold(False)
        # ax.plot(data, '*-')
        self.canvas.draw()

    def addData(self, G=None):
        G2 = G
        print("G2 is ->", G2)


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)

    main = Window()
    main.setWindowTitle('Simple QTpy and MatplotLib example with Zoom/Pan')
    # G = nx.balanced_tree(3, 5)
    # print("G is type", dir(G))
    # main.addData(G)
    main.show()

    sys.exit(app.exec_())
