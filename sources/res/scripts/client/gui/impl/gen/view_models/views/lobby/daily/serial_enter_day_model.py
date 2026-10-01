from enum import Enum
from frameworks.wulf import Array
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.common.missions.bonuses.icon_bonus_model import IconBonusModel

class DayState(Enum):
    DISABLED = b'disabled'
    CURRENT = b'current'
    NEEDRELOGIN = b'needRelogin'
    TODAY = b'today'
    COMPLETED = b'completed'


class SerialEnterDayModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=4, commands=0):
        super(SerialEnterDayModel, self).__init__(properties=properties, commands=commands)
        return

    def getDay(self):
        return self._getNumber(0)

    def setDay(self, value):
        self._setNumber(0, value)
        return

    def getState(self):
        return DayState(self._getString(1))

    def setState(self, value):
        self._setString(1, value.value)
        return

    def getIsFinal(self):
        return self._getBool(2)

    def setIsFinal(self, value):
        self._setBool(2, value)
        return

    def getBonuses(self):
        return self._getArray(3)

    def setBonuses(self, value):
        self._setArray(3, value)
        return

    @staticmethod
    def getBonusesType():
        return IconBonusModel

    def _initialize(self):
        super(SerialEnterDayModel, self)._initialize()
        self._addNumberProperty(b'day', 0)
        self._addStringProperty(b'state')
        self._addBoolProperty(b'isFinal', False)
        self._addArrayProperty(b'bonuses', Array())
        return
