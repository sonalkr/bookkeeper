from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel


class HomePage(QWidget):
    def __init__(self):
        super().__init__()

        windowName = QLabel()
        windowName.setText("Home")
        self.setLayout(QVBoxLayout())
        self.layout().addWidget(windowName)
