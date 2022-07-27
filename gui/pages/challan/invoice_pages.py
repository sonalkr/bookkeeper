from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel


class InvoicePage(QWidget):
    def __init__(self):
        super().__init__()

        windowName = QLabel()
        windowName.setText("Invoice Page")
        self.setLayout(QVBoxLayout())
        self.layout().addWidget(windowName)
