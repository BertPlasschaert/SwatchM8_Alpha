from swatchM8.core.util.Enum import Enum

class RightFrameStates(Enum):
    neutral = 0
    editSwatch = 1
    editPart = 2
    editModel = 3
    addPart = 4
    addSwatch = 5


class PopupFrameStates(Enum):
    loadOrCreateTexture = 0
    createTexture = 1
    textureSettings = 2
