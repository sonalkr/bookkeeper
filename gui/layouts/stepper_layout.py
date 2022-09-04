from typing import List
from PySide6.QtWidgets import QLabel, QWidget, QVBoxLayout, QHBoxLayout, QPushButton


class StepperLayout(QWidget):
    def __init__(self, pages: List[QWidget]):
        super().__init__()
        self.pages: List[QWidget] = []
        self.current_index = 0
        self.setLayout(QVBoxLayout())

        self.upperWindow = QWidget()
        self.upperWindow.setLayout(QVBoxLayout())
        self.lowerWindow = QWidget()
        self.lowerWindow.setLayout(QHBoxLayout())
        self.backButton = QPushButton('Back')
        self.backButton.clicked.connect(self.backPage)  # type: ignore
        self.lowerWindow.layout().addWidget(self.backButton)
        self.nextButton = QPushButton('Next')
        self.nextButton.clicked.connect(self.nextPage)  # type: ignore
        self.lowerWindow.layout().addWidget(self.nextButton)

        self.layout().addWidget(self.upperWindow)
        self.layout().addWidget(self.lowerWindow)
        # self.introPage()

        for page in pages:
            self.pages.append(page)  # type: ignore

        # self.lastPage()

    def nextPage(self):
        if self.current_index >= len(self.pages) - 1:
            return

        self.pages[self.current_index].setParent(None)  # type: ignore
        self.current_index = self.current_index + 1
        self.upperWindow.layout().addWidget(self.pages[self.current_index])

        if self.current_index >= len(self.pages) - 1:
            self.nextButton.setText("Done")
        else:
            self.nextButton.setText("Next")

    def backPage(self):
        if self.current_index <= 0:
            return

        self.nextButton.setText("Next")
        self.pages[self.current_index].setParent(None)  # type: ignore
        self.current_index = self.current_index - 1
        self.upperWindow.layout().addWidget(self.pages[self.current_index])

    def introPage(self):
        firstPage = QWidget()
        firstPage.setLayout(QVBoxLayout())
        firstPage.layout().addWidget(QLabel("start"))
        self.pages.append(firstPage)
        self.upperWindow.layout().addWidget(self.pages[self.current_index])

    def lastPage(self):
        lastPage = QWidget()
        lastPage.setLayout(QVBoxLayout())
        lastPage.layout().addWidget(QLabel("last"))
        self.pages.append(lastPage)
