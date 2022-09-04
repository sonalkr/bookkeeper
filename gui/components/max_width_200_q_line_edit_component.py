from typing import Optional
from PySide6.QtWidgets import QLineEdit, QWidget


class MaxWidth200QLineEdit(QLineEdit):

    def __init__(self, parent: Optional[QWidget] = ...) -> None:
        super().__init__(parent)
        self.setMaximumWidth(200)
