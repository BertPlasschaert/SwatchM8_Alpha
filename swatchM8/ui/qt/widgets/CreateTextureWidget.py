from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from swatchM8.ui.qt.WindowStates import PopupFrameStates
from PySide2 import QtCore, QtGui, QtWidgets


class CreateTextureWidget(QWidget):

    def __init__(self, mainUI, main):
        # type: (object, object) -> None

        super(CreateTextureWidget, self).__init__(None)  # Calls the init of the super class -> QWidget

        self.setupUi()
        self.connectElements()
        self.connectInputChecks()
        self.MainUI = mainUI
        self.Main = main

        layout = QHBoxLayout()
        layout.setMargin(0)
        layout.addWidget(self.CreateTextureFrame)
        self.setLayout(layout)

        self.MainUI.setInputInvalid(self.NameLineEdit)
        self.MainUI.setInputInvalid(self.SizeLineEdit)
        self.MainUI.setInputInvalid(self.AmountOnRowLineEdit)
        self.MainUI.setInputInvalid(self.SaveLocationLineEdit)

    def setupUi(self):
        self.CreateTextureFrame = QtWidgets.QFrame()
        self.CreateTextureFrame.setGeometry(QtCore.QRect(0, 0, 561, 331))
        self.CreateTextureFrame.setAutoFillBackground(True)
        self.CreateTextureFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.CreateTextureFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.CreateTextureFrame.setObjectName("CreateTextureFrame")
        self.label_28 = QtWidgets.QLabel(self.CreateTextureFrame)
        self.label_28.setGeometry(QtCore.QRect(20, 10, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_28.setFont(font)
        self.label_28.setObjectName("label_28")
        self.CreateButton = QtWidgets.QPushButton(self.CreateTextureFrame)
        self.CreateButton.setGeometry(QtCore.QRect(450, 290, 91, 23))
        self.CreateButton.setObjectName("CreateButton")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.CreateTextureFrame)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(100, 100, 331, 22))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.NameLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.NameLayout.setContentsMargins(0, 0, 0, 0)
        self.NameLayout.setObjectName("NameLayout")
        self.TextureNameLabel = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.TextureNameLabel.setObjectName("TextureNameLabel")
        self.NameLayout.addWidget(self.TextureNameLabel)
        self.NameLineEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.NameLineEdit.setText("")
        self.NameLineEdit.setObjectName("NameLineEdit")
        self.NameLayout.addWidget(self.NameLineEdit)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.CreateTextureFrame)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(110, 130, 205, 22))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.SizeLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.SizeLayout.setContentsMargins(0, 0, 0, 0)
        self.SizeLayout.setObjectName("SizeLayout")
        self.TextureSizeLabel = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TextureSizeLabel.sizePolicy().hasHeightForWidth())
        self.TextureSizeLabel.setSizePolicy(sizePolicy)
        self.TextureSizeLabel.setObjectName("TextureSizeLabel")
        self.SizeLayout.addWidget(self.TextureSizeLabel)
        self.SizeLineEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.SizeLineEdit.setText("")
        self.SizeLineEdit.setObjectName("SizeLineEdit")
        self.SizeLayout.addWidget(self.SizeLineEdit)
        self.TextureSizePixelLabel_4 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.TextureSizePixelLabel_4.setObjectName("TextureSizePixelLabel_4")
        self.SizeLayout.addWidget(self.TextureSizePixelLabel_4)
        self.Size2LineEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.Size2LineEdit.setEnabled(False)
        self.Size2LineEdit.setText("")
        self.Size2LineEdit.setObjectName("Size2LineEdit")
        self.SizeLayout.addWidget(self.Size2LineEdit)
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.CreateTextureFrame)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(90, 160, 146, 22))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.AmountOnRowLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.AmountOnRowLayout.setContentsMargins(0, 0, 0, 0)
        self.AmountOnRowLayout.setObjectName("AmountOnRowLayout")
        self.AmountOnRowLabel = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.AmountOnRowLabel.sizePolicy().hasHeightForWidth())
        self.AmountOnRowLabel.setSizePolicy(sizePolicy)
        self.AmountOnRowLabel.setObjectName("AmountOnRowLabel")
        self.AmountOnRowLayout.addWidget(self.AmountOnRowLabel)
        self.AmountOnRowLineEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget_3)
        self.AmountOnRowLineEdit.setText("")
        self.AmountOnRowLineEdit.setObjectName("AmountOnRowLineEdit")
        self.AmountOnRowLayout.addWidget(self.AmountOnRowLineEdit)
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(self.CreateTextureFrame)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(100, 190, 421, 25))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.SaveLayout = QtWidgets.QLabel(self.horizontalLayoutWidget_4)
        self.SaveLayout.setObjectName("SaveLayout")
        self.horizontalLayout_4.addWidget(self.SaveLayout)
        self.SaveLocationLineEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget_4)
        self.SaveLocationLineEdit.setText("")
        self.SaveLocationLineEdit.setObjectName("SaveLocationLineEdit")
        self.horizontalLayout_4.addWidget(self.SaveLocationLineEdit)
        self.BrowseButton = QtWidgets.QPushButton(self.horizontalLayoutWidget_4)
        self.BrowseButton.setObjectName("BrowseButton")
        self.horizontalLayout_4.addWidget(self.BrowseButton)
        self.BackButton = QtWidgets.QPushButton(self.CreateTextureFrame)
        self.BackButton.setGeometry(QtCore.QRect(20, 290, 91, 23))
        self.BackButton.setObjectName("BackButton")

        self.retranslateUi()

    def retranslateUi(self):
        self.label_28.setText(QtWidgets.QApplication.translate("Form", "Create a new Texture", None, -1))
        self.CreateButton.setText(QtWidgets.QApplication.translate("Form", "Create Texture", None, -1))
        self.TextureNameLabel.setText(QtWidgets.QApplication.translate("Form", "Texture Name:", None, -1))
        self.TextureSizeLabel.setText(QtWidgets.QApplication.translate("Form", "Texure Size:", None, -1))
        self.TextureSizePixelLabel_4.setText(QtWidgets.QApplication.translate("Form", "X ", None, -1))
        self.AmountOnRowLabel.setText(QtWidgets.QApplication.translate("Form", "Amount on Row:", None, -1))
        self.SaveLayout.setText(QtWidgets.QApplication.translate("Form", "Save Location:", None, -1))
        self.BrowseButton.setText(QtWidgets.QApplication.translate("Form", "Browse", None, -1))
        self.BackButton.setText(QtWidgets.QApplication.translate("Form", "Back", None, -1))

    def connectElements(self):
        # type: () -> None

        self.CreateButton.pressed.connect(self.createButton)
        self.BrowseButton.pressed.connect(self.browseButton)
        self.SizeLineEdit.textChanged.connect(lambda: self.Size2LineEdit.setText(self.SizeLineEdit.text()))
        self.BackButton.pressed.connect(lambda: self.MainUI.ui.PopUpFrame.setCurrentIndex(PopupFrameStates.loadOrCreateTexture.value))

    def connectInputChecks(self):
        self.NameLineEdit.textChanged.connect(lambda: self.MainUI.checkifFieldIsEmpty(self.NameLineEdit))
        self.SizeLineEdit.textChanged.connect(self.inputCheckSize)
        self.AmountOnRowLineEdit.textChanged.connect(self.inputCheckSize)
        self.SaveLocationLineEdit.textChanged.connect(lambda: self.MainUI.checkifFieldIsEmpty(self.SaveLocationLineEdit))

    def inputCheckSize(self):

        self.MainUI.checkifFieldIsEmpty(self.SizeLineEdit)
        self.MainUI.checkifFieldIsEmpty(self.AmountOnRowLineEdit)

        if self.SizeLineEdit.text().isdigit() == False:
            self.MainUI.setInputInvalid(self.SizeLineEdit)
            return

        if self.AmountOnRowLineEdit.text().isdigit() == False:
            self.MainUI.setInputInvalid(self.AmountOnRowLineEdit)
            return

        if int(self.SizeLineEdit.text()) % int(self.AmountOnRowLineEdit.text()) != 0:
            self.MainUI.setInputInvalid(self.AmountOnRowLineEdit)
            return

        self.MainUI.setInputValid(self.SizeLineEdit)
        self.MainUI.setInputValid(self.AmountOnRowLineEdit)

    def browseButton(self):
        # type: () -> None

        # dialog = QFileDialog(self, "select a save folder", r"D:\OneDrive - BUas\MGT\Scripts\SwatchM8\testFiles", "folder")
        dialog = QFileDialog(self, "select a save folder", "folder")
        path = dialog.getExistingDirectory()

        self.SaveLocationLineEdit.setText(path)

    def createButton(self):
        # type: () -> None

        self.Main.createTexture(self.NameLineEdit.text(), self.SaveLocationLineEdit.text(), int(self.SizeLineEdit.text()), int(self.AmountOnRowLineEdit.text()))
        self.Main.saveData()

        self.MainUI.loadData()
