from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QGridLayout
from PySide6.QtCore import Qt

from gui.components.no_style_q_tool_button_component import NoStyleQToolButton
from gui.constant import MAIN_GUI_SHEET_LAUNCH
from interface.Message import IMessage
from services.events import Broker


class TallyUtilityToolbarLayout(QWidget):
    def __init__(self):
        super().__init__()
        self.broker = Broker()  # type: ignore

        self.vBox = QVBoxLayout()
        self.vBox.setAlignment(Qt.AlignLeft)
        self.hBox1 = QHBoxLayout()
        self.hBox2 = QHBoxLayout()
        self.gridBox = QGridLayout()
        self.winRow1 = QWidget()
        self.winRow2 = QWidget()

        # Buttons start
        self.buttonAddVoucher = NoStyleQToolButton(self)
        self.buttonAddVoucher.setText("Journal")
        self.buttonAddVoucher.clicked.connect(  # type: ignore
            lambda: self.broker.emit(
                IMessage(name=MAIN_GUI_SHEET_LAUNCH,
                         value="ExcelToJournalTallyUtility")
            )
        )
        self.buttonAddLedger = NoStyleQToolButton(self)
        self.buttonAddLedger.setText("Add Ledger")
        self.buttonAddLedger.clicked.connect(  # type: ignore
            lambda: self.broker.emit(
                IMessage(name=MAIN_GUI_SHEET_LAUNCH, value="LedgerVoucher")
            )
        )
        # Buttons end

        # Row 1
        self.hBox1.layout().addWidget(self.buttonAddVoucher)
        self.winRow1.setLayout(self.hBox1)

        # Row 1 end

        # Row 2
        self.hBox2.layout().addWidget(self.buttonAddLedger)
        self.winRow2.setLayout(self.hBox2)

        # Row 2 end

        #
        self.vBox.layout().addWidget(self.winRow1)
        self.vBox.layout().addWidget(self.winRow2)
        self.setLayout(self.vBox)
        #
