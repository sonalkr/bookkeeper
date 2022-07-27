from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel


class LedgerPage(QWidget):
    def __init__(self):
        super().__init__()

        windowName = QLabel()
        windowName.setText("Ledger Page")
        self.setLayout(QVBoxLayout())
        self.layout().addWidget(windowName)
