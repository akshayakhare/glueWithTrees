# from glue.qt.widgets.data_viewer import DataViewer
from glue.viewers.common.qt.data_viewer import DataViewer

from MyWidget import MyStaticMplCanvas

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


class MyGlueWidget(DataViewer):
    # class MyGlueWidget(ApplicationWindow):

    def __init__(self, session, parent=None):
        super(MyGlueWidget, self).__init__(session, parent=parent)
        G = nx.balanced_tree(3, 5)
        self.my_widget = MyStaticMplCanvas(G, QtGui.QWidget(),  width=5,
                                           height=4, dpi=100)
        self.setCentralWidget(self.my_widget)

    def add_data(self, data):
        self.my_widget.plot(data)
        return True


# Register the viewer with glue
from glue.config import qt_client
qt_client.add(MyGlueWidget)
