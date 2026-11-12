from enum import IntEnum
from frameworks.wulf import ViewModel

class RewardState(IntEnum):
    NORMAL = 0
    DISABLED = 1


class LootBoxGuaranteedRewardModel(ViewModel):
    __slots__ = (b'onInfoClick',)

    def __init__(self, properties=5, commands=1):
        super(LootBoxGuaranteedRewardModel, self).__init__(properties=properties, commands=commands)
        return

    def getRealm(self):
        return self._getString(0)

    def setRealm(self, value):
        self._setString(0, value)
        return

    def getMaxBoxesCount(self):
        return self._getNumber(1)

    def setMaxBoxesCount(self, value):
        self._setNumber(1, value)
        return

    def getIsPremiumType(self):
        return self._getBool(2)

    def setIsPremiumType(self, value):
        self._setBool(2, value)
        return

    def getIsFocused(self):
        return self._getBool(3)

    def setIsFocused(self, value):
        self._setBool(3, value)
        return

    def getState(self):
        return RewardState(self._getNumber(4))

    def setState(self, value):
        self._setNumber(4, value.value)
        return

    def _initialize(self):
        super(LootBoxGuaranteedRewardModel, self)._initialize()
        self._addStringProperty(b'realm', b'')
        self._addNumberProperty(b'maxBoxesCount', 0)
        self._addBoolProperty(b'isPremiumType', False)
        self._addBoolProperty(b'isFocused', False)
        self._addNumberProperty(b'state')
        self.onInfoClick = self._addCommand(b'onInfoClick')
        return
