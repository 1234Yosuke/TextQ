# -*- coding: utf-8 -*-

from PySide2.QtWidgets import (QMainWindow, QApplication, QTextEdit, QGridLayout, QWidget)
import os
import sys

programName = "TextQ"

class TextEditor(QWidget):

    def UI(self):

        exitAct = QMainWindow.QAction("&Exit")
        exitAct.setShortcut("Ctrl+Q")
        exitAct.triggered.connect(QApplication.quit())

        menu = QMainWindow.menuBar()
        fileMenu = menu.addMenu("&File")
        fileMenu.addAction(exitAct)

        editor = QTextEdit()

        grid = QGridLayout()
        grid.setSpacing(10)
        grid.addWidget(editor,1,0)
        
        self.setLayout(grid)
        self.resize(300, 300)
        self.setWindowTitle(programName)
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    tq = TextEditor()
    sys.exit(app.exec_())