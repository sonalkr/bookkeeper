from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel


class ChallanPage(QWidget):
    def __init__(self):
        super().__init__()

        windowName = QLabel()
        windowName.setText("Challan Page")
        self.setLayout(QVBoxLayout())
        self.layout().addWidget(windowName)
