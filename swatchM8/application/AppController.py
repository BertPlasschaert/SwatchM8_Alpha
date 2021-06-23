import sys, os, re
import logging
logger = logging.getLogger(__name__)


# Kijken welke DCC het is
def getApplicationName():
    # type: () -> string

    if re.match("python\\.exe", os.path.basename(sys.executable), re.I):
        logger.info("start New Session: Standalone")
        return 'standalone'

    if re.match("maya\\.exe", os.path.basename(sys.executable), re.I):
        logger.info("start New Session: Maya")
        return 'maya'

    if re.match("blender\\.exe", os.path.basename(sys.executable), re.I):
        logger.info("start New Session: Blender")
        return 'blender'

    if re.match("UE4Editor\\.exe", os.path.basename(sys.executable), re.I):
        logger.info("start New Session: Unreal")
        return 'unreal'


# Juist Module voor dat programma importen
def getCorrectModule(currentApplicationName):
    # type: (str) -> object
    if currentApplicationName == 'standalone':
        from swatchM8.application.Standalone import StandAlone
        return StandAlone()

    elif currentApplicationName == 'maya':
        from swatchM8.application.Maya import Maya
        return Maya()

    elif currentApplicationName == 'blender':
        pass

    elif currentApplicationName == 'unreal':
        pass
