from PySide6.QtWidgets import QTabWidget

from gui.pages.home_page import HomePage


class RootRoute(QTabWidget):
    def __init__(self):
        super().__init__()
        self.setTabPosition(self.South)
        self.addTab(HomePage(), "Homepage")
