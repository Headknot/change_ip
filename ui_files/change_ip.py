# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\change_ip.ui',
# licensing of '.\change_ip.ui' applies.
#
# Created: Fri Sep 21 23:48:30 2018
#      by: pyside2-uic  running on PySide2 5.11.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 500)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("change_ip.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.groupBox_2 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.QLabel_interface = QtWidgets.QLabel(self.groupBox_2)
        self.QLabel_interface.setObjectName("QLabel_interface")
        self.horizontalLayout_5.addWidget(self.QLabel_interface)
        self.comboBox_interface = QtWidgets.QComboBox(self.groupBox_2)
        self.comboBox_interface.setObjectName("comboBox_interface")
        self.horizontalLayout_5.addWidget(self.comboBox_interface)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.QLabel_template = QtWidgets.QLabel(self.groupBox_2)
        self.QLabel_template.setObjectName("QLabel_template")
        self.horizontalLayout_4.addWidget(self.QLabel_template)
        self.comboBox_template = QtWidgets.QComboBox(self.groupBox_2)
        self.comboBox_template.setObjectName("comboBox_template")
        self.comboBox_template.addItem("")
        self.comboBox_template.addItem("")
        self.comboBox_template.addItem("")
        self.comboBox_template.addItem("")
        self.comboBox_template.addItem("")
        self.horizontalLayout_4.addWidget(self.comboBox_template)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.QLabel_ip = QtWidgets.QLabel(self.groupBox_2)
        self.QLabel_ip.setObjectName("QLabel_ip")
        self.horizontalLayout.addWidget(self.QLabel_ip)
        self.QLineEdit_ip = QtWidgets.QLineEdit(self.groupBox_2)
        self.QLineEdit_ip.setObjectName("QLineEdit_ip")
        self.horizontalLayout.addWidget(self.QLineEdit_ip)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.QLabel_mask = QtWidgets.QLabel(self.groupBox_2)
        self.QLabel_mask.setObjectName("QLabel_mask")
        self.horizontalLayout_2.addWidget(self.QLabel_mask)
        self.QLineEdit_mask = QtWidgets.QLineEdit(self.groupBox_2)
        self.QLineEdit_mask.setObjectName("QLineEdit_mask")
        self.horizontalLayout_2.addWidget(self.QLineEdit_mask)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.QLabel_gw = QtWidgets.QLabel(self.groupBox_2)
        self.QLabel_gw.setObjectName("QLabel_gw")
        self.horizontalLayout_3.addWidget(self.QLabel_gw)
        self.QLineEdit_gw = QtWidgets.QLineEdit(self.groupBox_2)
        self.QLineEdit_gw.setObjectName("QLineEdit_gw")
        self.horizontalLayout_3.addWidget(self.QLineEdit_gw)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.verticalLayout_4.addLayout(self.verticalLayout)
        self.textEdit = QtWidgets.QTextEdit(self.groupBox_2)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout_4.addWidget(self.textEdit)
        self.verticalLayout_2.addWidget(self.groupBox_2)
        self.pushButton_clear = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_clear.setObjectName("pushButton_clear")
        self.verticalLayout_2.addWidget(self.pushButton_clear)
        self.pushButton_set_static = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_set_static.setObjectName("pushButton_set_static")
        self.verticalLayout_2.addWidget(self.pushButton_set_static)
        self.pushButton_current_config = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_current_config.setObjectName("pushButton_current_config")
        self.verticalLayout_2.addWidget(self.pushButton_current_config)
        self.pushButton_quit = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_quit.setObjectName("pushButton_quit")
        self.verticalLayout_2.addWidget(self.pushButton_quit)
        self.verticalLayout_5.addLayout(self.verticalLayout_2)
        self.verticalLayout_3.addWidget(self.groupBox)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 400, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "change_ip", None, -1))
        self.groupBox_2.setTitle(QtWidgets.QApplication.translate("MainWindow", "Change IP", None, -1))
        self.QLabel_interface.setText(QtWidgets.QApplication.translate("MainWindow", "Interface", None, -1))
        self.QLabel_template.setText(QtWidgets.QApplication.translate("MainWindow", "Template", None, -1))
        self.comboBox_template.setItemText(0, QtWidgets.QApplication.translate("MainWindow", "Choose...", None, -1))
        self.comboBox_template.setItemText(1, QtWidgets.QApplication.translate("MainWindow", "DHCP", None, -1))
        self.comboBox_template.setItemText(2, QtWidgets.QApplication.translate("MainWindow", "Clavister G2", None, -1))
        self.comboBox_template.setItemText(3, QtWidgets.QApplication.translate("MainWindow", "Clavister GS", None, -1))
        self.comboBox_template.setItemText(4, QtWidgets.QApplication.translate("MainWindow", "VirtualAccess", None, -1))
        self.QLabel_ip.setText(QtWidgets.QApplication.translate("MainWindow", "IP     ", None, -1))
        self.QLabel_mask.setText(QtWidgets.QApplication.translate("MainWindow", "Mask", None, -1))
        self.QLabel_gw.setText(QtWidgets.QApplication.translate("MainWindow", "GW  ", None, -1))
        self.pushButton_clear.setText(QtWidgets.QApplication.translate("MainWindow", "Clear", None, -1))
        self.pushButton_set_static.setText(QtWidgets.QApplication.translate("MainWindow", "Set Config", None, -1))
        self.pushButton_current_config.setText(QtWidgets.QApplication.translate("MainWindow", "Show Current Config", None, -1))
        self.pushButton_quit.setText(QtWidgets.QApplication.translate("MainWindow", "Quit", None, -1))

