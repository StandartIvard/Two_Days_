import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.uic import loadUi
from PyQt5.QtGui import QCloseEvent
from PyQt5 import QtCore
from gui import resources


def closeEvent(event: QCloseEvent):
    # Предотвращаем закрытие окна
    event.ignore()


class TestUILoader(QMainWindow, app=QApplication(sys.argv)):
    testResult = 0
    senders = list()
    def __init__(self):
        super(TestUILoader, self).__init__()
        loadUi("gui/forBuTest/TESTMAIN.ui", self)

        self.checkBox.stateChanged.connect(self.checkbox_changed)
        self.checkBox_2.stateChanged.connect(self.checkbox_changed)
        self.checkBox_3.stateChanged.connect(self.checkbox_changed)
        self.checkBox_4.stateChanged.connect(self.checkbox_changed)
        self.checkBox_5.stateChanged.connect(self.checkbox_changed)
        self.checkBox_6.stateChanged.connect(self.checkbox_changed)
        self.checkBox_7.stateChanged.connect(self.checkbox_changed)
        self.checkBox_8.stateChanged.connect(self.checkbox_changed)

    def checkbox_changed(self, state):
        sender = self.sender().objectName()  # Получите отправителя события
        if sender in self.senders:
            self.senders.remove(sender)
        else:
            self.senders.append(sender)
        if (sender == "checkBox" and "checkBox_2" in self.senders) or (sender == "checkBox_2" and "checkBox" in self.senders):
            self.app.exit()
        elif (sender == "checkBox_3" and "checkBox_4" in self.senders) or (sender == "checkBox_4" and "checkBox_3" in self.senders):
            self.app.exit()
        elif (sender == "checkBox_8" and "checkBox_5" in self.senders) or (sender == "checkBox_5" and "checkBox_8" in self.senders):
            self.app.exit()
        elif (sender == "checkBox_6" and "checkBox_7" in self.senders) or (sender == "checkBox_7" and "checkBox_6" in self.senders):
            self.app.exit()
        if len(self.senders) == 4:
            print("ready")
            self.app.exit()


def PyQtMain():
    app = QApplication(sys.argv)
    window = TestUILoader(app)
    window.show()
    window.closeEvent = closeEvent

    sys.exit(app.exec_())