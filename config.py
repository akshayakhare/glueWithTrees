# from glue.qt.widgets.data_viewer import DataViewer
from glue.viewers.common.qt.data_viewer import DataViewer

from MyWidget import MyStaticMplCanvas
import sys
import networkx as nx
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


class MyGlueWidget(DataViewer):
    # class MyGlueWidget(ApplicationWindow):

    LABEL = "My first data viewer"

    def __init__(self, session, parent=None):
        super(MyGlueWidget, self).__init__(session, parent=parent)
        G = nx.balanced_tree(3, 5)
        qApp = QtGui.QApplication(sys.argv)
        self.my_widget = MyStaticMplCanvas(G, QtGui.QWidget(),  width=5,
                                           height=4, dpi=100)
        # sys.exit(qApp.exec_())

        self.setCentralWidget(self.my_widget)
        self.add_data(qApp)
        # sys.exit(qApp.exec_())

    def add_data(self, qApp):
        print("here?\n")
        self.my_widget.setWindowTitle("MyWindowMyRules")
        self.my_widget.show()
        qApp.exec_()
        # sys.exit(qApp.exec_())
        return True


# Register the viewer with glue
from glue.config import qt_client
qt_client.add(MyGlueWidget)
