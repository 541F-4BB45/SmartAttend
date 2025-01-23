from PyQt5.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PyQt5.QtWidgets import *
import sys

class Ui_LoginWindow(object):
    def setupUi(self, LoginWindow):
        if LoginWindow.objectName():
            LoginWindow.setObjectName(u"LoginWindow")
        LoginWindow.resize(900, 600)
        LoginWindow.setMinimumSize(QSize(900, 600))
        LoginWindow.setMaximumSize(QSize(900, 600))
        LoginWindow.setAutoFillBackground(False)
        LoginWindow.setStyleSheet(u"background-color: rgb(85, 255, 127);\n"
"background-color: rgb(0, 85, 0);")
        self.Background = QWidget(LoginWindow)
        self.Background.setObjectName(u"Background")
        self.Background.setStyleSheet(u"QWidget#Background\n"
"{\n"
"background-color: qlineargradient(spread:reflect, x1:0.323, y1:0.414955, x2:0.136, y2:1, stop:0.59887 rgba(0, 85, 127, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}")
        self.VerticalSeperator = QFrame(self.Background)
        self.VerticalSeperator.setObjectName(u"VerticalSeperator")
        self.VerticalSeperator.setGeometry(QRect(350, 0, 10, 600))
        self.VerticalSeperator.setMinimumSize(QSize(10, 600))
        self.VerticalSeperator.setMaximumSize(QSize(10, 600))
        self.VerticalSeperator.setStyleSheet(u"background-color: rgb(220, 220, 220);")
        self.VerticalSeperator.setFrameShadow(QFrame.Plain)
        self.VerticalSeperator.setMidLineWidth(0)
        self.VerticalSeperator.setFrameShape(QFrame.VLine)
        self.usernameLineEdit = QLineEdit(self.Background)
        self.usernameLineEdit.setObjectName(u"usernameLineEdit")
        self.usernameLineEdit.setGeometry(QRect(55, 200, 240, 30))
        self.usernameLineEdit.setMinimumSize(QSize(240, 30))
        self.usernameLineEdit.setMaximumSize(QSize(240, 30))
        self.usernameLineEdit.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0);")
        self.usernameLineEdit.setMaxLength(20)
        self.passwordLneEdit = QLineEdit(self.Background)
        self.passwordLneEdit.setObjectName(u"passwordLneEdit")
        self.passwordLneEdit.setGeometry(QRect(55, 310, 240, 30))
        self.passwordLneEdit.setMinimumSize(QSize(240, 30))
        self.passwordLneEdit.setMaximumSize(QSize(240, 30))
        self.passwordLneEdit.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0);")
        self.passwordLneEdit.setMaxLength(30)
        self.usernameLabel = QLabel(self.Background)
        self.usernameLabel.setObjectName(u"usernameLabel")
        self.usernameLabel.setGeometry(QRect(55, 170, 130, 20))
        font = QFont()
        font.setFamily(u"Arial")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.usernameLabel.setFont(font)
        self.usernameLabel.setStyleSheet(u"QLabel#usernameLabel\n"
"{\n"
"font: 75 14pt \"Arial\";\n"
"background-color: rgb(0, 85, 127);\n"
"}")
        self.passwordLabel = QLabel(self.Background)
        self.passwordLabel.setObjectName(u"passwordLabel")
        self.passwordLabel.setGeometry(QRect(55, 280, 130, 20))
        self.passwordLabel.setStyleSheet(u"QLabel#passwordLabel\n"
"{\n"
"font: 75 14pt \"Arial\";\n"
"	background-color: rgb(0, 85, 127);\n"
"}")
        self.loginButton = QPushButton(self.Background)
        self.loginButton.setObjectName(u"loginButton")
        self.loginButton.setGeometry(QRect(130, 350, 80, 25))
        self.loginButton.setStyleSheet(u"QPushButton#loginButton\n"
"{\n"
"	font: italic 10pt \"Arial\";\n"
"	background-color: rgb(0, 85, 127);\n"
"}\n"
"\n"
"QPushButton#loginButton:pressed\n"
"{\n"
"	font: italic 10pt \"Arial\";\n"
"	background-color: rgb(0, 85, 127);\n"
"	color: rgb(0, 136, 199);\n"
"	border: none\n"
"}\n"
"")
        self.loginButton.setCheckable(False)
        self.loginButton.setFlat(True)
        self.titleLabel = QLabel(self.Background)
        self.titleLabel.setObjectName(u"titleLabel")
        self.titleLabel.setGeometry(QRect(480, 90, 281, 61))
        self.titleLabel.setStyleSheet(u"QLabel#titleLabel\n"
"{\n"
"	font: 75 italic 42pt \"Tw Cen MT\";\n"
"	background-color: none\n"
"}")
        self.imageLabel = QLabel(self.Background)
        self.imageLabel.setObjectName(u"imageLabel")
        self.imageLabel.setGeometry(QRect(390, 90, 471, 501))
        self.imageLabel.setStyleSheet(u"QLabel#imageLabel\n"
"{\n"
"	background-color: none\n"
"}")
        self.imageLabel.setPixmap(QPixmap(u"../../Downloads/classroom-icon-images-vector-34189958-removebg-preview.png"))
        self.imageLabel.setScaledContents(True)
        self.loginLabel = QLabel(self.Background)
        self.loginLabel.setObjectName(u"loginLabel")
        self.loginLabel.setGeometry(QRect(120, 50, 101, 71))
        self.loginLabel.setStyleSheet(u"QLabel#loginLabel\n"
"{\n"
"	background-color: none;\n"
"	font: 75 italic 34pt \"Tw Cen MT\";\n"
"}")
        self.signUpButton = QPushButton(self.Background)
        self.signUpButton.setObjectName(u"signUpButton")
        self.signUpButton.setGeometry(QRect(120, 380, 101, 41))
        self.signUpButton.setStyleSheet(u"QPushButtonl#signUpButton\n"
"{\n"
"	font: italic 10pt \"Arial\";\n"
"	background-color: rgb(0, 85, 127);\n"
"}\n"
"\n"
"QPushButton#signUpButton:pressed\n"
"{\n"
"		font: italic 10pt \"Arial\";\n"
"		background-color: rgb(0, 85, 127);\n"
"		color: rgb(0, 136, 199);\n"
"		border: none;\n"
"}\n"
"")
        self.signUpButton.setCheckable(False)
        self.signUpButton.setFlat(True)
        LoginWindow.setCentralWidget(self.Background)

        self.retranslateUi(LoginWindow)

        self.loginButton.setDefault(False)
        self.signUpButton.setDefault(False)


        QMetaObject.connectSlotsByName(LoginWindow)
    # setupUi

    def retranslateUi(self, LoginWindow):
        LoginWindow.setWindowTitle(QCoreApplication.translate("LoginWindow", u"Login", None))
        self.usernameLineEdit.setText("")
        self.usernameLineEdit.setPlaceholderText("")
        self.usernameLabel.setText(QCoreApplication.translate("LoginWindow", u"Username:", None))
        self.passwordLabel.setText(QCoreApplication.translate("LoginWindow", u"Password:", None))
        self.loginButton.setText(QCoreApplication.translate("LoginWindow", u"Login", None))
        self.titleLabel.setText(QCoreApplication.translate("LoginWindow", u"SmartAttend", None))
        self.imageLabel.setText("")
        self.loginLabel.setText(QCoreApplication.translate("LoginWindow", u"Login", None))
        self.signUpButton.setText(QCoreApplication.translate("LoginWindow", u"Sign Up?", None))
    # retranslateUi

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = Ui_LoginWindow()
    sys.exit(app.exec_())