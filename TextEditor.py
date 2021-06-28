# -*- coding: utf-8 -*-

import sys
from typing import Text
from PySide2.QtCore import Qt
from PySide2.QtWidgets import QApplication, QHBoxLayout, QMainWindow, QTextEdit, QWidget
from PySide2.QtGui import QFont                                                   
class TextEditor(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        TextEdit = QTextEdit()

        mainfont = QFont("メイリオ")

        TextEdit.setFont(mainfont)

        UI = QHBoxLayout()
        UI.addWidget(TextEdit)

        widget = QWidget(self)
        widget.setLayout(UI)
        self.setCentralWidget(widget)
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TextEditor()
    sys.exit(app.exec_())