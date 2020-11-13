import sys

from PyQt5 import QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class ChatTingWindow(QTabWidget):
    def __init__(self, parent=None):
        super(ChatTingWindow, self).__init__(parent)
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tab3 = QWidget()
        self.addTab(self.tab1, "消息")
        self.addTab(self.tab2, '联系人分组')
        self.addTab(self.tab3, '联系人索引')
        self.show()

    def closeEvent(self, a0: QtGui.QCloseEvent) -> None:  # 关闭对话框
        reply = QMessageBox(QMessageBox.Question, self.tr('退出'), self.tr('您确定要退出吗'), QMessageBox.NoButton, self)
        yes = reply.addButton(self.tr('确定'), QMessageBox.YesRole)
        no = reply.addButton(self.tr('取消'), QMessageBox.NoRole)
        reply.exec_()
        if reply.clickedButton() == yes:
            a0.accept()
        else:
            a0.ignore()


app = QApplication(sys.argv)
mytab = ChatTingWindow()
sys.exit(app.exec_())
