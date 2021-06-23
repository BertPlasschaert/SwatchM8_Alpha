from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from swatchM8.core.util.Helpers import convertToQColor

from swatchM8.ui.qt.widgets.ColorPickerWidget import ColorPickerWidget

from PySide2 import QtCore, QtGui, QtWidgets


class AddPartWidget(QWidget):

    def __init__(self, MainUI, Main):
        # type: (object, object) -> None

        super(AddPartWidget, self).__init__(None)  # Calls the init of the super class -> QWidget

        self.setupUi()
        self.connectElements()
        self.connectInputChecks()
        self.MainUI = MainUI
        self.Main = Main

        layout = QHBoxLayout()
        layout.setMargin(0)
        layout.addWidget(self.AddPartFrame)
        self.setLayout(layout)

        self.ColorPicker = ColorPickerWidget()
        self.ColorPickerPlaceHolder.setLayout(self.ColorPicker)

        self.ModelComboBox.setCurrentIndex(0)

        self.MainUI.setInputInvalid(self.ModelNameLineEdit)
        self.MainUI.setInputInvalid(self.PartNameLineEdit)

        self.UniqueSwatchRadioButton.setChecked(True)
        self.setUniqueSwatchSetup()

    def setupUi(self):
        self.AddPartFrame = QtWidgets.QFrame()
        self.AddPartFrame.setGeometry(QtCore.QRect(0, 0, 311, 261))
        self.AddPartFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.AddPartFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.AddPartFrame.setObjectName("AddPartFrame")
        self.AddPartLabel = QtWidgets.QLabel(self.AddPartFrame)
        self.AddPartLabel.setGeometry(QtCore.QRect(10, 10, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.AddPartLabel.setFont(font)
        self.AddPartLabel.setObjectName("AddPartLabel")
        self.CreateButton = QtWidgets.QPushButton(self.AddPartFrame)
        self.CreateButton.setGeometry(QtCore.QRect(200, 180, 81, 71))
        self.CreateButton.setObjectName("CreateButton")
        self.ColorPickerPlaceHolder = QtWidgets.QFrame(self.AddPartFrame)
        self.ColorPickerPlaceHolder.setGeometry(QtCore.QRect(10, 170, 181, 81))
        self.ColorPickerPlaceHolder.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.ColorPickerPlaceHolder.setFrameShadow(QtWidgets.QFrame.Raised)
        self.ColorPickerPlaceHolder.setObjectName("ColorPickerPlaceHolder")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.AddPartFrame)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(10, 40, 271, 31))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.ModelLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.ModelLayout.setContentsMargins(-1, 2, -1, 2)
        self.ModelLayout.setObjectName("ModelLayout")
        self.ModelLabel = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.ModelLabel.setObjectName("ModelLabel")
        self.ModelLayout.addWidget(self.ModelLabel)
        self.ModelStackedWidget = QtWidgets.QStackedWidget(self.horizontalLayoutWidget_2)
        self.ModelStackedWidget.setToolTipDuration(0)
        self.ModelStackedWidget.setObjectName("ModelStackedWidget")
        self.page_5 = QtWidgets.QWidget()
        self.page_5.setObjectName("page_5")
        self.ModelComboBox = QtWidgets.QComboBox(self.page_5)
        self.ModelComboBox.setGeometry(QtCore.QRect(18, 3, 141, 21))
        self.ModelComboBox.setObjectName("ModelComboBox")
        self.NewModelButton = QtWidgets.QPushButton(self.page_5)
        self.NewModelButton.setGeometry(QtCore.QRect(160, 2, 51, 23))
        self.NewModelButton.setObjectName("NewModelButton")
        self.ModelStackedWidget.addWidget(self.page_5)
        self.page_6 = QtWidgets.QWidget()
        self.page_6.setObjectName("page_6")
        self.ModelNameLineEdit = QtWidgets.QLineEdit(self.page_6)
        self.ModelNameLineEdit.setGeometry(QtCore.QRect(20, 3, 141, 21))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ModelNameLineEdit.sizePolicy().hasHeightForWidth())
        self.ModelNameLineEdit.setSizePolicy(sizePolicy)
        self.ModelNameLineEdit.setMaximumSize(QtCore.QSize(240, 16777215))
        self.ModelNameLineEdit.setReadOnly(False)
        self.ModelNameLineEdit.setObjectName("ModelNameLineEdit")
        self.ExistingModelButton = QtWidgets.QPushButton(self.page_6)
        self.ExistingModelButton.setGeometry(QtCore.QRect(160, 2, 61, 23))
        self.ExistingModelButton.setObjectName("ExistingModelButton")
        self.ModelStackedWidget.addWidget(self.page_6)
        self.ModelLayout.addWidget(self.ModelStackedWidget)
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.AddPartFrame)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(10, 80, 271, 23))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.PartLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.PartLayout.setContentsMargins(-1, 2, 2, 2)
        self.PartLayout.setObjectName("PartLayout")
        self.PartNameLabel = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.PartNameLabel.setObjectName("PartNameLabel")
        self.PartLayout.addWidget(self.PartNameLabel)
        self.PartNameLineEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PartNameLineEdit.sizePolicy().hasHeightForWidth())
        self.PartNameLineEdit.setSizePolicy(sizePolicy)
        self.PartNameLineEdit.setMaximumSize(QtCore.QSize(240, 16777215))
        self.PartNameLineEdit.setReadOnly(False)
        self.PartNameLineEdit.setObjectName("PartNameLineEdit")
        self.PartLayout.addWidget(self.PartNameLineEdit)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.AddPartFrame)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 140, 271, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.NameLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.NameLayout.setContentsMargins(-1, 2, -1, 2)
        self.NameLayout.setObjectName("NameLayout")
        self.SwatchLabel = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.SwatchLabel.setObjectName("SwatchLabel")
        self.NameLayout.addWidget(self.SwatchLabel)
        self.SwatchStackedWidget = QtWidgets.QStackedWidget(self.horizontalLayoutWidget)
        self.SwatchStackedWidget.setObjectName("SwatchStackedWidget")
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.SwatchComboBox = QtWidgets.QComboBox(self.page_3)
        self.SwatchComboBox.setGeometry(QtCore.QRect(0, 3, 171, 21))
        self.SwatchComboBox.setObjectName("SwatchComboBox")
        self.NewSwatchButton = QtWidgets.QPushButton(self.page_3)
        self.NewSwatchButton.setGeometry(QtCore.QRect(171, 2, 51, 23))
        self.NewSwatchButton.setObjectName("NewSwatchButton")
        self.SwatchStackedWidget.addWidget(self.page_3)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.SwatchNameLineEdit = QtWidgets.QLineEdit(self.page_4)
        self.SwatchNameLineEdit.setGeometry(QtCore.QRect(0, 3, 161, 21))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SwatchNameLineEdit.sizePolicy().hasHeightForWidth())
        self.SwatchNameLineEdit.setSizePolicy(sizePolicy)
        self.SwatchNameLineEdit.setMaximumSize(QtCore.QSize(240, 16777215))
        self.SwatchNameLineEdit.setReadOnly(False)
        self.SwatchNameLineEdit.setObjectName("SwatchNameLineEdit")
        self.ExistingSwatchButton = QtWidgets.QPushButton(self.page_4)
        self.ExistingSwatchButton.setGeometry(QtCore.QRect(162, 2, 51, 23))
        self.ExistingSwatchButton.setObjectName("ExistingSwatchButton")
        self.SwatchStackedWidget.addWidget(self.page_4)
        self.NameLayout.addWidget(self.SwatchStackedWidget)
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(self.AddPartFrame)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(10, 120, 211, 21))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.RadioButtonLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.RadioButtonLayout.setContentsMargins(0, 0, 0, 0)
        self.RadioButtonLayout.setObjectName("RadioButtonLayout")
        self.UniqueSwatchRadioButton = QtWidgets.QRadioButton(self.horizontalLayoutWidget_4)
        self.UniqueSwatchRadioButton.setObjectName("UniqueSwatchRadioButton")
        self.RadioButtonLayout.addWidget(self.UniqueSwatchRadioButton)
        self.SharedSwatchRadioButton = QtWidgets.QRadioButton(self.horizontalLayoutWidget_4)
        self.SharedSwatchRadioButton.setObjectName("SharedSwatchRadioButton")
        self.RadioButtonLayout.addWidget(self.SharedSwatchRadioButton)
        self.line = QtWidgets.QFrame(self.AddPartFrame)
        self.line.setGeometry(QtCore.QRect(10, 108, 271, 8))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")

        self.retranslateUi()
        self.ModelStackedWidget.setCurrentIndex(0)
        self.SwatchStackedWidget.setCurrentIndex(0)

    def retranslateUi(self):
        self.AddPartLabel.setText(QtWidgets.QApplication.translate("FormName", "Add Part", None, -1))
        self.CreateButton.setText(QtWidgets.QApplication.translate("FormName", "Create", None, -1))
        self.ModelLabel.setText(QtWidgets.QApplication.translate("FormName", "Model:", None, -1))
        self.NewModelButton.setText(QtWidgets.QApplication.translate("FormName", "New", None, -1))
        self.ExistingModelButton.setText(QtWidgets.QApplication.translate("FormName", "Pick", None, -1))
        self.PartNameLabel.setText(QtWidgets.QApplication.translate("FormName", "PartName:", None, -1))
        self.SwatchLabel.setText(QtWidgets.QApplication.translate("FormName", "Swatch:", None, -1))
        self.NewSwatchButton.setText(QtWidgets.QApplication.translate("FormName", "New", None, -1))
        self.ExistingSwatchButton.setText(QtWidgets.QApplication.translate("FormName", "Pick", None, -1))
        self.UniqueSwatchRadioButton.setText(QtWidgets.QApplication.translate("FormName", "Unique Swatch", None, -1))
        self.SharedSwatchRadioButton.setText(QtWidgets.QApplication.translate("FormName", "Shared Swatch", None, -1))

    def connectElements(self):
        # type: () -> None

        self.NewSwatchButton.clicked.connect(self.newSwatchButton)
        self.NewModelButton.clicked.connect(self.newModelButton)
        self.ExistingSwatchButton.clicked.connect(self.existingSwatchButton)
        self.ExistingModelButton.clicked.connect(self.existingModelButton)

        self.SwatchComboBox.currentIndexChanged.connect(self.updateSwatch)

        self.CreateButton.clicked.connect(self.addButton)
        self.UniqueSwatchRadioButton.toggled.connect(self.setUniqueSwatchSetup)
        self.SharedSwatchRadioButton.toggled.connect(self.setSharedSwatchSetup)

        self.ModelComboBox.currentIndexChanged.connect(self.generateUniqueSwatchName)
        self.ModelNameLineEdit.textEdited.connect(self.generateUniqueSwatchName)
        self.PartNameLineEdit.textEdited.connect(self.generateUniqueSwatchName)

    def connectInputChecks(self):

        self.ModelComboBox.currentIndexChanged.connect(lambda: self.MainUI.checkIfPartNameEntryIsValid(self.PartNameLineEdit, self.ModelComboBox.currentData()))
        self.ModelNameLineEdit.textChanged.connect(lambda: self.MainUI.checkIfModelNameEntryIsValid(self.ModelNameLineEdit))
        self.PartNameLineEdit.textChanged.connect(self.inputCheckPartName)
        self.SwatchNameLineEdit.textChanged.connect(self.inputCheckSwatchName)

    def inputCheckPartName(self):

        if self.PartNameLineEdit.text() == "":
            self.MainUI.setInputInvalid(self.PartNameLineEdit)
            return

        if self.ModelStackedWidget.currentIndex() == 1:  # If new Model aka no parts yet
            self.MainUI.setInputValid(self.PartNameLineEdit)
            return

        self.MainUI.checkIfPartNameEntryIsValid(self.PartNameLineEdit, self.ModelComboBox.currentData())

    def inputCheckSwatchName(self):

        if self.SwatchStackedWidget.currentIndex() == 0:  # als er een gepicked word, geen check
            return

        if self.SwatchNameLineEdit.text() == "" and self.SharedSwatchRadioButton.isChecked():  # Leeg en customName, sws niet valid
            self.MainUI.setInputInvalid(self.SwatchNameLineEdit)
            return

        if self.Main.texture == None:  # Bij init code geeft hij anders een Attribute error
            return
        self.MainUI.checkifSwatchNameIsValid(self.SwatchNameLineEdit)

    def setNewData(self):
        # type: () -> None

        self.updateModelDropdown()

        if self.ModelComboBox.count() == 0:
            self.newModelButton()

        self.updateSwatchDropdown()

        self.ColorPicker.setNewData(QColor('white'))

        # self.updateSwatch(self.SwatchComboBox.currentIndex())

    def updateSwatchDropdown(self):
        # type: () -> None

        self.SwatchComboBox.clear()
        for index, item in enumerate(self.Main.texture.swatches):
            self.SwatchComboBox.addItem(item.name)
            self.SwatchComboBox.setItemData(index, item)

    def updateModelDropdown(self):
        # type: () -> None

        self.ModelComboBox.clear()
        for index, item in enumerate(self.Main.models):
            self.ModelComboBox.addItem(item.name)
            self.ModelComboBox.setItemData(index, item)

    def updateSwatch(self, index):
        # type: (int) -> None

        selectedSwatch = self.SwatchComboBox.itemData(index)
        if selectedSwatch != None:
            self.ColorPicker.setNewData(convertToQColor(selectedSwatch.color))
            # self.ColorPicker.setNewData(QColor('white'))

    def newSwatchButton(self):
        # type: () -> None

        self.SwatchStackedWidget.setCurrentIndex(1)
        self.ColorPicker.setNewData(QColor('white'))
        self.ColorPickerPlaceHolder.setEnabled(True)

    def newModelButton(self):
        # type: () -> None

        self.ModelStackedWidget.setCurrentIndex(1)

    def setUniqueSwatchSetup(self):
        # type: () -> None

        self.SwatchStackedWidget.setCurrentIndex(1)
        self.ExistingSwatchButton.setEnabled(0)
        self.SwatchNameLineEdit.setEnabled(0)
        self.ColorPickerPlaceHolder.setEnabled(True)
        self.ColorPicker.setNewData(QColor('white'))
        self.generateUniqueSwatchName()

    def setSharedSwatchSetup(self):
        # type: () -> None

        self.ExistingSwatchButton.setEnabled(1)
        self.SwatchNameLineEdit.setEnabled(1)
        self.SwatchNameLineEdit.setText('')

    def generateUniqueSwatchName(self):
        # type: () -> None

        if self.UniqueSwatchRadioButton.isChecked():

            if self.ModelStackedWidget.currentIndex() == 0:

                modelName = self.ModelComboBox.currentText()

            else:
                modelName = self.ModelNameLineEdit.text()

            partName = self.PartNameLineEdit.text()

            if partName == '':
                partName = 'PartName'

            if modelName == '':
                modelName = 'ModelName'

            self.SwatchNameLineEdit.setText(modelName + "-" + partName)

    def existingSwatchButton(self):
        # type: () -> None

        self.updateSwatch(self.SwatchComboBox.currentIndex())
        self.SwatchStackedWidget.setCurrentIndex(0)
        self.ColorPickerPlaceHolder.setEnabled(False)

    def existingModelButton(self):
        # type: () -> None

        self.ModelStackedWidget.setCurrentIndex(0)

    def addButton(self):
        # type: () -> None

        color = self.ColorPicker.getPickedColor()

        if self.ModelStackedWidget.currentIndex() == 0:
            model = self.ModelComboBox.currentData()
        else:
            model = self.Main.createModel(self.ModelNameLineEdit.text())

        if self.SwatchStackedWidget.currentIndex() == 0:
            swatch = self.SwatchComboBox.itemData(self.SwatchComboBox.currentIndex())
        else:
            swatch = self.Main.texture.createSwatch(self.SwatchNameLineEdit.text(), color)

        # TODO: model verwijderen als het fout loopt bij de swatch

        self.Main.addPartToSwatch(swatch, model, self.PartNameLineEdit.text())
        self.Main.app.unwrapSelection(swatch.coordinate, self.Main.texture.amountOfSwatchesOnRow)

        self.MainUI.applyChanges()
        self.reset()

    def reset(self):
        # type: () -> None

        self.SwatchNameLineEdit.setText('')
        self.ModelNameLineEdit.setText('')
        self.PartNameLineEdit.setText('')
        self.ModelStackedWidget.setCurrentIndex(0)

        self.setNewData()

    def setComboBoxModel(self, model):
        # if the add part button is pressed trought the edit model frame, the correct model will be set

        index = self.ModelComboBox.findData(model)
        self.ModelComboBox.setCurrentIndex(index)
