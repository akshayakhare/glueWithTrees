from glue.viewers.common.qt.data_viewer import DataViewer
import matplotlib.pyplot as plt

# from circularTree import CircularTree
from document4 import Window
import sys
import networkx as nx
from PyQt4 import QtGui, QtCore


class MyGlueWidget(DataViewer):
    LABEL = "My first data viewer"

    def __init__(self, session, parent=None):
        super(MyGlueWidget, self).__init__(session, parent=parent)
        self.my_widget = Window()
        self.my_widget.show()
        # self.setCentralWidget(self.my_widget)
        # self.add_data()

    def add_data(self):
        print("here?\n")
        self.my_widget.setWindowTitle("MyWindow")
        # self.my_widget.dummyFunc()
        self.my_widget.show()
        print("here????\n")
        return True


# Register the viewer with glue
from glue.config import qt_client
qt_client.add(MyGlueWidget)
