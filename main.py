import sys
from PyQt5 import QtWidgets, QtCore
from mainwin import Ui_MainWin
from signin import Ui_Signin
from database import Sql


class Signin(QtWidgets.QDialog, Ui_Signin):
    def __init__(self):
        super(Signin, self).__init__()

        # Set up the user interface from Designer.
        self.setupUi(self)

        # import user information from database
        users = Sql()
        self.all_users, self.all_passwords = users.show_all_data()
        for user in self.all_users:
            self.comboBox.addItem(user)
        self.lineEdit_password.setText(self.all_passwords[0])

        # connections
        self.pushButton_signin.clicked.connect(self.signin_clicked)
        self.pushButton_exit.clicked.connect(self.exit_clicked)
        self.comboBox.currentTextChanged.connect(self.update_user_password)

    def signin_clicked(self):
        print("sign in")
        self.accept()

    def exit_clicked(self):
        print("exit")
        self.reject()

    def update_user_password(self):
        index = self.all_users.index(self.comboBox.currentText())
        self.lineEdit_password.setText(self.all_passwords[index])


class MainWin(QtWidgets.QMainWindow, Ui_MainWin):
    user_s = QtCore.pyqtSignal(str)

    def __init__(self):
        super(MainWin, self).__init__()

        # Set up the user interface from Designer.
        self.setupUi(self)

        # connection
        self.user_s.connect(self.name_show)

        win_signin = Signin()
        if not win_signin.exec_():
            exit()
        else:
            self.user_s.emit(win_signin.comboBox.currentText())

    def name_show(self, name):
        self.pushButton_user.setText(name)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    win = MainWin()
    win.show()
    sys.exit(app.exec_())
