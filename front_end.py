# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.3
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from back_end import *
import creds

api_key = creds.API_KEY
api_key_sec = creds.API_KEY_SECRET
accs_tok = creds.ACCESS_TOKEN
accs_tok_sec = creds.ACCESS_TOKEN_SECRET
file_loc = '/home/jaden/Development/Notebooks/twitter'


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(673, 475)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(-20, 60, 121, 16))
        self.label_2.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.inpApiKeySec = QtWidgets.QLineEdit(self.centralwidget)
        self.inpApiKeySec.setGeometry(QtCore.QRect(470, 50, 191, 28))
        self.inpApiKeySec.setObjectName("inpApiKeySec")
        # self.inpApiKeySec.setEchoMode(QtGui.QLine)
        self.inpApiKeySec.setEchoMode(QtWidgets.QLineEdit.Password)

        self.inpAcsTok = QtWidgets.QLineEdit(self.centralwidget)
        self.inpAcsTok.setGeometry(QtCore.QRect(110, 90, 191, 28))
        self.inpAcsTok.setObjectName("inpAcsTok")
        self.inpAcsTok.setEchoMode(QtWidgets.QLineEdit.Password)

        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(10, 160, 181, 16))
        self.label_7.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName("label_7")
        self.inpAcsTokSec = QtWidgets.QLineEdit(self.centralwidget)
        self.inpAcsTokSec.setGeometry(QtCore.QRect(470, 90, 191, 28))
        self.inpAcsTokSec.setObjectName("inpAcsTokSec")
        self.inpAcsTokSec.setEchoMode(QtWidgets.QLineEdit.Password)

        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(0, 100, 101, 20))
        self.label_4.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(10, 10, 651, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.fileStorage = QtWidgets.QLineEdit(self.centralwidget)
        self.fileStorage.setGeometry(QtCore.QRect(200, 150, 441, 28))
        self.fileStorage.setObjectName("fileStorage")
        self.label_19 = QtWidgets.QLabel(self.centralwidget)
        self.label_19.setGeometry(QtCore.QRect(-10, 400, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_19.setFont(font)
        self.label_19.setAlignment(QtCore.Qt.AlignCenter)
        self.label_19.setObjectName("label_19")
        self.apiOutput = QtWidgets.QLabel(self.centralwidget)
        self.apiOutput.setGeometry(QtCore.QRect(90, 400, 541, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.apiOutput.setFont(font)
        self.apiOutput.setText("")
        self.apiOutput.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.apiOutput.setObjectName("apiOutput")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(10, 120, 651, 20))
        self.label_12.setObjectName("label_12")
        self.inpApiKey = QtWidgets.QLineEdit(self.centralwidget)
        self.inpApiKey.setGeometry(QtCore.QRect(110, 50, 191, 28))
        self.inpApiKey.setObjectName("inpApiKey")
        self.inpApiKey.setEchoMode(QtWidgets.QLineEdit.Password)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(310, 100, 151, 20))
        self.label_5.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(340, 60, 121, 16))
        self.label_3.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(10, 180, 651, 20))
        self.label_14.setObjectName("label_14")
        self.optTweets = QtWidgets.QRadioButton(self.centralwidget)
        self.optTweets.setGeometry(QtCore.QRect(10, 200, 191, 24))
        self.optTweets.setObjectName("optTweets")

        self.optTweets.setChecked(True)

        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(10, 290, 221, 16))
        self.label_10.setObjectName("label_10")
        self.inpTweets = QtWidgets.QLineEdit(self.centralwidget)
        self.inpTweets.setGeometry(QtCore.QRect(10, 310, 411, 28))
        self.inpTweets.setObjectName("inpTweets")
        self.label_18 = QtWidgets.QLabel(self.centralwidget)
        self.label_18.setGeometry(QtCore.QRect(10, 380, 651, 20))
        self.label_18.setObjectName("label_18")
        self.inpMax = QtWidgets.QLineEdit(self.centralwidget)
        self.inpMax.setGeometry(QtCore.QRect(460, 310, 201, 28))
        self.inpMax.setObjectName("inpMax")
        self.btnTweets = QtWidgets.QPushButton(self.centralwidget)
        self.btnTweets.setGeometry(QtCore.QRect(10, 350, 651, 28))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.btnTweets.setFont(font)
        self.btnTweets.setObjectName("btnTweets")
        self.btnTweets.clicked.connect(self.collectTweets)
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(460, 290, 161, 16))
        self.label_11.setObjectName("label_11")
        self.optFollowers = QtWidgets.QRadioButton(self.centralwidget)
        self.optFollowers.setGeometry(QtCore.QRect(10, 220, 201, 24))
        self.optFollowers.setObjectName("optFollowers")
        self.optFollowing = QtWidgets.QRadioButton(self.centralwidget)
        self.optFollowing.setGeometry(QtCore.QRect(10, 240, 181, 24))
        self.optFollowing.setObjectName("optFollowing")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(10, 260, 651, 20))
        self.label_15.setObjectName("label_15")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 673, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)

        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.inpApiKey.setText(api_key)
        self.inpApiKeySec.setText(api_key_sec)
        self.inpAcsTok.setText(accs_tok)
        self.inpAcsTokSec.setText(accs_tok_sec)
        self.fileStorage.setText(file_loc)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Twitter APi GUI"))
        self.label_2.setText(_translate("MainWindow", "API Key:"))
        self.label_7.setText(_translate("MainWindow", "CSV File Location Storage:"))
        self.label_4.setText(_translate("MainWindow", "Access Token:"))
        self.label_6.setText(_translate("MainWindow", "Twitter API Credentials"))
        self.label_19.setText(_translate("MainWindow", "Output: "))
        self.label_12.setText(_translate("MainWindow",
                                         "_____________________________________________________________________________________________________________________"))
        self.label_5.setText(_translate("MainWindow", "Access Token Secret:"))
        self.label_3.setText(_translate("MainWindow", "API Key Secret:"))
        self.label_14.setText(_translate("MainWindow",
                                         "_____________________________________________________________________________________________________________________"))
        self.optTweets.setText(_translate("MainWindow", "Collect Tweets"))
        self.label_10.setText(_translate("MainWindow", "Enter Search Query"))
        self.label_18.setText(_translate("MainWindow",
                                         "_____________________________________________________________________________________________________________________"))
        self.btnTweets.setText(_translate("MainWindow", "COLLECT"))
        self.label_11.setText(_translate("MainWindow", "Enter Max Number"))
        self.optFollowers.setText(_translate("MainWindow", "Collect Followers"))
        self.optFollowing.setText(_translate("MainWindow", "Collect Following"))
        self.label_15.setText(_translate("MainWindow",
                                         "_____________________________________________________________________________________________________________________"))

    def collectTweets(self):

        api_key = self.inpApiKey.text()
        api_key_secret = self.inpApiKeySec.text()
        access_token = self.inpAcsTok.text()
        access_token_secret = self.inpAcsTokSec.text()

        search_query = self.inpTweets.text()
        max_tweets = self.inpMax.text()
        file_location = self.fileStorage.text()

        if self.optTweets.isChecked():

            self.apiOutput.setText('Collecting Tweets...')
            self.apiOutput.repaint()

            result = collect(0, api_key, api_key_secret, access_token, access_token_secret, search_query, max_tweets, file_location)

        elif self.optFollowers.isChecked():
            self.apiOutput.setText('Collecting Followers...')
            self.apiOutput.repaint()
            result = collect(1, api_key, api_key_secret, access_token, access_token_secret, search_query, max_tweets, file_location)

        else:
            self.apiOutput.setText('Collecting Following...')
            self.apiOutput.repaint()
            result = collect(2, api_key, api_key_secret, access_token, access_token_secret, search_query, max_tweets, file_location)

        self.apiOutput.setText(result)
        self.apiOutput.repaint()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('Breeze')
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
