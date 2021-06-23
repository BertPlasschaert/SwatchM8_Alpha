import json
from copy import deepcopy
from os import path
from swatchM8.core import Texture, Model


def saveData(texture, modelList):
    # type: (object, list) -> None

    combinedExportObject = {

        "texture": createExportObject(texture),
        "modelList": createExportObject(modelList)
    }

    with open(path.join(texture.filePath, texture.name) + '.json', 'w') as savedFile:
        json.dump(combinedExportObject, savedFile, indent=4, sort_keys=True, cls=CustomEncoder)


def createExportObject(obj):
    # type: (object) -> object

    exportObject = deepcopy(obj)

    if isinstance(obj, Texture.Texture):

        del exportObject.swatchSize

        for i in exportObject.swatches:

            del i.size

            for j in i.parts:
                j.swatch = j.swatch.name
                j.model = j.model.name

    if isinstance(obj, list):

        for i in exportObject:
            for j in i.parts:
                del j.model
                j.swatch = j.swatch.name

    return exportObject


def loadData(filePath):
    # type: (str) -> list

    with open(filePath, 'r') as loadFile:
        dataDict = json.load(loadFile)

    return constructObjectsFromLoad(dataDict)


def constructObjectsFromLoad(dataDict):
    # type: (dict) -> tuple

    textureDict = dataDict["texture"]
    modelListDict = dataDict["modelList"]

    texture = Texture.Texture(textureDict["name"], textureDict["filePath"], textureDict["size"], textureDict["amountOfSwatchesOnRow"], textureDict["availableCoordinates"])

    for i in textureDict["swatches"]:
        texture.createSwatch(i["name"], i["color"], i["coordinate"])

    modelList = []

    for i in modelListDict:

        modelName = i["name"]  # name of part
        model = Model.Model(modelName)

        for j in i["parts"]:
            partName = j["name"]  # model name
            swatchName = j["swatch"]  # swatch name
            part = model.addPart(partName)
            swatch = texture.getSwatchByName(swatchName)
            part.swatch = swatch
            swatch.addPart(part)

        modelList.append(model)

    return texture, modelList


class CustomEncoder(json.JSONEncoder):
    def default(self, obj):
        return obj.__dict__
