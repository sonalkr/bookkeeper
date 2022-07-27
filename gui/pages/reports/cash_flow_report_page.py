from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel


class CashFlowReportPage(QWidget):
    def __init__(self):
        super().__init__()

        windowName = QLabel()
        windowName.setText("Cash Flow Report Page")
        self.setLayout(QVBoxLayout())
        self.layout().addWidget(windowName)
