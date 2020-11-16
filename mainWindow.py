import sys

from PyQt5 import QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QApplication
from qtpy import QtWidgets

from chattingWindow import *


class ListWidget(QListWidget):
    def __init__(self, parent=None):
        super(ListWidget, self).__init__(parent)
        self.itemDoubleClicked.connect(self.doubleClicked)

    def getIp(self, name: str) -> int:
        pass

    def doubleClicked(self, item: QListWidgetItem) -> None:
        # app: QApplication = QtWidgets.QApplication(sys.argv)
        self.ui: Ui_Form = Ui_Form(item.text(), self.getIp(item.text()))
        self.ui.show()
        # sys.exit(app.exec_())

    def add_person(self, persons: list) -> None:
        for person in persons:
            self.addItem(person)


class MainWindow(QTabWidget):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.tab1 = ListWidget()
        self.tab2 = ListWidget()
        self.tab3 = ListWidget()
        self.addTab(self.tab1, "消息")
        self.addTab(self.tab2, '联系人分组')
        self.addTab(self.tab3, '联系人索引')
        self.resize(300, 800)
        self.setWindowTitle('chatting room')
        self.tab1.add_person(['1', '123'])
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
mainWindow = MainWindow()
sys.exit(app.exec_())
