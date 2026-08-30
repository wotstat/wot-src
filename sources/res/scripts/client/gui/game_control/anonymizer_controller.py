import logging, BigWorld
from Event import Event
from gui import SystemMessages
from gui.ClientUpdateManager import g_clientUpdateManager
from gui.impl import backport
from gui.impl.gen import R
from gui.anonymizer.contacts_uploader import ContactsUploader
from helpers import dependency
from skeletons.gui.game_control import IAnonymizerController
from skeletons.gui.lobby_context import ILobbyContext
from skeletons.gui.shared import IItemsCache
_logger = logging.getLogger(__name__)
_RSettingsError = R.strings.messenger.server.errors.settingError

class AnonymizerController(IAnonymizerController):
    __lobbyContext = dependency.descriptor(ILobbyContext)
    __itemsCache = dependency.descriptor(IItemsCache)
    __slots__ = (b'__isEnabled', b'__isRestricted', b'__isAnonymized', b'__isInBattle', b'__uploader')

    def __init__(self):
        self.onStateChanged = Event()
        self.__isEnabled = False
        self.__isRestricted = False
        self.__isAnonymized = False
        self.__isInBattle = False
        self.__uploader = ContactsUploader()
        return

    def onConnected(self):
        self.__uploader.init()
        return

    def onDisconnected(self):
        self.__uploader.fini()
        self.__clear()
        return

    def onLobbyInited(self, _):
        self.__isInBattle = False
        self.__addListeners()
        self.__update()
        return

    def onAvatarBecomePlayer(self):
        self.__removeListeners()
        self.__isInBattle = True
        return

    def onAccountBecomeNonPlayer(self):
        if self.__uploader.isProcessing:
            _logger.info(b'contacts uploader stopping because of onAccountBecomeNonPlayer.')
            self.__uploader.stop()
        return

    @property
    def isInBattle(self):
        return self.__isInBattle

    @property
    def isEnabled(self):
        return self.__isEnabled

    @property
    def isRestricted(self):
        return self.__isRestricted

    @property
    def isAnonymized(self):
        return self.__isEnabled and self.__isAnonymized

    def setAnonymized(self, value):
        if self.isEnabled and not self.isRestricted:
            if value != self.__isAnonymized:
                self.__isAnonymized = value
                BigWorld.player().anonymizer.setAnonymized(self.__isAnonymized, self.__onSetAnonymizedResponse)
        else:
            self.__pushChangeUnavailableMessage()
        return

    def __addListeners(self):
        g_clientUpdateManager.addCallbacks({b'cache.SPA': (self.__onCacheSPAChanged), 
           b'anonymizer.enabled': (self.__onAnonymizedStateChanged), 
           b'anonymizer.contactsFeedback': (self.__onContactsFeedback)})
        self.__lobbyContext.getServerSettings().onServerSettingsChange += self.__onServerSettingsChanged
        return

    def __removeListeners(self):
        self.__lobbyContext.getServerSettings().onServerSettingsChange -= self.__onServerSettingsChanged
        g_clientUpdateManager.removeObjectCallbacks(self)
        return

    def __update(self):
        self.__isEnabled = self.__lobbyContext.getServerSettings().isAnonymizerEnabled()
        self.__isRestricted = self.__itemsCache.items.stats.isAnonymousRestricted
        self.__isAnonymized = self.__itemsCache.items.anonymizer.isPlayerAnonymized
        self.__processContacts()
        self.onStateChanged(enabled=self.isEnabled, restricted=self.isRestricted, anonymized=self.isAnonymized)
        return

    def __clear(self):
        self.onStateChanged.clear()
        self.__removeListeners()
        self.__isEnabled = False
        self.__isRestricted = False
        self.__isAnonymized = False
        self.__isInBattle = False
        return

    def __onServerSettingsChanged(self, *_):
        self.__isEnabled = self.__lobbyContext.getServerSettings().isAnonymizerEnabled()
        self.onStateChanged(enabled=self.isEnabled)
        return

    def __onCacheSPAChanged(self, *_):
        self.__isRestricted = self.__itemsCache.items.stats.isAnonymousRestricted
        self.onStateChanged(restricted=self.isRestricted)
        return

    def __onAnonymizedStateChanged(self, *_):
        self.__isAnonymized = self.__itemsCache.items.anonymizer.isPlayerAnonymized
        self.onStateChanged(anonymized=self.isAnonymized)
        return

    def __onContactsFeedback(self, *_):
        self.__processContacts()
        return

    def __processContacts(self):
        contactsFeedback = self.__itemsCache.items.anonymizer.contactsFeedback
        if contactsFeedback:
            arenaUniqueID, contactsBlob = self.__itemsCache.items.anonymizer.contactsFeedback[0]
            if self.__uploader.isProcessing:
                if self.__uploader.arenaUniqueID == arenaUniqueID:
                    _logger.info(b'contacts uploader continue upload arenaID %s', arenaUniqueID)
                    return
                self.__uploader.stop()
            self.__uploader.start(arenaUniqueID, contactsBlob)
        elif self.__uploader.isProcessing:
            self.__uploader.stop()
        return

    def __onSetAnonymizedResponse(self, resultID, errorCode):
        if errorCode:
            self.__onAnonymizedStateChanged()
            self.__pushChangeUnavailableMessage()
        _logger.debug(b'setAnonymized response: %s', (resultID, errorCode))
        return

    @staticmethod
    def __pushChangeUnavailableMessage():
        SystemMessages.pushMessage(backport.text(_RSettingsError.changeUnavailable.message()), SystemMessages.SM_TYPE.Warning)
        return
