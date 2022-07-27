from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel


class ProfitAndLossReportPage(QWidget):
    def __init__(self):
        super().__init__()

        windowName = QLabel()
        windowName.setText("Profit and Loss Report page")
        self.setLayout(QVBoxLayout())
        self.layout().addWidget(windowName)
