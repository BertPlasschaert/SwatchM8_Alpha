from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2 import QtCore, QtGui, QtWidgets
import os

import logging

logger = logging.getLogger()


class TextureSettingsWidget(QWidget):

    def __init__(self, mainUI, main):
        # type: (object, object) -> None

        super(TextureSettingsWidget, self).__init__(None)  # Calls the init of the super class -> QWidget

        self.setupUi()
        self.connectElements()
        self.MainUI = mainUI
        self.Main = main

        layout = QHBoxLayout()
        layout.setMargin(0)
        layout.addWidget(self.TextureSettingsFrame)
        self.setLayout(layout)

    def setupUi(self):
        self.TextureSettingsFrame = QtWidgets.QFrame()
        self.TextureSettingsFrame.setGeometry(QtCore.QRect(0, 0, 561, 331))
        self.TextureSettingsFrame.setAutoFillBackground(True)
        self.TextureSettingsFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.TextureSettingsFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.TextureSettingsFrame.setObjectName("TextureSettingsFrame")
        self.label_27 = QtWidgets.QLabel(self.TextureSettingsFrame)
        self.label_27.setGeometry(QtCore.QRect(20, 10, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_27.setFont(font)
        self.label_27.setObjectName("label_27")
        self.TextureSizePixelLabel_3 = QtWidgets.QLabel(self.TextureSettingsFrame)
        self.TextureSizePixelLabel_3.setGeometry(QtCore.QRect(190, 148, 16, 20))
        self.TextureSizePixelLabel_3.setObjectName("TextureSizePixelLabel_3")
        self.BrowseButton = QtWidgets.QPushButton(self.TextureSettingsFrame)
        self.BrowseButton.setGeometry(QtCore.QRect(428, 178, 61, 23))
        self.BrowseButton.setObjectName("BrowseButton")
        self.EditNameButton = QtWidgets.QPushButton(self.TextureSettingsFrame)
        self.EditNameButton.setGeometry(QtCore.QRect(260, 118, 51, 23))
        self.EditNameButton.setObjectName("EditNameButton")
        self.TextureSizeLabel = QtWidgets.QLabel(self.TextureSettingsFrame)
        self.TextureSizeLabel.setGeometry(QtCore.QRect(70, 148, 71, 16))
        self.TextureSizeLabel.setObjectName("TextureSizeLabel")
        self.SaveLocationLabel = QtWidgets.QLabel(self.TextureSettingsFrame)
        self.SaveLocationLabel.setGeometry(QtCore.QRect(60, 180, 71, 16))
        self.SaveLocationLabel.setObjectName("SaveLocationLabel")
        self.SaveLocationLineEdit = QtWidgets.QLineEdit(self.TextureSettingsFrame)
        self.SaveLocationLineEdit.setGeometry(QtCore.QRect(136, 180, 291, 20))
        self.SaveLocationLineEdit.setText("")
        self.SaveLocationLineEdit.setObjectName("SaveLocationLineEdit")
        self.TextureNameLabel = QtWidgets.QLabel(self.TextureSettingsFrame)
        self.TextureNameLabel.setGeometry(QtCore.QRect(60, 118, 71, 16))
        self.TextureNameLabel.setObjectName("TextureNameLabel")
        self.NameLineEdit = QtWidgets.QLineEdit(self.TextureSettingsFrame)
        self.NameLineEdit.setEnabled(False)
        self.NameLineEdit.setGeometry(QtCore.QRect(140, 118, 113, 20))
        self.NameLineEdit.setText("")
        self.NameLineEdit.setObjectName("NameLineEdit")
        self.RevertSaveLocationButton = QtWidgets.QPushButton(self.TextureSettingsFrame)
        self.RevertSaveLocationButton.setGeometry(QtCore.QRect(490, 178, 21, 23))
        self.RevertSaveLocationButton.setObjectName("RevertSaveLocationButton")
        self.Size2LineEdit = QtWidgets.QLineEdit(self.TextureSettingsFrame)
        self.Size2LineEdit.setEnabled(False)
        self.Size2LineEdit.setGeometry(QtCore.QRect(210, 148, 41, 20))
        self.Size2LineEdit.setText("")
        self.Size2LineEdit.setObjectName("Size2LineEdit")
        self.RevertNameButton = QtWidgets.QPushButton(self.TextureSettingsFrame)
        self.RevertNameButton.setGeometry(QtCore.QRect(312, 118, 21, 23))
        self.RevertNameButton.setObjectName("RevertNameButton")
        self.RevertSizeButton = QtWidgets.QPushButton(self.TextureSettingsFrame)
        self.RevertSizeButton.setGeometry(QtCore.QRect(312, 148, 21, 23))
        self.RevertSizeButton.setObjectName("RevertSizeButton")
        self.EditSizeButton = QtWidgets.QPushButton(self.TextureSettingsFrame)
        self.EditSizeButton.setGeometry(QtCore.QRect(260, 148, 51, 23))
        self.EditSizeButton.setObjectName("EditSizeButton")
        self.SizeLineEdit = QtWidgets.QLineEdit(self.TextureSettingsFrame)
        self.SizeLineEdit.setEnabled(False)
        self.SizeLineEdit.setGeometry(QtCore.QRect(140, 148, 41, 20))
        self.SizeLineEdit.setText("")
        self.SizeLineEdit.setObjectName("SizeLineEdit")
        self.SaveChangesButton = QtWidgets.QPushButton(self.TextureSettingsFrame)
        self.SaveChangesButton.setGeometry(QtCore.QRect(440, 270, 91, 23))
        self.SaveChangesButton.setObjectName("SaveChangesButton")

        self.retranslateUi()

    def retranslateUi(self):
        self.label_27.setText(QtWidgets.QApplication.translate("Form", "Texture Settings", None, -1))
        self.TextureSizePixelLabel_3.setText(QtWidgets.QApplication.translate("Form", "X ", None, -1))
        self.BrowseButton.setText(QtWidgets.QApplication.translate("Form", "Browse", None, -1))
        self.EditNameButton.setText(QtWidgets.QApplication.translate("Form", "Edit", None, -1))
        self.TextureSizeLabel.setText(QtWidgets.QApplication.translate("Form", "Texure Size:", None, -1))
        self.SaveLocationLabel.setText(QtWidgets.QApplication.translate("Form", "Save Location:", None, -1))
        self.TextureNameLabel.setText(QtWidgets.QApplication.translate("Form", "Texture Name:", None, -1))
        self.RevertSaveLocationButton.setText(QtWidgets.QApplication.translate("Form", "<", None, -1))
        self.RevertNameButton.setText(QtWidgets.QApplication.translate("Form", "<", None, -1))
        self.RevertSizeButton.setText(QtWidgets.QApplication.translate("Form", "<", None, -1))
        self.EditSizeButton.setText(QtWidgets.QApplication.translate("Form", "Edit", None, -1))
        self.SaveChangesButton.setText(QtWidgets.QApplication.translate("Form", "Save changes", None, -1))

    def connectElements(self):
        # type: () -> None

        self.EditNameButton.clicked.connect(lambda: self.NameLineEdit.setEnabled(True))
        self.EditSizeButton.clicked.connect(lambda: self.SizeLineEdit.setEnabled(True))

        self.RevertNameButton.clicked.connect(lambda: self.NameLineEdit.setText(str(self.textureObject.name)))
        self.RevertSizeButton.clicked.connect(lambda: self.SizeLineEdit.setText(str(self.textureObject.size)))
        self.RevertSaveLocationButton.clicked.connect(lambda: self.SaveLocationLineEdit.setText(str(self.textureObject.filePath)))
        self.SaveChangesButton.clicked.connect(self.saveChangesButton)
        self.BrowseButton.pressed.connect(self.browseButton)

        self.SizeLineEdit.textChanged.connect(lambda: self.Size2LineEdit.setText(self.SizeLineEdit.text()))
        self.SizeLineEdit.textChanged.connect(self.inputCheckSize)

    def inputCheckSize(self):

        if self.SizeLineEdit.text().isdigit() == False:
            self.MainUI.setInputInvalid(self.SizeLineEdit)
            return

        if int(self.SizeLineEdit.text()) < self.Main.texture.amountOfSwatchesOnRow:
            self.MainUI.setInputInvalid(self.SizeLineEdit)
            return

        self.MainUI.setInputValid(self.SizeLineEdit)

    def setNewData(self, textureObject):
        # type: (object) -> None

        self.textureObject = textureObject

        self.NameLineEdit.setText(textureObject.name)
        self.SizeLineEdit.setText(str(textureObject.size))
        self.SaveLocationLineEdit.setText(str(textureObject.filePath))

    def saveChangesButton(self):
        # type: () -> None

        self.removeOldImageAndJson()

        self.textureObject.name = str(self.NameLineEdit.text())
        self.textureObject.size = int(self.SizeLineEdit.text())

        if self.SaveLocationLineEdit.text() != "":
            self.textureObject.filePath = str(self.SaveLocationLineEdit.text())

        self.Main.saveData()
        self.MainUI.hideAllStates()

        self.reset()

    def browseButton(self):
        # type: () -> None

        dialog = QFileDialog(self, "select a save folder", r"D:\OneDrive - BUas\MGT\Scripts\SwatchM8\testFiles", "folder")
        path = dialog.getExistingDirectory()

        self.SaveLocationLineEdit.setText(path)

    def removeOldImageAndJson(self):

        files = [os.path.join(self.textureObject.filePath, self.textureObject.name) + '.json', os.path.join(self.textureObject.filePath, self.textureObject.name) + '.png']

        for i in files:

            if os.path.exists(i):
                os.remove(i)

            else:
                logger.warning("Could not delete / find specified file {}".format(i))

    def reset(self):
        self.NameLineEdit.setEnabled(False)
        self.SizeLineEdit.setEnabled(False)
