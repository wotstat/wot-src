from enum import IntEnum
from frameworks.wulf import Array, ViewModel
from gui.impl.gen.view_models.common.missions.bonuses.item_bonus_model import ItemBonusModel

class ScreenStatus(IntEnum):
    PENDING = 0
    ERROR = 1
    LOADED = 2


class StageInfoStatus(IntEnum):
    AVAILABLE = 0
    PURCHASED = 1
    UNAVAILABLE = 2


class StageInfoModel(ViewModel):
    __slots__ = (b'onRefresh',)

    def __init__(self, properties=9, commands=1):
        super(StageInfoModel, self).__init__(properties=properties, commands=commands)
        return

    def getId(self):
        return self._getNumber(0)

    def setId(self, value):
        self._setNumber(0, value)
        return

    def getIsPremium(self):
        return self._getBool(1)

    def setIsPremium(self, value):
        self._setBool(1, value)
        return

    def getIsBuyLoading(self):
        return self._getBool(2)

    def setIsBuyLoading(self, value):
        self._setBool(2, value)
        return

    def getStatus(self):
        return ScreenStatus(self._getNumber(3))

    def setStatus(self, value):
        self._setNumber(3, value.value)
        return

    def getStageStatus(self):
        return StageInfoStatus(self._getNumber(4))

    def setStageStatus(self, value):
        self._setNumber(4, value.value)
        return

    def getIsEnoughMoney(self):
        return self._getBool(5)

    def setIsEnoughMoney(self, value):
        self._setBool(5, value)
        return

    def getPrice(self):
        return self._getNumber(6)

    def setPrice(self, value):
        self._setNumber(6, value)
        return

    def getDeficiencyAmount(self):
        return self._getNumber(7)

    def setDeficiencyAmount(self, value):
        self._setNumber(7, value)
        return

    def getRewards(self):
        return self._getArray(8)

    def setRewards(self, value):
        self._setArray(8, value)
        return

    @staticmethod
    def getRewardsType():
        return ItemBonusModel

    def _initialize(self):
        super(StageInfoModel, self)._initialize()
        self._addNumberProperty(b'id', 0)
        self._addBoolProperty(b'isPremium', False)
        self._addBoolProperty(b'isBuyLoading', False)
        self._addNumberProperty(b'status')
        self._addNumberProperty(b'stageStatus')
        self._addBoolProperty(b'isEnoughMoney', True)
        self._addNumberProperty(b'price', 0)
        self._addNumberProperty(b'deficiencyAmount', 0)
        self._addArrayProperty(b'rewards', Array())
        self.onRefresh = self._addCommand(b'onRefresh')
        return
