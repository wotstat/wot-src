from enum import Enum
from frameworks.wulf import Array
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.common.personal_reserves.booster_model import BoosterModel

class GroupCategory(Enum):
    XP = b'xp'
    CREDITS = b'credits'
    COMBINED_XP = b'combined'
    EVENT = b'event'
    CLAN = b'clan'


class ReservesGroupModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(ReservesGroupModel, self).__init__(properties=properties, commands=commands)
        return

    def getCategory(self):
        return GroupCategory(self._getString(0))

    def setCategory(self, value):
        self._setString(0, value.value)
        return

    def getReserves(self):
        return self._getArray(1)

    def setReserves(self, value):
        self._setArray(1, value)
        return

    @staticmethod
    def getReservesType():
        return BoosterModel

    def _initialize(self):
        super(ReservesGroupModel, self)._initialize()
        self._addStringProperty(b'category')
        self._addArrayProperty(b'reserves', Array())
        return
