from enum import Enum
from frameworks.wulf import ViewModel

class CategoryType(Enum):
    PERSONAL = b'personal'
    CLAN = b'clan'
    EVENT = b'event'


class DisabledCategory(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(DisabledCategory, self).__init__(properties=properties, commands=commands)
        return

    def getCategoryType(self):
        return CategoryType(self._getString(0))

    def setCategoryType(self, value):
        self._setString(0, value.value)
        return

    def getIsDisabled(self):
        return self._getBool(1)

    def setIsDisabled(self, value):
        self._setBool(1, value)
        return

    def _initialize(self):
        super(DisabledCategory, self)._initialize()
        self._addStringProperty(b'categoryType')
        self._addBoolProperty(b'isDisabled', False)
        return
