from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2 import QtCore, QtGui, QtWidgets


from swatchM8.ui.qt.widgets.ColorPickerWidget import ColorPickerWidget


class AddSwatchWidget(QWidget):

    def __init__(self, MainUI, Main):
        # type: (object, object) -> None

        super(AddSwatchWidget, self).__init__(None)  # Calls the init of the super class -> QWidget

        self.setupUi()
        self.connectElements()
        self.MainUI = MainUI
        self.Main = Main

        layout = QHBoxLayout()
        layout.setMargin(0)
        layout.addWidget(self.AddSwatchFrame)
        self.setLayout(layout)

        self.ColorPicker = ColorPickerWidget()
        self.ColorPickerPlaceHolder.setLayout(self.ColorPicker)

        self.MainUI.setInputInvalid(self.NameLineEdit)

    def setupUi(self):
        self.AddSwatchFrame = QtWidgets.QFrame()
        self.AddSwatchFrame.setGeometry(QtCore.QRect(0, 0, 311, 241))
        self.AddSwatchFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.AddSwatchFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.AddSwatchFrame.setObjectName("AddSwatchFrame")
        self.label_26 = QtWidgets.QLabel(self.AddSwatchFrame)
        self.label_26.setGeometry(QtCore.QRect(10, 10, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_26.setFont(font)
        self.label_26.setObjectName("label_26")
        self.SwatchNameLabel_20 = QtWidgets.QLabel(self.AddSwatchFrame)
        self.SwatchNameLabel_20.setGeometry(QtCore.QRect(10, 40, 41, 16))
        self.SwatchNameLabel_20.setObjectName("SwatchNameLabel_20")
        self.CreateButton = QtWidgets.QPushButton(self.AddSwatchFrame)
        self.CreateButton.setGeometry(QtCore.QRect(200, 150, 51, 81))
        self.CreateButton.setObjectName("CreateButton")
        self.NameLineEdit = QtWidgets.QLineEdit(self.AddSwatchFrame)
        self.NameLineEdit.setGeometry(QtCore.QRect(50, 40, 161, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.NameLineEdit.sizePolicy().hasHeightForWidth())
        self.NameLineEdit.setSizePolicy(sizePolicy)
        self.NameLineEdit.setMaximumSize(QtCore.QSize(240, 16777215))
        self.NameLineEdit.setReadOnly(False)
        self.NameLineEdit.setObjectName("NameLineEdit")
        self.checkBox = QtWidgets.QCheckBox(self.AddSwatchFrame)
        self.checkBox.setEnabled(False)
        self.checkBox.setGeometry(QtCore.QRect(10, 70, 101, 17))
        self.checkBox.setObjectName("checkBox")
        self.PickLocationButton = QtWidgets.QPushButton(self.AddSwatchFrame)
        self.PickLocationButton.setEnabled(False)
        self.PickLocationButton.setGeometry(QtCore.QRect(110, 70, 31, 21))
        self.PickLocationButton.setObjectName("PickLocationButton")
        self.ColorPickerPlaceHolder = QtWidgets.QFrame(self.AddSwatchFrame)
        self.ColorPickerPlaceHolder.setGeometry(QtCore.QRect(10, 150, 181, 81))
        self.ColorPickerPlaceHolder.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.ColorPickerPlaceHolder.setFrameShadow(QtWidgets.QFrame.Raised)
        self.ColorPickerPlaceHolder.setObjectName("ColorPickerPlaceHolder")

        self.retranslateUi()

    def retranslateUi(self):
        self.label_26.setText(QtWidgets.QApplication.translate("Form", "Add Swatch", None, -1))
        self.SwatchNameLabel_20.setText(QtWidgets.QApplication.translate("Form", "Name:", None, -1))
        self.CreateButton.setText(QtWidgets.QApplication.translate("Form", "Create", None, -1))
        self.checkBox.setText(QtWidgets.QApplication.translate("Form", "Custom Location", None, -1))
        self.PickLocationButton.setText(QtWidgets.QApplication.translate("Form", "Pick", None, -1))

    def connectElements(self):
        # type: () -> None

        self.CreateButton.clicked.connect(self.createButton)

        self.NameLineEdit.textChanged.connect(lambda: self.MainUI.checkifSwatchNameIsValid(self.NameLineEdit))

    def setNewData(self):
        # type: () -> None

        self.ColorPicker.setNewData(QColor('white'))

    def createButton(self):
        # type: () -> None

        swatchName = self.NameLineEdit.text()  # TODO: check if name is empty
        self.Main.texture.createSwatch(swatchName, self.ColorPicker.getPickedColor())

        self.MainUI.applyChanges()

        self.reset()

    def reset(self):
        # type: () -> None

        self.NameLineEdit.setText('')
        self.ColorPicker.setNewData(QColor('white'))
