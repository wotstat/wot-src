from __future__ import absolute_import
from collections import namedtuple
from skeletons.gui.game_control import IFunRandomController
_FunRandomConfig = namedtuple(b'_FunRandomConfig', (b'isEnabled', b'subModes', b'metaProgression'))
_FunRandomProgressConfig = namedtuple(b'_FunRandomProgressConfig', (b'isEnabled', b'progressions'))
_FunRandomStatus = namedtuple(b'_FunRandomStatus', (b'state', b'rightBorder', b'primeDelta'))
_FUN_PROGRESS_CONFIG_STUB = _FunRandomProgressConfig(isEnabled=False, progressions=())
_FUN_CONFIG_STUB = _FunRandomConfig(isEnabled=False, subModes={}, metaProgression=_FUN_PROGRESS_CONFIG_STUB)
_FUN_STATUS_STUB = _FunRandomStatus(state=0, rightBorder=0, primeDelta=0)

class _FunHiddenVehicles(IFunRandomController.IFunHiddenVehicles):

    def startVehiclesListening(self):
        return

    def stopVehiclesListening(self):
        return

    def updateCurrentVehicle(self, desiredSubMode):
        return


class _FunNotifications(IFunRandomController.IFunNotifications):

    def isNotificationsAllowed(self):
        return False

    def isNotificationsEnabled(self):
        return False

    def addToQueue(self, notification):
        return

    def markSeenAsFrozen(self, subModesIDs):
        return

    def pushNotification(self, notification):
        return

    def startNotificationPushing(self):
        return

    def stopNotificationPushing(self):
        return

    def updateSettings(self, settings):
        return


class _FunProgressions(IFunRandomController.IFunProgressions):

    def isProgressionExecutor(self, questID):
        return False

    def getActiveProgression(self):
        return

    def getProgressionTimer(self):
        return 0

    def getSettings(self):
        return _FUN_PROGRESS_CONFIG_STUB

    def startProgressListening(self):
        return

    def stopProgressListening(self):
        return

    def updateSettings(self, progressionSettings):
        return


class _FunSubscription(IFunRandomController.IFunSubscription):

    def resume(self):
        return

    def suspend(self):
        return

    def addListener(self, eventType, handler, scope=None):
        return

    def removeListener(self, eventType, handler, scope=None):
        return

    def handleEvent(self, event, scope=None):
        return

    def startCoreNotifications(self):
        return


class _FunSubModesHolder(IFunRandomController.IFunSubModesHolder):

    def getBattleSubMode(self, arenaVisitor=None):
        return

    def getBattleSubModeID(self, arenaVisitor=None):
        return 0

    def getDesiredSubMode(self):
        return

    def getDesiredSubModeID(self):
        return 0

    def getSubMode(self, subModeID):
        return

    def getSubModes(self, subModesIDs=None, isOrdered=False):
        return []

    def getSubModesIDs(self):
        return []

    def setDesiredSubModeID(self, subModeID, trustedSource=False):
        return

    def startNotification(self):
        return

    def stopNotification(self):
        return

    def updateSettings(self, prevSettings, newSettings):
        return


class _FunSubModesInfo(IFunRandomController.IFunSubModesInfo):

    def isAvailable(self):
        return False

    def isEntryPointAvailable(self):
        return False

    def getEventEndDate(self, now=None, subModesIDs=None):
        return 0

    def getLeftTimeToPrimeTimesEnd(self, now=None, subModes=None):
        return 0

    def getPrimeTimesForDay(self, selectedTime, groupIdentical=False):
        return {}

    def getSubModesStatus(self, subModesIDs=None):
        return _FUN_STATUS_STUB

    def getPerformanceAlertGroup(self, subModesIDs=None):
        return 0


class FunRandomController(IFunRandomController):

    def __init__(self):
        super(FunRandomController, self).__init__()
        self.__progressions = _FunProgressions()
        self.__notifications = _FunNotifications()
        self.__subscription = _FunSubscription()
        self.__subModesHolder = _FunSubModesHolder()
        self.__subModesInfo = _FunSubModesInfo()
        self.__hiddenVehicles = _FunHiddenVehicles()
        return

    def fini(self):
        self.__hiddenVehicles.fini()
        self.__subModesInfo.fini()
        self.__subModesHolder.fini()
        self.__progressions.fini()
        self.__subscription.fini()
        self.__notifications.fini()
        super(FunRandomController, self).fini()
        return

    @property
    def hiddenVehicles(self):
        return self.__hiddenVehicles

    @property
    def notifications(self):
        return self.__notifications

    @property
    def progressions(self):
        return self.__progressions

    @property
    def subscription(self):
        return self.__subscription

    @property
    def subModesHolder(self):
        return self.__subModesHolder

    @property
    def subModesInfo(self):
        return self.__subModesInfo

    def isEnabled(self):
        return False

    def isFunRandomPrbActive(self):
        return False

    def isOnlyFunRandomVehicle(self, vehicle):
        return b'fun_random' in vehicle.tags

    def getConfigurationModel(self):
        return

    def getSettings(self):
        return _FUN_CONFIG_STUB

    def setDesiredSubModeID(self, subModeID, trustedSource=False):
        return

    def setSubModesHolder(self, subModesHolder):
        self.__subModesHolder = subModesHolder
        return

    def selectFunRandomBattle(self, desiredSubModeID, callback=None):
        return
