import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from gui.layouts.toolbar_layout import ToolBarLayout

from gui.routes.root_route import RootRoute


def gui():
    app = QApplication(sys.argv)
    Mwin = QMainWindow()
    Mwin.setMinimumHeight(500)
    Mwin.setMinimumWidth(600)
    routes = RootRoute()

    vbox = QVBoxLayout()
    vbox.addWidget(ToolBarLayout())
    vbox.addWidget(routes)

    win = QWidget()
    win.setLayout(vbox)
    Mwin.setCentralWidget(win)
    Mwin.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    gui()
