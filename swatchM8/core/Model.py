from swatchM8.core import Part
import logging
logger = logging.getLogger()


class Model:

    def __init__(self, name):
        # type: (str) -> None

        self.name = name
        self.mayaRef = None
        self.parts = []

        loggername = logger.name

        logger.debug('created Model named: {}'.format(self.name))

    def addPart(self, partName):
        # type: (str) -> object

        newPart = Part.Part(partName, self)
        self.parts.append(newPart)

        logger.debug('added Part: {} to Model: {}'.format(partName, self.name))
        return newPart

    def getPart(self, partName):
        # type: (str) -> object

        for i in self.parts:
            if i.name == partName:

                logger.debug('got part with name: {} from Model: {}'.format(partName, self.name))
                return i
        else:
            logger.debug('no part named: {} found on Model: {} '.format(partName, self.name))
            return None

    def deletePart(self, partToDel):
        # type: (object) -> None

        for i in self.parts:

            if i == partToDel:
                self.parts.remove(i)

        logger.debug('deleted Part: {} from Model: {}'.format(partToDel, self.name))