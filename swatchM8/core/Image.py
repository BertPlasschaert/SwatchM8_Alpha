from PySide2.QtCore import QSize
from PySide2.QtGui import QImage
import os

from swatchM8.core.util.Helpers import convertToQColor

# import core.util.cgLogging as cgLogging
# logger = cgLogging.getLogger(__name__)

import logging

logger = logging.getLogger(__name__)


class Image:

    def __init__(self, texture):
        # type: (object) -> None

        self.texture = texture
        self.backgroundColor = [203, 0, 186]
        self.image = None

        size = QSize(self.texture.size, self.texture.size)
        self.image = QImage(size, QImage.Format_RGB888)

    def drawSwatches(self):
        # type: () -> None

        self.image.fill(convertToQColor(self.backgroundColor))

        for swatch in self.texture.swatches:
            color = convertToQColor(swatch.color)

            UCoordinate = swatch.coordinate[0]
            VCoordinate = swatch.coordinate[1]

            xPos = int(UCoordinate) * int(self.texture.swatchSize)
            yPos = int((int(self.texture.size) - 1) - (int(VCoordinate) * int(self.texture.swatchSize)))

            self.drawSwatch(xPos, yPos, color)

    def drawSwatch(self, xPos, yPos, color):
        # type: (int,int,list) -> None

        for x in range(self.texture.swatchSize):
            for y in range(self.texture.swatchSize):
                self.image.setPixelColor(int(xPos) + x, int(yPos) - y, color)

    def save(self):
        # type: () -> None

        self.drawSwatches()
        self.image.save(os.path.join(self.texture.filePath, self.texture.name) + '.png', "PNG", 100)

        # Image for video, every update is incremetnal
        # from datetime import datetime
        # now = datetime.now()
        # dt_string = now.strftime("%d_%m_%Y-%H_%M_%S")
        # self.image.save(os.path.join(self.texture.filePath, self.texture.name + dt_string) + '.png', "PNG", 100)
        #####

        logger.debug('saved out Image at: {}'.format(self.texture.filePath))
