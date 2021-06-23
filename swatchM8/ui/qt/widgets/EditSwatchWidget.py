from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from swatchM8.core.util.Helpers import convertToQColor

from swatchM8.ui.qt.widgets.ColorPickerWidget import ColorPickerWidget
from PySide2 import QtCore, QtGui, QtWidgets


class EditSwatchWidget(QWidget):

    def __init__(self, MainUI, Main):
        # type: (object, object) -> None

        super(EditSwatchWidget, self).__init__(None)  # Calls the init of the super class -> QWidget

        self.setupUi()
        self.connectElements()

        self.MainUI = MainUI
        self.Main = Main

        layout = QHBoxLayout()
        layout.setMargin(0)
        layout.addWidget(self.EditSwatchFrame)
        self.setLayout(layout)

        self.ColorPicker = ColorPickerWidget()
        self.ColorPickerPlaceHolder.setLayout(self.ColorPicker)

    def setupUi(self):
        self.EditSwatchFrame = QtWidgets.QFrame()
        self.EditSwatchFrame.setGeometry(QtCore.QRect(0, 0, 311, 271))
        self.EditSwatchFrame.setAutoFillBackground(True)
        self.EditSwatchFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.EditSwatchFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.EditSwatchFrame.setObjectName("EditSwatchFrame")
        self.label_24 = QtWidgets.QLabel(self.EditSwatchFrame)
        self.label_24.setGeometry(QtCore.QRect(10, 10, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_24.setFont(font)
        self.label_24.setObjectName("label_24")
        self.EditNameButton = QtWidgets.QPushButton(self.EditSwatchFrame)
        self.EditNameButton.setGeometry(QtCore.QRect(220, 60, 31, 23))
        self.EditNameButton.setObjectName("EditNameButton")
        self.DeleteButton = QtWidgets.QPushButton(self.EditSwatchFrame)
        self.DeleteButton.setGeometry(QtCore.QRect(210, 10, 91, 23))
        self.DeleteButton.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.DeleteButton.setObjectName("DeleteButton")
        self.NameLineEdit = QtWidgets.QLineEdit(self.EditSwatchFrame)
        self.NameLineEdit.setEnabled(False)
        self.NameLineEdit.setGeometry(QtCore.QRect(10, 60, 211, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.NameLineEdit.sizePolicy().hasHeightForWidth())
        self.NameLineEdit.setSizePolicy(sizePolicy)
        self.NameLineEdit.setMaximumSize(QtCore.QSize(240, 16777215))
        self.NameLineEdit.setReadOnly(False)
        self.NameLineEdit.setObjectName("NameLineEdit")
        self.ModelTreeView = QtWidgets.QTreeWidget(self.EditSwatchFrame)
        self.ModelTreeView.setGeometry(QtCore.QRect(10, 174, 291, 91))
        self.ModelTreeView.setStyleSheet("width:100%;")
        self.ModelTreeView.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.ModelTreeView.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.ModelTreeView.setObjectName("ModelTreeView")
        self.SwatchNameLabel_12 = QtWidgets.QLabel(self.EditSwatchFrame)
        self.SwatchNameLabel_12.setGeometry(QtCore.QRect(10, 40, 81, 16))
        self.SwatchNameLabel_12.setObjectName("SwatchNameLabel_12")
        self.ColorPickerPlaceHolder = QtWidgets.QFrame(self.EditSwatchFrame)
        self.ColorPickerPlaceHolder.setGeometry(QtCore.QRect(10, 90, 181, 81))
        self.ColorPickerPlaceHolder.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.ColorPickerPlaceHolder.setFrameShadow(QtWidgets.QFrame.Raised)
        self.ColorPickerPlaceHolder.setObjectName("ColorPickerPlaceHolder")
        self.SaveButton = QtWidgets.QPushButton(self.EditSwatchFrame)
        self.SaveButton.setGeometry(QtCore.QRect(240, 140, 61, 31))
        self.SaveButton.setObjectName("SaveButton")
        self.RevertNameButton = QtWidgets.QPushButton(self.EditSwatchFrame)
        self.RevertNameButton.setGeometry(QtCore.QRect(252, 60, 21, 23))
        self.RevertNameButton.setObjectName("RevertNameButton")

        self.retranslateUi()

    def retranslateUi(self):
        self.label_24.setText(QtWidgets.QApplication.translate("Form", "Edit Swatch", None, -1))
        self.EditNameButton.setText(QtWidgets.QApplication.translate("Form", "[edit]", None, -1))
        self.DeleteButton.setText(QtWidgets.QApplication.translate("Form", "Delete Swatch", None, -1))
        self.ModelTreeView.headerItem().setText(0, QtWidgets.QApplication.translate("Form", "Parts", None, -1))
        self.ModelTreeView.headerItem().setText(1, QtWidgets.QApplication.translate("Form", "From Model", None, -1))
        self.SwatchNameLabel_12.setText(QtWidgets.QApplication.translate("Form", "Swatch Name:", None, -1))
        self.SaveButton.setText(QtWidgets.QApplication.translate("Form", "Save", None, -1))
        self.RevertNameButton.setText(QtWidgets.QApplication.translate("Form", "<", None, -1))

    def connectElements(self):
        # type: () -> None

        self.EditNameButton.clicked.connect(lambda: self.NameLineEdit.setEnabled(True))
        self.RevertNameButton.clicked.connect(lambda: self.NameLineEdit.setText(self.selectedObject.name))
        self.SaveButton.clicked.connect(self.saveButton)
        self.DeleteButton.clicked.connect(self.deleteButton)

        self.NameLineEdit.textChanged.connect(self.inputCheckSwatchName)

    def inputCheckSwatchName(self):

        if self.NameLineEdit.text() == self.selectedObject.name:
            self.MainUI.setInputValid(self.NameLineEdit)
            return

        self.MainUI.checkifSwatchNameIsValid(self.NameLineEdit)

    def setNewData(self, selectedObject):
        # type: (object) -> None

        self.selectedObject = selectedObject

        self.ColorPicker.setNewData(convertToQColor(selectedObject.color))
        self.NameLineEdit.setText(selectedObject.name)
        self.populateTree(selectedObject)

        self.reset()

    def populateTree(self, selectedObject):
        # type: (object) -> None

        self.ModelTreeView.clear()

        for i in selectedObject.parts:
            partEntry = QTreeWidgetItem(self.ModelTreeView)
            partEntry.setText(0, i.name)
            partEntry.setData(3, 0, i)

            partEntry.setText(1, i.model.name)
            partEntry.setData(3, 1, i.model)

    def reset(self):
        # type: () -> None

        self.NameLineEdit.setEnabled(False)

    def saveButton(self):
        # type: () -> None

        self.selectedObject.color = self.ColorPicker.getPickedColor()
        self.selectedObject.name = self.NameLineEdit.text()
        self.MainUI.applyChanges()
        self.reset()

    def deleteButton(self):
        # type: () -> None

        self.Main.deleteSwatch(self.selectedObject)
        self.MainUI.applyChanges()
        self.reset()
        self.MainUI.hideAllStates()
