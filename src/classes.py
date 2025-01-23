from PyQt5.QtWidgets import QMainWindow, QWidget, QLabel, QApplication, QFrame, QLineEdit
import sys

class MainDashboard(QMainWindow):

    def __init__(self) -> None:

        super().__init__()
        self.initUI()

    def initUI(self) -> None:

        # Frame configuration
        self.setWindowTitle('Dashboard')
        self.setObjectName('mainDashboard')
        self.setPositioning(self, 0, 0, 900, 600)

        # Background configuration
        self.background = QWidget(self)
        self.setPositioning(self.background, 0, 0, 900, 600)
        self.background.setObjectName('background')
        self.background.setStyleSheet('QWidget#background{background-color: rgb(0, 85, 127);}')
        
        # User information label
        self.userInformationWidget = QWidget(self.background)
        self.setPositioning(self.userInformationWidget, 10, 10, 880, 90)
        self.userInformationWidget.setObjectName('userInformationWidget')
        self.userInformationWidget.setStyleSheet('QWidget#userInformationWidget{background-color: rgb(222, 222, 222);}')

        # Username label
        self.userNameLabel = QLabel(self.userInformationWidget)
        self.setPositioning(self.userNameLabel, 10, 10, 80, 30)
        self.userNameLabel.setText('Username')
        self.userNameLabel.setObjectName('usernameLabel')
        self.userNameLabel.setStyleSheet('QLabel#usernameLabel{background-color: none; font: 11pt \"Arial\";}')

        # Ensure the window is displayed
        self.show()

    def setPositioning(self, component: QWidget, x: int, y: int, width: int, height: int) -> None:
        component.setGeometry(x, y, width, height)
        component.setMinimumSize(width, height)
        component.setMaximumSize(width, height)

class Login(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    
    def initUI(self):
    
        # Frame configuration
        self.setWindowTitle('Login')
        self.setObjectName(u"self")
        self.setPositioning(self, 0, 0, 900, 600)
        self.setAutoFillBackground(False)

        # Backgorund widget
        self.backgroundWidget = QWidget(Login)
        self.backgroundWidget.setObjectName(u"background")
        self.backgroundWidget.setStyleSheet(u"QWidget#background{background-color: qlineargradient(spread:reflect, x1:0.323, y1:0.414955, x2:0.136, y2:1, stop:0.59887 rgba(0, 85, 127, 255), stop:1 rgba(255, 255, 255, 255));}")
        self.setPositioning(self.backgroundWidget, 0, 0, 900, 600)

        # Vertical seperator
        self.verticalSeperator = QFrame(self.backgroundWidget)
        self.verticalSeperator.setObjectName(u"verticalSeperator")
        self.setPositioning(self.verticalSeperator, 350, 0, 10, 600)
        self.verticalSeperator.setStyleSheet(u"background-color: rgb(220, 220, 220);")
        # self.verticalSeperator.setFrameShadow(QFrame.Plain)
        # self.verticalSeperator.setMidLineWidth(0)
        # self.verticalSeperator.setFrameShape(QFrame.VLine)


        # Username line edit
        self.usernameLineEdit = QLineEdit(self.backgroundWidget)
        self.usernameLineEdit.setObjectName(u"usernameLineEdit")
        self.setPositioning(self.usernameLineEdit, 55, 200, 240, 30)
        self.usernameLineEdit.setStyleSheet(u"background-color: rgb(255, 255, 255); border-color: rgb(0, 0, 0);")
        self.usernameLineEdit.setMaxLength(20)


        # Passsword line edit
        self.passwordLineEdit = QLineEdit(self.backgroundWidget)
        self.passwordLineEdit.setObjectName(u"passwordLineEdit")
        self.setPositioning(self.passwordLineEdit, 55, 310, 240, 30)
        self.passwordLineEdit.setStyleSheet(u"background-color: rgb(255, 255, 255); border-color: rgb(0, 0, 0);")
        self.passwordLineEdit.setMaxLength(30)

        
        # username label
        self.usernameLabel = QLabel(self.backgroundWidget)
        self.usernameLabel.setObjectName(u"usernameLabel")
        self.setPositioning(self.usernameLabel, 55, 170, 130, 20)
        self.usernameLabel.setStyleSheet(u"QLabel#usernameLabel{font: 75 14pt \"Arial\"; background-color: rgb(0, 85, 127);}")


        # password label
        self.passwordLabel = QLabel(self.backgroundLabel)
        self.passwordLabel.setObjectName(u"passwordLabel")
        self.setPositioning(self.passwordLabel, 55, 280, 130, 20)
        self.passwordLabel.setStyleSheet(u"QLabel#passwordLabel{font: 75 14pt \"Arial\"; background-color: rgb(0, 85, 127);}")


    def setPositioning(self, component: QWidget, x: int, y: int, width: int, height: int) -> None:

        component.setGeometry(x, y, width, height)
        component.setMinimumSize(width, height)
        component.setMaximumSize(width, height)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MainDashboard()
    sys.exit(app.exec_())
    
