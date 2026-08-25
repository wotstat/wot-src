from enum import IntEnum
from frameworks.wulf import Array, ViewModel
from gui.impl.gen.view_models.common.missions.bonuses.bonus_model import BonusModel

class SubscriptionState(IntEnum):
    INACTIVE = 0
    ACTIVE = 1
    CANCELED = 2


class WotPlusTooltipModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=4, commands=0):
        super(WotPlusTooltipModel, self).__init__(properties=properties, commands=commands)
        return

    def getNextCharge(self):
        return self._getString(0)

    def setNextCharge(self, value):
        self._setString(0, value)
        return

    def getExpirationDate(self):
        return self._getString(1)

    def setExpirationDate(self, value):
        self._setString(1, value)
        return

    def getState(self):
        return SubscriptionState(self._getNumber(2))

    def setState(self, value):
        self._setNumber(2, value.value)
        return

    def getBonuses(self):
        return self._getArray(3)

    def setBonuses(self, value):
        self._setArray(3, value)
        return

    @staticmethod
    def getBonusesType():
        return BonusModel

    def _initialize(self):
        super(WotPlusTooltipModel, self)._initialize()
        self._addStringProperty(b'nextCharge', b'')
        self._addStringProperty(b'expirationDate', b'')
        self._addNumberProperty(b'state')
        self._addArrayProperty(b'bonuses', Array())
        return
