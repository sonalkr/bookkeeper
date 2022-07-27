from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel


class InventoryPage(QWidget):
    def __init__(self):
        super().__init__()

        windowName = QLabel()
        windowName.setText("Inventory page")
        self.setLayout(QVBoxLayout())
        self.layout().addWidget(windowName)
