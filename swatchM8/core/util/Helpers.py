from PySide2.QtGui import QColor


def convertToQColor(color):
    # type: (list) -> QColor

    return QColor(color[0], color[1], color[2])  # TODO: add opacity channel to converter


def reloadAllModules():
    from swatchM8.core.util import Enum
    from swatchM8.core import Main, Model, Part, Swatch, Texture
    from swatchM8.core import Image
    from swatchM8.data import JsonRepository
    from swatchM8.ui.qt.widgets import EditPartWidget
    from swatchM8.ui.qt import Controller_Splash, ui_main, ui_splash, WindowStates
    from swatchM8.ui.qt import Controller_Main
    from swatchM8.application import Standalone, Maya
    from swatchM8.application import AppController
    # import core.util.cgLogging

    reload(Maya)
    reload(Enum)
    reload(Image)
    reload(Main)
    reload(Model)
    reload(Part)
    reload(Swatch)
    reload(Texture)
    reload(JsonRepository)
    # reload(AddPartWidget)
    # reload(AddSwatchWidget)
    # reload(ColorPickerWidget)
    # reload(CreateTextureWidget)
    # reload(EditModelWidget)
    # reload(LoadOrCreateTextureWidget)
    # reload(NeutralStateWidget)
    # reload(TextureSettingsWidget)
    reload(EditPartWidget)
    # reload(EditSwatchWidget)
    reload(Controller_Main)
    reload(Controller_Splash)
    reload(ui_main)
    reload(ui_splash)
    reload(WindowStates)
    reload(AppController)
    reload(Standalone)
    reload(Maya)
    # reload(core.util.cgLogging)


def checkIfBetween(a, x, b):
    # type: (float, float, float) -> bool


    return min(a, b) < x < max(a, b)