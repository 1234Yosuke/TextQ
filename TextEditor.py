# -*- coding: utf-8 -*-

import sys
import codecs
from PySide2.QtCore import Qt
from PySide2.QtWidgets import QApplication, QHBoxLayout, QMainWindow, QTextEdit, QWidget, QAction, QFileDialog
from PySide2.QtGui import QFont

class TextEditor(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        save_act = QAction("Save", self)
        save_act.triggered.connect(self.save)

        main_font = QFont("メイリオ")

        menu_bar = self.menuBar()
        menu = menu_bar.addMenu("File")
        menu.addAction(save_act)


        textedit = QTextEdit()

        textedit.setFont(main_font)

        ui = QHBoxLayout()
        ui.addWidget(textedit)

        widget = QWidget(self)
        widget.setLayout(ui)
        self.setCentralWidget(widget)
        self.show()

    def save(self):
        savename = QFileDialog.getSaveFileName(self, "SaveFile", "text.txt") [0]
        if not savename:
            return
        with codecs.open(savename, "w", "utf-8") as f:
            f.write()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TextEditor()
    sys.exit(app.exec_())