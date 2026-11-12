from enum import Enum
from frameworks.wulf import ViewModel

class MenuNames(Enum):
    CITY = b'city'
    LEADERS = b'leaders'
    MACHINE = b'surprise_machine'
    QUESTS = b'quests'
    PET = b'pet'
    INFO = b'info'


class NewYearTabModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(NewYearTabModel, self).__init__(properties=properties, commands=commands)
        return

    def getName(self):
        return MenuNames(self._getString(0))

    def setName(self, value):
        self._setString(0, value.value)
        return

    def getInfoCount(self):
        return self._getNumber(1)

    def setInfoCount(self, value):
        self._setNumber(1, value)
        return

    def getIconName(self):
        return self._getString(2)

    def setIconName(self, value):
        self._setString(2, value)
        return

    def _initialize(self):
        super(NewYearTabModel, self)._initialize()
        self._addStringProperty(b'name')
        self._addNumberProperty(b'infoCount', 0)
        self._addStringProperty(b'iconName', b'')
        return
