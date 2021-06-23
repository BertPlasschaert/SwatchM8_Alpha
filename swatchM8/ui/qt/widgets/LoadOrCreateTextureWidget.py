from PySide2 import QtCore, QtGui, QtWidgets

from PySide2.QtWidgets import *

from swatchM8.ui.qt.WindowStates import PopupFrameStates

from swatchM8.core.util.ExeptionHandeling import InvalidInputExeption

import os

class LoadOrCreateTextureWidget(QWidget):

    def __init__(self, mainUI, main):
        # type: (object, object) -> None
        super(LoadOrCreateTextureWidget, self).__init__(None)  # Calls the init of the super class -> QWidget

        self.setupUi()
        self.connectElements()
        self.MainUI = mainUI
        self.Main = main

        layout = QHBoxLayout()
        layout.setMargin(0)
        layout.addWidget(self.LoadOrCreateTextureFrame)
        self.setLayout(layout)

    def setupUi(self):
        self.LoadOrCreateTextureFrame = QtWidgets.QFrame()
        self.LoadOrCreateTextureFrame.setGeometry(QtCore.QRect(0, 0, 561, 331))
        self.LoadOrCreateTextureFrame.setAutoFillBackground(True)
        self.LoadOrCreateTextureFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.LoadOrCreateTextureFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.LoadOrCreateTextureFrame.setObjectName("LoadOrCreateTextureFrame")
        self.LoadButton = QtWidgets.QPushButton(self.LoadOrCreateTextureFrame)
        self.LoadButton.setGeometry(QtCore.QRect(130, 130, 131, 91))
        self.LoadButton.setObjectName("LoadButton")
        self.label_28 = QtWidgets.QLabel(self.LoadOrCreateTextureFrame)
        self.label_28.setGeometry(QtCore.QRect(20, 10, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_28.setFont(font)
        self.label_28.setObjectName("label_28")
        self.CreateButton = QtWidgets.QPushButton(self.LoadOrCreateTextureFrame)
        self.CreateButton.setGeometry(QtCore.QRect(310, 130, 131, 91))
        self.CreateButton.setObjectName("CreateButton")

        self.retranslateUi()

    def retranslateUi(self):
        self.LoadButton.setText(QtWidgets.QApplication.translate("Form", "Load Texture", None, -1))
        self.label_28.setText(QtWidgets.QApplication.translate("Form", "Load or create a Texture", None, -1))
        self.CreateButton.setText(QtWidgets.QApplication.translate("Form", "Create New Texture", None, -1))

    def connectElements(self):
        # type: () -> None

        self.LoadButton.pressed.connect(self.loadButton)
        self.CreateButton.pressed.connect(lambda: self.MainUI.ui.PopUpFrame.setCurrentIndex(PopupFrameStates.createTexture.value))

    def loadButton(self):
        # type: () -> None

        try:

            dialog = QFileDialog(self)
            # path = dialog.getOpenFileName(None, "Open Project file", r"D:\OneDrive - BUas\MGT\Scripts\SwatchM8\testFiles", "Json files (*.json)")[0]
            path = dialog.getOpenFileName(None, "Open Project file", os.path.expanduser("~"), "Json files (*.json)")[0]

            if path == '':
                raise InvalidInputExeption('please select a valid .Json file')

        except InvalidInputExeption:
            raise

        self.Main.loadData(path)
        self.MainUI.loadData()