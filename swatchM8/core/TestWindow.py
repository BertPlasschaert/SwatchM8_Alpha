from PySide2 import QtUiTools
from PySide2 import QtWidgets
from PySide2 import QtCore
from PySide2 import QtGui

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import maya.OpenMayaUI as omui
import shiboken2


def get_main_window():
    try:
        mayaMainWindowPtr = omui.MQtUtil.mainWindow()
        mayaMainWindow = shiboken2.wrapInstance(long(mayaMainWindowPtr), QWidget)
    except:
        mayaMainWindow = None
    return mayaMainWindow


class SplashScreenCompiled(QMainWindow):

    def __init__(self, parent=None):
        # type: (object, object) -> None

        # QtWidgets.QMainWindow.__init__(parent)
        super(SplashScreenCompiled, self).__init__(parent)

        # self.ui = Ui_SplashWindowOLD()
        self.ui = Ui_SplashWindow2020()
        self.ui.setupUi(self)

        self.show()


class Ui_SplashWindowOLD(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(680, 230)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(680, 230))
        MainWindow.setMaximumSize(QSize(680, 235))
        MainWindow.setStyleSheet(u"background-color: rgb(39, 39, 39);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)

        self.Title = QLabel(self.centralwidget)
        self.Title.setObjectName(u"Title")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.Title.sizePolicy().hasHeightForWidth())
        self.Title.setSizePolicy(sizePolicy1)
        self.Title.setMinimumSize(QSize(381, 88))
        self.Title.setMaximumSize(QSize(10000, 88))
        font = QFont()
        font.setFamily(u"Bebas Neue")
        font.setPointSize(76)
        self.Title.setFont(font)
        self.Title.setStyleSheet(u"color: rgb(242, 242, 242);")
        self.Title.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.Title)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetMinimumSize)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.Swatch00_2 = QFrame(self.centralwidget)
        self.Swatch00_2.setObjectName(u"Swatch00_2")
        sizePolicy.setHeightForWidth(self.Swatch00_2.sizePolicy().hasHeightForWidth())
        self.Swatch00_2.setSizePolicy(sizePolicy)
        self.Swatch00_2.setMinimumSize(QSize(19, 19))
        self.Swatch00_2.setStyleSheet(u"background-color: rgb(191, 0, 0);\n"
                                      "border: 0px;")
        self.Swatch00_2.setFrameShape(QFrame.StyledPanel)
        self.Swatch00_2.setFrameShadow(QFrame.Raised)

        self.horizontalLayout.addWidget(self.Swatch00_2)

        self.Swatch01_2 = QFrame(self.centralwidget)
        self.Swatch01_2.setObjectName(u"Swatch01_2")
        sizePolicy.setHeightForWidth(self.Swatch01_2.sizePolicy().hasHeightForWidth())
        self.Swatch01_2.setSizePolicy(sizePolicy)
        self.Swatch01_2.setMinimumSize(QSize(19, 19))
        self.Swatch01_2.setStyleSheet(u"border: 0px;\n"
                                      "background-color: rgb(255, 192, 0);")
        self.Swatch01_2.setFrameShape(QFrame.StyledPanel)
        self.Swatch01_2.setFrameShadow(QFrame.Raised)

        self.horizontalLayout.addWidget(self.Swatch01_2)

        self.Swatch02_2 = QFrame(self.centralwidget)
        self.Swatch02_2.setObjectName(u"Swatch02_2")
        sizePolicy.setHeightForWidth(self.Swatch02_2.sizePolicy().hasHeightForWidth())
        self.Swatch02_2.setSizePolicy(sizePolicy)
        self.Swatch02_2.setMinimumSize(QSize(19, 19))
        self.Swatch02_2.setStyleSheet(u"background-color: rgb(255, 255, 0);\n"
                                      "border: 0px;")
        self.Swatch02_2.setFrameShape(QFrame.StyledPanel)
        self.Swatch02_2.setFrameShadow(QFrame.Raised)

        self.horizontalLayout.addWidget(self.Swatch02_2)

        self.Swatch03_3 = QFrame(self.centralwidget)
        self.Swatch03_3.setObjectName(u"Swatch03_3")
        sizePolicy.setHeightForWidth(self.Swatch03_3.sizePolicy().hasHeightForWidth())
        self.Swatch03_3.setSizePolicy(sizePolicy)
        self.Swatch03_3.setMinimumSize(QSize(19, 19))
        self.Swatch03_3.setStyleSheet(u"background-color: rgb(146, 208, 80);\n"
                                      "border: 0px;")
        self.Swatch03_3.setFrameShape(QFrame.StyledPanel)
        self.Swatch03_3.setFrameShadow(QFrame.Raised)

        self.horizontalLayout.addWidget(self.Swatch03_3)

        self.Swatch03_2 = QFrame(self.centralwidget)
        self.Swatch03_2.setObjectName(u"Swatch03_2")
        sizePolicy.setHeightForWidth(self.Swatch03_2.sizePolicy().hasHeightForWidth())
        self.Swatch03_2.setSizePolicy(sizePolicy)
        self.Swatch03_2.setMinimumSize(QSize(19, 19))
        self.Swatch03_2.setStyleSheet(u"background-color: rgb(0, 176, 80);\n"
                                      "border: 0px;")
        self.Swatch03_2.setFrameShape(QFrame.StyledPanel)
        self.Swatch03_2.setFrameShadow(QFrame.Raised)

        self.horizontalLayout.addWidget(self.Swatch03_2)

        self.Swatch03_4 = QFrame(self.centralwidget)
        self.Swatch03_4.setObjectName(u"Swatch03_4")
        sizePolicy.setHeightForWidth(self.Swatch03_4.sizePolicy().hasHeightForWidth())
        self.Swatch03_4.setSizePolicy(sizePolicy)
        self.Swatch03_4.setMinimumSize(QSize(19, 19))
        self.Swatch03_4.setStyleSheet(u"background-color: rgb(0, 176, 240);\n"
                                      "border: 0px;")
        self.Swatch03_4.setFrameShape(QFrame.StyledPanel)
        self.Swatch03_4.setFrameShadow(QFrame.Raised)

        self.horizontalLayout.addWidget(self.Swatch03_4)

        self.Swatch03_5 = QFrame(self.centralwidget)
        self.Swatch03_5.setObjectName(u"Swatch03_5")
        sizePolicy.setHeightForWidth(self.Swatch03_5.sizePolicy().hasHeightForWidth())
        self.Swatch03_5.setSizePolicy(sizePolicy)
        self.Swatch03_5.setMinimumSize(QSize(19, 19))
        self.Swatch03_5.setStyleSheet(u"background-color: rgb(0, 112, 192);\n"
                                      "border: 0px;")
        self.Swatch03_5.setFrameShape(QFrame.StyledPanel)
        self.Swatch03_5.setFrameShadow(QFrame.Raised)

        self.horizontalLayout.addWidget(self.Swatch03_5)

        self.Swatch03_6 = QFrame(self.centralwidget)
        self.Swatch03_6.setObjectName(u"Swatch03_6")
        sizePolicy.setHeightForWidth(self.Swatch03_6.sizePolicy().hasHeightForWidth())
        self.Swatch03_6.setSizePolicy(sizePolicy)
        self.Swatch03_6.setMinimumSize(QSize(19, 19))
        self.Swatch03_6.setStyleSheet(u"background-color: rgb(0, 32, 96);\n"
                                      "border: 0px;")
        self.Swatch03_6.setFrameShape(QFrame.StyledPanel)
        self.Swatch03_6.setFrameShadow(QFrame.Raised)

        self.horizontalLayout.addWidget(self.Swatch03_6)

        self.Swatch03_7 = QFrame(self.centralwidget)
        self.Swatch03_7.setObjectName(u"Swatch03_7")
        sizePolicy.setHeightForWidth(self.Swatch03_7.sizePolicy().hasHeightForWidth())
        self.Swatch03_7.setSizePolicy(sizePolicy)
        self.Swatch03_7.setMinimumSize(QSize(19, 19))
        self.Swatch03_7.setStyleSheet(u"background-color: rgb(112, 48, 160);\n"
                                      "border: 0px;")
        self.Swatch03_7.setFrameShape(QFrame.StyledPanel)
        self.Swatch03_7.setFrameShadow(QFrame.Raised)

        self.horizontalLayout.addWidget(self.Swatch03_7)

        self.Swatch03_9 = QFrame(self.centralwidget)
        self.Swatch03_9.setObjectName(u"Swatch03_9")
        sizePolicy.setHeightForWidth(self.Swatch03_9.sizePolicy().hasHeightForWidth())
        self.Swatch03_9.setSizePolicy(sizePolicy)
        self.Swatch03_9.setMinimumSize(QSize(19, 19))
        self.Swatch03_9.setStyleSheet(u"border: 0px;\n"
                                      "background-color: rgb(177, 1, 143);")
        self.Swatch03_9.setFrameShape(QFrame.StyledPanel)
        self.Swatch03_9.setFrameShadow(QFrame.Raised)

        self.horizontalLayout.addWidget(self.Swatch03_9)

        self.Swatch03_8 = QFrame(self.centralwidget)
        self.Swatch03_8.setObjectName(u"Swatch03_8")
        sizePolicy.setHeightForWidth(self.Swatch03_8.sizePolicy().hasHeightForWidth())
        self.Swatch03_8.setSizePolicy(sizePolicy)
        self.Swatch03_8.setMinimumSize(QSize(19, 19))
        self.Swatch03_8.setStyleSheet(u"border: 0px;\n"
                                      "background-color: rgb(230, 20, 100);")
        self.Swatch03_8.setFrameShape(QFrame.StyledPanel)
        self.Swatch03_8.setFrameShadow(QFrame.Raised)

        self.horizontalLayout.addWidget(self.Swatch03_8)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalSpacer = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.LoadingString01 = QLabel(self.centralwidget)
        self.LoadingString01.setObjectName(u"LoadingString01")
        sizePolicy.setHeightForWidth(self.LoadingString01.sizePolicy().hasHeightForWidth())
        self.LoadingString01.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setFamily(u"Calibri")
        font1.setPointSize(8)
        self.LoadingString01.setFont(font1)
        self.LoadingString01.setStyleSheet(u"color: rgb(255, 255, 255)")

        self.verticalLayout.addWidget(self.LoadingString01)

        self.LoadingString02 = QLabel(self.centralwidget)
        self.LoadingString02.setObjectName(u"LoadingString02")
        sizePolicy.setHeightForWidth(self.LoadingString02.sizePolicy().hasHeightForWidth())
        self.LoadingString02.setSizePolicy(sizePolicy)
        self.LoadingString02.setFont(font1)
        self.LoadingString02.setStyleSheet(u"color: rgb(255, 255, 255)")

        self.verticalLayout.addWidget(self.LoadingString02)

        self.verticalLayout.setStretch(0, 500)
        self.verticalLayout.setStretch(2, 500)
        self.verticalLayout.setStretch(3, 500)

        self.horizontalLayout_4.addLayout(self.verticalLayout)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_3)

        self.verticalLayout_3.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.owner = QLabel(self.centralwidget)
        self.owner.setObjectName(u"owner")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.owner.sizePolicy().hasHeightForWidth())
        self.owner.setSizePolicy(sizePolicy2)
        self.owner.setMinimumSize(QSize(0, 25))
        self.owner.setFont(font1)
        self.owner.setStyleSheet(u"color: rgb(255, 255, 255)")
        self.owner.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.owner)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.version = QLabel(self.centralwidget)
        self.version.setObjectName(u"version")
        sizePolicy2.setHeightForWidth(self.version.sizePolicy().hasHeightForWidth())
        self.version.setSizePolicy(sizePolicy2)
        self.version.setMinimumSize(QSize(0, 25))
        self.version.setFont(font1)
        self.version.setStyleSheet(u"color: rgb(255, 255, 255)")
        self.version.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.version)

        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.Title.setText(QCoreApplication.translate("MainWindow", u"Swatch M8", None))
        self.LoadingString01.setText(QCoreApplication.translate("MainWindow", u"Loading 01", None))
        self.LoadingString02.setText(QCoreApplication.translate("MainWindow", u"Loading 02", None))
        self.owner.setText(QCoreApplication.translate("MainWindow", u"\u00a9 Bert Plasschaert", None))
        self.version.setText(QCoreApplication.translate("MainWindow", u"Alpha V0.01", None))
    # retranslateUi


class Ui_SplashWindow2020(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(680, 230)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(680, 230))
        MainWindow.setMaximumSize(QtCore.QSize(680, 235))
        MainWindow.setStyleSheet("background-color: rgb(39, 39, 39);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_3.addItem(spacerItem)
        self.Title = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Title.sizePolicy().hasHeightForWidth())
        self.Title.setSizePolicy(sizePolicy)
        self.Title.setMinimumSize(QtCore.QSize(381, 88))
        self.Title.setMaximumSize(QtCore.QSize(10000, 88))
        font = QtGui.QFont()
        font.setFamily("Bebas Neue")
        font.setPointSize(76)
        self.Title.setFont(font)
        self.Title.setStyleSheet("color: rgb(242, 242, 242);")
        self.Title.setAlignment(QtCore.Qt.AlignCenter)
        self.Title.setObjectName("Title")
        self.verticalLayout_3.addWidget(self.Title)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Swatch00_2 = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Swatch00_2.sizePolicy().hasHeightForWidth())
        self.Swatch00_2.setSizePolicy(sizePolicy)
        self.Swatch00_2.setMinimumSize(QtCore.QSize(19, 19))
        self.Swatch00_2.setStyleSheet("background-color: rgb(191, 0, 0);\n"
                                      "border: 0px;")
        self.Swatch00_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Swatch00_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Swatch00_2.setObjectName("Swatch00_2")
        self.horizontalLayout.addWidget(self.Swatch00_2)
        self.Swatch01_2 = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Swatch01_2.sizePolicy().hasHeightForWidth())
        self.Swatch01_2.setSizePolicy(sizePolicy)
        self.Swatch01_2.setMinimumSize(QtCore.QSize(19, 19))
        self.Swatch01_2.setStyleSheet("border: 0px;\n"
                                      "background-color: rgb(255, 192, 0);")
        self.Swatch01_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Swatch01_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Swatch01_2.setObjectName("Swatch01_2")
        self.horizontalLayout.addWidget(self.Swatch01_2)
        self.Swatch02_2 = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Swatch02_2.sizePolicy().hasHeightForWidth())
        self.Swatch02_2.setSizePolicy(sizePolicy)
        self.Swatch02_2.setMinimumSize(QtCore.QSize(19, 19))
        self.Swatch02_2.setStyleSheet("background-color: rgb(255, 255, 0);\n"
                                      "border: 0px;")
        self.Swatch02_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Swatch02_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Swatch02_2.setObjectName("Swatch02_2")
        self.horizontalLayout.addWidget(self.Swatch02_2)
        self.Swatch03_3 = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Swatch03_3.sizePolicy().hasHeightForWidth())
        self.Swatch03_3.setSizePolicy(sizePolicy)
        self.Swatch03_3.setMinimumSize(QtCore.QSize(19, 19))
        self.Swatch03_3.setStyleSheet("background-color: rgb(146, 208, 80);\n"
                                      "border: 0px;")
        self.Swatch03_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Swatch03_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Swatch03_3.setObjectName("Swatch03_3")
        self.horizontalLayout.addWidget(self.Swatch03_3)
        self.Swatch03_2 = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Swatch03_2.sizePolicy().hasHeightForWidth())
        self.Swatch03_2.setSizePolicy(sizePolicy)
        self.Swatch03_2.setMinimumSize(QtCore.QSize(19, 19))
        self.Swatch03_2.setStyleSheet("background-color: rgb(0, 176, 80);\n"
                                      "border: 0px;")
        self.Swatch03_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Swatch03_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Swatch03_2.setObjectName("Swatch03_2")
        self.horizontalLayout.addWidget(self.Swatch03_2)
        self.Swatch03_4 = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Swatch03_4.sizePolicy().hasHeightForWidth())
        self.Swatch03_4.setSizePolicy(sizePolicy)
        self.Swatch03_4.setMinimumSize(QtCore.QSize(19, 19))
        self.Swatch03_4.setStyleSheet("background-color: rgb(0, 176, 240);\n"
                                      "border: 0px;")
        self.Swatch03_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Swatch03_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Swatch03_4.setObjectName("Swatch03_4")
        self.horizontalLayout.addWidget(self.Swatch03_4)
        self.Swatch03_5 = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Swatch03_5.sizePolicy().hasHeightForWidth())
        self.Swatch03_5.setSizePolicy(sizePolicy)
        self.Swatch03_5.setMinimumSize(QtCore.QSize(19, 19))
        self.Swatch03_5.setStyleSheet("background-color: rgb(0, 112, 192);\n"
                                      "border: 0px;")
        self.Swatch03_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Swatch03_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Swatch03_5.setObjectName("Swatch03_5")
        self.horizontalLayout.addWidget(self.Swatch03_5)
        self.Swatch03_6 = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Swatch03_6.sizePolicy().hasHeightForWidth())
        self.Swatch03_6.setSizePolicy(sizePolicy)
        self.Swatch03_6.setMinimumSize(QtCore.QSize(19, 19))
        self.Swatch03_6.setStyleSheet("background-color: rgb(0, 32, 96);\n"
                                      "border: 0px;")
        self.Swatch03_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Swatch03_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Swatch03_6.setObjectName("Swatch03_6")
        self.horizontalLayout.addWidget(self.Swatch03_6)
        self.Swatch03_7 = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Swatch03_7.sizePolicy().hasHeightForWidth())
        self.Swatch03_7.setSizePolicy(sizePolicy)
        self.Swatch03_7.setMinimumSize(QtCore.QSize(19, 19))
        self.Swatch03_7.setStyleSheet("background-color: rgb(112, 48, 160);\n"
                                      "border: 0px;")
        self.Swatch03_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Swatch03_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Swatch03_7.setObjectName("Swatch03_7")
        self.horizontalLayout.addWidget(self.Swatch03_7)
        self.Swatch03_9 = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Swatch03_9.sizePolicy().hasHeightForWidth())
        self.Swatch03_9.setSizePolicy(sizePolicy)
        self.Swatch03_9.setMinimumSize(QtCore.QSize(19, 19))
        self.Swatch03_9.setStyleSheet("border: 0px;\n"
                                      "background-color: rgb(177, 1, 143);")
        self.Swatch03_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Swatch03_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Swatch03_9.setObjectName("Swatch03_9")
        self.horizontalLayout.addWidget(self.Swatch03_9)
        self.Swatch03_8 = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Swatch03_8.sizePolicy().hasHeightForWidth())
        self.Swatch03_8.setSizePolicy(sizePolicy)
        self.Swatch03_8.setMinimumSize(QtCore.QSize(19, 19))
        self.Swatch03_8.setStyleSheet("border: 0px;\n"
                                      "background-color: rgb(230, 20, 100);")
        self.Swatch03_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Swatch03_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Swatch03_8.setObjectName("Swatch03_8")
        self.horizontalLayout.addWidget(self.Swatch03_8)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem2 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem2)
        self.LoadingString01 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LoadingString01.sizePolicy().hasHeightForWidth())
        self.LoadingString01.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(8)
        self.LoadingString01.setFont(font)
        self.LoadingString01.setStyleSheet("color: rgb(255, 255, 255)")
        self.LoadingString01.setObjectName("LoadingString01")
        self.verticalLayout.addWidget(self.LoadingString01)
        self.LoadingString02 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LoadingString02.sizePolicy().hasHeightForWidth())
        self.LoadingString02.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(8)
        self.LoadingString02.setFont(font)
        self.LoadingString02.setStyleSheet("color: rgb(255, 255, 255)")
        self.LoadingString02.setObjectName("LoadingString02")
        self.verticalLayout.addWidget(self.LoadingString02)
        self.verticalLayout.setStretch(0, 500)
        self.verticalLayout.setStretch(2, 500)
        self.verticalLayout.setStretch(3, 500)
        self.horizontalLayout_4.addLayout(self.verticalLayout)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.owner = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.owner.sizePolicy().hasHeightForWidth())
        self.owner.setSizePolicy(sizePolicy)
        self.owner.setMinimumSize(QtCore.QSize(0, 25))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(8)
        self.owner.setFont(font)
        self.owner.setStyleSheet("color: rgb(255, 255, 255)")
        self.owner.setAlignment(QtCore.Qt.AlignCenter)
        self.owner.setObjectName("owner")
        self.horizontalLayout_3.addWidget(self.owner)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem4)
        self.version = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.version.sizePolicy().hasHeightForWidth())
        self.version.setSizePolicy(sizePolicy)
        self.version.setMinimumSize(QtCore.QSize(0, 25))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(8)
        self.version.setFont(font)
        self.version.setStyleSheet("color: rgb(255, 255, 255)")
        self.version.setAlignment(QtCore.Qt.AlignCenter)
        self.version.setObjectName("version")
        self.horizontalLayout_3.addWidget(self.version)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "MainWindow", None, -1))
        self.Title.setText(QtWidgets.QApplication.translate("MainWindow", "Swatch M8", None, -1))
        self.LoadingString01.setText(QtWidgets.QApplication.translate("MainWindow", "Loading 01", None, -1))
        self.LoadingString02.setText(QtWidgets.QApplication.translate("MainWindow", "Loading 02", None, -1))
        self.owner.setText(QtWidgets.QApplication.translate("MainWindow", "┬® Bert Plasschaert", None, -1))
        self.version.setText(QtWidgets.QApplication.translate("MainWindow", "Alpha V0.01", None, -1))


splashScreen = SplashScreenCompiled()


class Main(QDialog):
    def __init__(self, parent):
        super(Main, self).__init__(parent)

        ui_file = QFile("D:\OneDrive - BUas\MGT\Scripts\SwatchM8\\resources\qt\ui_splash.ui")
        ui_file.open(QFile.ReadOnly)
        self.window = QtUiTools.QUiLoader().load(ui_file, parent=self)
        ui_file.close()

        # btn = self.window.findChild(QPushButton, 'exportas_button')
        # btn.clicked.connect(self.closeEvent)

# main_window = get_main_window()
# md = Main(main_window)
# md.show()
