from __future__ import absolute_import, division
import logging, typing, math, weakref
from past.utils import old_div
import AnimationSequence, BigWorld, Math
from account_helpers.settings_core.settings_constants import BattleCommStorageKeys
from chat_commands_consts import INVALID_TARGET_ID, MarkerType
from ids_generators import SequenceIDGenerator
from account_helpers.settings_core import ISettingsCore, settings_constants
from helpers import dependency
from shared_utils import BitmaskHelper
from vehicle_systems.stricted_loading import makeCallbackWeak
from gui.Scaleform.daapi.view.battle.shared import indicators
from gui.Scaleform.daapi.view.battle.shared.markers2d.markers import ReplyStateForMarker
from gui.Scaleform.daapi.view.battle.shared.indicators import _DIRECT_INDICATOR_SWF as SWF, _DIRECT_INDICATOR_MC_NAME as MC_NAME
from gui.Scaleform.daapi.view.battle.shared.markers2d.settings import MARKER_SYMBOL_NAME, CommonMarkerType
from gui.impl import backport
from gui.impl.gen import R
from debug_utils import LOG_CURRENT_EXCEPTION
import CombatSelectedArea
from gui.battle_control import minimap_utils
if typing.TYPE_CHECKING:
    import ResMgr
_logger = logging.getLogger(__name__)

def _getDirectionIndicator(swf, mcName):
    indicator = None
    try:
        indicator = indicators.createDirectIndicator(swf, mcName)
    except Exception:
        LOG_CURRENT_EXCEPTION()

    return indicator


class Blending(object):
    NORMAL = b'normal'
    ADD = b'add'
    MULTIPLY = b'multiply'
    SCREEN = b'screen'
    SUBTRACT = b'subtract'


class ComponentBitMask(BitmaskHelper):
    NONE = 0
    MARKER_2D = 1
    MINIMAP_MARKER = 2
    DIRECTION_INDICATOR = 4
    ANIM_SEQUENCE_MARKER = 8
    TERRAIN_MARKER = 16
    FULLSCREEN_MAP_MARKER = 32
    LIST = (
     MARKER_2D, MINIMAP_MARKER, DIRECTION_INDICATOR, ANIM_SEQUENCE_MARKER, TERRAIN_MARKER, FULLSCREEN_MAP_MARKER)


COMPONENT_MARKER_TYPE_NAMES = {k: v for k, v in ComponentBitMask.__dict__.items() if isinstance(v, int)}
COMPONENT_MARKER_TYPE_IDS = {v: k for k, v in COMPONENT_MARKER_TYPE_NAMES.items()}

class _IMarkerComponentBase(object):
    settingsCore = dependency.descriptor(ISettingsCore)
    _idGen = SequenceIDGenerator()

    def __init__(self, config, matrixProduct, entity=None, targetID=INVALID_TARGET_ID, isVisible=True):
        super(_IMarkerComponentBase, self).__init__()
        self._componentID = self._idGen.nextSequenceID
        self._config = config
        self._matrixProduct = matrixProduct
        self._isVisible = isVisible
        self._targetID = targetID
        self._entity = weakref.proxy(entity) if entity else None
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

    @property
    def bcMarkerType(self):
        return MarkerType.INVALID_MARKER_TYPE

    def update(self, *args, **kwargs):
        return

    def clear(self):
        return

    def setVisible(self, isVisible):
        return

    def attachGUI(self, guiProvider, **kwargs):
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

    @classmethod
    def configReader(cls, section):
        raise NotImplementedError
        return


class World2DMarkerComponent(_IMarkerComponentBase):
    _METERS_STRING = b' ' + backport.text(R.strings.ingame_gui.marker.meters())

    def __init__(self, config, matrixProduct, entity=None, targetID=INVALID_TARGET_ID, isVisible=True):
        super(World2DMarkerComponent, self).__init__(config, matrixProduct, entity, targetID, isVisible)
        self._gui = lambda : None
        self._isMarkerExists = False
        self._displayDistance = self._config.get(b'display_distance', True)
        self._distance = self._config.get(b'distance', 0)
        self._symbol = self._config[b'symbol']
        return

    @classmethod
    def configReader(cls, section):
        config = {b'shape': (section.readString(b'shape', b'arrow')), 
           b'min_distance': (section.readFloat(b'min_distance', 0.0)), 
           b'max_distance': (section.readFloat(b'max_distance', 0.0)), 
           b'distance': (section.readFloat(b'distance', 0.0)), 
           b'distanceFieldColor': (section.readString(b'distanceFieldColor', b'yellow')), 
           b'display_distance': (section.readBool(b'display_distance', True)), 
           b'symbol': (section.readString(b'symbol', MARKER_SYMBOL_NAME.STATIC_OBJECT_MARKER))}
        return config

    @property
    def maskType(self):
        return ComponentBitMask.MARKER_2D

    @property
    def guiMarkerType(self):
        return CommonMarkerType.NORMAL

    @property
    def symbol(self):
        return self._symbol

    def attachGUI(self, guiProvider, **kwargs):
        self._gui = weakref.ref(guiProvider.getMarkers2DPlugin())
        self.settingsCore.onSettingsChanged += self._onSettingsChanged
        self._createMarker(**kwargs)
        return self._isMarkerExists

    def detachGUI(self):
        self.settingsCore.onSettingsChanged -= self._onSettingsChanged
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
            gui = self._gui()
            if gui is None:
                return
            gui.setMarkerActive(self._componentID, self._isVisible)
            return

    def update(self, distance, *args, **kwargs):
        self._distance = distance
        gui = self._gui()
        if not self._displayDistance:
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

    def _createMarker(self, **kwargs):
        gui = self._gui()
        if gui and not self._isMarkerExists:
            self._isMarkerExists = gui.createMarker(self._componentID, self._targetID, self.symbol, self._matrixProduct, self._isVisible, self.bcMarkerType, self.guiMarkerType)
            if self._isMarkerExists:
                self._setupMarker(gui, **kwargs)
        return

    def _deleteMarker(self):
        gui = self._gui()
        if self._isMarkerExists and gui:
            gui.deleteMarker(self._componentID)
        self._isMarkerExists = False
        self._isVisible = False
        return

    def _setupMarker(self, gui, **kwargs):
        config = self._config
        gui.invokeMarker(self._componentID, b'init', config[b'shape'], config[b'min_distance'], config[b'max_distance'], self._distance, self._METERS_STRING, config[b'distanceFieldColor'])
        return True

    def _onSettingsChanged(self, diff):
        return


class World2DActionMarkerComponent(World2DMarkerComponent):
    MARKER_CULL_DISTANCE = 1800
    MARKER_MIN_SCALE = 60.0
    MARKER_BOUNDS = Math.Vector4(30, 30, 30, 30)
    MARKER_INNER_BOUNDS = Math.Vector4(17, 17, 18, 18)
    MARKER_BOUND_MIN_SCALE = Math.Vector2(1.0, 1.0)

    def __init__(self, config, matrixProduct, entity=None, targetID=INVALID_TARGET_ID, isVisible=True):
        super(World2DActionMarkerComponent, self).__init__(config, matrixProduct, entity, targetID, isVisible)
        self._isStickyFromConfig = config.get(b'is_sticky', True)
        return

    @classmethod
    def configReader(cls, section):
        config = {b'shape': (section.readString(b'shape', b'targetPoint')), 
           b'shapeReplyMe': (section.readString(b'shapeReplyMe', b'targetPointReplyMe')), 
           b'shapeHighlight': (section.readString(b'shapeHighlight', b'targetPointHighlight')), 
           b'min_distance': (section.readFloat(b'min_distance', 0.0)), 
           b'max_distance': (section.readFloat(b'max_distance', 0.0)), 
           b'distance': (section.readFloat(b'distance', 0.0)), 
           b'distanceFieldColor': (section.readString(b'distanceFieldColor', b'yellow')), 
           b'display_distance': (section.readBool(b'display_distance', True)), 
           b'symbol': (section.readString(b'symbol', MARKER_SYMBOL_NAME.STATIC_OBJECT_MARKER)), 
           b'is_sticky': (section.readBool(b'is_sticky', True)), 
           b'cull_distance': (section.readFloat(b'cull_distance', cls.MARKER_CULL_DISTANCE)), 
           b'min_scale': (section.readFloat(b'min_scale', cls.MARKER_MIN_SCALE)), 
           b'bounds': (section.readVector4(b'bounds', cls.MARKER_BOUNDS)), 
           b'inner_bounds': (section.readVector4(b'inner_bounds', cls.MARKER_INNER_BOUNDS)), 
           b'bounds_min_scale': (section.readVector2(b'bounds_min_scale', cls.MARKER_BOUND_MIN_SCALE))}
        return config

    @property
    def guiMarkerType(self):
        return CommonMarkerType.TARGET_POINT

    @property
    def bcMarkerType(self):
        return MarkerType.TARGET_POINT_MARKER_TYPE

    @property
    def symbol(self):
        return self._symbol or MARKER_SYMBOL_NAME.TARGET_POINT_MARKER

    def _setupMarker(self, gui, **kwargs):
        config = self._config
        gui.invokeMarker(self._componentID, b'init', config[b'shape'], config[b'shapeReplyMe'], config[b'shapeHighlight'], config[b'min_distance'], config[b'max_distance'], self._distance, self._METERS_STRING, config[b'distanceFieldColor'])
        isSticky = config[b'is_sticky'] & bool(self.settingsCore.getSetting(BattleCommStorageKeys.SHOW_STICKY_MARKERS))
        gui.setMarkerSticky(self.componentID, isSticky)
        gui.setActiveState(self._componentID, ReplyStateForMarker.CREATE_STATE)
        gui.setMarkerRenderInfo(self._componentID, config[b'min_scale'], config[b'bounds'], config[b'inner_bounds'], config[b'cull_distance'], config[b'bounds_min_scale'])
        gui.setMarkerBoundEnabled(self._componentID, True)
        return True

    def _deleteMarker(self):
        gui = self._gui()
        if self._isMarkerExists and gui:
            gui.setMarkerSticky(self._componentID, False)
            gui.setActiveState(self._componentID, ReplyStateForMarker.CREATE_STATE)
            gui.setMarkerReplied(self._componentID, False)
            gui.setMarkerBoundEnabled(self._componentID, False)
            gui.deleteMarker(self._componentID)
        self._isMarkerExists = False
        self._isVisible = False
        return

    def _onSettingsChanged(self, diff):
        gui = self._gui()
        if not gui:
            return
        addSettings = {}
        for item in diff:
            if item in (BattleCommStorageKeys.SHOW_STICKY_MARKERS,):
                addSettings[item] = diff[item]

        if not addSettings:
            return
        newIsSticky = bool(addSettings.get(BattleCommStorageKeys.SHOW_STICKY_MARKERS, self._isStickyFromConfig))
        gui.setMarkerSticky(self.componentID, newIsSticky & self._isStickyFromConfig)
        return


class World2DLocationMarkerComponent(World2DMarkerComponent):
    CULL_DISTANCE = 1800
    MIN_SCALE = 50.0
    BOUNDS = Math.Vector4(30, 30, 90, -15)
    INNER_BOUNDS = Math.Vector4(15, 15, 70, -35)
    BOUNDS_MIN_SCALE = Math.Vector2(1.0, 0.8)
    MIN_Y_OFFSET = 1.2
    MAX_Y_OFFSET = 3.2
    DISTANCE_FOR_MIN_Y_OFFSET = 400
    MAX_Y_BOOST = 1.4
    BOOST_START = 120

    def __init__(self, config, matrixProduct, entity=None, targetID=INVALID_TARGET_ID, isVisible=True):
        super(World2DLocationMarkerComponent, self).__init__(config, matrixProduct, entity, targetID, isVisible)
        self._isStickyFromConfig = config.get(b'is_sticky', True)
        return

    @classmethod
    def configReader(cls, section):
        config = {b'symbol': (section.readString(b'symbol', MARKER_SYMBOL_NAME.LOCATION_MARKER)), 
           b'cull_distance': (section.readFloat(b'cull_distance', cls.CULL_DISTANCE)), 
           b'min_scale': (section.readFloat(b'min_scale', cls.MIN_SCALE)), 
           b'bounds': (section.readVector4(b'bounds', cls.BOUNDS)), 
           b'inner_bounds': (section.readVector4(b'inner_bounds', cls.INNER_BOUNDS)), 
           b'bounds_min_scale': (section.readVector2(b'bounds_min_scale', cls.BOUNDS_MIN_SCALE)), 
           b'is_sticky': (section.readBool(b'is_sticky', True)), 
           b'min_y_offset': (section.readFloat(b'min_y_offset', cls.MIN_Y_OFFSET)), 
           b'max_y_offset': (section.readFloat(b'max_y_offset', cls.MAX_Y_OFFSET)), 
           b'max_y_boost': (section.readFloat(b'max_y_boost', cls.MAX_Y_BOOST)), 
           b'distance_for_min_y_offset': (section.readFloat(b'distance_for_min_y_offset', cls.DISTANCE_FOR_MIN_Y_OFFSET)), 
           b'boost_start': (section.readFloat(b'boost_start', cls.BOOST_START))}
        return config

    @property
    def guiMarkerType(self):
        return CommonMarkerType.LOCATION

    @property
    def bcMarkerType(self):
        return MarkerType.TARGET_POINT_MARKER_TYPE

    @property
    def symbol(self):
        return self._symbol or MARKER_SYMBOL_NAME.LOCATION_MARKER

    def update(self, distance, *args, **kwargs):
        return

    def _setupMarker(self, gui, **kwargs):
        config = self._config
        isSticky = config[b'is_sticky'] & bool(self.settingsCore.getSetting(BattleCommStorageKeys.SHOW_STICKY_MARKERS))
        gui.setMarkerSticky(self._componentID, isSticky)
        gui.setMarkerRenderInfo(self._componentID, config[b'min_scale'], config[b'bounds'], config[b'inner_bounds'], config[b'cull_distance'], config[b'bounds_min_scale'])
        gui.setMarkerLocationOffset(self._componentID, config[b'min_y_offset'], config[b'max_y_offset'], config[b'distance_for_min_y_offset'], config[b'max_y_boost'], config[b'boost_start'])
        return

    def _onSettingsChanged(self, diff):
        gui = self._gui()
        if not gui:
            return
        addSettings = {}
        for item in diff:
            if item in (BattleCommStorageKeys.SHOW_STICKY_MARKERS,):
                addSettings[item] = diff[item]

        if not addSettings:
            return
        newIsSticky = bool(addSettings.get(BattleCommStorageKeys.SHOW_STICKY_MARKERS, self._isStickyFromConfig))
        gui.setMarkerSticky(self.componentID, newIsSticky & self._isStickyFromConfig)
        return


class BaseMinimapMarkerComponent(_IMarkerComponentBase):

    def __init__(self, config, matrixProduct, entity=None, targetID=INVALID_TARGET_ID, isVisible=True):
        super(BaseMinimapMarkerComponent, self).__init__(config, matrixProduct, entity, targetID, isVisible)
        self._gui = lambda : None
        self._isMarkerExists = False
        self._onlyTranslation = self._config.get(b'onlyTranslation', False)
        self._translationOnlyMP = Math.WGTranslationOnlyMP()
        self._translationOnlyMP.source = self._matrixProduct.a
        return

    @classmethod
    def configReader(cls, section):
        config = {b'symbol': (section.readString(b'symbol', b'ArtyMarkerMinimapEntry')), 
           b'container': (section.readString(b'container', b'personal')), 
           b'onlyTranslation': (section.readBool(b'onlyTranslation', False))}
        return config

    @property
    def maskType(self):
        raise NotImplementedError
        return

    def attachGUI(self, guiProvider, **kwargs):
        self._gui = weakref.ref(self._getPlugin(guiProvider))
        self._createMarker(**kwargs)
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
            gui = self._gui()
            if gui is None:
                return
            gui.setActive(self._componentID, self._isVisible)
            return

    def _createMarker(self, **kwargs):
        gui = self._gui()
        if gui and not self._isMarkerExists:
            matrix = self._translationOnlyMP if self._onlyTranslation else self._matrixProduct.a
            self._isMarkerExists = gui.createMarker(self._componentID, self._config[b'symbol'], self._config[b'container'], matrix=matrix, active=self._isVisible)
            if self._isMarkerExists:
                self._setupMarker(gui, **kwargs)
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
        super(BaseMinimapMarkerComponent, self).setMarkerMatrix(matrix)
        self._translationOnlyMP.source = self._matrixProduct.a
        gui = self._gui()
        if gui and self._isMarkerExists:
            mtx = self._translationOnlyMP if self._onlyTranslation else self._matrixProduct.a
            gui.setMatrix(self._componentID, mtx)
        return

    def _getPlugin(self, guiProvider):
        if self.maskType == ComponentBitMask.FULLSCREEN_MAP_MARKER:
            return guiProvider.getFullscreenMapPlugin()
        return guiProvider.getMinimapPlugin()

    def _setupMarker(self, gui, **kwargs):
        return


class MinimapMarkerComponent(BaseMinimapMarkerComponent):

    @property
    def maskType(self):
        return ComponentBitMask.MINIMAP_MARKER


class FullscreenMapComponent(BaseMinimapMarkerComponent):

    @property
    def maskType(self):
        return ComponentBitMask.FULLSCREEN_MAP_MARKER


class DirectionIndicatorMarkerComponent(_IMarkerComponentBase):
    _DIRECT_INDICATOR_SWF = SWF
    _DIRECT_INDICATOR_MC_NAME = MC_NAME

    def __init__(self, config, matrixProduct, entity=None, targetID=INVALID_TARGET_ID, isVisible=True):
        super(DirectionIndicatorMarkerComponent, self).__init__(config, matrixProduct, entity, targetID, isVisible)
        self.__shapes = self._config[b'dIndicatorShapes']
        self.__indicator = None
        self.__prevPosition = self.positionWithOffset
        self.__swf = self._config[b'swf']
        self.__mcName = self._config[b'mcName']
        return

    @classmethod
    def configReader(cls, section):
        config = {b'dIndicatorShapes': (
                               section.readString(b'dIndicatorShapes/default', b'green'),
                               section.readString(b'dIndicatorShapes/colorBlind', b'green')), 
           b'swf': (section.readString(b'swf', cls._DIRECT_INDICATOR_SWF)), 
           b'mcName': (section.readString(b'mcName', cls._DIRECT_INDICATOR_MC_NAME))}
        return config

    @property
    def maskType(self):
        return ComponentBitMask.DIRECTION_INDICATOR

    def attachGUI(self, _, **kwargs):
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

    def __init__(self, config, matrixProduct, entity=None, targetID=INVALID_TARGET_ID, isVisible=True):
        super(AnimationSequenceMarkerComponent, self).__init__(config, matrixProduct, entity, targetID, isVisible)
        self.__path = self._config[b'path']
        self.__animator = None
        self.__spaceID = BigWorld.player().spaceID
        if self.__path is not None:
            loader = AnimationSequence.Loader(self.__path, self.__spaceID)
            BigWorld.loadResourceListBG((loader,), makeCallbackWeak(self.__onSequenceLoaded))
        return

    @classmethod
    def configReader(cls, section):
        config = {b'path': (section.readString(b'path'))}
        return config

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
    DEF_COLOR = CombatSelectedArea.COLOR_WHITE

    def __init__(self, config, matrixProduct, entity=None, targetID=INVALID_TARGET_ID, isVisible=True):
        super(TerrainMarkerComponent, self).__init__(config, matrixProduct, entity, targetID, isVisible)
        self.__area = CombatSelectedArea.CombatSelectedArea()
        self.__direction = self._config[b'direction']
        self.__objDirection = self._config[b'objDirection']
        path = self._config[b'path']
        size = self._config[b'size']
        color = self._config[b'color']
        direction = Math.Matrix(self._matrixProduct.a).applyToAxis(2) if self.__objDirection else self.__direction
        self.__area.setup(self.position, direction, size, path, color, None)
        self.__area.setGUIVisible(self._isVisible)
        self.__area.enableWaterCollision(self._config[b'enableWaterCollision'])
        self.__area.enableAccurateCollision(self._config[b'enableAccurateCollision'])
        self.__prevPosition = self.position
        return

    @classmethod
    def configReader(cls, section):
        config = {b'path': (section.readString(b'path')), 
           b'size': (section.readVector2(b'size', cls.DEF_SIZE)), 
           b'direction': (section.readVector3(b'direction', cls.DEF_DIRECTION)), 
           b'objDirection': (section.readBool(b'objDirection', True)), 
           b'color': (int(section.readString(b'color', b'0'), 16) or cls.DEF_COLOR), 
           b'enableWaterCollision': (section.readBool(b'enableWaterCollision', False)), 
           b'enableAccurateCollision': (section.readBool(b'enableAccurateCollision', True))}
        return config

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

    def __init__(self, config, matrixProduct, entity=None, targetID=INVALID_TARGET_ID, isVisible=True):
        super(PolygonalZoneMinimapMarkerComponent, self).__init__(config, matrixProduct, entity, targetID, isVisible)
        self._polygon = None
        self._isBorderVisible = False
        self._maskingPolygons = []
        self._properties = config[b'color']
        return

    @classmethod
    def configReader(cls, section):
        config = super(PolygonalZoneMinimapMarkerComponent, cls).configReader(section)
        colorSection = section[b'color']
        color = {}
        for colorType in (b'default', b'colorBlind'):
            colorTypeSection = colorSection[colorType]
            color.update({colorType: {b'fillColor': (int(colorTypeSection.readString(b'fillColor', b'0'), 16)), 
                           b'fillAlpha': (colorTypeSection.readFloat(b'fillAlpha')), 
                           b'fillBlendMode': (colorTypeSection.readString(b'fillBlendMode', Blending.NORMAL)), 
                           b'outlineColor': (int(colorTypeSection.readString(b'outlineColor', b'0'), 16)), 
                           b'outlineAlpha': (colorTypeSection.readFloat(b'outlineAlpha')), 
                           b'outlineBlendMode': (colorTypeSection.readString(b'outlineBlendMode', Blending.NORMAL)), 
                           b'lineThickness': (colorTypeSection.readFloat(b'lineThickness')), 
                           b'useGradient': (colorTypeSection.readBool(b'useGradient', False)), 
                           b'gradientColor': (int(colorTypeSection.readString(b'gradientColor', b'0'), 16)), 
                           b'gradientAlpha': (colorTypeSection.readFloat(b'gradientAlpha', 1.0))}})

        config.update({b'color': color})
        return config

    @property
    def isVisible(self):
        return self._entity.entityPolygonalTrigger.isActive and self._entity.clientVisualComp.isVisible

    def getPolygon(self):
        udo = BigWorld.userDataObjects.get(self._entity.clientVisualComp.udoGuid, None)
        if udo is None:
            return []
        else:
            return udo.minimapMarkerPolygon

    def _setupMarker(self, gui, **kwargs):
        self.settingsCore.onSettingsChanged += self.__onSettingsChanged
        self._entity.onMaskAdded += self._addMask
        self._initPolygon()
        if self._polygon:
            self._updatePolygon()
        return

    def detachGUI(self):
        super(PolygonalZoneMinimapMarkerComponent, self).detachGUI()
        self._polygon = None
        self.settingsCore.onSettingsChanged -= self.__onSettingsChanged
        self._entity.onMaskAdded -= self._addMask
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
        gui.setActive(self._componentID, self._isBorderVisible and self._isVisible)
        return

    def setVisible(self, isVisible):
        if self._isVisible == isVisible:
            return
        else:
            self._isVisible = isVisible
            gui = self._gui()
            if gui is None:
                return
            gui.setActive(self._componentID, self._isBorderVisible and self._isVisible)
            return

    def _addMask(self, guid):
        xc, yc = self._getSize()
        udo = BigWorld.userDataObjects.get(guid, None)
        if udo:
            delta = udo.position - self.position
            polygon = sum(([(p[0] + delta[0]) * xc, (p[1] - delta[2]) * yc] for p in udo.minimapMarkerPolygon), [])
            self._gui().invoke(self._componentID, b'addZoneData', polygon)
        return

    def _initPolygon(self):
        polygon = self.getPolygon()
        if not polygon:
            return
        else:
            xc, yc = self._getSize()
            self._polygon = sum(([p[0] * xc, p[1] * yc] for p in polygon), [])
            for mask in self._entity.masks:
                udo = BigWorld.userDataObjects.get(mask.udoGuid, None)
                if udo:
                    delta = udo.position - self.position
                    self._maskingPolygons.append(sum(([(p[0] + delta[0]) * xc, (p[1] - delta[2]) * yc] for p in udo.minimapMarkerPolygon), []))

            return

    def _getSize(self):
        boundingBox = BigWorld.player().arena.arenaType.boundingBox
        arenaSize = boundingBox[1] - boundingBox[0]
        xc = minimap_utils.MINIMAP_SIZE[0] / arenaSize[0] * 2
        yc = minimap_utils.MINIMAP_SIZE[1] / arenaSize[1] * 2
        return (xc, yc)

    def _updatePolygon(self):
        self._gui().invoke(self._componentID, b'setProperties', *self.__getMarkerProperties(self.__isColorBlind()))
        self._gui().invoke(self._componentID, b'addZoneData', self._polygon)
        self._gui().setActive(self._componentID, self._isBorderVisible and self._isVisible)
        for polygon in self._maskingPolygons:
            self._gui().invoke(self._componentID, b'addZoneData', polygon)

        return

    def _getGradientSize(self):
        dimensions = self._entity.clientVisualComp.getDimensions()
        return old_div(max(dimensions.x, dimensions.z), 2)

    def __getMarkerProperties(self, isColorBlind):
        props = (isColorBlind or self._properties)[b'default'] if 1 else self._properties[b'colorBlind']
        return (
         props[b'fillColor'], props[b'fillAlpha'],
         props[b'outlineColor'], props[b'outlineAlpha'],
         props[b'lineThickness'], props[b'fillBlendMode'],
         props[b'outlineBlendMode'], props[b'useGradient'],
         props[b'gradientColor'], props[b'gradientAlpha'],
         self._getGradientSize())

    def __isColorBlind(self):
        return self.settingsCore.getSetting(settings_constants.GRAPHICS.COLOR_BLIND)

    def __onSettingsChanged(self, diff):
        if settings_constants.GRAPHICS.COLOR_BLIND in diff:
            self._gui().invoke(self._componentID, b'setProperties', *self.__getMarkerProperties(self.__isColorBlind()))
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


class W2GTBattleZoneMinimapMarkerComponent(MinimapMarkerComponent):
    FILL_COLOR = b'0xffdd99'
    FILL_ALPHA = 0.5
    OUTLINE_THICKNESS = 1.0
    OUTLINE_COLOR = b'0xffdd99'
    OUTLINE_ALPHA = 1.0
    DOT_RADIUS = 1.0
    DOT_GAP = 2.0

    class OutlineStyle(object):
        SOLID = b'solid'
        DOTTED = b'dotted'

    class Colors(object):
        DEFAULT = b'color'
        BLIND = b'colorBlind'
        ALL = (
         DEFAULT, BLIND)

    class ZoneState(object):
        DEFAULT = b'default'
        ACTIVE = b'active'
        HIGHLIGHT = b'highlight'
        ALL = (
         DEFAULT, ACTIVE, HIGHLIGHT)

    def __init__(self, config, matrixProduct, entity=None, targetID=INVALID_TARGET_ID, isVisible=True):
        super(W2GTBattleZoneMinimapMarkerComponent, self).__init__(config, matrixProduct, entity, targetID, isVisible)
        self.__polygon = None
        self.__isHighlight = False
        self.__isActive = False
        self.__colorSection = None
        self.__state = None
        self.__isVisible = True
        self._properties = config[b'colors']
        self._states = config[b'states']
        return

    @property
    def bcMarkerType(self):
        return MarkerType.ZONE_MARKER_TYPE

    @classmethod
    def configReader(cls, section):
        config = super(W2GTBattleZoneMinimapMarkerComponent, cls).configReader(section)
        colors = {}
        for sectionType in cls.Colors.ALL:
            colorSection = section[sectionType]
            colors.update({sectionType: {b'fillColor': (int(colorSection.readString(b'fillColor', cls.FILL_COLOR), 16)), 
                             b'fillAlpha': (colorSection.readFloat(b'fillAlpha', cls.FILL_ALPHA)), 
                             b'fillBlendMode': (colorSection.readString(b'fillBlendMode', Blending.NORMAL)), 
                             b'outlineStyle': (colorSection.readString(b'outlineStyle', cls.OutlineStyle.SOLID)), 
                             b'outlineThickness': (colorSection.readFloat(b'outlineThickness', cls.OUTLINE_THICKNESS)), 
                             b'outlineColor': (int(colorSection.readString(b'outlineColor', cls.OUTLINE_COLOR), 16)), 
                             b'outlineAlpha': (colorSection.readFloat(b'outlineAlpha', cls.OUTLINE_ALPHA)), 
                             b'dotRadius': (colorSection.readFloat(b'dotRadius', cls.DOT_RADIUS)), 
                             b'dotGap': (colorSection.readFloat(b'dotGap', cls.DOT_GAP)), 
                             b'outlineBlendMode': (colorSection.readString(b'outlineBlendMode', Blending.NORMAL))}})

        states = {}
        statesSection = section[b'states']
        for stateType in cls.ZoneState.ALL:
            stateSection = statesSection[stateType]
            states.update({stateType: {b'fillAlpha': (stateSection.readFloat(b'fillAlpha', cls.FILL_ALPHA))}})

        config.update({b'colors': colors, 
           b'states': states})
        return config

    def highlightZone(self, isHighlight):
        if self.__isHighlight == isHighlight:
            return
        self.__isHighlight = isHighlight
        self.__updateState()
        return

    def activeZone(self, isActive):
        if self.__isActive == isActive:
            return
        self.__isActive = isActive
        self.__updateState()
        return

    def changeVisibility(self, isVisible):
        self.__isVisible = isVisible
        return

    def detachGUI(self):
        super(W2GTBattleZoneMinimapMarkerComponent, self).detachGUI()
        self.__polygon = None
        self.settingsCore.onSettingsChanged -= self.__onSettingsChanged
        return

    def setVisible(self, isVisible):
        super(W2GTBattleZoneMinimapMarkerComponent, self).setVisible(isVisible and self.__isVisible)
        return

    def _setupMarker(self, gui, polygon=None, zoneType=b'', icon=b'empty', iconX=0, iconY=0, **kwargs):
        self.settingsCore.onSettingsChanged += self.__onSettingsChanged
        state = self._states[self.ZoneState.HIGHLIGHT]
        hoverAlpha = state.get(b'fillAlpha', 0)
        self._gui().invoke(self._componentID, b'initUI', zoneType, hoverAlpha)
        self.__setIcon(icon, iconX, iconY)
        self._initPolygon(polygon)
        if self.__polygon:
            self._setupPolygon()
        self.__updateState()
        return

    def _initPolygon(self, polygon):
        if not polygon:
            return
        if not self.__isPolygonValid(polygon):
            _logger.error(b'W2GT: BattleZone has invalid polygon')
            return
        xc, yc = self._getSize()
        self.__polygon = sum(([p[0] * xc, -p[1] * yc] for p in polygon), [])
        return

    def _getSize(self):
        boundingBox = BigWorld.player().arena.arenaType.boundingBox
        arenaSize = boundingBox[1] - boundingBox[0]
        xc = minimap_utils.MINIMAP_SIZE[0] / arenaSize[0]
        yc = minimap_utils.MINIMAP_SIZE[1] / arenaSize[1]
        return (xc, yc)

    def _setupPolygon(self):
        self.__updateColorsProperties()
        self._gui().invoke(self._componentID, b'addZoneData', self.__polygon)
        self._gui().setActive(self._componentID, self._isVisible and self.__isVisible)
        return

    def __setIcon(self, icon, iconX, iconY):
        xc, yc = self._getSize()
        self._gui().invoke(self._componentID, b'setIcon', icon, iconX * xc, -iconY * yc)
        return

    def __getMarkerProperties(self, colorSection, state):
        props = self._properties[colorSection]
        state = self._states[state]
        props.update(state)
        return (
         props[b'fillColor'],
         props[b'fillAlpha'],
         props[b'fillBlendMode'],
         props[b'outlineStyle'],
         props[b'outlineThickness'],
         props[b'outlineColor'],
         props[b'outlineAlpha'],
         props[b'dotRadius'],
         props[b'dotGap'],
         props[b'outlineBlendMode'])

    def __getState(self):
        if self.__isHighlight:
            return self.ZoneState.HIGHLIGHT
        if self.__isActive:
            return self.ZoneState.ACTIVE
        return self.ZoneState.DEFAULT

    def __isColorBlind(self):
        return self.settingsCore.getSetting(settings_constants.GRAPHICS.COLOR_BLIND)

    def __updateColorsProperties(self):
        gui = self._gui()
        if gui is None:
            return
        else:
            colorSection = b'colorBlind' if self.__isColorBlind() else b'color'
            state = self.__getState()
            if self.__colorSection == colorSection and self.__state == state:
                return
            self.__colorSection = colorSection
            self.__state = state
            gui.invoke(self._componentID, b'setProperties', *self.__getMarkerProperties(colorSection, state))
            return

    def __updateState(self):
        gui = self._gui()
        if gui is None:
            return
        else:
            stateType = self.__getState()
            state = self._states[stateType]
            gui.invoke(self._componentID, b'setState', state[b'fillAlpha'])
            return

    def __onSettingsChanged(self, diff):
        if settings_constants.GRAPHICS.COLOR_BLIND in diff:
            self.__updateColorsProperties()
        return

    def __isPolygonValid(self, polygon):
        return all(len(p) == 2 for p in polygon)
