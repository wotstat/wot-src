from enum import Enum
from frameworks.wulf import ViewModel

class AdditionalMissionType(Enum):
    DAILY = b'daily'
    WEEKLY = b'weekly'


class AdditionalMissionModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=5, commands=0):
        super(AdditionalMissionModel, self).__init__(properties=properties, commands=commands)
        return

    def getType(self):
        return AdditionalMissionType(self._getString(0))

    def setType(self, value):
        self._setString(0, value.value)
        return

    def getMaxPoints(self):
        return self._getNumber(1)

    def setMaxPoints(self, value):
        self._setNumber(1, value)
        return

    def getCurrentPoints(self):
        return self._getNumber(2)

    def setCurrentPoints(self, value):
        self._setNumber(2, value)
        return

    def getIsEnabled(self):
        return self._getBool(3)

    def setIsEnabled(self, value):
        self._setBool(3, value)
        return

    def getIsProgressHidden(self):
        return self._getBool(4)

    def setIsProgressHidden(self, value):
        self._setBool(4, value)
        return

    def _initialize(self):
        super(AdditionalMissionModel, self)._initialize()
        self._addStringProperty(b'type')
        self._addNumberProperty(b'maxPoints', 0)
        self._addNumberProperty(b'currentPoints', 0)
        self._addBoolProperty(b'isEnabled', False)
        self._addBoolProperty(b'isProgressHidden', False)
        return
