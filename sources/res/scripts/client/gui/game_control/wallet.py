import logging, BigWorld, Event, constants
from account_helpers import AccountSettings
from account_helpers.AccountSettings import GUI_START_BEHAVIOR
from adisp import adisp_process
from gui import SystemMessages, DialogsInterface
from gui.ClientUpdateManager import g_clientUpdateManager
from gui.Scaleform.daapi.view.dialogs.FreeXPInfoDialogMeta import FreeXPInfoMeta
from gui.Scaleform.locale.SYSTEM_MESSAGES import SYSTEM_MESSAGES
from gui.SystemMessages import SM_TYPE
from helpers import dependency
from helpers.aop import Aspect, Pointcut, Weaver
from shared_utils import CONST_CONTAINER
from skeletons.account_helpers.settings_core import ISettingsCore
from skeletons.gui.game_control import IWalletController
from skeletons.gui.shared import IItemsCache
_logger = logging.getLogger(__name__)

class WalletController(IWalletController):
    itemsCache = dependency.descriptor(IItemsCache)
    settingsCore = dependency.descriptor(ISettingsCore)

    class STATUS(CONST_CONTAINER):
        SYNCING = 0
        NOT_AVAILABLE = 1
        AVAILABLE = 2

    def __init__(self):
        super(WalletController, self).__init__()
        self.onWalletStatusChanged = Event.Event()
        self.__currentStatus = None
        self.__currentCallbackId = None
        self.__useGold = False
        self.__useFreeXP = False
        self.__weaver = None
        return

    def init(self):
        _logger.debug(b'WalletController init')
        g_clientUpdateManager.addCallbacks({b'cache.mayConsumeWalletResources': (self.__onWalletStatusChanged)})
        return

    def fini(self):
        _logger.debug(b'WalletController fini')
        g_clientUpdateManager.removeObjectCallbacks(self, force=True)
        self.__clearCallback()
        self.__clearWeaver()
        super(WalletController, self).fini()
        return

    def onLobbyStarted(self, event):
        wallet = BigWorld.player().serverSettings[b'wallet']
        self.__useGold = bool(wallet[0])
        self.__useFreeXP = bool(wallet[1])
        if self.itemsCache.items.stats.mayConsumeWalletResources:
            status = self.STATUS.AVAILABLE
        else:
            status = self.STATUS.SYNCING
        self.__processStatus(status, True)
        return

    def onAvatarBecomePlayer(self):
        self.__clearWeaver()
        return

    def onDisconnected(self):
        self.__clearWeaver()
        return

    @property
    def status(self):
        return self.__currentStatus

    @property
    def componentsStatuses(self):
        return {b'gold': (self.__currentStatus if self.__useGold else self.STATUS.AVAILABLE), 
           b'freeXP': (self.__currentStatus if self.__useFreeXP else self.STATUS.AVAILABLE), 
           b'credits': ((constants.IS_CHINA or self).__currentStatus if 1 else self.STATUS.AVAILABLE), 
           b'crystal': ((constants.IS_CHINA or self).__currentStatus if 1 else self.STATUS.AVAILABLE), 
           b'eventCoin': ((constants.IS_CHINA or self).__currentStatus if 1 else self.STATUS.AVAILABLE), 
           b'bpcoin': ((constants.IS_CHINA or self).__currentStatus if 1 else self.STATUS.AVAILABLE)}

    @property
    def dynamicComponentsStatuses(self):
        return {currencyCode: self.__currentStatus if 1 else self.STATUS.AVAILABLE for currencyCode in self.itemsCache.items.stats.dynamicCurrencies.keys() if not constants.IS_CHINA}

    @property
    def isSyncing(self):
        return self.__checkStatus(self.STATUS.SYNCING)

    @property
    def isNotAvailable(self):
        return self.__checkStatus(self.STATUS.NOT_AVAILABLE)

    @property
    def isAvailable(self):
        return self.__checkStatus(self.STATUS.AVAILABLE)

    @property
    def useGold(self):
        return self.__useGold

    @property
    def useFreeXP(self):
        return self.__useFreeXP

    def cleanWeave(self, pointcuts):
        if self.__weaver:
            for pointcut in pointcuts:
                self.__weaver.clear(idx=self.__weaver.findPointcut(pointcut))

        return

    def __clearWeaver(self):
        if self.__weaver is not None:
            self.__weaver.clear()
            self.__weaver = None
        return

    def __processCallback(self):
        self.__currentCallbackId = None
        if self.isSyncing:
            self.__processStatus(self.STATUS.NOT_AVAILABLE)
            self.__sendNotification(status=b'not_available')
        return

    def __clearCallback(self):
        if self.__currentCallbackId is not None:
            BigWorld.cancelCallback(self.__currentCallbackId)
            self.__currentCallbackId = None
        return

    def __processStatus(self, status, initialize=False):
        if self.__currentStatus != status:
            self.__currentStatus = status
            self.__notify()
            _logger.info(b'Wallet status changed: %s(%s)', self.STATUS.getKeyByValue(self.__currentStatus), self.__currentStatus)
            if self.isAvailable:
                self.__clearCallback()
                if not initialize:
                    self.__sendNotification(status=b'available')
            elif self.isSyncing and self.__currentCallbackId is None:
                self.__currentCallbackId = BigWorld.callback(30, self.__processCallback)
        return

    def __onWalletStatusChanged(self, available):
        status = self.__currentStatus
        if available and not self.isAvailable:
            status = self.STATUS.AVAILABLE
        elif not available and self.isAvailable:
            status = self.STATUS.SYNCING
        self.__processStatus(status)
        return

    def __checkStatus(self, status):
        return self.__currentStatus == status

    def __notify(self):
        self.onWalletStatusChanged(self.componentsStatuses)
        return

    def __checkFreeXPConditions(self):
        defaults = AccountSettings.getFilterDefault(GUI_START_BEHAVIOR)
        filters = self.settingsCore.serverSettings.getSection(GUI_START_BEHAVIOR, defaults)
        if filters[b'isFreeXPInfoDialogShowed']:
            return
        self.__weaver = Weaver()
        if self.__weaver.findPointcut(UnlockItemPointcut) == -1:
            self.__weaver.weave(pointcut=UnlockItemPointcut, aspects=[
             ShowXPInfoDialogAspect(self.cleanWeave)])
        return

    def __sendNotification(self, status):
        msgType = SM_TYPE.Information if status == b'available' else SM_TYPE.Warning
        if constants.IS_CHINA:
            if not self.__useFreeXP:
                status += b'_gold'
            elif not self.__useGold:
                status += b'_freexp'
        SystemMessages.pushI18nMessage(SYSTEM_MESSAGES.getWalletStatus(status), type=msgType)
        return


class ShowXPInfoDialogAspect(Aspect):
    settingsCore = dependency.descriptor(ISettingsCore)

    def __init__(self, callBack):
        super(ShowXPInfoDialogAspect, self).__init__()
        self.callback = callBack
        return

    @adisp_process
    def atCall(self, cd):
        defaults = AccountSettings.getFilterDefault(GUI_START_BEHAVIOR)
        filters = self.settingsCore.serverSettings.getSection(GUI_START_BEHAVIOR, defaults)
        filters[b'isFreeXPInfoDialogShowed'] = True
        self.settingsCore.serverSettings.setSectionSettings(GUI_START_BEHAVIOR, filters)
        cd.avoid()
        yield DialogsInterface.showDialog(FreeXPInfoMeta())
        cd.function(*cd._packArgs(), **cd._kwargs)
        self.callback((UnlockItemPointcut,))
        return

    def clear(self):
        self.callback = None
        return


class UnlockItemPointcut(Pointcut):

    def __init__(self):
        super(UnlockItemPointcut, self).__init__(b'gui.shared.gui_items.items_actions.actions', b'UnlockItemAction', b'^_unlockItem$')
        return
