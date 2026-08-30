from enum import Enum, IntEnum
from frameworks.wulf import Array
from frameworks.wulf import ViewModel

class DailyTypes(Enum):
    DEFAULT = b'default'


class DailyTabs(IntEnum):
    QUESTS = 0
    PREMIUM = 1
    SERIAL = 2


class DailyQuestsViewModel(ViewModel):
    __slots__ = (b'onClose', b'onTabClick', b'onInfoClick', b'onShowInfo', b'onInfoToggle', b'onBuyPremiumBtnClick', b'onRerollEnabled', b'onClaimRewards')

    def __init__(self, properties=8, commands=8):
        super(DailyQuestsViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getDailyType(self):
        return DailyTypes(self._getString(0))

    def setDailyType(self, value):
        self._setString(0, value.value)
        return

    def getIsDailyRegularEnabled(self):
        return self._getBool(1)

    def setIsDailyRegularEnabled(self, value):
        self._setBool(1, value)
        return

    def getIsDailyPremEnabled(self):
        return self._getBool(2)

    def setIsDailyPremEnabled(self, value):
        self._setBool(2, value)
        return

    def getIsSerialEnterEnabled(self):
        return self._getBool(3)

    def setIsSerialEnterEnabled(self, value):
        self._setBool(3, value)
        return

    def getDailyBattleTypes(self):
        return self._getArray(4)

    def setDailyBattleTypes(self, value):
        self._setArray(4, value)
        return

    @staticmethod
    def getDailyBattleTypesType():
        return unicode

    def getSerialEnterBattleTypes(self):
        return self._getArray(5)

    def setSerialEnterBattleTypes(self, value):
        self._setArray(5, value)
        return

    @staticmethod
    def getSerialEnterBattleTypesType():
        return unicode

    def getCurrentTabIdx(self):
        return self._getNumber(6)

    def setCurrentTabIdx(self, value):
        self._setNumber(6, value)
        return

    def getIntroSeen(self):
        return self._getBool(7)

    def setIntroSeen(self, value):
        self._setBool(7, value)
        return

    def _initialize(self):
        super(DailyQuestsViewModel, self)._initialize()
        self._addStringProperty(b'dailyType')
        self._addBoolProperty(b'isDailyRegularEnabled', False)
        self._addBoolProperty(b'isDailyPremEnabled', False)
        self._addBoolProperty(b'isSerialEnterEnabled', False)
        self._addArrayProperty(b'dailyBattleTypes', Array())
        self._addArrayProperty(b'serialEnterBattleTypes', Array())
        self._addNumberProperty(b'currentTabIdx', 0)
        self._addBoolProperty(b'introSeen', False)
        self.onClose = self._addCommand(b'onClose')
        self.onTabClick = self._addCommand(b'onTabClick')
        self.onInfoClick = self._addCommand(b'onInfoClick')
        self.onShowInfo = self._addCommand(b'onShowInfo')
        self.onInfoToggle = self._addCommand(b'onInfoToggle')
        self.onBuyPremiumBtnClick = self._addCommand(b'onBuyPremiumBtnClick')
        self.onRerollEnabled = self._addCommand(b'onRerollEnabled')
        self.onClaimRewards = self._addCommand(b'onClaimRewards')
        return
