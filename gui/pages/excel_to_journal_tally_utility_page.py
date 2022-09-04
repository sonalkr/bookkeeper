from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel  # type: ignore

from gui.layouts.stepper_layout import StepperLayout


class ExcelToJournalTallyUtilityPage(QWidget):
    def __init__(self):
        super().__init__()

        windowName = QLabel()
        windowName.setText("Excel to Journal Tally Utility")
        self.setLayout(QVBoxLayout())
        self.layout().addWidget(windowName)

        self.stepperLayout = StepperLayout([])
        self.layout().addWidget(self.stepperLayout)
