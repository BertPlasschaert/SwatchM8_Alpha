from PySide2 import QtCore
from PySide2 import QtWidgets

from swatchM8.ui.qt.ui_splash import Ui_SplashWindow


class SplashScreen(QtWidgets.QMainWindow):

    def __init__(self, MainUI, parent=None):
        # type: (object, object) -> None

        # QtWidgets.QMainWindow.__init__(parent)
        super(SplashScreen, self).__init__(parent)

        self.MainUI = MainUI

        self.ui = Ui_SplashWindow()
        self.ui.setupUi(self)

        ## QTimer ==> Start
        self.timer = QtCore.QTimer()
        self.timer.start(40)

        ## UI ==> interface Codes
        ################################################################################
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)

        ## UI ==> Loading strings Logic
        self.currentString1Index = 0
        self.currentString2Index = 0
        self.updateString()

        self.timer.timeout.connect(self.updateString)

        # self.ui.Title.setText("Swatch M8")

        print(self.ui.Title.text())


    def updateString(self):
        # type: () -> None

        stringOptions = [["Loading dataBase", ["Loading Parts", "Loading Models", "Initializing Sprites", "Loading Textures", "reading into memory", "Saving BackupL", "Done"]],
                         ["Loading Classes", ["Loading UI Runner", "Loading Main Controller", "Initializing Controller", "Loading Json Repository", "Loading Texture", "Loading Model and Part Classes", "Defining ImageClass", "Done"]],
                         ["Loading Preferences", ["Loading User settings", "Loading hotKeys", "Initializing custom User Interface", "Done"]], ["initializing swatchM8", ["Loading Final pieces", "Calculating Swatch locations", "Done"]]]

        # print(str(self.currentString1Index) + "  " + str(self.currentString2Index))

        if self.currentString2Index == (len(stringOptions[self.currentString1Index][1])):
            self.currentString1Index = self.currentString1Index + 1
            self.currentString2Index = 0

        if self.currentString1Index == len(stringOptions):

            self.timer.stop()
            self.close()

        else:

            self.ui.LoadingString01.setText(str(stringOptions[self.currentString1Index][0]))
            self.ui.LoadingString02.setText(stringOptions[self.currentString1Index][1][self.currentString2Index])
            self.currentString2Index = self.currentString2Index + 1

    def closeEvent(self, event):

        self.MainUI.runMainWindow()
