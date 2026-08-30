import weakref, MusicControllerWWISE as _MC, SoundGroups
from gui.sounds.ambients import GuiAmbientsCtrl
from gui.sounds.sound_constants import EnabledStatus
from gui.sounds.sound_systems import getCurrentSoundSystem
from gui.sounds.sound_utils import SOUND_DEBUG
from helpers import dependency
from skeletons.gui.game_control import IGameSessionController
from skeletons.gui.shared import IItemsCache
from skeletons.gui.sounds import ISoundsController

class SoundsController(ISoundsController):
    itemsCache = dependency.descriptor(IItemsCache)
    gameSession = dependency.descriptor(IGameSessionController)

    def __init__(self):
        super(SoundsController, self).__init__()
        self.__soundSystem = getCurrentSoundSystem()
        self.__guiAmbients = GuiAmbientsCtrl(weakref.proxy(self))
        SOUND_DEBUG(b'Sound system has been created', self.__soundSystem)
        return

    def init(self):
        self.__soundSystem.init()
        self.__guiAmbients.init()
        return

    def fini(self):
        self.__soundSystem.fini()
        self.__guiAmbients.fini()
        return

    def start(self):
        self.__guiAmbients.start()
        self.gameSession.onPremiumNotify += self.__onPremiumChanged
        self.__setAccountAttrs()
        return

    def stop(self, isDisconnected=False):
        self.gameSession.onPremiumNotify -= self.__onPremiumChanged
        self.__guiAmbients.stop(isDisconnected)
        if isDisconnected:
            _MC.g_musicController.unloadServerSounds(isDisconnected)
        return

    @property
    def system(self):
        return self.__soundSystem

    def enable(self):
        if not self.isEnabled():
            SoundGroups.g_instance.setEnableStatus(EnabledStatus.ENABLED_BY_USER)
        return

    def disable(self):
        if self.isEnabled():
            SoundGroups.g_instance.setEnableStatus(EnabledStatus.DISABLED)
        return

    def isEnabled(self):
        return EnabledStatus.isEnabled(SoundGroups.g_instance.getEnableStatus())

    def setEnvForSpace(self, spaceID, newEnv):
        return self.__guiAmbients.setEnvForSpace(spaceID, newEnv)

    def __onPremiumChanged(self, isPremium, attrs, premiumExpiryTime):
        SOUND_DEBUG(b'Premium account status changed', isPremium, attrs, premiumExpiryTime)
        self.__setAccountAttrs(restartSounds=True)
        return

    def __setAccountAttrs(self, restartSounds=False):
        SOUND_DEBUG(b'Set current account premium state', self.itemsCache.items.stats.isPremium, restartSounds)
        _MC.g_musicController.setAccountPremiumState(self.itemsCache.items.stats.isPremium, restart=restartSounds)
        return
