from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel


class SheetExcelPage(QWidget):
    def __init__(self):
        super().__init__()

        windowName = QLabel()
        windowName.setText("Sheet Excel Page")
        self.setLayout(QVBoxLayout())
        self.layout().addWidget(windowName)
