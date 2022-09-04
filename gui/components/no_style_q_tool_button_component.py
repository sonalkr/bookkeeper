from typing import Optional
from PySide6.QtWidgets import QToolButton, QWidget


class NoStyleQToolButton(QToolButton):
    def __init__(self, parent: Optional[QWidget] = ...) -> None:
        super().__init__(parent)
    # def __init__(self) -> None:
    #     super().__init__()
        self.setStyleSheet("""
            QToolButton{
                border: none
            }
            QToolButton:hover{
                border: 1px solid black
            }

            """)
