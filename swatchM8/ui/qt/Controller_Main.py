from PySide2 import QtWidgets

from swatchM8.ui.qt.ui_main import Ui_MainWindow

from swatchM8.ui.qt.widgets.EditPartWidget import EditPartWidget
from swatchM8.ui.qt.widgets.EditSwatchWidget import EditSwatchWidget
from swatchM8.ui.qt.widgets.EditModelWidget import EditModelWidget
from swatchM8.ui.qt.widgets.NeutralStateWidget import NeutralStateWidget
from swatchM8.ui.qt.widgets.AddPartWidget import AddPartWidget
from swatchM8.ui.qt.widgets.AddSwatchWidget import AddSwatchWidget
from swatchM8.ui.qt.widgets.LoadOrCreateTextureWidget import LoadOrCreateTextureWidget
from swatchM8.ui.qt.widgets.CreateTextureWidget import CreateTextureWidget
from swatchM8.ui.qt.widgets.TextureSettingsWidget import TextureSettingsWidget
from swatchM8.ui.qt.WindowStates import RightFrameStates, PopupFrameStates

from swatchM8.core.Swatch import Swatch
from swatchM8.core.Part import Part
from swatchM8.core.Model import Model

import logging

logger = logging.getLogger(__name__)


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, Main, parent2=None):
        # type: (object, object) -> None

        super(MainWindow, self).__init__(parent2)
        self.Main = Main

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.loadCustomWidgets()
        self.hideAllStates()

        self.ui.PopUpFrame.show()
        self.ui.PopUpFrame.setCurrentIndex(PopupFrameStates.loadOrCreateTexture.value)

        self.connectElements()

        self.ui.ModelsTree.setColumnWidth(0,120)
        self.ui.SwatchTree.setColumnWidth(0,120)

    def closeEvent(self, event):

        logger.info("Stop Session")


    def loadCustomWidgets(self):
        # type: () -> None

        self.neutralFrame = NeutralStateWidget()
        self.ui.RightFrame.insertWidget(RightFrameStates.neutral.value, self.neutralFrame)

        self.editSwatchFrame = EditSwatchWidget(self, self.Main)
        self.ui.RightFrame.insertWidget(RightFrameStates.editSwatch.value, self.editSwatchFrame)

        self.editPartFrame = EditPartWidget(self, self.Main)
        self.ui.RightFrame.insertWidget(RightFrameStates.editPart.value, self.editPartFrame)

        self.editModelFrame = EditModelWidget(self, self.Main)
        self.ui.RightFrame.insertWidget(RightFrameStates.editModel.value, self.editModelFrame)

        self.addPartFrame = AddPartWidget(self, self.Main)
        self.ui.RightFrame.insertWidget(RightFrameStates.addPart.value, self.addPartFrame)

        self.addSwatchFrame = AddSwatchWidget(self, self.Main)
        self.ui.RightFrame.insertWidget(RightFrameStates.addSwatch.value, self.addSwatchFrame)

        self.loadOrCreateTextureFrame = LoadOrCreateTextureWidget(self, self.Main)
        self.ui.PopUpFrame.insertWidget(PopupFrameStates.loadOrCreateTexture.value, self.loadOrCreateTextureFrame)

        self.createTextureFrame = CreateTextureWidget(self, self.Main)
        self.ui.PopUpFrame.insertWidget(PopupFrameStates.createTexture.value, self.createTextureFrame)

        self.textureSettingsFrame = TextureSettingsWidget(self, self.Main)
        self.ui.PopUpFrame.insertWidget(PopupFrameStates.textureSettings.value, self.textureSettingsFrame)

    def connectElements(self):
        # type: () -> None

        self.ui.TextureSettingsButton.clicked.connect(self.showTextureSettingsFrame)

        self.ui.AddPartButton.clicked.connect(lambda: self.ui.RightFrame.setCurrentIndex(RightFrameStates.addPart.value))
        self.ui.AddPartButton.clicked.connect(self.addPartFrame.setNewData)
        self.ui.AddSwatchButton.clicked.connect(lambda: self.ui.RightFrame.setCurrentIndex(RightFrameStates.addSwatch.value))
        self.ui.AddSwatchButton.clicked.connect(self.addSwatchFrame.setNewData)

        # self.ui.ModelsTree.itemActivated.connect(self.pressedTreeItem)
        self.ui.ModelsTree.itemClicked.connect(self.pressedTreeItem)
        # self.ui.SwatchTree.itemActivated.connect(self.pressedTreeItem)
        self.ui.SwatchTree.itemClicked.connect(self.pressedTreeItem)

        self.ui.ApplyMaterialButton.pressed.connect(lambda: self.Main.app.assignMaterial(self.Main.texture))

    def hideAllStates(self):
        # type: () -> None

        self.ui.RightFrame.setCurrentIndex(RightFrameStates.neutral.value)
        self.ui.PopUpFrame.hide()

    def showStateFromTree(self, selectedObject, edit=True):
        # type: (object, bool) -> None

        self.hideAllStates()

        if edit:

            if isinstance(selectedObject, Swatch):
                self.ui.RightFrame.setCurrentIndex(RightFrameStates.editSwatch.value)
                self.editSwatchFrame.setNewData(selectedObject)

            elif isinstance(selectedObject, Part):
                self.ui.RightFrame.setCurrentIndex(RightFrameStates.editPart.value)
                self.editPartFrame.setNewData(selectedObject)

            elif isinstance(selectedObject, Model):
                self.ui.RightFrame.setCurrentIndex(RightFrameStates.editModel.value)
                self.editModelFrame.setNewData(selectedObject)

    def loadData(self):
        # type: () -> None

        self.ui.PopUpFrame.hide()
        self.populateModelList()
        self.populateSwatchList()

    def applyChanges(self):
        # type: () -> None

        expandedModels = self.getTreeWidgetExpanded(self.ui.ModelsTree)
        expandedSwatches = self.getTreeWidgetExpanded(self.ui.SwatchTree)

        self.Main.saveData()
        self.loadData()

        self.setTreeWidgetExpanded(self.ui.ModelsTree, expandedModels)
        self.setTreeWidgetExpanded(self.ui.SwatchTree, expandedSwatches)

    def showTextureSettingsFrame(self):
        # type: () -> None

        self.ui.PopUpFrame.show()
        self.ui.PopUpFrame.setCurrentIndex(PopupFrameStates.textureSettings.value)
        self.textureSettingsFrame.setNewData(self.Main.texture)

    def pressedTreeItem(self, item, column):
        # type: (object, int) -> None

        selectedObject = item.data(3 + column, 0)
        self.showStateFromTree(selectedObject, edit=True)
        # print(selectedObject.name)

    def populateModelList(self):
        # type: () -> None

        self.ui.ModelsTree.clear()

        for i in self.Main.models:

            modelEntry = QtWidgets.QTreeWidgetItem(self.ui.ModelsTree)
            modelEntry.setText(0, i.name)
            modelEntry.setData(3, 0, i)

            for j in i.parts:
                partEntry = QtWidgets.QTreeWidgetItem(modelEntry)
                partEntry.setText(0, j.name)
                partEntry.setText(1, j.swatch.name)
                partEntry.setData(3, 0, j)
                partEntry.setData(4, 0, j.swatch)

    def populateSwatchList(self):
        # type: () -> None

        self.ui.SwatchTree.clear()

        for i in self.Main.texture.swatches:

            swatchEntry = QtWidgets.QTreeWidgetItem(self.ui.SwatchTree)
            swatchEntry.setText(0, i.name)
            swatchEntry.setData(3, 0, i)

            for j in i.parts:
                partEntry = QtWidgets.QTreeWidgetItem(swatchEntry)
                partEntry.setText(0, j.name)
                partEntry.setData(3, 0, j)
                partEntry.setText(1, j.model.name)
                partEntry.setData(4, 0, j.model)

    def getTreeWidgetExpanded(self, QTreeWidget):

        expandedList = []

        iterator = QtWidgets.QTreeWidgetItemIterator(QTreeWidget)
        while iterator.value():

            item = iterator.value()
            if item.isExpanded():
                expandedList.append(item.text(0))

            iterator += 1

        return expandedList

    def setTreeWidgetExpanded(self, QTreeWidget, expandedList):

        iterator = QtWidgets.QTreeWidgetItemIterator(QTreeWidget)
        while iterator.value():

            item = iterator.value()

            if item.text(0) in expandedList:
                item.setExpanded(True)

            iterator += 1

    def checkIfModelNameEntryIsValid(self, field):

        if field.text() == "":
            self.setInputInvalid(field)
            return

        if self.Main.checkIfModelExists(field.text()) is not None:
            self.setInputInvalid(field)
            return

        self.setInputValid(field)

    def checkIfPartNameEntryIsValid(self, field, model):

        if field.text() == "":
            self.setInputInvalid(field)
            return

        if self.Main.checkIfPartExists(field.text(), model) is not None:
            self.setInputInvalid(field)
            return

        self.setInputValid(field)

    def checkifSwatchNameIsValid(self, field):

        if field.text() == "":
            self.setInputInvalid(field)
            return

        if self.Main.texture.checkIfSwatchExists(field.text()) is not None:
            self.setInputInvalid(field)
            return

        self.setInputValid(field)

    def checkifFieldIsEmpty(self,field):

        if field.text() == "":
            self.setInputInvalid(field)
            return

        self.setInputValid(field)

    def setInputValid(self, field):
        field.setStyleSheet("")

    def setInputInvalid(self, field):
        field.setStyleSheet("border: 1px solid red")

# Dit is code voor een docking window te maken
# Er waren heel wat problemen met dit dus dit is teruggeschoven naar block C


# vergeet niet de UI naar een QDialog te veranderen
# class MainWindowMaya(MayaQWidgetDockableMixin, MainWindow):
#
#     def __init__(self, Main):
#         MainWindow.__init__(self, Main)

# class MainWindowMaya(MayaQWidgetDockableMixin, QtWidgets.QDialog):
#
#     def __init__(self, Main):
#         super(MainWindowMaya, self).__init__()
#
#         self.mainWindow = MainWindow(Main)
#
#         self.setLayout(QtWidgets.QVBoxLayout())
#         self.layout().addWidget(self.mainWindow)
#
#         print(self)
