from Event import Event
from adisp import adisp_async
from gui.ClientUpdateManager import g_clientUpdateManager
from gui.shared.utils.requesters.IntSettingsRequester import IntSettingsRequester
from account_helpers.settings_core.settings_constants import VERSION
from skeletons.account_helpers.settings_core import ISettingsCache

class SettingsCache(ISettingsCache):

    def __init__(self):
        self.__intSettings = IntSettingsRequester()
        self.__waitForSync = False
        self.onSyncStarted = Event()
        self.onSyncCompleted = Event()
        return

    def isSynced(self):
        return not self.__waitForSync and self.settings.isSynced()

    def init(self):
        g_clientUpdateManager.addCallbacks({b'intUserSettings': (self._onResync)})
        return

    def fini(self):
        self.onSyncStarted.clear()
        self.onSyncCompleted.clear()
        g_clientUpdateManager.removeObjectCallbacks(self)
        return

    def clear(self):
        self.__intSettings.clear()
        return

    @property
    def waitForSync(self):
        return self.__waitForSync

    @property
    def settings(self):
        return self.__intSettings

    def _onResync(self, *args):
        self.__invalidateData()
        return

    @adisp_async
    def update(self, callback=None):
        self.__invalidateData(callback)
        return

    def getSectionSettings(self, section, defaultValue=0):
        return self.__intSettings.getSetting(section, defaultValue)

    def setSectionSettings(self, section, value):
        self.__intSettings.setSetting(section, value)
        return

    def setSettings(self, settings):
        self.__intSettings.setSettings(settings)
        return

    def getSetting(self, key, defaultValue=0):
        return self.__intSettings.getSetting(key, defaultValue)

    def getVersion(self, defaultValue=0):
        return self.__intSettings.getSetting(VERSION, defaultValue)

    def setVersion(self, value):
        self.__intSettings.setSetting(VERSION, value)
        return

    def delSettings(self, settings):
        self.__intSettings.delSettings(settings)
        return

    def __invalidateData(self, callback=(lambda *args: None)):

        def cbWrapper(*args):
            self.__waitForSync = False
            self.onSyncCompleted()
            callback(*args)
            return

        self.__waitForSync = True
        self.onSyncStarted()
        import BattleReplay
        if BattleReplay.g_replayCtrl.isPlaying:
            cbWrapper(dict())
            return
        self.__intSettings.request()(cbWrapper)
        return
