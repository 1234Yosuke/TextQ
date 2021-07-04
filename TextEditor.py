# -*- coding: utf-8 -*-

import sys
import codecs
from PySide2.QtCore import Qt
from PySide2.QtWidgets import QApplication, QHBoxLayout, QMainWindow, QPlainTextEdit, QWidget, QAction, QFileDialog
from PySide2.QtGui import QFont, QKeyEvent

class TextEditor(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        save_act = QAction("Save", self)
        save_act.triggered.connect(self.saveFile)

        main_font = QFont("メイリオ")

        menu_bar = self.menuBar()
        menu = menu_bar.addMenu("File")
        menu.addAction(save_act)


        self.textedit = QPlainTextEdit()

        self.textedit.setFont(main_font)

        ui = QHBoxLayout()
        ui.addWidget(self.textedit)

        widget = QWidget(self)
        widget.setLayout(ui)
        self.setCentralWidget(widget)
        self.show()

    def keyPressEvent(self, event: QKeyEvent) -> None:
        if (
            event.modifiers() == Qt.ControlModifier
            and event.key() == Qt.Key_0
        ):
            self.loadFile()
            return
        elif (
            event.modifiters() == Qt.ControlModifier
            and event.key() == Qt.Key_S
        ):
            self.saveFile()
            return
        super().keyPressEvent(event)

    def saveFile(self):
        savename = QFileDialog.getSaveFileName(self, "SaveFile", "text.txt", "Text Files (*.txt)") [0]
        if not savename:
            return
        with codecs.open(savename, "w", "utf-8") as f:
            f.write(QPlainTextEdit.toPlainText(self.textedit))
    
    def loadFile(self):
        filename = QFileDialog.getOpenFileName(self, "Open", "", "Text Files (*.txt)") [0]
        if not filename:
            return
        with open(filename) as f:
            QPlainTextEdit.setPlainText(f.read())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TextEditor()
    sys.exit(app.exec_())