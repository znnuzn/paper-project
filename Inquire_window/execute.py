# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'admin_interface.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from query_system import Ui_mainWindow


class mwindow(QtWidgets.QMainWindow, Ui_mainWindow):
    def __init__(self):
        super(mwindow, self).__init__()
        self.setupUi(self)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    my_show = mwindow()
    my_show.show()
    sys.exit(app.exec_())

