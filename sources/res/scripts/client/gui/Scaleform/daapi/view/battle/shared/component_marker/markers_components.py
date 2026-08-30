import math, weakref, AnimationSequence, BigWorld, Math
from ids_generators import SequenceIDGenerator
from account_helpers.settings_core import ISettingsCore, settings_constants
from helpers import dependency
from shared_utils import BitmaskHelper
from vehicle_systems.stricted_loading import makeCallbackWeak
from gui.Scaleform.daapi.view.battle.shared import indicators
from gui.Scaleform.daapi.view.battle.shared.markers2d import settings
from gui.Scaleform.daapi.view.battle.shared.indicators import _DIRECT_INDICATOR_SWF, _DIRECT_INDICATOR_MC_NAME
from debug_utils import LOG_CURRENT_EXCEPTION
import CombatSelectedArea
from gui.battle_control import minimap_utils
from gui.impl import backport
from gui.impl.gen import R

def _getDirectionIndicator(swf, mcName):
    indicator = None
    try:
        indicator = indicators.createDirectIndicator(swf, mcName)
    except Exception:
        LOG_CURRENT_EXCEPTION()

    return indicator


class ComponentBitMask(BitmaskHelper):
    NONE = 0
    MARKER_2D = 1
    MINIMAP_MARKER = 2
    DIRECTION_INDICATOR = 4
    ANIM_SEQUENCE_MARKER = 8
    TERRAIN_MARKER = 16
    ALL = MARKER_2D | MINIMAP_MARKER | DIRECTION_INDICATOR | ANIM_SEQUENCE_MARKER | TERRAIN_MARKER
    BASE = MARKER_2D | MINIMAP_MARKER | DIRECTION_INDICATOR
    BASE_SEQ = ANIM_SEQUENCE_MARKER | MINIMAP_MARKER | DIRECTION_INDICATOR
    BASE_T = BASE | TERRAIN_MARKER
    BASE_SEQ_T = BASE_SEQ | TERRAIN_MARKER
    LIST = (
     MARKER_2D, MINIMAP_MARKER, DIRECTION_INDICATOR, ANIM_SEQUENCE_MARKER, TERRAIN_MARKER)


class _IMarkerComponentBase(object):
    _idGen = SequenceIDGenerator()

    def __init__(self, data):
        super(_IMarkerComponentBase, self).__init__()
        self._componentID = self._idGen.next()
        self._initData = data
        self._matrixProduct = data.get(b'matrixProduct')
        self._isVisible = data.get(b'visible', True)
        self._entity = None
        return

    @property
    def isVisible(self):
        return self._isVisible

    @property
    def componentID(self):
        return self._componentID

    @property
    def position(self):
        return Math.Matrix(self._matrixProduct.a).translation

    @property
    def positionWithOffset(self):
        return Math.Matrix(self._matrixProduct).translation

    @property
    def maskType(self):
        raise NotImplementedError
        return

    def update(self, *args, **kwargs):
        return

    def clear(self):
        return

    def setVisible(self, isVisible):
        return

    def attachGUI(self, guiProvider):
        return

    def detachGUI(self):
        return

    def setMarkerMatrix(self, matrix):
        self._matrixProduct.a = matrix
        return

    def setMarkerEntity(self, entity):
        self._entity = weakref.proxy(entity)
        return

    def setMarkerPosition(self, position):
        matrix = Math.Matrix()
        matrix.setTranslate(position)
        self.setMarkerMatrix(matrix)
        return


class World2DMarkerComponent(_IMarkerComponentBase):

    def __init__(self, idx, data):
        super(World2DMarkerComponent, self).__init__(data)
        self.__marker2DData = data.get(self.maskType)[idx]
        self._gui = lambda : None
        self._isMarkerExists = False
        self.__displayDistance = self.__marker2DData.get(b'displayDistance', True)
        self.__distance = self.__marker2DData.get(b'distance', 0)
        return

    @property
    def maskType(self):
        return ComponentBitMask.MARKER_2D

    def attachGUI(self, guiProvider):
        self._gui = weakref.ref(guiProvider.getMarkers2DPlugin())
        if self._isVisible:
            self._createMarker()
        return self._isMarkerExists

    def detachGUI(self):
        self.clear()
        return

    def clear(self):
        self._deleteMarker()
        self._gui = lambda : None
        return

    def setVisible(self, isVisible):
        if self._isVisible == isVisible:
            return
        else:
            self._isVisible = isVisible
            if self._gui() is None:
                return
            if self._isVisible:
                self._createMarker()
            else:
                self._deleteMarker()
            return

    def update(self, distance, *args, **kwargs):
        self.__distance = distance
        gui = self._gui()
        if not self.__displayDistance:
            distance = -1
        if self._isVisible and self._isMarkerExists and gui:
            gui.markerSetDistance(self._componentID, distance)
        return

    def setMarkerMatrix(self, matrix):
        super(World2DMarkerComponent, self).setMarkerMatrix(matrix)
        gui = self._gui()
        if gui and not self._isMarkerExists:
            gui.setMarkerMatrix(self._componentID, matrix)
        return

    def _createMarker(self):
        gui = self._gui()
        if gui and not self._isMarkerExists:
            self._isMarkerExists = self.__createMarkerAndSetup(gui, self._componentID)
        return

    def _deleteMarker(self):
        gui = self._gui()
        if self._isMarkerExists and gui:
            gui.deleteMarker(self._componentID)
        self._isMarkerExists = False
        self._isVisible = False
        return

    def __createMarkerAndSetup(self, gui, objectID):
        symbol = self.__marker2DData.get(b'symbol', settings.MARKER_SYMBOL_NAME.STATIC_OBJECT_MARKER)
        if not gui.createMarker(objectID, self._matrixProduct, active=self._isVisible, symbol=symbol):
            return False
        gui.setupMarker(objectID, self.__marker2DData.get(b'shape', b'arrow'), self.__marker2DData.get(b'min-distance', 0), self.__marker2DData.get(b'max-distance', 0), self.__distance, self.__marker2DData.get(b'metersString', backport.text(R.strings.ingame_gui.marker.meters())), self.__marker2DData.get(b'distanceFieldColor', b'yellow'))
        return True


class MinimapMarkerComponent(_IMarkerComponentBase):

    def __init__(self, idx, data):
        super(MinimapMarkerComponent, self).__init__(data)
        self.__minimapData = data.get(self.maskType)[idx]
        self._gui = lambda : None
        self._isMarkerExists = False
        self._onlyTranslation = self.__minimapData.get(b'onlyTranslation', False)
        self._translationOnlyMP = Math.TranslationOnlyMP()
        self._translationOnlyMP.source = self._matrixProduct.a
        return

    @property
    def maskType(self):
        return ComponentBitMask.MINIMAP_MARKER

    def attachGUI(self, guiProvider):
        self._gui = weakref.ref(guiProvider.getMinimapPlugin())
        if self._isVisible:
            self._createMarker()
        return self._isMarkerExists

    def detachGUI(self):
        self.clear()
        return

    def clear(self):
        self._deleteMarker()
        self._gui = lambda : None
        return

    def setVisible(self, isVisible):
        if self._isVisible == isVisible:
            return
        else:
            self._isVisible = isVisible
            if self._gui() is None:
                return
            if self._isVisible:
                self._createMarker()
            else:
                self._deleteMarker()
            return

    def _createMarker(self):
        gui = self._gui()
        if gui and not self._isMarkerExists:
            matrix = self._translationOnlyMP if self._onlyTranslation else self._matrixProduct.a
            self._isMarkerExists = gui.createMarker(self._componentID, self.__minimapData.get(b'symbol', b''), self.__minimapData.get(b'container', b''), matrix=matrix, active=self._isVisible)
        return

    def _deleteMarker(self):
        gui = self._gui()
        if self._isMarkerExists and gui:
            gui.deleteMarker(self._componentID)
        self._isMarkerExists = False
        self._isVisible = False
        return

    def update(self, *args, **kwargs):
        gui = self._gui()
        if self._isVisible and gui and self._isMarkerExists:
            gui.update(self._componentID, *args, **kwargs)
        return

    def setMarkerMatrix(self, matrix):
        super(MinimapMarkerComponent, self).setMarkerMatrix(matrix)
        self._translationOnlyMP.source = self._matrixProduct.a
        gui = self._gui()
        if gui and self._isMarkerExists:
            mtx = self._translationOnlyMP if self._onlyTranslation else self._matrixProduct.a
            gui.setMatrix(self._componentID, mtx)
        return


class DirectionIndicatorMarkerComponent(_IMarkerComponentBase):
    settingsCore = dependency.descriptor(ISettingsCore)

    def __init__(self, idx, data):
        super(DirectionIndicatorMarkerComponent, self).__init__(data)
        dIndicatorData = data.get(self.maskType)[idx]
        self.__shapes = dIndicatorData.get(b'dIndicatorShapes', (b'green', b'green'))
        self.__indicator = None
        self.__prevPosition = self.positionWithOffset
        self.__swf = dIndicatorData.get(b'swf', _DIRECT_INDICATOR_SWF)
        self.__mcName = dIndicatorData.get(b'mcName', _DIRECT_INDICATOR_MC_NAME)
        return

    @property
    def maskType(self):
        return ComponentBitMask.DIRECTION_INDICATOR

    def attachGUI(self, _):
        if self.__indicator is None:
            self.__indicator = _getDirectionIndicator(self.__swf, self.__mcName)
            self.__indicator.setShape(self.__currentShape)
            self.__indicator.track(self.positionWithOffset)
        if not self.__indicator:
            return False
        else:
            self.settingsCore.onSettingsChanged += self.__onSettingsChanged
            self.__indicator.setPosition(self.positionWithOffset)
            self.__indicator.setVisibility(self._isVisible)
            return True

    def detachGUI(self):
        self.settingsCore.onSettingsChanged -= self.__onSettingsChanged
        self.clear()
        return

    def update(self, distance, *args, **kwargs):
        if self.__indicator is None:
            return
        else:
            self.__indicator.setDistance(distance)
            currentPosition = self.positionWithOffset
            if currentPosition != self.__prevPosition:
                self.__indicator.setPosition(currentPosition)
                self.__prevPosition = currentPosition
            return

    def clear(self):
        if self.__indicator is None:
            return
        else:
            self.setVisible(False)
            self.__indicator.remove()
            self.__indicator = None
            return

    def setVisible(self, isVisible):
        if not self._isVisible and isVisible:
            self.__updateVisibility()
        elif self._isVisible and not isVisible:
            self._isVisible = False
            if self.__indicator is not None:
                self.__indicator.setVisibility(False)
        if self._isVisible and self.__indicator:
            self.__indicator.setPosition(self.positionWithOffset)
        return

    def __updateVisibility(self):
        if self.__indicator is not None:
            if not hasattr(BigWorld.player().inputHandler.ctrl, b'camera'):
                return
            self._isVisible = True
            camera = BigWorld.player().inputHandler.ctrl.camera.camera
            camMat = Math.Matrix(camera.invViewMatrix)
            if camMat is not None:
                view = camMat.applyV4Point(Math.Vector4(0, 0, 1, 0))
                direction = self.positionWithOffset - BigWorld.player().getOwnVehiclePosition()
                dotProduct = direction.dot(view[0:3])
                cosFov = math.cos(BigWorld.projection().fov / 2)
                if dotProduct > cosFov * direction.length:
                    self._isVisible = False
            self.__indicator.setVisibility(self._isVisible)
        return

    @property
    def __currentShape(self):
        if self.settingsCore.getSetting(b'isColorBlind'):
            return self.__shapes[1]
        return self.__shapes[0]

    def __onSettingsChanged(self, diff):
        if self.__indicator is None:
            return
        else:
            if b'isColorBlind' in diff:
                self.__indicator.setShape(self.__currentShape)
            return


class AnimationSequenceMarkerComponent(_IMarkerComponentBase):

    def __init__(self, idx, data):
        super(AnimationSequenceMarkerComponent, self).__init__(data)
        animSeqData = data.get(self.maskType)[idx]
        self.__path = animSeqData.get(b'path', None)
        self.__animator = None
        self.__spaceID = BigWorld.player().spaceID
        if self.__path is not None:
            loader = AnimationSequence.Loader(self.__path, self.__spaceID)
            BigWorld.loadResourceListBG((loader,), makeCallbackWeak(self.__onSequenceLoaded))
        return

    @property
    def maskType(self):
        return ComponentBitMask.ANIM_SEQUENCE_MARKER

    def clear(self):
        if self.__animator is not None:
            self.__animator.stop()
            self.__animator = None
        return

    def update(self, *args, **kwargs):
        if self.__animator:
            self.__animator.bindToWorld(Math.Matrix(self._matrixProduct))
        return

    def setVisible(self, isVisible):
        if self._isVisible == isVisible:
            return
        self._isVisible = isVisible
        if not self.__animator:
            return
        if self._isVisible:
            self.__animator.setEnabled(True)
            self.__animator.start()
        else:
            self.__animator.setEnabled(False)
            self.__animator.stop()
        return

    def __onSequenceLoaded(self, resourceRefs):
        if self.__path in resourceRefs.failedIDs:
            return
        self.__animator = resourceRefs[self.__path]
        self.__animator.bindToWorld(Math.Matrix(self._matrixProduct))
        if self._isVisible:
            self.__animator.start()
        return


class TerrainMarkerComponent(_IMarkerComponentBase):
    DEF_SIZE = (10, 10)
    DEF_DIRECTION = Math.Vector3(1.0, 0.0, 0.0)

    def __init__(self, idx, data):
        super(TerrainMarkerComponent, self).__init__(data)
        terrainData = data.get(self.maskType)[idx]
        self.__area = CombatSelectedArea.CombatSelectedArea()
        self.__direction = terrainData.get(b'direction', self.DEF_DIRECTION)
        self.__objDirection = terrainData.get(b'objDirection', True)
        path = terrainData.get(b'path', b'')
        size = terrainData.get(b'size', self.DEF_SIZE)
        color = terrainData.get(b'color', CombatSelectedArea.COLOR_WHITE)
        direction = Math.Matrix(self._matrixProduct.a).applyToAxis(2) if self.__objDirection else self.__direction
        self.__area.setup(self.position, direction, size, path, color, None)
        self.__area.setGUIVisible(self._isVisible)
        self.__prevPosition = self.position
        return

    @property
    def maskType(self):
        return ComponentBitMask.TERRAIN_MARKER

    def clear(self):
        if self.__area is not None:
            self.__area.destroy()
            self.__area = None
        return

    def update(self, *args, **kwargs):
        currentPosition = self.position
        if self.__area and currentPosition != self.__prevPosition:
            direction = Math.Matrix(self._matrixProduct.a).applyToAxis(2) if self.__objDirection else self.__direction
            self.__area.relocate(currentPosition, direction)
            self.__prevPosition = currentPosition
        return

    def setVisible(self, isVisible):
        if self._isVisible == isVisible:
            return
        self._isVisible = isVisible
        if not self.__area:
            return
        self.__area.setGUIVisible(self._isVisible)
        return


class PolygonalZoneMinimapMarkerComponent(MinimapMarkerComponent):
    settingsCore = dependency.descriptor(ISettingsCore)

    class Blending(object):
        NORMAL = b'normal'
        ADD = b'add'
        MULTIPLY = b'multiply'
        SCREEN = b'screen'
        SUBTRACT = b'subtract'

    def __init__(self, idx, data):
        super(PolygonalZoneMinimapMarkerComponent, self).__init__(idx, data)
        self._polygon = None
        self._isBorderVisible = False
        markerData = data.get(self.maskType)[idx]
        self._properties = markerData[b'color']
        return

    @property
    def isVisible(self):
        return self._entity.entityPolygonalTrigger.isActive and self._entity.clientVisualComp.isVisible

    def getPolygon(self):
        udo = BigWorld.userDataObjects.get(self._entity.clientVisualComp.udoGuid, None)
        if udo is None:
            return []
        else:
            return udo.minimapMarkerPolygon

    def attachGUI(self, gui):
        super(PolygonalZoneMinimapMarkerComponent, self).attachGUI(gui)
        self.settingsCore.onSettingsChanged += self.__onSettingsChanged
        if not self._polygon:
            polygon = self.getPolygon()
            if not polygon:
                return
            arenaSize = BigWorld.player().arena.arenaType.boundingBox[1]
            xc = minimap_utils.MINIMAP_SIZE[0] / arenaSize[0]
            yc = minimap_utils.MINIMAP_SIZE[1] / arenaSize[1]
            self._polygon = sum(([p[0] * xc, p[1] * yc] for p in polygon), list())
        self._updatePolygon()
        return

    def detachGUI(self):
        super(PolygonalZoneMinimapMarkerComponent, self).detachGUI()
        self.settingsCore.onSettingsChanged -= self.__onSettingsChanged
        return

    def update(self, *args, **kwargs):
        super(PolygonalZoneMinimapMarkerComponent, self).update(*args, **kwargs)
        gui = self._gui()
        if not self._isVisible or not gui or not self._isMarkerExists:
            return
        newIsVisible = self.isVisible
        if self._isBorderVisible == newIsVisible:
            return
        self._isBorderVisible = newIsVisible
        gui.setActive(self._componentID, self._isBorderVisible)
        gui.invoke(self._componentID, b'setVisible', self._isBorderVisible)
        return

    def _updatePolygon(self):
        isColorBlind = self.settingsCore.getSetting(settings_constants.GRAPHICS.COLOR_BLIND)
        self._gui().invoke(self._componentID, b'setProperties', *self.__getMarkerProperties(isColorBlind))
        self._gui().invoke(self._componentID, b'setZoneData', self._polygon)
        self._gui().invoke(self._componentID, b'setVisible', self._isBorderVisible)
        self._gui().setActive(self._componentID, self._isBorderVisible)
        return

    def __getMarkerProperties(self, isColorBlind):
        props = (isColorBlind or self._properties)[b'default'] if 1 else self._properties[b'colorBlind']
        return (
         props[b'fillColor'], props[b'fillAlpha'],
         props[b'outlineColor'], props[b'outlineAlpha'],
         props[b'lineThickness'], props[b'fillBlendMode'],
         props[b'outlineBlendMode'])

    def __onSettingsChanged(self, diff):
        if settings_constants.GRAPHICS.COLOR_BLIND in diff:
            self._updatePolygon()
        return


class StaticDeathZoneMinimapMarkerComponent(PolygonalZoneMinimapMarkerComponent):

    @property
    def isVisible(self):
        return self._entity.isActive

    def getPolygon(self):
        p = self._entity.position
        min, max = self._entity.clientVisualComp.getCorners()
        return [
         (
          min.x - p.x, min.z - p.z),
         (
          min.x - p.x, max.z - p.z),
         (
          max.x - p.x, max.z - p.z),
         (
          max.x - p.x, min.z - p.z)]
