import sys, BigWorld, ResMgr
from constants import Configs
from helpers import dependency
from helpers.events_handler import EventsHandler
from helpers.server_settings import ServerSettings
from skeletons.gui.game_control import IControlPointOverrideController
from skeletons.gui.lobby_context import ILobbyContext
from SectorBase import resetSectorSettings
from PlayerEvents import g_playerEvents
from soft_exception import SoftException

class ControlPointOverrideController(IControlPointOverrideController, EventsHandler):
    _lobbyContext = dependency.descriptor(ILobbyContext)

    def __init__(self):
        super(ControlPointOverrideController, self).__init__()
        self._hasListeners = False
        g_playerEvents.onAvatarBecomePlayer += self._onAvatarBecomePlayer
        return

    def _getEvents(self):
        return (
         (
          self._lobbyContext.onServerSettingsChanged, self._onServerSettingsChanged),
         (
          self._lobbyContext.getServerSettings().onServerSettingsChange, self._onServerSettingsChange))

    def onLobbyInited(self, event):
        super(ControlPointOverrideController, self).onLobbyInited(event)
        if not self._hasListeners:
            self._subscribe()
            self._hasListeners = True
            self._applySettings()
            g_playerEvents.onAvatarBecomePlayer -= self._onAvatarBecomePlayer
        return

    def fini(self):
        self._unsubscribe()
        self._hasListeners = False
        g_playerEvents.onAvatarBecomePlayer -= self._onAvatarBecomePlayer
        super(ControlPointOverrideController, self).fini()
        return

    def _onServerSettingsChanged(self, newServerSettings):
        newServerSettings.onServerSettingsChange += self._onServerSettingsChange
        self._applySettings()
        return

    def _onServerSettingsChange(self, diff):
        if Configs.CONTROL_POINT_OVERRIDE_CONFIG.value in diff:
            self._applySettings()
        return

    def _onAvatarBecomePlayer(self):
        g_playerEvents.onAvatarBecomePlayer -= self._onAvatarBecomePlayer
        self._applySettings()
        return

    def _applySettings(self):
        config = self._lobbyContext.getServerSettings().controlPointConfig
        flagPath = b''
        flagstaffPath = b''
        flagSound = b''
        effectPrefab = b''
        isEnabled = config.isEnabled
        if isEnabled:
            flagPath = config.flagPath if ResMgr.isFile(config.flagPath) else b''
            flagstaffPath = config.flagstaffPath if ResMgr.isFile(config.flagstaffPath) else b''
            flagSound = config.wweventName if flagPath and flagstaffPath else b''
            effectPrefab = config.effectPrefab if ResMgr.isFile(config.effectPrefab) else b''
        resetSectorSettings()
        BigWorld.setFlagOverrides(flagPath, flagstaffPath, flagSound, effectPrefab)
        if isEnabled:
            self.__validateFiles(config)
        return

    def __validateFiles(self, config):
        invalidFiles = []

        def checkIsValidFilePath(filePath):
            return filePath == b'' or filePath and ResMgr.isFile(filePath)

        flagPath = config.flagPath
        flagstaffPath = config.flagstaffPath
        effectPrefab = config.effectPrefab
        if not checkIsValidFilePath(flagPath):
            invalidFiles.append(flagPath)
        if not checkIsValidFilePath(flagstaffPath):
            invalidFiles.append(flagstaffPath)
        if not checkIsValidFilePath(effectPrefab):
            invalidFiles.append(effectPrefab)
        if invalidFiles:
            errorMsg = b'"Invalid file paths %s"' % (b', ').join(invalidFiles)
            try:
                raise SoftException(errorMsg)
            except SoftException:
                BigWorld.catReportException(sys.exc_info())

        return
