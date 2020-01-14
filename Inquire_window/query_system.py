# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'query_system.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import pymysql
import decimal
import webbrowser
import time




msglog = ''#日志信息

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(1245, 525)
        mainWindow.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout.addWidget(self.line_2, 1, 0, 1, 1)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.comboBox_5 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_5.setAutoFillBackground(False)
        self.comboBox_5.setObjectName("comboBox_5")
        self.horizontalLayout_9.addWidget(self.comboBox_5)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setMaximumSize(QtCore.QSize(75, 23))
        self.pushButton.setAutoFillBackground(True)
        self.pushButton.setIconSize(QtCore.QSize(16, 16))
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_9.addWidget(self.pushButton)
        self.gridLayout_3.addLayout(self.horizontalLayout_9, 0, 0, 1, 1)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_10.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_10.addWidget(self.pushButton_3)
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout_10.addWidget(self.pushButton_5)
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_10.addWidget(self.pushButton_4)
        self.gridLayout_3.addLayout(self.horizontalLayout_10, 1, 0, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_3, 2, 0, 1, 3)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setAutoFillBackground(True)
        self.pushButton_9.setObjectName("pushButton_9")
        self.verticalLayout_2.addWidget(self.pushButton_9)
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setAutoFillBackground(True)
        self.pushButton_7.setObjectName("pushButton_7")
        self.verticalLayout_2.addWidget(self.pushButton_7)
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setAutoFillBackground(True)
        self.pushButton_8.setObjectName("pushButton_8")
        self.verticalLayout_2.addWidget(self.pushButton_8)
        self.gridLayout.addLayout(self.verticalLayout_2, 2, 4, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setMaximumSize(QtCore.QSize(60, 48))
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setMaximumSize(QtCore.QSize(218, 20))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalLayout.addWidget(self.comboBox)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setMaximumSize(QtCore.QSize(60, 49))
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.dateEdit_2 = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit_2.setMaximumSize(QtCore.QSize(88, 20))
        self.dateEdit_2.setObjectName("dateEdit_2")
        # 设置弹出日历窗口
        self.dateEdit_2.setCalendarPopup(True)
        # 设置最小及最大日期
        self.dateEdit_2.setMinimumDate(QtCore.QDate.currentDate().addYears(-40))
        self.dateEdit_2.setMaximumDate(QtCore.QDate.currentDate())
        # 设置默认显示时间
        self.dateEdit_2.setDate(QtCore.QDate.currentDate().addYears(-40))
        self.horizontalLayout_4.addWidget(self.dateEdit_2)
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setMaximumSize(QtCore.QSize(30, 49))
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_4.addWidget(self.label_8)
        self.dateEdit = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit.setMaximumSize(QtCore.QSize(88, 20))
        self.dateEdit.setObjectName("dateEdit")
        # 设置弹出日历窗口
        self.dateEdit.setCalendarPopup(True)
        # 设置最小及最大日期
        self.dateEdit.setMinimumDate(QtCore.QDate.currentDate().addYears(-40))
        self.dateEdit.setMaximumDate(QtCore.QDate.currentDate())
        # 设置默认显示时间
        self.dateEdit.setDate(QtCore.QDate.currentDate())
        self.horizontalLayout_4.addWidget(self.dateEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setMaximumSize(QtCore.QSize(60, 48))
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_5.addWidget(self.label_5)
        self.comboBox_3 = QtWidgets.QComboBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_3.sizePolicy().hasHeightForWidth())
        self.comboBox_3.setSizePolicy(sizePolicy)
        self.comboBox_3.setMaximumSize(QtCore.QSize(218, 20))
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.horizontalLayout_5.addWidget(self.comboBox_3)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setMaximumSize(QtCore.QSize(60, 48))
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_6.addWidget(self.label_6)
        self.comboBox_4 = QtWidgets.QComboBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_4.sizePolicy().hasHeightForWidth())
        self.comboBox_4.setSizePolicy(sizePolicy)
        self.comboBox_4.setMaximumSize(QtCore.QSize(218, 20))
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.horizontalLayout_6.addWidget(self.comboBox_4)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setMaximumSize(QtCore.QSize(108, 48))
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setMaximumSize(QtCore.QSize(73, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_2.addWidget(self.lineEdit)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setMaximumSize(QtCore.QSize(12, 48))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setMaximumSize(QtCore.QSize(73, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_2.addWidget(self.lineEdit_2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setMaximumSize(QtCore.QSize(60, 49))
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_7.addWidget(self.label_9)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setMaximumSize(QtCore.QSize(218, 20))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.horizontalLayout_7.addWidget(self.lineEdit_4)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setMaximumSize(QtCore.QSize(60, 48))
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_3.addWidget(self.label_7)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setMaximumSize(QtCore.QSize(218, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.horizontalLayout_3.addWidget(self.lineEdit_3)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setMinimumSize(QtCore.QSize(500, 391))
        self.tableWidget.setAutoFillBackground(True)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(9)
        self.tableWidget.setRowCount(1)
        self.tableWidget.setRowCount(2)
        self.tableWidget.setRowCount(3)
        self.tableWidget.setRowCount(4)
        self.tableWidget.setRowCount(5)
        self.tableWidget.setRowCount(6)
        self.tableWidget.setRowCount(7)
        self.tableWidget.setRowCount(8)
        self.tableWidget.setRowCount(9)
        self.tableWidget.setRowCount(10)
        self.tableWidget.setRowCount(11)
        #设置表格为可编辑
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.AllEditTriggers)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, item)
        self.gridLayout.addWidget(self.tableWidget, 0, 2, 1, 3)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 0, 1, 1, 1)
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.gridLayout.addWidget(self.line_3, 2, 3, 1, 1)
        mainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)


        # 查询按钮信号与槽函数设置
        self.pushButton_2.clicked.connect(self.DB_inquire)
        # 退出按钮信号与槽函数设置
        self.pushButton_8.clicked.connect(self.close)
        # 重置按钮信号与槽函数设置
        self.pushButton_9.clicked.connect(self.DB_reset)
        #访问按钮信号与槽函数设置
        self.pushButton.clicked.connect(self.Visit_url)
        #添加按钮信号与槽函数设置
        self.pushButton_3.clicked.connect(self.DB_insert)
        #删除按钮信号与槽函数设置
        self.pushButton_5.clicked.connect(self.DB_del)
        # 修改按钮信号与槽函数设置
        self.pushButton_4.clicked.connect(self.DB_update)
        #保存记录按钮信号与槽函数设置
        self.pushButton_7.clicked.connect(self.Save_log)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "危化品事故信息查询系统"))
        self.pushButton.setText(_translate("mainWindow", "访问"))
        self.pushButton_2.setText(_translate("mainWindow", "查询"))
        self.pushButton_3.setText(_translate("mainWindow", "添加"))
        self.pushButton_5.setText(_translate("mainWindow", "删除"))
        self.pushButton_4.setText(_translate("mainWindow", "修改"))
        self.pushButton_9.setText(_translate("mainWindow", "重置"))
        self.pushButton_7.setText(_translate("mainWindow", "保存记录"))
        self.pushButton_8.setText(_translate("mainWindow", "退出"))
        self.label.setText(_translate("mainWindow", "所在省："))
        self.comboBox.setItemText(0, _translate("mainWindow", "江苏"))
        self.comboBox.setItemText(1, _translate("mainWindow", "河南"))
        self.comboBox.setItemText(2, _translate("mainWindow", "安徽"))
        self.comboBox.setItemText(3, _translate("mainWindow", "北京"))
        self.comboBox.setItemText(4, _translate("mainWindow", "重庆"))
        self.comboBox.setItemText(5, _translate("mainWindow", "上海"))
        self.comboBox.setItemText(6, _translate("mainWindow", "湖南"))
        self.comboBox.setItemText(7, _translate("mainWindow", "湖北"))
        self.comboBox.setItemText(8, _translate("mainWindow", "河北"))
        self.comboBox.setItemText(9, _translate("mainWindow", "黑龙江"))
        self.comboBox.setItemText(10, _translate("mainWindow", "吉林"))
        self.comboBox.setItemText(11, _translate("mainWindow", "辽宁"))
        self.comboBox.setItemText(12, _translate("mainWindow", "内蒙古"))
        self.comboBox.setItemText(13, _translate("mainWindow", "新疆"))
        self.comboBox.setItemText(14, _translate("mainWindow", "西藏"))
        self.comboBox.setItemText(15, _translate("mainWindow", "四川"))
        self.comboBox.setItemText(16, _translate("mainWindow", "山西"))
        self.comboBox.setItemText(17, _translate("mainWindow", "陕西"))
        self.comboBox.setItemText(18, _translate("mainWindow", "贵州"))
        self.comboBox.setItemText(19, _translate("mainWindow", "广东"))
        self.comboBox.setItemText(20, _translate("mainWindow", "广西"))
        self.comboBox.setItemText(21, _translate("mainWindow", "云南"))
        self.comboBox.setItemText(22, _translate("mainWindow", "浙江"))
        self.comboBox.setItemText(23, _translate("mainWindow", "天津"))
        self.comboBox.setItemText(24, _translate("mainWindow", "山东"))
        self.comboBox.setItemText(25, _translate("mainWindow", "宁夏"))
        self.comboBox.setItemText(26, _translate("mainWindow", "青海"))
        self.comboBox.setItemText(27, _translate("mainWindow", "江西"))
        self.comboBox.setItemText(28, _translate("mainWindow", "甘肃"))
        self.comboBox.setItemText(29, _translate("mainWindow", "海南"))
        self.comboBox.setItemText(30, _translate("mainWindow", "总局"))
        self.comboBox.setItemText(31, _translate("mainWindow", "重庆"))
        self.label_4.setText(_translate("mainWindow", "事故日期："))
        self.label_8.setText(_translate("mainWindow", "--"))
        self.label_5.setText(_translate("mainWindow", "事故类型："))
        self.comboBox_3.setItemText(0, _translate("mainWindow", "爆炸事故"))
        self.comboBox_3.setItemText(1, _translate("mainWindow", "其它危险化学品事故"))
        self.comboBox_3.setItemText(2, _translate("mainWindow", "泄漏事故"))
        self.comboBox_3.setItemText(3, _translate("mainWindow", "灼伤事故"))
        self.comboBox_3.setItemText(4, _translate("mainWindow", "中毒和窒息事故"))
        self.label_6.setText(_translate("mainWindow", "运输OR存储事故："))
        self.comboBox_4.setItemText(0, _translate("mainWindow", "ALL"))
        self.comboBox_4.setItemText(1, _translate("mainWindow", "运输事故"))
        self.comboBox_4.setItemText(2, _translate("mainWindow", "存储事故"))
        self.label_2.setText(_translate("mainWindow", "事故伤亡人数："))
        self.label_3.setText(_translate("mainWindow", "--"))
        self.label_9.setText(_translate("mainWindow", "事故名称："))
        self.label_7.setText(_translate("mainWindow", "原文链接："))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("mainWindow", "事故名称"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("mainWindow", "事故类型"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("mainWindow", "原文链接"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("mainWindow", "事故伤亡人数"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("mainWindow", "事故日期"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("mainWindow", "所属省份"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("mainWindow", "具体位置"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("mainWindow", "具体原因"))
        item = self.tableWidget.horizontalHeaderItem(8)
        item.setText(_translate("mainWindow", "具体工厂"))

    # 查询操作
    def DB_inquire(self):
        global msglog
        flag = 0#异常处理标志
        msglog = '开始查找\n'

        #获取输入
        province = self.comboBox.currentText()
        status = self.comboBox_3.currentText()
        area = self.comboBox_4.currentText()
        date_lower_limit = self.dateEdit_2.date()
        date_upper_limit = self.dateEdit.date()
        fund_lower_limit = self.lineEdit.text()
        fund_upper_limit = self.lineEdit_2.text()
        name = self.lineEdit_4.text()
        representative = self.lineEdit_3.text()

        #构造sql语句
        sql_inquire = "SELECT * FROM mysql.company_info_v3 WHERE name IS NOT NULL"
        isini = 1#用于判断是否第一个动态构造块，即是否需要加 and
        if province == 'default':
            print('province is empty')
            pass
        else:
            if isini == 1:
                sql_inquire += ' and '
            sql_inquire += "company_info_v3.province = '" + province +"'"
            isini = 1

        if status == 'default':
            print('status is empty')
            pass
        else:
            if isini == 1:
                sql_inquire += ' and '
            sql_inquire += "company_info_v3.status = '" + status +"'"
            isini = 1

        if area == 'default':
            print('area is empty')
            pass
        else:
            if isini == 1:
                sql_inquire += ' and '
            sql_inquire += "company_info_v3.area = '" + area +"'"
            isini = 1

        if date_lower_limit == QtCore.QDate.currentDate().addYears(-40):
            print('date_lower_limit is default')
            pass
        else:
            if isini == 1:
                sql_inquire += ' and '
            sql_inquire += "company_info_v3.date > '" + date_lower_limit.toString("yyyy-MM-dd") + "'"
            isini = 1
        if date_upper_limit == QtCore.QDate.currentDate():
            print('date_upper_limit is default')
            pass
        else:
            if isini == 1:
                sql_inquire += ' and '
            sql_inquire += "company_info_v3.date < '" + date_upper_limit.toString("yyyy-MM-dd") + "'"
            isini = 1

        if fund_lower_limit == '':
            print('fund_lower_limit is empty')
            pass
        else:
            if isini == 1:
                sql_inquire += ' and '
            sql_inquire += "company_info_v3.fund > "+fund_lower_limit
            isini = 1
        if fund_upper_limit == '':
            print('fund_upper_limit is empty')
            pass
        else:
            if isini == 1:
                sql_inquire += ' and '
            sql_inquire += "company_info_v3.fund < "+fund_upper_limit
            isini = 1

        if name == '':
            print('name is empty')
            pass
        else:
            if isini == 1:
                sql_inquire += ' and '
            sql_inquire += "company_info_v3.name like '%" + name +"%'"
            isini = 1

        if representative == '':
            print('representative is empty')
            pass
        else:
            if isini == 1:
                sql_inquire += ' and '
            sql_inquire += "company_info_v3.representative = '" + representative +"'"
            isini = 1

        msglog += sql_inquire + "\n"

        #数据库操作
        try:
            host = "127.0.0.1"
            user = "root"
            passwd = "123456"
            db = 'mysql'
            print('Connect to MYSQL...')
            conn = pymysql.connect(host=host, user=user, passwd=passwd, db=db, port=3306, charset='utf8')
            print('Connect...')
            cursor = conn.cursor()
            print(sql_inquire)
            cursor.execute(sql_inquire)
            rows = cursor.fetchall()
            #在窗口上显示查询结果
            self.tableWidget.clearContents()
            # print(rows[0][0])
            self.tableWidget.setRowCount(len(rows))
            for j in range(len(rows)):
                self.comboBox_5.addItem("")
                self.comboBox_5.setItemText(j, rows[j][7])
                for i in range(9):
                    item = QtWidgets.QTableWidgetItem(str(rows[j][i]))
                    self.tableWidget.setItem(j, i, item)
            cursor.close()
            conn.close()
            self.statusbar.showMessage('查询成功', 2000)
            flag = 1
        except Exception:
            if flag == 0:
                self.statusbar.showMessage('查询异常', 2000)
                msglog += '查询异常'
        # print(province, area, status, fund_lower_limit, fund_upper_limit, name, representative)
        # print(date_lower_limit.toString("yyyy-MM-dd"), date_upper_limit.year())
        pass
    # 重置搜索条件
    def DB_reset(self):
        self.comboBox.setCurrentText('default')
        self.comboBox_3.setCurrentText('default')
        self.comboBox_4.setCurrentText('default')
        self.dateEdit_2.setDate(QtCore.QDate.currentDate().addYears(-40))
        self.dateEdit.setDate(QtCore.QDate.currentDate())
        self.lineEdit.setText('')
        self.lineEdit_2.setText('')
        self.lineEdit_4.setText('')
        self.lineEdit_3.setText('')
        self.tableWidget.clearContents()
        self.comboBox_5.clear()
        pass
    #插入操作
    def DB_insert(self):
        global msglog
        msglog = '开始插入\n'
        flag = 0#异常处理标志
        #获取输入
        empty_value = 'NULL'
        zero = 0
        if self.tableWidget.item(0, 0) == None:
            name = False
        else:
            name = self.tableWidget.item(0, 0).text()
        if self.tableWidget.item(0, 1) == None:
            status = False
        else:
            status = self.tableWidget.item(0, 1).text()
        if self.tableWidget.item(0, 2) == None:
            representative = False
        else:
            representative = self.tableWidget.item(0, 2).text()
        if self.tableWidget.item(0, 3) == None:
            fund = False
        else:
            fund = self.tableWidget.item(0, 3).text()
        if self.tableWidget.item(0, 4) == None:
            date = False
        else:
            date = self.tableWidget.item(0, 4).text()
        if self.tableWidget.item(0, 5) == None:
            area = False
        else:
            area = self.tableWidget.item(0, 5).text()
        if self.tableWidget.item(0, 6) == None:
            location = False
        else:
            location = self.tableWidget.item(0, 6).text()
        if self.tableWidget.item(0, 7) == None:
            company_url = False
        else:
            company_url = self.tableWidget.item(0, 7).text()
        if self.tableWidget.item(0, 8) == None:
            province = False
        else:
            province = self.tableWidget.item(0, 8).text()
        #构造sql语句
        sql_insert = "INSERT INTO mysql.company_info_v3 VALUES("
        if name:
            sql_insert += "'" + name + "',"
        else:
            sql_insert += "'" + empty_value + "',"
        if status:
            sql_insert += "'" + status + "',"
        else:
            sql_insert += "'" + empty_value + "',"
        if representative:
            sql_insert += "'" + representative + "',"
        else:
            sql_insert += "'" + empty_value + "',"
        if fund:
            sql_insert += "'" + fund + "',"
        else:
            sql_insert += str(zero) + ","
        if date:
            sql_insert += "'" + date + "',"
        else:
            sql_insert += str(zero) + ","
        if area:
            sql_insert += "'" + area + "',"
        else:
            sql_insert += "'" + empty_value + "',"
        if location:
            sql_insert += "'" + location + "',"
        else:
            sql_insert += "'" + empty_value + "',"
        if company_url:
            sql_insert += "'" + company_url + "',"
        else:
            sql_insert += "'" + empty_value + "',"
        if province:
            sql_insert += "'" + province + "')"
        else:
            sql_insert += "'" + empty_value + "')"
        #数据库操作
        print(sql_insert)
        try:
            host = "127.0.0.1"
            user = "sa"
            passwd = "123456"
            db = 'aaa'
            print('Connect to MYSQL...')
            conn = pymysql.connect(host=host, user=user, passwd=passwd, db=db, port=3306, charset='utf8')
            print('Connect...')
            cursor = conn.cursor()
            print(sql_insert)
            cursor.execute(sql_insert)
            conn.commit()#提交当前事务
            cursor.close()
            conn.close()
            self.tableWidget.clearContents()
            self.statusbar.showMessage('添加数据成功', 2000)
            flag = 1
        except Exception:
            if flag == 0:
                self.statusbar.showMessage('添加数据异常', 2000)
                msglog += '添加数据异常'
        pass
    #删除操作
    def DB_del(self):
        global msglog
        msglog  = '开始删除\n'
        flag = 0#异常处理标志
        #获取输入
        list = self.Get_selectedrow()
        self.company_urls = []
        try:
            for i in list:
                self.company_urls.append(self.tableWidget.item(i, 7).text())
        except Exception:
            self.statusbar.showMessage('获取删除数据异常', 2000)
            msglog += '获取删除数据异常'
            return
        #构造sql语句
        sql_del = "DELETE FROM mysql.company_info_v3 where "
        for company_url in self.company_urls:
            sql_del += "company_info_v3.company_url = " + "'" + company_url + "'" +" or "
        sql_del = sql_del[:-4]
        #数据库操作
        try:
            host = "127.0.0.1"
            user = "root"
            passwd = "123456"
            db = 'mysql'
            print('Connect to MYSQL...')
            conn = pymysql.connect(host=host, user=user, passwd=passwd, db=db, port=3306, charset='utf8')
            print('Connect...')
            cursor = conn.cursor()
            print(sql_del)
            cursor.execute(sql_del)
            conn.commit()  # 提交当前事务
            cursor.close()
            conn.close()
            self.DB_reset()
            self.statusbar.showMessage('删除数据成功', 2000)
            flag = 1
        except Exception:
            if flag == 0:
                self.statusbar.showMessage('删除数据异常', 2000)
                msglog += '删除数据异常'
        pass
    #更新操作
    def DB_update(self):
        global msglog
        msglog = '开始更新数据'
        flag = 0#异常处理标志
        #获取输入
        list = self.Get_selectedrow()
        company_url = ''
        try:
            if self.tableWidget.item(list[0], 0) == None:
                name = False
            else:
                name = self.tableWidget.item(list[0], 0).text()
            if self.tableWidget.item(list[0], 1) == None:
                status = False
            else:
                status = self.tableWidget.item(list[0], 1).text()
            if self.tableWidget.item(list[0], 2) == None:
                representative = False
            else:
                representative = self.tableWidget.item(list[0], 2).text()
            if self.tableWidget.item(list[0], 3) == None:
                fund = False
            else:
                fund = self.tableWidget.item(list[0], 3).text()
            if self.tableWidget.item(list[0], 4) == None:
                date = False
            else:
                date = self.tableWidget.item(list[0], 4).text()
            if self.tableWidget.item(list[0], 5) == None:
                area = False
            else:
                area = self.tableWidget.item(list[0], 5).text()
            if self.tableWidget.item(list[0], 6) == None:
                location = False
            else:
                location = self.tableWidget.item(list[0], 6).text()
            if self.tableWidget.item(list[0], 7) == None:
                company_url = ''
            else:
                company_url = self.tableWidget.item(list[0], 7).text()
            if self.tableWidget.item(list[0], 8) == None:
                province = False
            else:
                province = self.tableWidget.item(list[0], 8).text()
        except Exception:
            self.statusbar.showMessage('获取更新数据异常', 2000)
            msglog += '获取更新数据异常\n'
            return
        # 构造sql语句
        sql_update = "UPDATE mysql.company_info_v3 SET "
        if name:
            sql_update += "name = " + "'" + name + "',"
        else:
            sql_update += "name = 'null',"
        if status:
            sql_update += "status = " + "'"+status+"',"
        if  representative:
            sql_update += "representative = " + "'"+representative+"',"
        if fund:
            sql_update += "fund = " + "'"+fund+"',"
        if date:
            sql_update += "date = " + "'"+date+"',"
        if area:
            sql_update += "area = " + "'"+area+"',"
        if location:
            sql_update += "location = " + "'"+location+"',"
        if province:
            sql_update += "province = " + "'"+province+"' "
        sql_update += "where company_url = " + "'" + company_url + "'"
        print(sql_update)
        # 数据库操作
        try:
            host = "127.0.0.1"
            user = "root"
            passwd = "123456"
            db = 'mysql'
            print('Connect to MYSQL...')
            conn = pymysql.connect(host=host, user=user, passwd=passwd, db=db, port=3306, charset='utf8')
            print('Connect...')
            cursor = conn.cursor()
            print(sql_update)
            cursor.execute(sql_update)
            conn.commit()  # 提交当前事务
            cursor.close()
            conn.close()
            self.DB_reset()
            self.statusbar.showMessage('更新数据成功', 2000)
            flag = 1
        except Exception:
            if flag == 0:
                self.statusbar.showMessage('更新数据异常', 2000)
                msglog += '更新数据异常'
        pass
    #保存日志
    def Save_log(self):
        fw = open('log.txt', 'a+')  # 追加模式打开log
        global msglog
        fw.write("\n"+time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))+"\n"+msglog+"\n")
        fw.close()
        self.statusbar.showMessage('保存成功', 5000)
        pass
    #访问公司URL
    def Visit_url(self):
        url = self.comboBox_5.currentText()
        webbrowser.open(url)
        pass

    def Get_selectedrow(self):
        self.seletedRow = []
        self.seletedItem = []
        items = self.tableWidget.selectedItems()
        for item in items:
            self.seletedItem.append(self.tableWidget.indexFromItem(item).row())
        for i in self.seletedItem:
            if self.seletedItem.count(i) == 9 and i not in self.seletedRow:
                self.seletedRow.append(i)
        return self.seletedRow

