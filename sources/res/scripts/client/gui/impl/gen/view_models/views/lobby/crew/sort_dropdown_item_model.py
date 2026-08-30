from enum import IntEnum
from frameworks.wulf import ViewModel

class SortingTypeEnum(IntEnum):
    DEFAULT = 0
    COMMON = 1
    LEGENDARY = 2


class SortDropdownItemModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(SortDropdownItemModel, self).__init__(properties=properties, commands=commands)
        return

    def getIsSelected(self):
        return self._getBool(0)

    def setIsSelected(self, value):
        self._setBool(0, value)
        return

    def getIsEnabled(self):
        return self._getBool(1)

    def setIsEnabled(self, value):
        self._setBool(1, value)
        return

    def getMType(self):
        return SortingTypeEnum(self._getNumber(2))

    def setMType(self, value):
        self._setNumber(2, value.value)
        return

    def _initialize(self):
        super(SortDropdownItemModel, self)._initialize()
        self._addBoolProperty(b'isSelected', False)
        self._addBoolProperty(b'isEnabled', False)
        self._addNumberProperty(b'mType', SortingTypeEnum.DEFAULT.value)
        return
