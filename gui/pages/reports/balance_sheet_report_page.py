from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel


class BalanceSheetReportPage(QWidget):
    def __init__(self):
        super().__init__()

        windowName = QLabel()
        windowName.setText("Balance Sheet Report Pages")
        self.setLayout(QVBoxLayout())
        self.layout().addWidget(windowName)
