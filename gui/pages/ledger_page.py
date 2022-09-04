from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QGridLayout, QFormLayout, QLabel
from PySide6.QtCore import Qt

from gui.components.max_width_200_q_line_edit_component import MaxWidth200QLineEdit


class LedgerPage(QWidget):
    def __init__(self):
        super().__init__()

        self.hBox = QHBoxLayout()
        # self.hBox.setAlignment(Qt.AlignRight)
        self.vBox1 = QVBoxLayout()
        self.vBox2 = QVBoxLayout()
        self.vBox1.setAlignment(Qt.AlignTop)
        self.vBox2.setAlignment(Qt.AlignTop)
        self.gridBox = QGridLayout()
        self.winCol1 = QWidget()
        self.winCol2 = QWidget()
        self.formWin1 = QFormLayout()

        self.lineEditName = MaxWidth200QLineEdit(self)
        self.formWin1.addRow("Name", self.lineEditName)

        self.lineEditAlias = MaxWidth200QLineEdit(self)
        self.formWin1.addRow("Alias", self.lineEditAlias)

        self.lineEditNote = MaxWidth200QLineEdit(self)
        self.formWin1.addRow("Note", self.lineEditNote)

        self.lineEditDesc = MaxWidth200QLineEdit(self)
        self.formWin1.addRow("Desc", self.lineEditDesc)

        self.lineEditUnder = MaxWidth200QLineEdit(self)
        self.formWin1.addRow("Under", self.lineEditUnder)

        self.win1 = QWidget()
        self.win1.setLayout(self.formWin1)
        self.vBox1.addWidget(self.win1)

        self.winBankDetailLabel = QWidget()
        self.winBankDetailLabel.setLayout(QVBoxLayout())
        self.winBankDetailLabel.layout().addWidget(QLabel("Bank Account Detail"))
        self.vBox1.addWidget(self.winBankDetailLabel)

        self.formWin2 = QFormLayout()

        self.lineEditMailName = MaxWidth200QLineEdit(self)
        self.formWin2.addRow("Mail Name", self.lineEditMailName)

        self.lineEditAddress1 = MaxWidth200QLineEdit(self)
        self.formWin2.addRow("Address", self.lineEditAddress1)

        self.lineEditAddress2 = MaxWidth200QLineEdit(self)
        self.formWin2.addRow("", self.lineEditAddress2)

        self.lineEditState = MaxWidth200QLineEdit(self)
        self.formWin2.addRow("State", self.lineEditState)

        self.lineEditPincode = MaxWidth200QLineEdit(self)
        self.formWin2.addRow("Pincode", self.lineEditPincode)

        self.lineEditContactNumber = MaxWidth200QLineEdit(self)
        self.formWin2.addRow("Contact Number", self.lineEditContactNumber)

        self.win2 = QWidget()
        self.win2.setLayout(self.formWin2)
        self.vBox1.addWidget(self.win2)
        self.winCol1.setLayout(self.vBox1)

        self.formWin3 = QFormLayout()

        self.lineEditMailName = MaxWidth200QLineEdit(self)
        self.formWin3.addRow("Mail Name", self.lineEditMailName)

        self.lineEditAddress1 = MaxWidth200QLineEdit(self)
        self.formWin3.addRow("Address", self.lineEditAddress1)

        self.lineEditAddress2 = MaxWidth200QLineEdit(self)
        self.formWin3.addRow("", self.lineEditAddress2)

        self.lineEditState = MaxWidth200QLineEdit(self)
        self.formWin3.addRow("State", self.lineEditState)

        self.lineEditPincode = MaxWidth200QLineEdit(self)
        self.formWin3.addRow("Pincode", self.lineEditPincode)

        self.lineEditContactNumber = MaxWidth200QLineEdit(self)
        self.formWin3.addRow("Contact Number", self.lineEditContactNumber)

        self.win3 = QWidget()
        self.win3.setLayout(self.formWin3)
        self.vBox2.addWidget(self.win3)
        self.winCol2.setLayout(self.vBox2)

        self.hBox.addWidget(self.winCol1)
        self.hBox.addWidget(self.winCol2)
        # self.hBox2 = QHBoxLayout()
        # self.scrollBarWin = QScrollArea()
        # self.scrollBarWin.setWidget(self)
        # self.hBox2.layout().addWidget(self.scrollBarWin)
        self.setLayout(self.hBox)
        # hbox end
