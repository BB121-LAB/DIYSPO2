# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'spo2_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1049, 588)
        MainWindow.setMinimumSize(QtCore.QSize(1049, 588))
        MainWindow.setMaximumSize(QtCore.QSize(1049, 588))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.graph = PlotWidget(self.centralwidget)
        self.graph.setGeometry(QtCore.QRect(10, 10, 471, 451))
        self.graph.setObjectName("graph")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(490, 10, 301, 451))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.lcd_r = QtWidgets.QLCDNumber(self.verticalLayoutWidget)
        self.lcd_r.setMinimumSize(QtCore.QSize(299, 78))
        self.lcd_r.setObjectName("lcd_r")
        self.verticalLayout.addWidget(self.lcd_r)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.lcd_r_avg = QtWidgets.QLCDNumber(self.verticalLayoutWidget)
        self.lcd_r_avg.setMinimumSize(QtCore.QSize(299, 78))
        self.lcd_r_avg.setObjectName("lcd_r_avg")
        self.verticalLayout.addWidget(self.lcd_r_avg)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.lcd_spo2 = QtWidgets.QLCDNumber(self.verticalLayoutWidget)
        self.lcd_spo2.setMinimumSize(QtCore.QSize(299, 78))
        self.lcd_spo2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.lcd_spo2.setLineWidth(2)
        self.lcd_spo2.setObjectName("lcd_spo2")
        self.verticalLayout.addWidget(self.lcd_spo2)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.lcd_heart = QtWidgets.QLCDNumber(self.verticalLayoutWidget)
        self.lcd_heart.setMinimumSize(QtCore.QSize(299, 78))
        self.lcd_heart.setObjectName("lcd_heart")
        self.verticalLayout.addWidget(self.lcd_heart)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 480, 551, 51))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.port_combo_box = QtWidgets.QComboBox(self.horizontalLayoutWidget)
        self.port_combo_box.setObjectName("port_combo_box")
        self.horizontalLayout.addWidget(self.port_combo_box)
        self.button_refresh = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.button_refresh.setMinimumSize(QtCore.QSize(115, 27))
        self.button_refresh.setMaximumSize(QtCore.QSize(115, 27))
        self.button_refresh.setObjectName("button_refresh")
        self.horizontalLayout.addWidget(self.button_refresh)
        self.button_connect = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.button_connect.setMinimumSize(QtCore.QSize(116, 27))
        self.button_connect.setMaximumSize(QtCore.QSize(116, 27))
        self.button_connect.setObjectName("button_connect")
        self.horizontalLayout.addWidget(self.button_connect)
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(10, 460, 67, 17))
        self.label_10.setObjectName("label_10")
        self.button_capture = QtWidgets.QPushButton(self.centralwidget)
        self.button_capture.setGeometry(QtCore.QRect(570, 480, 221, 51))
        self.button_capture.setObjectName("button_capture")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(800, 10, 321, 17))
        self.label_5.setObjectName("label_5")
        self.button_update = QtWidgets.QPushButton(self.centralwidget)
        self.button_update.setEnabled(True)
        self.button_update.setGeometry(QtCore.QRect(800, 230, 71, 27))
        self.button_update.setObjectName("button_update")
        self.graph_2 = PlotWidget(self.centralwidget)
        self.graph_2.setGeometry(QtCore.QRect(800, 300, 241, 161))
        self.graph_2.setObjectName("graph_2")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(800, 280, 321, 17))
        self.label_6.setObjectName("label_6")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(800, 30, 241, 192))
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setObjectName("tableWidget")
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.button_add_row = QtWidgets.QPushButton(self.centralwidget)
        self.button_add_row.setGeometry(QtCore.QRect(1010, 230, 31, 27))
        font = QtGui.QFont()
        font.setFamily("Loma")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.button_add_row.setFont(font)
        self.button_add_row.setObjectName("button_add_row")
        self.button_reload = QtWidgets.QPushButton(self.centralwidget)
        self.button_reload.setGeometry(QtCore.QRect(880, 230, 71, 27))
        self.button_reload.setObjectName("button_reload")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(800, 470, 241, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1049, 24))
        self.menuBar.setObjectName("menuBar")
        self.menuFile = QtWidgets.QMenu(self.menuBar)
        self.menuFile.setObjectName("menuFile")
        self.menuHelp = QtWidgets.QMenu(self.menuBar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menuBar)
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionGet_Source_Code = QtWidgets.QAction(MainWindow)
        self.actionGet_Source_Code.setObjectName("actionGet_Source_Code")
        self.actionLicense = QtWidgets.QAction(MainWindow)
        self.actionLicense.setObjectName("actionLicense")
        self.menuFile.addAction(self.actionQuit)
        self.menuHelp.addAction(self.actionGet_Source_Code)
        self.menuHelp.addAction(self.actionLicense)
        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuBar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "SPO2 Monitor"))
        self.label.setText(_translate("MainWindow", "R Value Instantaneous"))
        self.label_4.setText(_translate("MainWindow", "R Value Average"))
        self.label_2.setText(_translate("MainWindow", "Approximate SPO2 (%)"))
        self.label_3.setText(_translate("MainWindow", "Heart Rate (BPM)"))
        self.button_refresh.setText(_translate("MainWindow", "Refresh"))
        self.button_connect.setText(_translate("MainWindow", "Connect"))
        self.label_10.setText(_translate("MainWindow", "Device:"))
        self.button_capture.setText(_translate("MainWindow", "Start Capture"))
        self.label_5.setText(_translate("MainWindow", "SPO2/R Calibration Coefficients"))
        self.button_update.setText(_translate("MainWindow", "Apply"))
        self.label_6.setText(_translate("MainWindow", "SPO2/R Calibration Curve"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "R Value"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "SPO2"))
        self.button_add_row.setText(_translate("MainWindow", "+"))
        self.button_reload.setText(_translate("MainWindow", "Reload"))
        self.label_7.setText(_translate("MainWindow", "NOT FOR\n"
"MEDICAL USE"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionGet_Source_Code.setText(_translate("MainWindow", "Get Source Code"))
        self.actionLicense.setText(_translate("MainWindow", "License"))
from pyqtgraph import PlotWidget
