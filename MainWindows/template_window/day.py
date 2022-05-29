# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'day.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(700, 450)
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.btn_back = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_back.setFont(font)
        self.btn_back.setObjectName("btn_back")
        self.horizontalLayout_5.addWidget(self.btn_back, 0, QtCore.Qt.AlignLeft)
        self.btn_create_excel = QtWidgets.QPushButton(self.centralwidget)
        self.btn_create_excel.setObjectName("btn_create_excel")
        self.horizontalLayout_5.addWidget(self.btn_create_excel)
        self.btn_load_table = QtWidgets.QPushButton(self.centralwidget)
        self.btn_load_table.setObjectName("btn_load_table")
        self.horizontalLayout_5.addWidget(self.btn_load_table)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.lbl_name_day = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.lbl_name_day.setFont(font)
        self.lbl_name_day.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_name_day.setObjectName("lbl_name_day")
        self.verticalLayout_8.addWidget(self.lbl_name_day)
        self.EventView = QtWidgets.QListWidget(self.centralwidget)
        self.EventView.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.EventView.setObjectName("EventView")
        self.verticalLayout_8.addWidget(self.EventView)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btn_clear_day = QtWidgets.QPushButton(self.centralwidget)
        self.btn_clear_day.setObjectName("btn_clear_day")
        self.horizontalLayout_2.addWidget(self.btn_clear_day)
        self.btn_add_event = QtWidgets.QPushButton(self.centralwidget)
        self.btn_add_event.setObjectName("btn_add_event")
        self.horizontalLayout_2.addWidget(self.btn_add_event)
        self.verticalLayout_8.addLayout(self.horizontalLayout_2)
        self.horizontalLayout.addLayout(self.verticalLayout_8)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_6.addWidget(self.label)
        self.event_description = QtWidgets.QTextEdit(self.centralwidget)
        self.event_description.setObjectName("event_description")
        self.verticalLayout_6.addWidget(self.event_description)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.btn_edit_info = QtWidgets.QPushButton(self.centralwidget)
        self.btn_edit_info.setObjectName("btn_edit_info")
        self.horizontalLayout_4.addWidget(self.btn_edit_info)
        self.btn_clear_event = QtWidgets.QPushButton(self.centralwidget)
        self.btn_clear_event.setObjectName("btn_clear_event")
        self.horizontalLayout_4.addWidget(self.btn_clear_event)
        self.verticalLayout_6.addLayout(self.horizontalLayout_4)
        self.horizontalLayout.addLayout(self.verticalLayout_6)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(mainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 585, 21))
        self.menubar.setObjectName("menubar")
        mainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "График дня"))
        self.btn_back.setText(_translate("mainWindow", "Назад"))
        self.btn_create_excel.setText(_translate("mainWindow", "Создать таблицу excel"))
        self.btn_load_table.setText(_translate("mainWindow", "Загрузить события из excel"))
        self.lbl_name_day.setText(_translate("mainWindow", "Понедельник"))
        self.btn_clear_day.setText(_translate("mainWindow", "Очистить события"))
        self.btn_add_event.setText(_translate("mainWindow", "Добавить событие"))
        self.label.setText(_translate("mainWindow", "Описание"))
        self.btn_edit_info.setText(_translate("mainWindow", "Редактировать"))
        self.btn_clear_event.setText(_translate("mainWindow", "Удалить"))
