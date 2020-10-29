from PyQt5.QtWidgets import QApplication, QPushButton, QWidget, QMessageBox
import sys

from PyQt5.uic.Compiler.qtproxies import QtGui


class ChattingWindow(QWidget):
    def __init__(self):
        super(ChattingWindow, self).__init__()
        self.initUi()
    
    def initUi(self) -> None:
        pass
    
    
    
    def closeEvent(self, a0: QtGui.QCloseEvent) -> None:
        reply = QMessageBox(QMessageBox.Question, self.tr('退出'), self.tr('您确定要退出吗'), QMessageBox.NoButton, self)
        yes = reply.addButton(self.tr('确定'), QMessageBox.YesRole)
        no = reply.addButton(self.tr('取消'), QMessageBox.NoRole)
        reply.exec_()
        if reply.clickedButton() == yes:
            a0.accept()
        else:
            a0.ignore()
