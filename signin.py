# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\大学\huawei\hisensor\signin.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Signin(object):
    def setupUi(self, Signin):
        Signin.setObjectName("Signin")
        Signin.setWindowModality(QtCore.Qt.ApplicationModal)
        Signin.resize(422, 357)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Signin.sizePolicy().hasHeightForWidth())
        Signin.setSizePolicy(sizePolicy)
        Signin.setMinimumSize(QtCore.QSize(422, 357))
        Signin.setMaximumSize(QtCore.QSize(422, 400))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:\\大学\\huawei\\hisensor\\nakelulu.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Signin.setWindowIcon(icon)
        self.verticalLayout = QtWidgets.QVBoxLayout(Signin)
        self.verticalLayout.setContentsMargins(-1, -1, -1, 50)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(Signin)
        self.frame.setMinimumSize(QtCore.QSize(400, 200))
        self.frame.setMaximumSize(QtCore.QSize(400, 200))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setContentsMargins(71, 31, 71, 0)
        self.verticalLayout_2.setSpacing(17)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setMinimumSize(QtCore.QSize(60, 0))
        self.label.setMaximumSize(QtCore.QSize(60, 16777215))
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.comboBox = QtWidgets.QComboBox(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy)
        self.comboBox.setMinimumSize(QtCore.QSize(0, 25))
        self.comboBox.setMaximumSize(QtCore.QSize(16777215, 25))
        self.comboBox.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.comboBox.setAcceptDrops(False)
        self.comboBox.setAutoFillBackground(False)
        self.comboBox.setStyleSheet("QComboBox{\n"
"    background:white;\n"
"}")
        self.comboBox.setEditable(True)
        self.comboBox.setFrame(True)
        self.comboBox.setObjectName("comboBox")
        self.horizontalLayout.addWidget(self.comboBox)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setMinimumSize(QtCore.QSize(60, 0))
        self.label_2.setMaximumSize(QtCore.QSize(60, 16777215))
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.lineEdit_password = QtWidgets.QLineEdit(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_password.sizePolicy().hasHeightForWidth())
        self.lineEdit_password.setSizePolicy(sizePolicy)
        self.lineEdit_password.setMinimumSize(QtCore.QSize(0, 25))
        self.lineEdit_password.setMaximumSize(QtCore.QSize(16777215, 25))
        self.lineEdit_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_password.setObjectName("lineEdit_password")
        self.horizontalLayout_2.addWidget(self.lineEdit_password)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(0, -1, -1, -1)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.checkBox_remember_psw = QtWidgets.QCheckBox(self.frame)
        self.checkBox_remember_psw.setObjectName("checkBox_remember_psw")
        self.horizontalLayout_4.addWidget(self.checkBox_remember_psw)
        self.checkBox_reserved = QtWidgets.QCheckBox(self.frame)
        self.checkBox_reserved.setObjectName("checkBox_reserved")
        self.horizontalLayout_4.addWidget(self.checkBox_reserved)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.verticalLayout.addWidget(self.frame)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(30, -1, 30, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton_signin = QtWidgets.QPushButton(Signin)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_signin.sizePolicy().hasHeightForWidth())
        self.pushButton_signin.setSizePolicy(sizePolicy)
        self.pushButton_signin.setObjectName("pushButton_signin")
        self.horizontalLayout_3.addWidget(self.pushButton_signin)
        self.pushButton_exit = QtWidgets.QPushButton(Signin)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_exit.sizePolicy().hasHeightForWidth())
        self.pushButton_exit.setSizePolicy(sizePolicy)
        self.pushButton_exit.setObjectName("pushButton_exit")
        self.horizontalLayout_3.addWidget(self.pushButton_exit)
        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.retranslateUi(Signin)
        QtCore.QMetaObject.connectSlotsByName(Signin)

    def retranslateUi(self, Signin):
        _translate = QtCore.QCoreApplication.translate
        Signin.setWindowTitle(_translate("Signin", "登录"))
        self.label.setText(_translate("Signin", "用户："))
        self.label_2.setText(_translate("Signin", "密码："))
        self.checkBox_remember_psw.setText(_translate("Signin", "记住密码"))
        self.checkBox_reserved.setText(_translate("Signin", "备用"))
        self.pushButton_signin.setText(_translate("Signin", "登录"))
        self.pushButton_exit.setText(_translate("Signin", "退出"))
