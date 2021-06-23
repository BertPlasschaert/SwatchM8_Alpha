import sys
import os
import tempfile

from PySide2 import QtWidgets

from swatchM8.core import Texture, Model
from swatchM8.data import JsonRepository as Repo

from swatchM8.ui.qt import Controller_Splash
from swatchM8.ui.qt import Controller_Main

from swatchM8.application import AppController
from swatchM8.core.util.ExeptionHandeling import InvalidInputExeption

import swatchM8.core.util.cgLogging as cgLogging

LOGGING_LEVEL = cgLogging.DEBUG

tempDir = os.path.join(tempfile.gettempdir(), "swatchM8")
if not os.path.isdir(tempDir):
    os.makedirs(os.path.join(tempfile.gettempdir(), "swatchM8"))

logger = cgLogging.getLogger(file=os.path.join(tempDir, r"baseLog.log"), level=LOGGING_LEVEL)


class Main:

    def __init__(self, GUI=True):
        # type: () -> None

        self.texture = None
        self.models = []
        self.workSpaceName = 'customWorkspace'

        self.splashScreen = None
        self.mainWindow = None

        self.app = AppController.getCorrectModule(AppController.getApplicationName())

        if GUI:
            self.runSplashScreen()

    def createTexture(self, textureName, filePath, size, amountOfSwatchesOnRow):
        # type: (str, str, int, int) -> object
        self.linkLoggingFile(filePath, textureName)

        self.texture = Texture.Texture(textureName, filePath, size, amountOfSwatchesOnRow)

        logger.info('texture created with name: {}, filePath: {}, size: {}, amount on Row: {}'.format(textureName, filePath, size, amountOfSwatchesOnRow))
        return self.texture

    def createModel(self, modelName):
        # type: (str) -> object

        try:
            if self.checkIfModelExists(modelName) is not None:
                raise InvalidInputExeption("A model already exists with the name: {}".format(modelName))

        except InvalidInputExeption as e:
            logger.exception(e)
            raise

        model = Model.Model(modelName)
        self.models.append(model)

        logger.info('model created with name: {}'.format(modelName))
        return model

    def addPartToSwatch(self, swatch, model, partName):
        # type: (object, object, str) -> object

        try:
            if swatch is None or model is None:
                raise InvalidInputExeption("Swatch: {} or Model: {} entry is invalid".format(swatch, model))
        except InvalidInputExeption as e:
            logger.exception(e)
            raise

        try:
            if self.checkIfPartExists(partName, model) is not None:
                raise InvalidInputExeption("Part: {} already exist on model: {}".format(partName, model.name))
        except InvalidInputExeption as e:
            logger.exception(e)
            raise

        part = model.addPart(partName)

        swatch.addPart(part)
        part.swatch = swatch

        logger.info("added Part: {} to swatch: {}".format(partName, swatch.name))
        return part

    def getModelByName(self, modelName):
        # type: (str) -> object

        for i in self.models:
            if i.name == modelName:
                logger.debug('requested and returned model with name: {}'.format(modelName))
                return i

        logger.debug('requested model with name: {}, returned None'.format(modelName))
        return None

    def getTextureByName(self, textureName):
        # type: (str) -> object

        for i in self.textures:
            if i.name == textureName:
                logger.debug('requested and returned texture with name: {}'.format(textureName))
                return i

        logger.debug('requested texture with name: {}, returned None'.format(textureName))
        return None

    def saveData(self):
        # type: () -> None

        self.texture.saveImage()
        Repo.saveData(self.texture, self.models)
        self.app.reloadTextureFile(self.texture.name, self.texture.filePath)

        logger.info('image saved, Json saved, reloaded texture file')

    def loadData(self, filePath):
        # type: (str) -> None

        self.linkLoggingFile(os.path.split(filePath)[0], os.path.split(filePath)[1].split('.')[0])

        logger.info("start loading data from: {}".format(filePath))

        loadedObjects = Repo.loadData(filePath)
        self.texture = loadedObjects[0]
        self.models = loadedObjects[1]

        logger.info("loading DONE")

    def runSplashScreen(self):
        # type: () -> None

        if self.app.name == 'standalone':
            app = QtWidgets.QApplication(sys.argv)
            self.splashScreen = Controller_Splash.SplashScreen(self)
            self.splashScreen.show()
            sys.exit(app.exec_())

        elif self.app.name == 'maya':

            # self.mainWindow = Controller_Main.MainWindowMaya(self)
            self.splashScreen = Controller_Splash.SplashScreen(self)
            self.splashScreen.show()

    def runMainWindow(self):
        # type: () -> None

        if self.splashScreen is not None:
            self.splashScreen.close()

        if self.app.name == 'standalone':

            self.mainWindow = Controller_Main.MainWindow(self)
            self.mainWindow.show()

        elif self.app.name == 'maya':

            self.mainWindow = Controller_Main.MainWindow(self, self.app.getMayaWindow())
            self.mainWindow.show()

            # self.mainWindow = Controller_Main.MainWindowMaya(self)
            # self.mainWindow.show(dockable=True)

    def deleteModel(self, model):
        # type: (object) -> None

        removeList = []

        for i in self.texture.swatches:

            for j in i.parts:

                if j.model == model:
                    removeList.append(j)

            for part in removeList:
                self.deletePart(i, part)

                removeList = []

        self.models.remove(model)
        logger.info("Model: {} deleted successfully.".format(model.name))

    def deletePart(self, swatch, part):
        # type: (object, object) -> None

        swatch.parts.remove(part)

        for i in self.models:

            if i == part.model:
                i.parts.remove(part)

        logger.info("Part: {} from Model: {} deleted successfully.".format(part.name, part.model.name))

    def deleteSwatch(self, swatch):
        # type: (object) -> None

        removeList = []

        for i in self.models:

            for j in i.parts:

                if j in swatch.parts:
                    removeList.append(j)

            for part in removeList:
                i.parts.remove(part)

            removeList = []

        self.texture.setCoordinateAvailable(swatch)
        self.texture.swatches.remove(swatch)

        logger.info("Swatch: {} deleted successfully.".format(swatch.name))

    def checkIfModelExists(self, modelName):
        # type: (str) -> object
        
        
        for i in self.models:
            if i.name.lower() == modelName.lower():
                logger.debug('Model with name: {} ALREADY exist'.format(modelName))
                return i

        # print('model with name: ' + modelName + ' does NOT exist')
        return None

    def checkIfPartExists(self, partName, model):

        if len(model.parts) == 0:
            return None

        for i in model.parts:
            if i.name.lower() == partName.lower():
                logger.debug('Part with name: {} ALREADY exist on Model: {}'.format(partName, model.name))
                return i

        # print('swatch with name: ' + partName + ' does NOT exist on model: ' + model.name)
        return None

    def linkLoggingFile(self, filePath, textureName):

        global logger

        path = os.path.join(filePath, textureName) + ".log"
        logger = cgLogging.getLogger(file=path, level=LOGGING_LEVEL)
