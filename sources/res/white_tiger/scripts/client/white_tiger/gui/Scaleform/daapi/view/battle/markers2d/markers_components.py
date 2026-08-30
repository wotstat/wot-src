from __future__ import absolute_import
import Math
from chat_commands_consts import INVALID_TARGET_ID
from gui.Scaleform.daapi.view.battle.shared.component_marker.markers_components import MinimapMarkerComponent, World2DActionMarkerComponent
from helpers import dependency
from skeletons.gui.battle_session import IBattleSessionProvider
from aih_constants import MAP_CASE_MODES
import BigWorld
from gui.Scaleform.daapi.view.battle.shared.markers2d.settings import CommonMarkerType
from white_tiger.skeletons.white_tiger_generator_marker import IGeneratorMarker
from account_helpers.settings_core import ISettingsCore, settings_constants

class World2DLocationMarkerComponent(World2DActionMarkerComponent):
    _CULL_DISTANCE = 1800
    _MIN_SCALE = 50.0
    _BOUNDS = Math.Vector4(30, 30, 90, -15)
    _INNER_BOUNDS = Math.Vector4(15, 15, 70, -35)
    _BOUNDS_MIN_SCALE = Math.Vector2(1.0, 0.8)
    _MIN_DISTANCE = 18
    _MAX_CAPTURE_PROGRESS = 100

    def __init__(self, config, matrixProduct, entity=None, targetID=INVALID_TARGET_ID, isVisible=True):
        super(World2DLocationMarkerComponent, self).__init__(config, matrixProduct, entity, targetID, isVisible)
        self._minDistance = self._MIN_DISTANCE
        self._config = config
        self._distance = self._config.get(b'distance', 0)
        self._isSticky = self._config.get(b'is_sticky', False)
        self._inputHandler = BigWorld.player().inputHandler
        return

    @classmethod
    def configReader(cls, section):
        config = super(World2DLocationMarkerComponent, cls).configReader(section)
        colorSection = section[b'color']
        color = {}
        colorTypeSection = colorSection[b'default']
        color.update({b'default': {b'fillAlpha': (colorTypeSection.readFloat(b'fillAlpha'))}})
        config.update({b'color': color})
        return config

    @property
    def guiMarkerType(self):
        return CommonMarkerType.LOCATION

    def update(self, distance, *args, **kwargs):
        super(World2DLocationMarkerComponent, self).update(distance)
        if self._distance != distance:
            self._distance = distance
        self.setVisible(self._getActualVisibility())
        return

    def _getActualVisibility(self):
        return self._inputHandler.ctrlModeName in MAP_CASE_MODES or self._distance >= self._minDistance


class World2DIndexedMarkerComponent(World2DLocationMarkerComponent):
    _DEFAULT_ALPHA = 1.0
    sessionProvider = dependency.descriptor(IBattleSessionProvider)
    settingsCore = dependency.descriptor(ISettingsCore)

    def __init__(self, config, matrixProduct, entity=None, targetID=INVALID_TARGET_ID, isVisible=True):
        super(World2DIndexedMarkerComponent, self).__init__(config, matrixProduct, entity, targetID, isVisible)
        self._isFirstShow = True
        return

    def _createMarker(self, **kwargs):
        super(World2DIndexedMarkerComponent, self)._createMarker(**kwargs)
        gui = self._gui()
        if gui:
            alpha = self.getAlpha()
            gui.mapCustomEntityID(self._componentID, self._entityIndex)
            gui.invokeMarker(self._componentID, b'setEntityIndex', self._entityIndex)
            gui.invokeMarker(self._componentID, b'setIsColorBlind', self.settingsCore.getSetting(b'isColorBlind'))
            gui.invokeMarker(self._componentID, b'setAlpha', alpha)
            gui.setMarkerSticky(self._componentID, self._isSticky)
            minScale = self._config.get(b'min_scale', self._MIN_SCALE)
            gui.setMarkerRenderInfo(self._componentID, minScale, self._BOUNDS, self._INNER_BOUNDS, self._CULL_DISTANCE, self._BOUNDS_MIN_SCALE)
            gui.setMarkerBoundEnabled(self._componentID, True)
            ctrl = self.sessionProvider.shared.feedback
            if ctrl is not None:
                ctrl.onAddCommandReceived += self.__onAddCommandReceived
        return

    def _deleteMarker(self):
        gui = self._gui()
        if gui:
            gui.deleteCustomEntityID(self._componentID)
        ctrl = self.sessionProvider.shared.feedback
        if ctrl is not None:
            ctrl.onAddCommandReceived -= self.__onAddCommandReceived
        super(World2DIndexedMarkerComponent, self)._deleteMarker()
        return

    @property
    def _entityIndex(self):
        if self._entity and b'indexPool' in self._entity.dynamicComponents:
            return self._entity.indexPool.index
        return 0

    def getAlpha(self):
        return self._config[b'color'][b'default'][b'fillAlpha']

    def __onAddCommandReceived(self, addedID, markerType):
        gui = self._gui()
        if gui:
            markerID = gui.getMarkerIdFormEntityID(addedID)
            if markerID == self._componentID:
                gui.invokeMarker(markerID, b'playAnimation')
        return

    def _onSettingsChanged(self, diff):
        super(World2DIndexedMarkerComponent, self)._onSettingsChanged(diff)
        if settings_constants.GRAPHICS.COLOR_BLIND in diff:
            gui = self._gui()
            if gui:
                gui.invokeMarker(self._componentID, b'setIsColorBlind', self.settingsCore.getSetting(b'isColorBlind'))
        return


class World2DGeneratorMarkerComponentOn(World2DIndexedMarkerComponent, IGeneratorMarker):

    def __init__(self, config, matrixProduct, entity=None, targetID=INVALID_TARGET_ID, isVisible=True):
        super(World2DGeneratorMarkerComponentOn, self).__init__(config, matrixProduct, entity, targetID, isVisible)
        self.__lastProgressValue = 0
        self.__isLocked = False
        return

    def _createMarker(self, **kwargs):
        super(World2DGeneratorMarkerComponentOn, self)._createMarker(**kwargs)
        gui = self._gui()
        if gui and self.__lastProgressValue > 0:
            gui.invokeMarker(self._componentID, b'setMarkerProgress', self.__lastProgressValue)
        self.onGeneratorLocked(self._entityIndex, self.__isLocked)
        return

    def onGeneratorCapture(self, generatorIndex, progress, timeLeft, numInvaders):
        gui = self._gui()
        if gui and generatorIndex == self._entityIndex:
            gui.invokeMarker(self._componentID, b'setMarkerProgress', progress)
            self.__lastProgressValue = progress
        return

    def onGeneratorStopCapture(self, generatorIndex):
        gui = self._gui()
        if gui and generatorIndex == self._entityIndex:
            gui.invokeMarker(self._componentID, b'resetGeneratorMarker')
            self.__lastProgressValue = 0
            if self.__isLocked:
                gui.invokeMarker(self._componentID, b'lockGeneratorMarker', self.__isLocked)
        return

    def onGeneratorLocked(self, generatorID, isLocked):
        if generatorID != self._entityIndex:
            return
        self.__isLocked = isLocked
        gui = self._gui()
        if gui:
            gui.invokeMarker(self._componentID, b'lockGeneratorMarker', isLocked)
        return


class World2DGeneratorMarkerComponentOff(World2DIndexedMarkerComponent, IGeneratorMarker):

    def _createMarker(self, **kwargs):
        super(World2DGeneratorMarkerComponentOff, self)._createMarker(**kwargs)
        gui = self._gui()
        if gui:
            alpha = self.getAlpha()
            gui.invokeMarker(self._componentID, b'setAlpha', alpha)
        return


class MinimapIndexedMarkerComponent(MinimapMarkerComponent):
    _DEFAULT_ALPHA = 0.5
    sessionProvider = dependency.descriptor(IBattleSessionProvider)
    settingsCore = dependency.descriptor(ISettingsCore)

    def __init__(self, config, matrixProduct, entity=None, targetID=INVALID_TARGET_ID, isVisible=True):
        super(MinimapIndexedMarkerComponent, self).__init__(config, matrixProduct, entity, targetID, isVisible)
        self._minimapData = config
        return

    @classmethod
    def configReader(cls, section):
        config = super(MinimapIndexedMarkerComponent, cls).configReader(section)
        colorSection = section[b'color']
        color = {}
        colorTypeSection = colorSection[b'default']
        color.update({b'default': {b'fillAlpha': (colorTypeSection.readFloat(b'fillAlpha'))}})
        config.update({b'color': color})
        return config

    @property
    def _entityIndex(self):
        if self._entity and b'indexPool' in self._entity.dynamicComponents:
            return self._entity.indexPool.index
        return 0

    def _createMarker(self, **kwargs):
        super(MinimapIndexedMarkerComponent, self)._createMarker(**kwargs)
        gui = self._gui()
        if gui:
            alpha = self.getAlpha()
            gui.mapCustomEntityID(self._componentID, self._entityIndex)
            gui.invoke(self._componentID, b'setEntityIndex', self._entityIndex)
            gui.invoke(self._componentID, b'setIsColorBlind', self.settingsCore.getSetting(b'isColorBlind'))
            gui.invoke(self._componentID, b'setAlpha', alpha)
            gui.invoke(self._componentID, b'setGeneratorProgress', 0)
        ctrl = self.sessionProvider.shared.feedback
        if ctrl is not None:
            ctrl.onAddCommandReceived += self.__onAddCommandReceived
        return

    def _deleteMarker(self):
        gui = self._gui()
        if gui:
            gui.deleteCustomEntityID(self._componentID)
        ctrl = self.sessionProvider.shared.feedback
        if ctrl is not None:
            ctrl.onAddCommandReceived -= self.__onAddCommandReceived
        super(MinimapIndexedMarkerComponent, self)._deleteMarker()
        return

    def attachGUI(self, guiProvider, **kwargs):
        self.settingsCore.onSettingsChanged += self.__onSettingsChanged
        super(MinimapIndexedMarkerComponent, self).attachGUI(guiProvider, **kwargs)
        return

    def detachGUI(self):
        self.settingsCore.onSettingsChanged -= self.__onSettingsChanged
        super(MinimapIndexedMarkerComponent, self).detachGUI()
        return

    def getAlpha(self):
        return self._config[b'color'][b'default'][b'fillAlpha']

    def __onAddCommandReceived(self, addedID, markerType):
        gui = self._gui()
        if gui:
            markerID = gui.getMarkerIdFormEntityID(addedID)
            if markerID == self._componentID:
                gui.invoke(markerID, b'playAnimation')
        return

    def __onSettingsChanged(self, diff):
        if settings_constants.GRAPHICS.COLOR_BLIND in diff:
            gui = self._gui()
            if gui:
                gui.invoke(self._componentID, b'setIsColorBlind', self.settingsCore.getSetting(b'isColorBlind'))
        return


class MinimapGeneratorMarkerComponentOn(MinimapIndexedMarkerComponent, IGeneratorMarker):

    def __init__(self, config, matrixProduct, entity=None, targetID=INVALID_TARGET_ID, isVisible=True):
        super(MinimapGeneratorMarkerComponentOn, self).__init__(config, matrixProduct, entity, targetID, isVisible)
        self.__isLocked = False
        return

    def _createMarker(self, **kwargs):
        super(MinimapGeneratorMarkerComponentOn, self)._createMarker(**kwargs)
        self.onGeneratorLocked(self._entityIndex, self.__isLocked)
        return

    def onGeneratorCapture(self, generatorIndex, progress, timeLeft, numInvaders):
        gui = self._gui()
        if gui:
            if generatorIndex == self._entityIndex:
                gui.invoke(self._componentID, b'setGeneratorProgress', progress)
        return

    def onGeneratorStopCapture(self, generatorIndex):
        gui = self._gui()
        if gui:
            gui.invoke(self._componentID, b'resetGeneratorMarker')
        return

    def onGeneratorLocked(self, generatorID, isLocked):
        if generatorID != self._entityIndex:
            return
        self.__isLocked = isLocked
        gui = self._gui()
        if gui:
            gui.invoke(self._componentID, b'lockGeneratorMarker', isLocked)
        return


class MinimapGeneratorMarkerComponentOff(MinimapIndexedMarkerComponent, IGeneratorMarker):

    def _createMarker(self, **kwargs):
        super(MinimapGeneratorMarkerComponentOff, self)._createMarker(**kwargs)
        gui = self._gui()
        if gui:
            alpha = self.getAlpha()
            gui.invoke(self._componentID, b'setAlpha', alpha)
        return
