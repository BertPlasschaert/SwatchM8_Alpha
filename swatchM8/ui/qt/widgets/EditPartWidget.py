from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2 import QtCore, QtGui, QtWidgets
from swatchM8.core.util.Helpers import convertToQColor


class EditPartWidget(QWidget):

    def __init__(self, MainUI, Main):
        # type: (object, object) -> None

        super(EditPartWidget, self).__init__(None)  # Calls the init of the super class -> QWidget

        self.setupUi()
        self.connectElements()
        self.connectInputChecks()
        self.MainUI = MainUI
        self.Main = Main

        layout = QHBoxLayout()
        layout.setMargin(0)
        layout.addWidget(self.EditPartFrame)
        self.setLayout(layout)

        self.ColorPicker = None
        # self.ColorPicker = ColorPickerWidget()
        # self.ColorPickerPlaceHolder.setLayout(self.ColorPicker)

        ##########  NEEDS MORE WORK TO FUNCTION WITH UNWRAP  ##############
        self.ChangeSwatchComboBox.setEnabled(False)
        self.SwatchNameLabel_27.setEnabled(False)
        self.RevertSwatchComboBox.setEnabled(False)
        ###################################################################

    def setupUi(self):
        self.EditPartFrame = QtWidgets.QFrame()
        self.EditPartFrame.setGeometry(QtCore.QRect(0, 0, 311, 275))
        self.EditPartFrame.setAutoFillBackground(True)
        self.EditPartFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.EditPartFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.EditPartFrame.setObjectName("EditPartFrame")
        self.SwatchNameLabel_10 = QtWidgets.QLabel(self.EditPartFrame)
        self.SwatchNameLabel_10.setGeometry(QtCore.QRect(10, 50, 61, 16))
        self.SwatchNameLabel_10.setObjectName("SwatchNameLabel_10")
        self.NameLineEdit = QtWidgets.QLineEdit(self.EditPartFrame)
        self.NameLineEdit.setEnabled(False)
        self.NameLineEdit.setGeometry(QtCore.QRect(90, 52, 158, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.NameLineEdit.sizePolicy().hasHeightForWidth())
        self.NameLineEdit.setSizePolicy(sizePolicy)
        self.NameLineEdit.setMaximumSize(QtCore.QSize(25555, 16777215))
        self.NameLineEdit.setReadOnly(False)
        self.NameLineEdit.setObjectName("NameLineEdit")
        self.label_23 = QtWidgets.QLabel(self.EditPartFrame)
        self.label_23.setGeometry(QtCore.QRect(10, 10, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_23.setFont(font)
        self.label_23.setObjectName("label_23")
        self.EditNameButton = QtWidgets.QPushButton(self.EditPartFrame)
        self.EditNameButton.setGeometry(QtCore.QRect(248, 50, 31, 23))
        self.EditNameButton.setObjectName("EditNameButton")
        self.DeletePart = QtWidgets.QPushButton(self.EditPartFrame)
        self.DeletePart.setGeometry(QtCore.QRect(230, 10, 71, 23))
        self.DeletePart.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.DeletePart.setObjectName("DeletePart")
        self.ChangeModelComboBox = QtWidgets.QComboBox(self.EditPartFrame)
        self.ChangeModelComboBox.setGeometry(QtCore.QRect(90, 90, 191, 22))
        self.ChangeModelComboBox.setObjectName("ChangeModelComboBox")
        self.SwatchNameLabel_26 = QtWidgets.QLabel(self.EditPartFrame)
        self.SwatchNameLabel_26.setGeometry(QtCore.QRect(10, 90, 71, 20))
        self.SwatchNameLabel_26.setObjectName("SwatchNameLabel_26")
        self.ChangeSwatchComboBox = QtWidgets.QComboBox(self.EditPartFrame)
        self.ChangeSwatchComboBox.setGeometry(QtCore.QRect(90, 120, 191, 22))
        self.ChangeSwatchComboBox.setObjectName("ChangeSwatchComboBox")
        self.SwatchNameLabel_27 = QtWidgets.QLabel(self.EditPartFrame)
        self.SwatchNameLabel_27.setGeometry(QtCore.QRect(10, 120, 81, 16))
        self.SwatchNameLabel_27.setObjectName("SwatchNameLabel_27")
        self.ColorPickerFrame = QtWidgets.QFrame(self.EditPartFrame)
        self.ColorPickerFrame.setGeometry(QtCore.QRect(90, 150, 111, 41))
        self.ColorPickerFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.ColorPickerFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.ColorPickerFrame.setObjectName("ColorPickerFrame")
        self.SaveButton = QtWidgets.QPushButton(self.EditPartFrame)
        self.SaveButton.setGeometry(QtCore.QRect(210, 150, 91, 81))
        self.SaveButton.setObjectName("SaveButton")
        self.RevertModelComboBox = QtWidgets.QPushButton(self.EditPartFrame)
        self.RevertModelComboBox.setGeometry(QtCore.QRect(280, 90, 21, 23))
        self.RevertModelComboBox.setObjectName("RevertModelComboBox")
        self.RevertNameButton = QtWidgets.QPushButton(self.EditPartFrame)
        self.RevertNameButton.setGeometry(QtCore.QRect(280, 50, 21, 23))
        self.RevertNameButton.setObjectName("RevertNameButton")
        self.RevertSwatchComboBox = QtWidgets.QPushButton(self.EditPartFrame)
        self.RevertSwatchComboBox.setGeometry(QtCore.QRect(280, 120, 21, 23))
        self.RevertSwatchComboBox.setObjectName("RevertSwatchComboBox")
        self.AddPolysButton = QtWidgets.QPushButton(self.EditPartFrame)
        self.AddPolysButton.setGeometry(QtCore.QRect(125, 245, 81, 23))
        self.AddPolysButton.setObjectName("AddPolysButton")
        self.line = QtWidgets.QFrame(self.EditPartFrame)
        self.line.setGeometry(QtCore.QRect(0, 230, 311, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.SelectPolysButton = QtWidgets.QPushButton(self.EditPartFrame)
        self.SelectPolysButton.setGeometry(QtCore.QRect(10, 245, 101, 23))
        self.SelectPolysButton.setObjectName("SelectPolysButton")
        self.RemovePolysButton = QtWidgets.QPushButton(self.EditPartFrame)
        self.RemovePolysButton.setGeometry(QtCore.QRect(210, 245, 91, 23))
        self.RemovePolysButton.setObjectName("RemovePolysButton")
        self.GoToSwatchButton = QtWidgets.QPushButton(self.EditPartFrame)
        self.GoToSwatchButton.setGeometry(QtCore.QRect(90, 200, 111, 21))
        self.GoToSwatchButton.setObjectName("GoToSwatchButton")
        self.SwatchNameLabel_28 = QtWidgets.QLabel(self.EditPartFrame)
        self.SwatchNameLabel_28.setGeometry(QtCore.QRect(10, 200, 81, 16))
        self.SwatchNameLabel_28.setObjectName("SwatchNameLabel_28")

        self.retranslateUi()

    def retranslateUi(self):
        self.SwatchNameLabel_10.setText(QtWidgets.QApplication.translate("Form", "Part Name:", None, -1))
        self.label_23.setText(QtWidgets.QApplication.translate("Form", "Edit Part", None, -1))
        self.EditNameButton.setText(QtWidgets.QApplication.translate("Form", "edit", None, -1))
        self.DeletePart.setText(QtWidgets.QApplication.translate("Form", "Delete Part", None, -1))
        self.SwatchNameLabel_26.setText(QtWidgets.QApplication.translate("Form", "Change Model:", None, -1))
        self.SwatchNameLabel_27.setText(QtWidgets.QApplication.translate("Form", "Change Swatch:", None, -1))
        self.SaveButton.setText(QtWidgets.QApplication.translate("Form", "Save", None, -1))
        self.RevertModelComboBox.setText(QtWidgets.QApplication.translate("Form", "<", None, -1))
        self.RevertNameButton.setText(QtWidgets.QApplication.translate("Form", "<", None, -1))
        self.RevertSwatchComboBox.setText(QtWidgets.QApplication.translate("Form", "<", None, -1))
        self.AddPolysButton.setText(QtWidgets.QApplication.translate("Form", "+ Add Poly\'s", None, -1))
        self.SelectPolysButton.setText(QtWidgets.QApplication.translate("Form", "Select used Poly\'s ", None, -1))
        self.RemovePolysButton.setText(QtWidgets.QApplication.translate("Form", "- Remove Poly\'s", None, -1))
        self.GoToSwatchButton.setText(QtWidgets.QApplication.translate("Form", "Go to Swatch", None, -1))
        self.SwatchNameLabel_28.setText(QtWidgets.QApplication.translate("Form", "Change Color:", None, -1))


    def connectElements(self):
        # type: () -> None

        self.EditNameButton.clicked.connect(lambda: self.NameLineEdit.setEnabled(True))
        self.ChangeSwatchComboBox.currentIndexChanged.connect(self.updateSwatchComboBox)

        self.RevertNameButton.clicked.connect(lambda: self.NameLineEdit.setText(self.origionalName))
        self.RevertModelComboBox.clicked.connect(lambda: self.ChangeModelComboBox.setCurrentIndex(self.origionalModelIndex))
        self.RevertSwatchComboBox.clicked.connect(lambda: self.ChangeSwatchComboBox.setCurrentIndex(self.origionalSwatchIndex))

        self.GoToSwatchButton.clicked.connect(lambda: self.MainUI.showStateFromTree(self.selectedObject.swatch))

        self.SaveButton.clicked.connect(self.saveButton)
        self.DeletePart.clicked.connect(self.deleteButton)

        self.SelectPolysButton.clicked.connect(lambda: self.Main.app.selectFromCoordinate(self.selectedObject.swatch.coordinate, self.Main.texture.amountOfSwatchesOnRow))
        self.AddPolysButton.clicked.connect(lambda: self.Main.app.unwrapSelection(self.selectedObject.swatch.coordinate, self.Main.texture.amountOfSwatchesOnRow))
        self.RemovePolysButton.clicked.connect(lambda: self.Main.app.resetUnwrapSelection())

    def connectInputChecks(self):

        self.ChangeModelComboBox.currentIndexChanged.connect(self.inputCheckPartName)
        self.NameLineEdit.textChanged.connect(self.inputCheckPartName)

    def inputCheckPartName(self):
        if self.NameLineEdit.text() == self.selectedObject.name and self.ChangeModelComboBox.currentData() == self.selectedObject.model:
            self.MainUI.setInputValid(self.NameLineEdit)
            return

        if self.ChangeModelComboBox.currentData() is None: # fout bij init window anders
            return

        self.MainUI.checkIfPartNameEntryIsValid(self.NameLineEdit, self.ChangeModelComboBox.currentData())

    def setNewData(self, selectedObject):
        # type: (object) -> None

        self.selectedObject = selectedObject
        # self.ColorPicker.setNewData(convertToQColor(selectedObject.swatch.color))

        self.NameLineEdit.setText(selectedObject.name)

        self.updateModelComboBox(selectedObject)
        self.updateSwatchDropdown(selectedObject)

        self.ColorPickerFrame.setStyleSheet("background-color:" + convertToQColor(self.selectedObject.swatch.color).name() + ";")

        self.origionalModelIndex = self.ChangeModelComboBox.currentIndex()
        self.origionalSwatchIndex = self.ChangeSwatchComboBox.currentIndex()
        self.origionalName = selectedObject.name

        self.reset()

    def updateModelComboBox(self, selectedObject):
        # type: (object) -> None

        self.ChangeModelComboBox.clear()
        for index, item in enumerate(self.Main.models):
            self.ChangeModelComboBox.addItem(item.name)
            self.ChangeModelComboBox.setItemData(index, item)

            if item.name == selectedObject.model.name:
                self.ChangeModelComboBox.setCurrentIndex(index)

    def updateSwatchDropdown(self, selectedObject):
        # type: (object) -> None

        self.ChangeSwatchComboBox.clear()
        for index, item in enumerate(self.Main.texture.swatches):
            self.ChangeSwatchComboBox.addItem(item.name)
            self.ChangeSwatchComboBox.setItemData(index, item)

            if item.name == selectedObject.swatch.name:
                self.ChangeSwatchComboBox.setCurrentIndex(index)

    def updateSwatchComboBox(self, index):
        # type: (int) -> None

        selectedSwatch = self.ChangeSwatchComboBox.itemData(index)
        if selectedSwatch != None:
            pass
            # self.ColorPicker.setNewData(convertToQColor(selectedSwatch.color))

    def saveButton(self):
        # type: () -> None

        newModel = self.ChangeModelComboBox.itemData(self.ChangeModelComboBox.currentIndex())
        originalModel = self.ChangeModelComboBox.itemData(self.origionalModelIndex)

        self.selectedObject.name = self.NameLineEdit.text()

        if newModel != originalModel:
            newPart = self.Main.addPartToSwatch(self.selectedObject.swatch, newModel, self.selectedObject.name)
            self.Main.deletePart(self.selectedObject.swatch, self.selectedObject)
            self.setNewData(newPart)

        self.MainUI.applyChanges()
        self.reset()

    def reset(self):
        # type: () -> None

        self.NameLineEdit.setEnabled(False)

    def deleteButton(self):
        # type: () -> None

        self.Main.deletePart(self.selectedObject.swatch, self.selectedObject)
        self.MainUI.applyChanges()
        self.reset()
        self.MainUI.hideAllStates()
