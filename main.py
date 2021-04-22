import sys
from PyQt5 import QtWidgets, QtCore, sip
from mainwin import Ui_MainWin
from signin import Ui_Signin
from database import Sql
from chooseitem import Ui_Chooseitem
from workthreads import Thread1, Thread2


class Signin(QtWidgets.QDialog, Ui_Signin):
    def __init__(self):
        super(Signin, self).__init__()

        # Set up the user interface from Designer.
        self.setupUi(self)

        # import user information from database
        self.users = Sql()
        self.all_users, self.all_passwords = self.users.show_all_data()
        self.comboBox.addItems(self.all_users)
        self.lineEdit_password.setText(self.all_passwords[0])

        # connections
        self.pushButton_signin.clicked.connect(self.signin_clicked)
        self.pushButton_exit.clicked.connect(self.exit_clicked)
        self.comboBox.currentTextChanged.connect(self.update_user_password)

    def signin_clicked(self):
        print("sign in")
        if self.checkBox_remember_psw.isChecked() and self.comboBox.currentText() not in self.all_users:
            self.users.add_user(self.comboBox.currentText(), self.lineEdit_password.text())
        self.accept()

    def exit_clicked(self):
        print("exit")
        self.reject()

    def update_user_password(self):
        if self.comboBox.currentText() in self.all_users:
            index = self.all_users.index(self.comboBox.currentText())
            self.lineEdit_password.setText(self.all_passwords[index])
        else:
            self.lineEdit_password.clear()


class ChooseItem(QtWidgets.QDialog, Ui_Chooseitem):
    def __init__(self):
        super(ChooseItem, self).__init__()

        # Set up the user interface from Designer.
        self.setupUi(self)


class MainWin(QtWidgets.QMainWindow, Ui_MainWin):
    def __init__(self):
        super(MainWin, self).__init__()

        # Set up the user interface from Designer.
        self.setupUi(self)

        self.thread1 = Thread1()
        self.thread2 = Thread2()

        # connection
        self.pushButton_user.clicked.connect(self.change_user)
        self.pushButton_additem.clicked.connect(self.additem)
        self.pushButton_deleteitem.clicked.connect(self.deleteitem)
        self.pushButton_work1.clicked.connect(self.work1)
        self.pushButton_work2.clicked.connect(self.work2)
        self.thread2.log.connect(self.log_display)
        self.thread2.signal.connect(self.set_btn)

        win_signin = Signin()
        if not win_signin.exec_():
            exit()
        else:
            self.pushButton_user.setText(win_signin.comboBox.currentText())

    def change_user(self):
        print("change user")
        win_signin = Signin()
        if win_signin.exec_():
            self.pushButton_user.setText(win_signin.comboBox.currentText())

    def additem(self):
        print("add item")
        win_chooseitem = ChooseItem()
        if win_chooseitem.exec_():
            checkBox_new = QtWidgets.QCheckBox(self.verticalLayoutWidget)
            self.verticalLayout.addWidget(checkBox_new)
            checkBox_new.setText(win_chooseitem.lineEdit.text())
            checkBox_new.setObjectName("checkBox_" + win_chooseitem.lineEdit.text())

    def deleteitem(self):
        print("delete item")
        win_chooseitem = ChooseItem()
        if win_chooseitem.exec_():
            checkBox_delete = self.findChild(QtWidgets.QCheckBox, "checkBox_" + win_chooseitem.lineEdit.text())
            print(checkBox_delete)
            if checkBox_delete is not None:
                sip.delete(checkBox_delete)

    def work1(self):
        self.thread1.start()

    def work2(self):
        self.pushButton_work2.setEnabled(False)
        self.thread2.start()

    def set_btn(self):
        self.pushButton_work2.setEnabled(True)

    def log_display(self, text):
        self.textBrowser.append(text)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    win = MainWin()
    win.show()
    sys.exit(app.exec_())
