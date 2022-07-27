from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel


class VoucherPage(QWidget):
    def __init__(self):
        super().__init__()

        windowName = QLabel()
        windowName.setText("Voucher pages")
        self.setLayout(QVBoxLayout())
        self.layout().addWidget(windowName)
