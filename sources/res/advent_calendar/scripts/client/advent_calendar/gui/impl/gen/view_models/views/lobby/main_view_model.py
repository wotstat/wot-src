from enum import Enum
from frameworks.wulf import Array, ViewModel
from advent_calendar.gui.impl.gen.view_models.views.lobby.components.advent_calendar_events import AdventCalendarEvents
from advent_calendar.gui.impl.gen.view_models.views.lobby.door_view_model import DoorViewModel
from advent_calendar.gui.impl.gen.view_models.views.lobby.progression_rewards_view_model import ProgressionRewardsViewModel

class StatePhase(Enum):
    ACTIVE_PHASE = b'activePhase'
    POST_ACTIVE_PHASE = b'postActivePhase'


class TooltipConstants(Enum):
    NOT_ENOUGH = b'notEnough'
    LOOTBOX = b'lootbox'


class MainViewModel(ViewModel):
    __slots__ = (b'onClose', b'onOpenDoorAnimStarted', b'onOpenDoorAnimEnded', b'onShowPurchaseDialog', b'onAnimationCompleted', b'onOpenDownloadLink', b'onInfoClick')

    def __init__(self, properties=20, commands=7):
        super(MainViewModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def progressionRewards(self):
        return self._getViewModel(0)

    @staticmethod
    def getProgressionRewardsType():
        return ProgressionRewardsViewModel

    @property
    def event(self):
        return self._getViewModel(1)

    @staticmethod
    def getEventType():
        return AdventCalendarEvents

    def getStatePhase(self):
        return StatePhase(self._getString(2))

    def setStatePhase(self, value):
        self._setString(2, value.value)
        return

    def getStartTime(self):
        return self._getNumber(3)

    def setStartTime(self, value):
        self._setNumber(3, value)
        return

    def getShowBlur(self):
        return self._getBool(4)

    def setShowBlur(self, value):
        self._setBool(4, value)
        return

    def getPostEventStartDate(self):
        return self._getNumber(5)

    def setPostEventStartDate(self, value):
        self._setNumber(5, value)
        return

    def getPostEventEndDate(self):
        return self._getNumber(6)

    def setPostEventEndDate(self, value):
        self._setNumber(6, value)
        return

    def getDoors(self):
        return self._getArray(7)

    def setDoors(self, value):
        self._setArray(7, value)
        return

    @staticmethod
    def getDoorsType():
        return DoorViewModel

    def getDoorOpenBlocked(self):
        return self._getBool(8)

    def setDoorOpenBlocked(self, value):
        self._setBool(8, value)
        return

    def getCurrencyName(self):
        return self._getString(9)

    def setCurrencyName(self, value):
        self._setString(9, value)
        return

    def getBalanceCurrencyValue(self):
        return self._getNumber(10)

    def setBalanceCurrencyValue(self, value):
        self._setNumber(10, value)
        return

    def getCurrencyIcon(self):
        return self._getString(11)

    def setCurrencyIcon(self, value):
        self._setString(11, value)
        return

    def getIsAnimationEnabled(self):
        return self._getBool(12)

    def setIsAnimationEnabled(self, value):
        self._setBool(12, value)
        return

    def getIsCalendarCompleted(self):
        return self._getBool(13)

    def setIsCalendarCompleted(self, value):
        self._setBool(13, value)
        return

    def getIsIntroScreenVisible(self):
        return self._getBool(14)

    def setIsIntroScreenVisible(self, value):
        self._setBool(14, value)
        return

    def getIsWalletAvailable(self):
        return self._getBool(15)

    def setIsWalletAvailable(self, value):
        self._setBool(15, value)
        return

    def getBalancePluginPath(self):
        return self._getString(16)

    def setBalancePluginPath(self, value):
        self._setString(16, value)
        return

    def getIsBalancePanelVisible(self):
        return self._getBool(17)

    def setIsBalancePanelVisible(self, value):
        self._setBool(17, value)
        return

    def getSubTitle(self):
        return self._getString(18)

    def setSubTitle(self, value):
        self._setString(18, value)
        return

    def getCurrencyTooltipId(self):
        return self._getString(19)

    def setCurrencyTooltipId(self, value):
        self._setString(19, value)
        return

    def _initialize(self):
        super(MainViewModel, self)._initialize()
        self._addViewModelProperty(b'progressionRewards', ProgressionRewardsViewModel())
        self._addViewModelProperty(b'event', AdventCalendarEvents())
        self._addStringProperty(b'statePhase', StatePhase.ACTIVE_PHASE.value)
        self._addNumberProperty(b'startTime', 0)
        self._addBoolProperty(b'showBlur', False)
        self._addNumberProperty(b'postEventStartDate', 0)
        self._addNumberProperty(b'postEventEndDate', 0)
        self._addArrayProperty(b'doors', Array())
        self._addBoolProperty(b'doorOpenBlocked', False)
        self._addStringProperty(b'currencyName', b'')
        self._addNumberProperty(b'balanceCurrencyValue', 0)
        self._addStringProperty(b'currencyIcon', b'')
        self._addBoolProperty(b'isAnimationEnabled', False)
        self._addBoolProperty(b'isCalendarCompleted', False)
        self._addBoolProperty(b'isIntroScreenVisible', False)
        self._addBoolProperty(b'isWalletAvailable', True)
        self._addStringProperty(b'balancePluginPath', b'')
        self._addBoolProperty(b'isBalancePanelVisible', True)
        self._addStringProperty(b'subTitle', b'')
        self._addStringProperty(b'currencyTooltipId', b'')
        self.onClose = self._addCommand(b'onClose')
        self.onOpenDoorAnimStarted = self._addCommand(b'onOpenDoorAnimStarted')
        self.onOpenDoorAnimEnded = self._addCommand(b'onOpenDoorAnimEnded')
        self.onShowPurchaseDialog = self._addCommand(b'onShowPurchaseDialog')
        self.onAnimationCompleted = self._addCommand(b'onAnimationCompleted')
        self.onOpenDownloadLink = self._addCommand(b'onOpenDownloadLink')
        self.onInfoClick = self._addCommand(b'onInfoClick')
        return
