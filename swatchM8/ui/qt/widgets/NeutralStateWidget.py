from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2 import QtCore, QtGui, QtWidgets


class NeutralStateWidget(QWidget):

    def __init__(self):
        # type: () -> None

        super(NeutralStateWidget, self).__init__(None)  # Calls the init of the super class -> QWidget
        self.setupUi()

        layout = QHBoxLayout()
        layout.setMargin(0)
        layout.addWidget(self.NeutralFrame)
        self.setLayout(layout)

    def setupUi(self):
        self.NeutralFrame = QtWidgets.QFrame()
        self.NeutralFrame.setGeometry(QtCore.QRect(0, 0, 311, 241))
        self.NeutralFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.NeutralFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.NeutralFrame.setObjectName("NeutralFrame")
        self.SwatchNameLabel_32 = QtWidgets.QLabel(self.NeutralFrame)
        self.SwatchNameLabel_32.setGeometry(QtCore.QRect(50, 70, 240, 111))
        self.SwatchNameLabel_32.setAlignment(QtCore.Qt.AlignCenter)
        self.SwatchNameLabel_32.setObjectName("SwatchNameLabel_32")

        self.retranslateUi()

    def retranslateUi(self):
        self.SwatchNameLabel_32.setText(QtWidgets.QApplication.translate("Form", "Press a Part, Model or Swatch to edit", None, -1))


