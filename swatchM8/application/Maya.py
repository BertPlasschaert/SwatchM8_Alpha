from PySide2 import QtWidgets
import os

import maya.cmds as cmds
import pymel.core as pm

import maya.OpenMayaUI as omui
import shiboken2

from swatchM8.core.util import Helpers

import logging
logger = logging.getLogger(__name__)

if not 'customMixinWindow' in globals():
    customMixinWindow = None


class Maya:

    def __init__(self):
        # type: () -> None

        self.name = 'maya'
        self.reloadModules()

    def getMayaWindow(self):
        # type: () -> shiboken2.wrapInstance()
        """
        Get the main Maya window as a QtGui.QMainWindow instance
        @return: QtGui.QMainWindow instance of the top level Maya windows
        """

        pointer = omui.MQtUtil.mainWindow()
        if pointer is not None:
            return shiboken2.wrapInstance(long(pointer), QtWidgets.QWidget)

    def makeWindowDockable(self, window):
        # type: () -> None
        pass

    def reloadModules(self):
        # type: () -> None

        from swatchM8.core.util import Helpers
        reload(Helpers)
        Helpers.reloadAllModules()

        logger.debug("reloaded all modules")

    def unwrapSelection(self, coordinate, amountOnRow):
        # type: (list, int) -> None

        selectedFaces = cmds.ls(selection=True, flatten=True)

        if selectedFaces == []:
            logging.warning("no faces or object was selected, nothing Unwrapped")
            return
            # raise InvalidInputExeption("No object was selected, please select an object")


        chunkSize = float(1) / float(amountOnRow)

        # cmds.polyAutoProjection(selectedFaces)
        cmds.polyPlanarProjection(selectedFaces)

        cmds.polyEditUV(pu=0, pv=0, su=chunkSize, sv=chunkSize)

        uvs = cmds.polyListComponentConversion(selectedFaces, tuv=True)
        cmds.select(uvs)
        cmds.polyEditUVShell(relative=True, uValue=float(coordinate[0]) / float(amountOnRow), vValue=float(coordinate[1]) / float(amountOnRow))

        bufferScale = 0.9
        cmds.polyEditUV(pu=float(coordinate[0]) / float(amountOnRow) + float(chunkSize / 2), pv=float(coordinate[1]) / float(amountOnRow) + float(chunkSize / 2), su=bufferScale, sv=bufferScale)

        logger.info("Unwrapped: {}".format(selectedFaces))

    def selectFromCoordinate(self, coordinate, amountOnRow): #TODO: change this code to Open Maya
        # type: (list, int) -> None

        chunkSize = float(1) / float(amountOnRow)

        UCoordinate = float(coordinate[0]) / float(amountOnRow)
        VCoordinate = float(coordinate[1]) / float(amountOnRow)

        buffer = chunkSize / 10

        selection = pm.selected()

        print selection

        if selection == []:
            print("please select object to find Poly's on")
            return None

        if isinstance(selection[0], pm.nodetypes.Transform):  # if selected object is full Object
            selection = selection[0].faces  # get the faces from it

        finalFaces = []

        for i in selection:  # Loops over faces in selection

            qualifyingFaces = []

            uvs = zip(*i.getUVs())

            for pt in uvs:  # loops over the UV coordinates of a single face

                if Helpers.checkIfBetween(UCoordinate - buffer, pt[0], UCoordinate + chunkSize + buffer) and Helpers.checkIfBetween(VCoordinate - buffer, pt[1], VCoordinate + chunkSize + buffer):
                    qualifyingFaces.append(i)

            if len(qualifyingFaces) == len(uvs):  # checks if all the availible points are qualifying

                finalFaces = finalFaces + qualifyingFaces

        pm.select(finalFaces)

        logger.debug("selected Faces from Coordinate: {}, in total {} amount of faces selected".format(coordinate,len(finalFaces)))

        # selectionTrf = selection[0]

        # help(selectionShp)

        # help(selectionTrf.getUVs)
        # print selectionTrf.getUVs()

        # print selectionTrf.verts.indices()
        # print selectionTrf.verts.getUVs()
        # print selectionTrf.verts.numUVs()

        # object = cmds.ls(selection=True, flatten=True)
        #
        # uvs = cmds.polyListComponentConversion(object, tuv=True)
        # cmds.select(uvs)
        #
        # for i in uvs:
        #
        #     cmds.ls(i)
        #     coordinate = cmds.polyEditUV(q=True)
        #     print coordinate

        # https: // forums.cgsociety.org / t / maya - python - api - 2 - 0 - getpointsatuv / 1849098
        # https://forums.cgsociety.org/t/pymel-seeking-help-in-getting-uv-location-and-map-name/1797553/3
        # selection = om.MSelectionList()
        # selection.add('pTorus1')
        # print(om.MSelectionList(0))
        # ground_path = om.MDagPath()
        # nodeDagPath = selection.getDagPath(0, ground_path)
        # mfnMesh = om.MFnMesh(nodeDagPath)
        # faces=mfnMesh.numPolygons
        # u = 0.5
        # v = 0.5
        # p = mfnMesh.getPointsAtUV(u, v, space=om.MSpace.kObject, uvSet='map1', tolerance=1e-5)
        # print p

    def resetUnwrapSelection(self):
        # type: () -> None

        self.unwrapSelection([0, 0], 1)

    def createMayaMaterial(self, name, saveLocation):
        # type: (str, str) -> object

        shaderNode = pm.shadingNode('blinn', name=name, asShader=1)
        textureNode = pm.shadingNode('file', name=name + '_textureFile', asTexture=1)
        pm.connectAttr(textureNode.outColor, shaderNode.color, force=1)

        sg = pm.sets(renderable=1, noSurfaceShader=1, empty=1, name=shaderNode + '_SG')
        pm.connectAttr(shaderNode.outColor, sg.surfaceShader, force=1)
        pm.sets(sg, edit=1, forceElement=pm.select(cl=True))

        textureNode.fileTextureName.set(saveLocation)
        textureNode.filterType.set(0)

        logger.info("created a Maya Material with name: {}".format(name))
        return sg

        # print pm.listAttr(textureNode.filter)
        # help(textureNode.filter)

    def checkIfMaterialExist(self, name):
        # type: (str) -> None

        matList = pm.ls(mat=True)

        for i in matList:

            if i.name() == name:
                logger.debug('requested and returned maya Material with name: {}'.format(name))
                return i

        logger.debug('requested maya Material with name: {}, returned None'.format(name))
        return None

    def reloadTextureFile(self, name, filePath):
        # type: (str, str) -> None

        if self.checkIfMaterialExist(name) is not None:
            textureNode = pm.ls(name + '_textureFile')[0]
            textureNode.fileTextureName.set(os.path.join(filePath, name) + '.png')

            logger.debug("reloaded texture file inside Maya Material")

    def assignMaterial(self, texture):
        # type: (object) -> None

        materialName = texture.name.replace(" ", "_")

        objs = pm.selected()

        if self.checkIfMaterialExist(materialName) is None:
            self.createMayaMaterial(materialName, os.path.join(texture.filePath, texture.name) + '.png')

        pm.sets(materialName + '_SG', forceElement=objs, e=True)

        allViewPorts = pm.getPanel(type='modelPanel')

        for i in allViewPorts:
            pm.modelEditor(i, e=1, displayTextures=1)

        logging.info("assigned Material to Object: {}".format(objs))