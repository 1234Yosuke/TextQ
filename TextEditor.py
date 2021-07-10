# -*- coding: utf-8 -*-

import sys
import codecs
from PySide2.QtCore import Qt
from PySide2.QtWidgets import QApplication, QHBoxLayout, QMainWindow, QPlainTextEdit, QWidget, QAction, QFileDialog, \
    QMessageBox
from PySide2.QtGui import QFont, QKeyEvent


class TextEditor(QMainWindow):
    def __init__(self):
        super().__init__()

        self.textedit = QPlainTextEdit()

        self.init_ui()

    def init_ui(self):
        save_act = QAction("セーブ", self)
        save_act.triggered.connect(self.save_file)

        load_act = QAction("開く", self)
        load_act.triggered.connect(self.load_file)

        github = QAction("GitHub", self)
        github.triggered.connect(self.github_help)

        main_font = QFont("メイリオ")

        self.textedit.setStyleSheet("color:white; background-color:black;")
        self.textedit.setFont(main_font)

        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu("ファイル")
        file_menu.addAction(save_act)
        file_menu.addAction(load_act)

        help_menu = menu_bar.addMenu("ヘルプ")
        help_menu.addAction(github)

        self.setWindowTitle("新規ファイル - TextQ")

        ui = QHBoxLayout()
        ui.addWidget(self.textedit)

        widget = QWidget(self)
        widget.setLayout(ui)
        self.setCentralWidget(widget)
        self.show()

    def key_press_event(self, event: QKeyEvent) -> None:
        if (
                event.modifiers() == Qt.ControlModifier
                and event.key() == Qt.Key_O
        ):
            self.load_file()
            return
        elif (
                event.modifiers() == Qt.ControlModifier
                and event.key() == Qt.Key_S
        ):
            self.save_file()
            return
        super().key_press_event(event)

    def save_file(self):
        save_name = QFileDialog.getSaveFileName(self, "SaveFile", "text.txt", "Text Files (*.txt)")[0]
        if not save_name:
            return
        with codecs.open(save_name, "w", "utf-8") as f:
            f.write(QPlainTextEdit.toPlainText(self.textedit))

    def load_file(self):
        filename = QFileDialog.getOpenFileName(self, "Open", "", "Text Files (*.txt)")[0]
        if not filename:
            return
        with open(filename, encoding="utf-8") as f:
            self.textedit.setPlainText(f.read())
            self.setWindowTitle(filename + " - TextQ")

    def github_help(self):
        QMessageBox.information(self, "Help", "GitHub repo:\nhttps://github.com/1234Yosuke/TextQ")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TextEditor()
    sys.exit(app.exec_())
