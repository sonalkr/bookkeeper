from PySide6.QtWidgets import QTabWidget, QToolButton, QWidget, QHBoxLayout, QLabel  # type: ignore
from PySide6.QtCore import Qt
from gui.constant import MAIN_GUI_SHEET_LAUNCH
from gui.pages.home_page import HomePage
from gui.pages.ledger_page import LedgerPage
from gui.pages.excel_to_journal_tally_utility_page import ExcelToJournalTallyUtilityPage
from services.events import Broker


class RootRoute(QTabWidget):
    def __init__(self):
        super().__init__()
        broker = Broker()
        broker.on(MAIN_GUI_SHEET_LAUNCH, self.insertTab)
        # add tab's
        self.setTabPosition(self.South)
        # self.tabCloseRequested.connect(self.deleteTab)  # type: ignore
        self.tabBar().setTabsClosable(True)
        self.tabBar().tabCloseRequested.connect(self.deleteTab)  # type: ignore
        self.addTab(HomePage(), "Homepage")

        self.cornerWindow = QWidget()
        hbox = QHBoxLayout()
        addButton = QToolButton()
        addButton.setText("+")
        addButton.clicked.connect(  # type: ignore
            lambda: self.insertTab("Homepage"))
        hbox.addWidget(addButton)
        hbox.addStretch()
        self.cornerWindow.setLayout(hbox)
        self.setCornerWidget(self.cornerWindow, Qt.BottomRightCorner)
        # self.tabBar().setTabButton(last_index, self. , addButton)

    def insertTab(self, name: str):
        """
        Open new page in new tab
        ctrl + I
        """
        match name:  # type: ignore
            case "Homepage":
                self.addTab(HomePage(), "Homepage")
                # newtab = self.addTab(HomePage(), "Homepage")
                # self.currentIndex(newtab)
                return
            case "LedgerVoucher":
                self.addTab(LedgerPage(), "Ledger Voucher")
                return
            case "ExcelToJournalTallyUtility":
                self.addTab(ExcelToJournalTallyUtilityPage(),
                            "Excel To Journal")
                return

        pass

    def deleteTab(self, index: int):
        """
        ctrl + Q
        """
        self.removeTab(index)

    def switchTab(self):
        """
        move between tab by 
        ctrl + pgUP and ctrl + pgDOWN
        """

        pass
