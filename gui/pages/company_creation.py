from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel


class CompanyCreationPage(QWidget):
    def __init__(self):
        super().__init__()

        windowName = QLabel()
        windowName.setText("Companay Creation page")
        self.setLayout(QVBoxLayout())
        self.layout().addWidget(windowName)
