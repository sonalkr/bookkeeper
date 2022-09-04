from PySide6.QtWidgets import QTabWidget
from gui.layouts.toolbar.data_toolbar_layout import DataToolbarLayout
from gui.layouts.toolbar.formula_toolbar_layout import FormulaToolbarLayout

from gui.layouts.toolbar.file_toolbar_layout import FileToolbarLayout
from gui.layouts.toolbar.help_toolbar_layout import HelpToolbarLayout
from gui.layouts.toolbar.home_toolbar_layout import HomeToolbarLayout
from gui.layouts.toolbar.insert_toolbar_layout import InsertToolbarLayout
from gui.layouts.toolbar.page_layout_toolbar_layout import PageLayoutToolbarLayout
from gui.layouts.toolbar.tax_toolbar_layout import TaxToolbarLayout
from gui.layouts.toolbar.view_toolbar_layout import ViewToolbarLayout
from gui.layouts.toolbar.tally_utility_toolbar_layout import TallyUtilityToolbarLayout


class ToolBarLayout(QTabWidget):
    def __init__(self):
        super().__init__()
        self.addTab(TallyUtilityToolbarLayout(), "Tally Utility")
        self.addTab(FileToolbarLayout(), "File")
        self.addTab(HomeToolbarLayout(), "Home")
        self.addTab(TaxToolbarLayout(), "Tax")
        self.addTab(InsertToolbarLayout(), "Insert")
        self.addTab(PageLayoutToolbarLayout(), "Page Layout")
        self.addTab(DataToolbarLayout(), "Data")
        self.addTab(FormulaToolbarLayout(), "Formula")
        self.addTab(ViewToolbarLayout(), "View")
        self.addTab(HelpToolbarLayout(), "Help")
        self.setMaximumHeight(150)
