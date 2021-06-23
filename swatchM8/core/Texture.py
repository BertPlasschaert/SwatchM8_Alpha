from swatchM8.core import Swatch
from swatchM8.core import Image
from swatchM8.core.util.ExeptionHandeling import InvalidInputExeption

import logging
logger = logging.getLogger(__name__)

class Texture:

    def __init__(self, name, filePath, size, amountOfSwatchesOnRow, availableCoordinates=None):
        # type: (str,str,int,int,list) -> None

        self.name = name
        self.filePath = filePath
        self.size = size
        self.amountOfSwatchesOnRow = amountOfSwatchesOnRow

        self.swatchSize = self.calculateSwatchSize(amountOfSwatchesOnRow, size)
        self.swatches = []  # lijst van alle swatch objecten

        self.availableCoordinates = availableCoordinates  # lijst met booleans
        if availableCoordinates is None:
            self.availableCoordinates = self.generateAvailableCoordinates()

        logger.info('done Initializing TextureObject with Name: {}, filePath: {}, size: {}, amountOnRow: {}'.format(name, filePath, size, amountOfSwatchesOnRow))

    def saveImage(self):
        # type: () -> None

        image = Image.Image(self)
        image.save()

    def createSwatch(self, swatchName, color, coordinate=None):
        # type: (str, list, object) -> object

        try:
            if self.checkIfSwatchExists(swatchName) is not None:
                raise ("Swatch with name: {} already exists".format(swatchName))

        except InvalidInputExeption as e:
            logger.exception(e)
            raise

        if coordinate is None:
            coordinate = self.requestCoordinate()

        swatch = Swatch.Swatch(swatchName, coordinate, self.swatchSize, color)
        self.swatches.append(swatch)

        if coordinate is not None:
            self.setCoordinateUnavailable(swatch)

        logger.info("swatch created with name: {} on Coordinate: {} using Color: {}".format(swatchName, coordinate, color))
        return swatch

    def deleteSwatch(self, swatchName):
        # type: (str) -> list

        swatch = self.getSwatchByName(swatchName)

        self.setCoordinateAvailable(swatch)

        self.swatches.remove(swatch)

        logger.info("Swatch with name {} successfully deleted".format(swatchName))
        return self.swatches

    def getSwatchByName(self, swatchName):
        # type: (str) -> object

        if self.checkIfSwatchExists(swatchName):
            for i in self.swatches:
                if i.name == swatchName:
                    logger.debug('requested and returned Swatch with name: {}'.format(swatchName))
                    return i
        else:
            logger.debug('requested Swatch with name: {}, returned None'.format(swatchName))
            return None

    def generateAvailableCoordinates(self):
        # type: () -> None

        possibleCoordinates = []

        for i in range(self.amountOfSwatchesOnRow):
            col = []
            for j in range(self.amountOfSwatchesOnRow):
                col.append(True)

            possibleCoordinates.append(col)

        for i in self.swatches:
            possibleCoordinates[i.coordinate[0]][i.coordinate[1]] = False

        availableCoordinates = possibleCoordinates

        logger.debug('generated list with availible Coordinates: {}'.format(availableCoordinates))
        return availableCoordinates

    def requestCoordinate(self):
        # type: () -> List

        for i in range(self.amountOfSwatchesOnRow):
            for j in range(self.amountOfSwatchesOnRow):

                if self.availableCoordinates[i][j] == True:
                    logger.debug('requested coordinated returned: {}'.format([i, j]))
                    return [i, j]

        try:
            raise ValueError('All the coordinates are used!')

        except ValueError as e:
            logger.exception(e)
            raise
        # return None

    def setCoordinateAvailable(self, swatch):
        # type: (object) -> None

        self.availableCoordinates[(swatch.coordinate)[0]][(swatch.coordinate)[1]] = True
        logger.debug('Coordinate {} back availible'.format([(swatch.coordinate)[0], (swatch.coordinate)[1]]))

    def setCoordinateUnavailable(self, swatch):
        # type: (object) -> None

        self.availableCoordinates[(swatch.coordinate)[0]][(swatch.coordinate)[1]] = False
        logger.debug('Coordinate {} now unavailible'.format([(swatch.coordinate)[0], (swatch.coordinate)[1]]))

    def calculateSwatchSize(self, amountSwatchesOnRow, size):
        # type: (int, int) -> int

        return int(size / amountSwatchesOnRow)

    def checkIfSwatchExists(self, swatchName):
        # type: (str) -> bool

        for i in self.swatches:

            if i.name.lower() == swatchName.lower():
                logger.debug('Swatch with name: {} ALREADY exist'.format(swatchName))

                return i

        return None
