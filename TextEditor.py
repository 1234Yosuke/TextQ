# -*- coding: utf-8 -*-

import sys
import codecs
from PySide2.QtCore import Qt
from PySide2.QtWidgets import QApplication, QHBoxLayout, QMainWindow, QPlainTextEdit, QWidget, QAction, QFileDialog, QMessageBox
from PySide2.QtGui import QFont, QKeyEvent

class TextEditor(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        save_act = QAction("セーブ", self)
        save_act.triggered.connect(self.saveFile)

        load_act = QAction("開く", self)
        load_act.triggered.connect(self.loadFile)


        github = QAction("GitHub", self)
        github.triggered.connect(self.GitHubHelp)

        main_font = QFont("メイリオ")

        menu_bar = self.menuBar()
        filemenu = menu_bar.addMenu("ファイル")
        filemenu.addAction(save_act)
        filemenu.addAction(load_act)

        helpmenu = menu_bar.addMenu("ヘルプ")
        helpmenu.addAction(github)


        self.textedit = QPlainTextEdit()

        self.textedit.setFont(main_font)
        self.textedit.setStyleSheet("color:white; background-color:black;")
        self.setWindowTitle("新規ファイル - TextQ")

        ui = QHBoxLayout()
        ui.addWidget(self.textedit)

        widget = QWidget(self)
        widget.setLayout(ui)
        self.setCentralWidget(widget)
        self.show()

    def keyPressEvent(self, event: QKeyEvent) -> None:
        if (
            event.modifiers() == Qt.ControlModifier
            and event.key() == Qt.Key_O
        ):
            self.loadFile()
            return
        elif (
            event.modifiers() == Qt.ControlModifier
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
        with open(filename,encoding="utf-8") as f:
            self.textedit.setPlainText(f.read())
            self.setWindowTitle(filename + " - TextQ")
    
    def GitHubHelp(self):
        QMessageBox.information(self, "Help", "GitHub repo:\nhttps://github.com/1234Yosuke/TextQ")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TextEditor()
    sys.exit(app.exec_())