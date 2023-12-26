import PyQt6.QtWidgets as qt
import PyQt6.QtGui as qt1
import PyQt6.QtCore as qt2
from . import models,userManager
# create your forms
class NewUser(qt.QDialog):
    def __init__(self,p):
        super().__init__(p)
        self.setWindowTitle(_("create new user"))
        self.first_name=qt.QLineEdit()
        self.first_name.setAccessibleName(_("first name"))
        self.last_name=qt.QLineEdit()
        self.last_name.setAccessibleName(_("last name"))
        self.email=qt.QLineEdit()
        self.email.setAccessibleName(_("email"))
        self.gender=qt.QComboBox()
        self.gender.addItems(["male","female"])
        self.gender.setAccessibleName(_("gender"))
        self.bio=qt.QLineEdit()
        self.bio.setAccessibleName(_("bio"))
        self.user_name=qt.QLineEdit()
        self.user_name.setAccessibleName(_("user name"))
        self.password=qt.QLineEdit()
        self.password.setEchoMode(qt.QLineEdit.EchoMode.Password)
        self.password.setAccessibleName(_("password"))
        self.create=qt.QPushButton(_("create"))
        self.create.clicked.connect(self.oncreate)
        layout=qt.QVBoxLayout(self)
        layout.addWidget(self.first_name)
        layout.addWidget(self.last_name)
        layout.addWidget(self.email)
        layout.addWidget(self.gender)
        layout.addWidget(self.user_name)
        layout.addWidget(self.bio)
        layout.addWidget(self.password)
        layout.addWidget(self.create)
    def oncreate(self):
        setion=models.get_session()
        user=models.user(first_name=self.first_name.text(),last_name=self.last_name.text(),email=self.email.text(),bio=self.bio.text(),gender=self.gender.currentText(),user_name=self.user_name.text(),password=self.password.text())
        setion.add(user)
        setion.commit()
        userManager.lugin(self.user_name.text())
        self.close()