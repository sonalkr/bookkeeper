from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel


class LedgerReportPage(QWidget):
    def __init__(self):
        super().__init__()

        windowName = QLabel()
        windowName.setText("Ledger Report Page")
        self.setLayout(QVBoxLayout())
        self.layout().addWidget(windowName)
