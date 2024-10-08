# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'jarvisGUI_new.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_jarvisGUI(object):
    def setupUi(self, jarvisGUI):
        jarvisGUI.setObjectName("jarvisGUI")
        jarvisGUI.resize(1427, 921)
        self.centralwidget = QtWidgets.QWidget(jarvisGUI)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-4, -7, 1431, 831))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("jarvis gif/7LP8.gif"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(1100, 480, 281, 241))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("jarvis gif/spheres-motion-for-ai-product-design-by-gleb-large.gif"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(0, -10, 401, 161))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("jarvis gif/T8bahf.gif"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(1310, 10, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: rgb(255, 0, 0);\n"
"")
        self.pushButton_2.setObjectName("pushButton_2")
        self.logo = QtWidgets.QLabel(self.centralwidget)
        self.logo.setGeometry(QtCore.QRect(36, 443, 331, 261))
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap("jarvis gif/jarvis.gif"))
        self.logo.setScaledContents(True)
        self.logo.setObjectName("logo")
        self.lower_backgroung = QtWidgets.QLabel(self.centralwidget)
        self.lower_backgroung.setGeometry(QtCore.QRect(0, 760, 1431, 161))
        self.lower_backgroung.setText("")
        self.lower_backgroung.setPixmap(QtGui.QPixmap("jarvis gif/sound-wave-waves.gif"))
        self.lower_backgroung.setScaledContents(True)
        self.lower_backgroung.setObjectName("lower_backgroung")
        self.listening_label = QtWidgets.QLabel(self.centralwidget)
        self.listening_label.setGeometry(QtCore.QRect(1100, 20, 201, 171))
        self.listening_label.setText("")
        self.listening_label.setPixmap(QtGui.QPixmap("jarvis gif/sirilike.gif"))
        self.listening_label.setScaledContents(True)
        self.listening_label.setObjectName("listening_label")
        self.speaking_label = QtWidgets.QLabel(self.centralwidget)
        self.speaking_label.setGeometry(QtCore.QRect(1100, 20, 201, 171))
        self.speaking_label.setText("")
        self.speaking_label.setPixmap(QtGui.QPixmap("jarvis gif/ava_ai.gif"))
        self.speaking_label.setScaledContents(True)
        self.speaking_label.setObjectName("speaking_label")
        self.processing_label = QtWidgets.QLabel(self.centralwidget)
        self.processing_label.setGeometry(QtCore.QRect(1100, 20, 201, 171))
        self.processing_label.setText("")
        self.processing_label.setPixmap(QtGui.QPixmap("jarvis gif/a064a7f04f9ecbf99cc543f1ba976adb69949e71_hq.gif"))
        self.processing_label.setScaledContents(True)
        self.processing_label.setObjectName("processing_label")
        self.terminalOutputBox = QtWidgets.QTextEdit(self.centralwidget)
        self.terminalOutputBox.setGeometry(QtCore.QRect(0, 770, 1331, 111))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.terminalOutputBox.setFont(font)
        self.terminalOutputBox.setStyleSheet("color: rgb(0, 255, 0);\n"
"background-color:transparent;\n"
"border:none;\n"
"")
        self.terminalOutputBox.setObjectName("terminalOutputBox")
        self.terminalInputBox = QtWidgets.QLineEdit(self.centralwidget)
        self.terminalInputBox.setGeometry(QtCore.QRect(0, 890, 1331, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True) 
        font.setWeight(75)
        self.terminalInputBox.setFont(font)
        self.terminalInputBox.setStyleSheet("color: rgb(0, 255, 0);\n"
"background-color:transparent;\n"
"border:none;\n"
"")
        self.terminalInputBox.setObjectName("terminalInputBox")
        self.enterBotton = QtWidgets.QPushButton(self.centralwidget)
        self.enterBotton.setGeometry(QtCore.QRect(1340, 890, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.enterBotton.setFont(font)
        self.enterBotton.setStyleSheet("background-color: rgb(255, 0, 0);\n"
"")
        self.enterBotton.setObjectName("enterBotton")
        jarvisGUI.setCentralWidget(self.centralwidget)

        self.retranslateUi(jarvisGUI)
        QtCore.QMetaObject.connectSlotsByName(jarvisGUI)

    def retranslateUi(self, jarvisGUI):
        _translate = QtCore.QCoreApplication.translate
        jarvisGUI.setWindowTitle(_translate("jarvisGUI", "MainWindow"))
        self.pushButton_2.setText(_translate("jarvisGUI", "EXIT"))
        self.enterBotton.setText(_translate("jarvisGUI", "ENTER"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    jarvisGUI = QtWidgets.QMainWindow()
    ui = Ui_jarvisGUI()
    ui.setupUi(jarvisGUI)
    jarvisGUI.show()
    sys.exit(app.exec_())
