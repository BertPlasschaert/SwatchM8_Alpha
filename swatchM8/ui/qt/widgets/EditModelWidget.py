from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2 import QtCore, QtGui, QtWidgets

from swatchM8.ui.qt.WindowStates import RightFrameStates


class EditModelWidget(QWidget):

    def __init__(self, MainUI, Main):
        # type: (object, object) -> None

        super(EditModelWidget, self).__init__(None)  # Calls the init of the super class -> QWidget

        self.setupUi()
        self.MainUI = MainUI
        self.Main = Main
        self.connectElements()


        layout = QHBoxLayout()
        layout.setMargin(0)
        layout.addWidget(self.EditModelFrame)
        self.setLayout(layout)

    def setupUi(self):
        self.EditModelFrame = QtWidgets.QFrame()
        self.EditModelFrame.setGeometry(QtCore.QRect(0, 0, 311, 271))
        self.EditModelFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.EditModelFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.EditModelFrame.setObjectName("EditModelFrame")
        self.label_21 = QtWidgets.QLabel(self.EditModelFrame)
        self.label_21.setGeometry(QtCore.QRect(10, 10, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_21.setFont(font)
        self.label_21.setObjectName("label_21")
        self.EditNameButton = QtWidgets.QPushButton(self.EditModelFrame)
        self.EditNameButton.setGeometry(QtCore.QRect(230, 40, 31, 23))
        self.EditNameButton.setObjectName("EditNameButton")
        self.DeleteButton = QtWidgets.QPushButton(self.EditModelFrame)
        self.DeleteButton.setGeometry(QtCore.QRect(220, 10, 81, 23))
        self.DeleteButton.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.DeleteButton.setObjectName("DeleteButton")
        self.NameLineEdit = QtWidgets.QLineEdit(self.EditModelFrame)
        self.NameLineEdit.setEnabled(False)
        self.NameLineEdit.setGeometry(QtCore.QRect(80, 40, 151, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.NameLineEdit.sizePolicy().hasHeightForWidth())
        self.NameLineEdit.setSizePolicy(sizePolicy)
        self.NameLineEdit.setMaximumSize(QtCore.QSize(240, 16777215))
        self.NameLineEdit.setReadOnly(False)
        self.NameLineEdit.setObjectName("NameLineEdit")
        self.ModelTreeView = QtWidgets.QTreeWidget(self.EditModelFrame)
        self.ModelTreeView.setGeometry(QtCore.QRect(10, 70, 291, 161))
        self.ModelTreeView.setStyleSheet("width:100%;")
        self.ModelTreeView.setObjectName("ModelTreeView")
        self.ModelTreeView.headerItem().setText(0, "Name")
        self.ModelNameLabel = QtWidgets.QLabel(self.EditModelFrame)
        self.ModelNameLabel.setGeometry(QtCore.QRect(10, 40, 61, 16))
        self.ModelNameLabel.setObjectName("ModelNameLabel")
        self.SaveButton = QtWidgets.QPushButton(self.EditModelFrame)
        self.SaveButton.setGeometry(QtCore.QRect(230, 240, 75, 23))
        self.SaveButton.setObjectName("SaveButton")
        self.RevertNameButton = QtWidgets.QPushButton(self.EditModelFrame)
        self.RevertNameButton.setGeometry(QtCore.QRect(262, 40, 21, 23))
        self.RevertNameButton.setObjectName("RevertNameButton")
        self.AddPartButton = QtWidgets.QPushButton(self.EditModelFrame)
        self.AddPartButton.setGeometry(QtCore.QRect(10, 240, 71, 23))
        self.AddPartButton.setObjectName("AddPartButton")

        self.retranslateUi()

    def retranslateUi(self):
        self.label_21.setText(QtWidgets.QApplication.translate("Form", "Edit Model", None, -1))
        self.EditNameButton.setText(QtWidgets.QApplication.translate("Form", "[edit]", None, -1))
        self.DeleteButton.setText(QtWidgets.QApplication.translate("Form", "Delete Model", None, -1))
        self.ModelTreeView.headerItem().setText(1, QtWidgets.QApplication.translate("Form", "Swatch", None, -1))
        self.ModelNameLabel.setText(QtWidgets.QApplication.translate("Form", "Model Name:", None, -1))
        self.SaveButton.setText(QtWidgets.QApplication.translate("Form", "Save", None, -1))
        self.RevertNameButton.setText(QtWidgets.QApplication.translate("Form", "<", None, -1))
        self.AddPartButton.setText(QtWidgets.QApplication.translate("Form", "Add Part", None, -1))

    def connectElements(self):
        # type: () -> None

        self.EditNameButton.clicked.connect(lambda: self.NameLineEdit.setEnabled(True))
        self.RevertNameButton.clicked.connect(self.revertNameButton)
        self.SaveButton.clicked.connect(self.saveButton)
        self.DeleteButton.clicked.connect(self.deleteButton)
        self.AddPartButton.clicked.connect(self.addPartButton)

        self.NameLineEdit.textChanged.connect(self.inputCheckModelName)

    def inputCheckModelName(self):
        if self.NameLineEdit.text() == self.selectedObject.name:
            self.MainUI.setInputValid(self.NameLineEdit)
            return

        self.MainUI.checkIfModelNameEntryIsValid(self.NameLineEdit)

    def setNewData(self, selectedObject):
        # type: (object) -> None

        self.selectedObject = selectedObject
        self.NameLineEdit.setText(selectedObject.name)
        self.populateTree(selectedObject)
        self.reset()

    def populateTree(self, selectedObject):
        # type: (object) -> None

        self.ModelTreeView.clear()

        for i in selectedObject.parts:
            Entry = QTreeWidgetItem(self.ModelTreeView)
            Entry.setText(0, i.name)
            Entry.setData(3, 0, i)

            Entry.setText(1, i.swatch.name)
            Entry.setData(4, 0, i.swatch)

    def revertNameButton(self):
        # type: () -> None

        self.NameLineEdit.setText(self.selectedObject.name)
        self.NameLineEdit.setEnabled(False)

    def addPartButton(self):

        self.MainUI.ui.RightFrame.setCurrentIndex(RightFrameStates.addPart.value)
        self.MainUI.addPartFrame.setNewData()
        self.MainUI.addPartFrame.setComboBoxModel(self.selectedObject)

    def saveButton(self):
        # type: () -> None

        self.selectedObject.name = self.NameLineEdit.text()
        self.MainUI.applyChanges()
        self.reset()

    def reset(self):
        # type: () -> None

        self.NameLineEdit.setEnabled(False)

    def deleteButton(self):
        # type: () -> None

        self.Main.deleteModel(self.selectedObject)
        self.MainUI.applyChanges()
        self.reset()
        self.MainUI.hideAllStates()
