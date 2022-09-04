import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from gui.layouts.toolbar_layout import ToolBarLayout

from gui.routes.root_route import RootRoute
from services.events import Broker
from gui.constant import MAIN_GUI_SHEET_LAUNCH


def gui():
    broker = Broker()
    broker.on(MAIN_GUI_SHEET_LAUNCH, printoutput)
    app = QApplication(sys.argv)
    Mwin = QMainWindow()
    Mwin.setMinimumHeight(600)
    Mwin.setMinimumWidth(800)
    routes = RootRoute()

    vbox = QVBoxLayout()
    vbox.addWidget(ToolBarLayout())
    vbox.addWidget(routes)

    win = QWidget()
    win.setLayout(vbox)
    Mwin.setCentralWidget(win)
    Mwin.show()
    sys.exit(app.exec())


def printoutput(a: str) -> None:
    print(a)


if __name__ == "__main__":
    gui()
