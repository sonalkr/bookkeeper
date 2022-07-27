from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel


class RatioAnalysisReportPage(QWidget):
    def __init__(self):
        super().__init__()

        windowName = QLabel()
        windowName.setText("Ratio Analysis Report Page")
        self.setLayout(QVBoxLayout())
        self.layout().addWidget(windowName)
