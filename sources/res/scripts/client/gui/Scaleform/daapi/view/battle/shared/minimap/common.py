from __future__ import absolute_import
import typing
from functools import partial
import BigWorld
from aih_constants import CTRL_MODE_NAME
from AvatarInputHandler import AvatarInputHandler
from gui.battle_control import avatar_getter
from gui.Scaleform.daapi.view.battle.shared.minimap import entries, settings
from gui.shared.utils.plugins import IPlugin, PluginsCollection
from helpers import dependency
from skeletons.account_helpers.settings_core import ISettingsCore
from skeletons.gui.battle_session import IBattleSessionProvider
if typing.TYPE_CHECKING:
    import Math
    from account_helpers.settings_core.settings_constants import GAME

class SimplePlugin(IPlugin):
    __slots__ = (b'__weakref__', b'_arenaVisitor', b'_arenaDP', b'_ctrlMode', b'_ctrlVehicleID')
    sessionProvider = dependency.descriptor(IBattleSessionProvider)
    settingsCore = dependency.descriptor(ISettingsCore)

    def __init__(self, parent):
        super(SimplePlugin, self).__init__(parent)
        self._arenaVisitor = None
        self._arenaDP = None
        self._ctrlMode = CTRL_MODE_NAME.ARCADE
        self._ctrlVehicleID = 0
        return

    def init(self, arenaVisitor, arenaDP):
        super(SimplePlugin, self).init()
        self._arenaVisitor = arenaVisitor
        self._arenaDP = arenaDP
        return

    def fini(self):
        self._arenaVisitor = None
        self._arenaDP = None
        super(SimplePlugin, self).fini()
        return

    def initControlMode(self, mode, available):
        self._ctrlMode = mode
        return

    def updateControlMode(self, mode, vehicleID):
        self._ctrlMode = mode
        self._ctrlVehicleID = vehicleID
        return

    def setSettings(self):
        return

    def updateSettings(self, diff):
        return

    def onMinimapClicked(self, x, y, buttonIdx, minimapScaleIndex):
        return

    def applyNewSize(self, sizeIndex):
        return

    def _addEntry(self, symbol, container, matrix=None, active=False, transformProps=settings.TRANSFORM_FLAG.DEFAULT):
        return self._parentObj.addEntry(symbol, container, matrix=matrix, active=active, transformProps=transformProps)

    def _delEntry(self, entryID):
        self._parentObj.delEntry(entryID)
        return

    def _invoke(self, entryID, name, *args):
        self._parentObj.invoke(entryID, name, *args)
        return

    def _move(self, entryID, container):
        self._parentObj.move(entryID, container)
        return

    def _setMatrix(self, entryID, matrix):
        self._parentObj.setMatrix(entryID, matrix)
        return

    def _setActive(self, entryID, active):
        self._parentObj.setActive(entryID, active)
        return

    def _playSound2D(self, soundID):
        self._parentObj.playSound2D(soundID)
        return

    def _isInStrategicMode(self):
        return self._ctrlMode in (CTRL_MODE_NAME.STRATEGIC, CTRL_MODE_NAME.ARTY, CTRL_MODE_NAME.MAP_CASE,
         CTRL_MODE_NAME.MAP_CASE_EPIC)

    def _isInArcadeMode(self):
        return self._ctrlMode in (CTRL_MODE_NAME.ARCADE, CTRL_MODE_NAME.SNIPER)

    def _isInArtyMode(self):
        return self._ctrlMode == CTRL_MODE_NAME.ARTY

    def _isInPostmortemMode(self):
        return self._ctrlMode == CTRL_MODE_NAME.POSTMORTEM

    def _isInVideoMode(self):
        return self._ctrlMode in (CTRL_MODE_NAME.VIDEO, CTRL_MODE_NAME.DEATH_FREE_CAM)

    def _isInFreeCamMode(self):
        return self._ctrlMode in CTRL_MODE_NAME.DEATH_FREE_CAM

    def _isInRespawnDeath(self):
        return self._ctrlMode == CTRL_MODE_NAME.RESPAWN_DEATH

    def _isVehicleSelection(self):
        return self._ctrlMode == CTRL_MODE_NAME.VEHICLES_SELECTION


class EntriesPlugin(SimplePlugin):
    __slots__ = (b'_entries', b'_clazz')

    def __init__(self, parent, clazz=None):
        super(EntriesPlugin, self).__init__(parent)
        self._entries = {}
        self._clazz = clazz or entries.MinimapEntry
        return

    def stop(self):
        while self._entries:
            _, model = self._entries.popitem()
            model.clear()

        super(EntriesPlugin, self).stop()
        return

    def _addEntryEx(self, uniqueID, symbol, container, matrix=None, active=False, transformProps=settings.TRANSFORM_FLAG.DEFAULT):
        if uniqueID in self._entries:
            return self._entries[uniqueID]
        else:
            entryID = self._addEntry(symbol, container, matrix=matrix, active=active, transformProps=transformProps)
            if entryID:
                model = self._clazz(entryID, active, matrix)
                self._entries[uniqueID] = model
            else:
                model = None
            return model

    def _delEntryEx(self, uniqueID):
        if uniqueID not in self._entries:
            return False
        model = self._entries.pop(uniqueID)
        self._delEntry(model.getID())
        model.clear()
        return True

    def _setMatrixEx(self, uniqueID, matrix):
        model = self._entries.get(uniqueID, None)
        if model:
            self._setMatrix(model.getID(), matrix)
        return

    def _invokeEx(self, uniqueID, name, *args):
        model = self._entries.get(uniqueID)
        if model:
            self._invoke(model.getID(), name, *args)
        return

    def _setActiveEx(self, uniqueID, isActive):
        model = self._entries.get(uniqueID)
        if model:
            self._setActive(model.getID(), isActive)
        return


class IntervalPlugin(EntriesPlugin):
    __slots__ = (b'__callbackIDs',)

    def __init__(self, parent):
        super(IntervalPlugin, self).__init__(parent)
        self.__callbackIDs = {}
        return

    def stop(self):
        while self.__callbackIDs:
            _, callbackID = self.__callbackIDs.popitem()
            if callbackID is not None:
                BigWorld.cancelCallback(callbackID)

        super(IntervalPlugin, self).stop()
        return

    def _clearCallback(self, uniqueID):
        callbackID = self.__callbackIDs.pop(uniqueID, None)
        if callbackID is not None:
            BigWorld.cancelCallback(callbackID)
        return

    def _setCallback(self, uniqueID, interval):
        self._clearCallback(uniqueID)
        self.__callbackIDs[uniqueID] = BigWorld.callback(interval, partial(self._handleCallback, uniqueID))
        return

    def _handleCallback(self, uniqueID):
        self.__callbackIDs[uniqueID] = None
        self._delEntryEx(uniqueID)
        return

    def _isCallbackExisting(self, uniqueID):
        if uniqueID in self.__callbackIDs:
            return self.__callbackIDs[uniqueID] is not None
        else:
            return False

    def _clearAllCallbacks(self):
        for key in self.__callbackIDs:
            self._delEntryEx(key)

        self.__callbackIDs.clear()
        return

    def _killOtherCallbacks(self, uniqueID):
        toKill = []
        for key in self.__callbackIDs:
            if key != uniqueID:
                self._delEntryEx(key)
                self.__callbackIDs[key] = None
                toKill.append(key)

        for key in toKill:
            del self.__callbackIDs[key]

        return


class BaseAreaMarkerEntriesPlugin(EntriesPlugin):
    __slots__ = ()

    def createMarker(self, uniqueID, symbol, container, matrix, active):
        model = self._addEntryEx(uniqueID, symbol, container, matrix=matrix, active=active)
        if model is not None:
            return True
        else:
            return False

    def deleteMarker(self, uniqueID):
        self._delEntryEx(uniqueID)
        return

    def setMatrix(self, uniqueID, matrix):
        self._setMatrixEx(uniqueID, matrix)
        return

    def update(self, *args, **kwargs):
        super(BaseAreaMarkerEntriesPlugin, self).update()
        return

    def invoke(self, uniqueID, name, *args):
        self._invokeEx(uniqueID, name, *args)
        return

    def setActive(self, uniqueID, isActive):
        self._setActiveEx(uniqueID, isActive)
        return


class MinimapPluginsCollection(PluginsCollection):
    settingsCore = dependency.descriptor(ISettingsCore)

    def start(self):
        super(MinimapPluginsCollection, self).start()
        handler = avatar_getter.getInputHandler()
        if handler is not None:
            if isinstance(handler, AvatarInputHandler):
                handler.onCameraChanged += self.__onCameraChanged
            self._invoke(b'initControlMode', handler.ctrlModeName, handler.ctrls.keys())
        self.settingsCore.onSettingsChanged += self.__onSettingsChanged
        self._invoke(b'setSettings')
        return

    def stop(self):
        handler = avatar_getter.getInputHandler()
        if handler is not None and isinstance(handler, AvatarInputHandler):
            handler.onCameraChanged -= self.__onCameraChanged
        self.settingsCore.onSettingsChanged -= self.__onSettingsChanged
        super(MinimapPluginsCollection, self).stop()
        return

    def onMinimapClicked(self, x, y, buttonIdx, minimapScaleIndex):
        self._invoke(b'onMinimapClicked', x, y, buttonIdx, minimapScaleIndex)
        return

    def applyNewSize(self, sizeIndex):
        self._invoke(b'applyNewSize', sizeIndex)
        return

    def updateControlMode(self, mode, vehicleID):
        self._invoke(b'updateControlMode', mode, vehicleID)
        return

    def initControlMode(self, mode, available):
        self._invoke(b'initControlMode', mode, available)
        return

    def updateSettings(self, diff):
        self._invoke(b'updateSettings', diff)
        return

    def setSettings(self):
        self._invoke(b'setSettings')
        return

    def __onSettingsChanged(self, diff):
        self._invoke(b'updateSettings', diff)
        return

    def __onCameraChanged(self, mode, vehicleID=0):
        self._invoke(b'updateControlMode', mode, vehicleID)
        return
