from enum import Enum, IntEnum
from frameworks.wulf import Array
from frameworks.wulf import ViewModel
from gui_lootboxes.gui.impl.gen.view_models.views.lobby.gui_lootboxes.lootbox_key_view_model import LootboxKeyViewModel
from gui_lootboxes.gui.impl.gen.view_models.views.lobby.gui_lootboxes.lootbox_view_model import LootboxViewModel

class States(Enum):
    STORAGE_VIEWING = b'STORAGE_VIEWING'
    REQUEST_TO_OPEN = b'REQUEST_TO_OPEN'
    OPENING = b'OPENING'
    LOSE_OPENING = b'LOSE_OPENING'
    OPENING_ERROR = b'OPENING_ERROR'
    UNIQUE_REWARDING = b'UNIQUE_REWARDING'
    REWARDING = b'REWARDING'


class ReturnPlace(IntEnum):
    TO_HANGAR = 0
    TO_SHOP = 1
    TO_NY_CUSTOMIZATION = 2
    TO_SHARDS = 3
    TO_REFERRAL = 4
    TO_FIR = 5
    TO_LIGHTS = 6
    TO_INSTALLATIONS = 7
    TO_FAIR = 8
    TO_SKATING = 9
    TO_ATTRACTION = 10
    TO_PET = 11


class Glows(Enum):
    DEFAULT = b'DEFAULT'
    UNIQUE = b'UNIQUE'


class LootboxesStorageViewModel(ViewModel):
    __slots__ = (b'openLootBoxes', b'onClose', b'onCloseEsc', b'buyBox', b'openningFinished', b'onLootboxSelected', b'changeAnimationEnabledSetting', b'showBonusProbabilities', b'hideTriggerHint', b'onError', b'showLootBoxInfoPage', b'showStatistic')

    def __init__(self, properties=15, commands=12):
        super(LootboxesStorageViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getLootboxes(self):
        return self._getArray(0)

    def setLootboxes(self, value):
        self._setArray(0, value)
        return

    @staticmethod
    def getLootboxesType():
        return LootboxViewModel

    def getLootboxKeys(self):
        return self._getArray(1)

    def setLootboxKeys(self, value):
        self._setArray(1, value)
        return

    @staticmethod
    def getLootboxKeysType():
        return LootboxKeyViewModel

    def getCurrentState(self):
        return States(self._getString(2))

    def setCurrentState(self, value):
        self._setString(2, value.value)
        return

    def getCurrentLootboxID(self):
        return self._getNumber(3)

    def setCurrentLootboxID(self, value):
        self._setNumber(3, value)
        return

    def getIsAnimationEnabled(self):
        return self._getBool(4)

    def setIsAnimationEnabled(self, value):
        self._setBool(4, value)
        return

    def getIsBuyAvailable(self):
        return self._getBool(5)

    def setIsBuyAvailable(self, value):
        self._setBool(5, value)
        return

    def getReturnPlace(self):
        return ReturnPlace(self._getNumber(6))

    def setReturnPlace(self, value):
        self._setNumber(6, value.value)
        return

    def getIsShowTriggerHint(self):
        return self._getBool(7)

    def setIsShowTriggerHint(self, value):
        self._setBool(7, value)
        return

    def getIsShowInfoButton(self):
        return self._getBool(8)

    def setIsShowInfoButton(self, value):
        self._setBool(8, value)
        return

    def getIfHasUniqueURL(self):
        return self._getBool(9)

    def setIfHasUniqueURL(self, value):
        self._setBool(9, value)
        return

    def getGlowType(self):
        return Glows(self._getString(10))

    def setGlowType(self, value):
        self._setString(10, value.value)
        return

    def getIsShowZeroStateStatistic(self):
        return self._getBool(11)

    def setIsShowZeroStateStatistic(self, value):
        self._setBool(11, value)
        return

    def getIsShowStatistic(self):
        return self._getBool(12)

    def setIsShowStatistic(self, value):
        self._setBool(12, value)
        return

    def getIsShowStatisticHint(self):
        return self._getBool(13)

    def setIsShowStatisticHint(self, value):
        self._setBool(13, value)
        return

    def getIsShowStatisticHintNoBoxes(self):
        return self._getBool(14)

    def setIsShowStatisticHintNoBoxes(self, value):
        self._setBool(14, value)
        return

    def _initialize(self):
        super(LootboxesStorageViewModel, self)._initialize()
        self._addArrayProperty(b'lootboxes', Array())
        self._addArrayProperty(b'lootboxKeys', Array())
        self._addStringProperty(b'currentState')
        self._addNumberProperty(b'currentLootboxID', 0)
        self._addBoolProperty(b'isAnimationEnabled', True)
        self._addBoolProperty(b'isBuyAvailable', True)
        self._addNumberProperty(b'returnPlace')
        self._addBoolProperty(b'isShowTriggerHint', False)
        self._addBoolProperty(b'isShowInfoButton', False)
        self._addBoolProperty(b'ifHasUniqueURL', True)
        self._addStringProperty(b'glowType', Glows.DEFAULT.value)
        self._addBoolProperty(b'isShowZeroStateStatistic', False)
        self._addBoolProperty(b'isShowStatistic', False)
        self._addBoolProperty(b'isShowStatisticHint', False)
        self._addBoolProperty(b'isShowStatisticHintNoBoxes', False)
        self.openLootBoxes = self._addCommand(b'openLootBoxes')
        self.onClose = self._addCommand(b'onClose')
        self.onCloseEsc = self._addCommand(b'onCloseEsc')
        self.buyBox = self._addCommand(b'buyBox')
        self.openningFinished = self._addCommand(b'openningFinished')
        self.onLootboxSelected = self._addCommand(b'onLootboxSelected')
        self.changeAnimationEnabledSetting = self._addCommand(b'changeAnimationEnabledSetting')
        self.showBonusProbabilities = self._addCommand(b'showBonusProbabilities')
        self.hideTriggerHint = self._addCommand(b'hideTriggerHint')
        self.onError = self._addCommand(b'onError')
        self.showLootBoxInfoPage = self._addCommand(b'showLootBoxInfoPage')
        self.showStatistic = self._addCommand(b'showStatistic')
        return
