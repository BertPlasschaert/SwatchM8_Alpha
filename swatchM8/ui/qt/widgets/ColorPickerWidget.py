from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2 import QtCore, QtGui, QtWidgets


class ColorPickerWidget(QHBoxLayout):

    def __init__(self):
        # type: () -> None

        super(ColorPickerWidget, self).__init__()  # Calls the init of the super class -> QWidget
        self.setupUi()
        self.connectElements()

        self.pickedColor = None
        self.oldColor = None

        self.addWidget(self.ColorPickerGroupBox)
        self.setMargin(0)
        self.setNewData(QColor('white'))

    def setupUi(self):
        self.ColorPickerGroupBox = QtWidgets.QGroupBox()
        self.ColorPickerGroupBox.setGeometry(QtCore.QRect(0, 0, 181, 81))
        self.ColorPickerGroupBox.setObjectName("ColorPickerGroupBox")
        self.OldColorFrame = QtWidgets.QFrame(self.ColorPickerGroupBox)
        self.OldColorFrame.setGeometry(QtCore.QRect(90, 20, 41, 51))
        self.OldColorFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.OldColorFrame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.OldColorFrame.setObjectName("OldColorFrame")
        self.SwatchNameLabel_23 = QtWidgets.QLabel(self.OldColorFrame)
        self.SwatchNameLabel_23.setGeometry(QtCore.QRect(0, 0, 21, 16))
        self.SwatchNameLabel_23.setObjectName("SwatchNameLabel_23")
        self.ColorHexLineEdit = QtWidgets.QLineEdit(self.ColorPickerGroupBox)
        self.ColorHexLineEdit.setGeometry(QtCore.QRect(10, 50, 71, 20))
        self.ColorHexLineEdit.setMaximumSize(QtCore.QSize(80, 16777215))
        self.ColorHexLineEdit.setText("")
        self.ColorHexLineEdit.setReadOnly(False)
        self.ColorHexLineEdit.setObjectName("ColorHexLineEdit")
        self.ColorPickerButton = QtWidgets.QPushButton(self.ColorPickerGroupBox)
        self.ColorPickerButton.setGeometry(QtCore.QRect(10, 20, 71, 21))
        self.ColorPickerButton.setObjectName("ColorPickerButton")
        self.NewColorFrame = QtWidgets.QFrame(self.ColorPickerGroupBox)
        self.NewColorFrame.setGeometry(QtCore.QRect(130, 20, 41, 51))
        self.NewColorFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.NewColorFrame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.NewColorFrame.setObjectName("NewColorFrame")
        self.SwatchNameLabel_24 = QtWidgets.QLabel(self.NewColorFrame)
        self.SwatchNameLabel_24.setGeometry(QtCore.QRect(0, 0, 21, 16))
        self.SwatchNameLabel_24.setObjectName("SwatchNameLabel_24")
        self.RevertColorButton = QtWidgets.QPushButton(self.ColorPickerGroupBox)
        self.RevertColorButton.setGeometry(QtCore.QRect(120, 50, 21, 23))
        self.RevertColorButton.setObjectName("RevertColorButton")

        self.retranslateUi()

    def retranslateUi(self):
        self.ColorPickerGroupBox.setTitle(QtWidgets.QApplication.translate("Form", "Color", None, -1))
        self.SwatchNameLabel_23.setText(QtWidgets.QApplication.translate("Form", "Old", None, -1))
        self.ColorPickerButton.setText(QtWidgets.QApplication.translate("Form", "Color Picker", None, -1))
        self.SwatchNameLabel_24.setText(QtWidgets.QApplication.translate("Form", "New", None, -1))
        self.RevertColorButton.setText(QtWidgets.QApplication.translate("Form", ">", None, -1))

    def connectElements(self):
        # type: () -> None

        self.ColorPickerButton.clicked.connect(self.colorPickerButton)
        self.RevertColorButton.clicked.connect(self.revertColorButton)

        self.ColorHexLineEdit.textEdited.connect(self.updatePickedColorFromHex)

    def setNewData(self, currentColor):
        # type: (QColor) -> None

        self.oldColor = currentColor
        self.setColorFrame(self.OldColorFrame, currentColor)
        self.setHexLine(self.oldColor)

        self.NewColorFrame.setStyleSheet("")

    def colorPickerButton(self):
        # type: () -> None

        self.pickedColor = QColorDialog.getColor()
        self.setHexLine(self.pickedColor)
        self.setColorFrame(self.NewColorFrame, self.pickedColor)

    def revertColorButton(self):
        # type: () -> None

        self.setColorFrame(self.NewColorFrame, self.oldColor)
        self.setHexLine(self.oldColor)
        self.pickedColor = self.oldColor

    def updatePickedColorFromHex(self):
        # type: () -> None

        self.pickedColor = QColor(self.ColorHexLineEdit.text())
        self.setColorFrame(self.NewColorFrame, self.pickedColor)

    def setColorFrame(self, frame, color):
        # type: (QFrame, QColor) -> None

        frame.setStyleSheet("background-color:" + color.name() + ";")

    def setHexLine(self, color):
        # type: (QColor) -> None

        self.ColorHexLineEdit.setText(color.name())

    def getPickedColor(self):
        # type: () -> list

        if self.pickedColor == None:

            return self.oldColor.getRgb()

        else:
            return self.pickedColor.getRgb()
