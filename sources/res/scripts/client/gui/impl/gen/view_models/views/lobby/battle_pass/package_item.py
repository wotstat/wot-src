from enum import Enum, IntEnum
from frameworks.wulf import ViewModel
from gui.impl.wrappers.user_compound_price_model import UserCompoundPriceModel

class ChapterStates(IntEnum):
    ACTIVE = 0
    PAUSED = 1
    COMPLETED = 2
    NOTSTARTED = 3
    DISABLED = 4


class PackageType(IntEnum):
    BATTLEPASS = 0
    ANYLEVELS = 1
    SHOPOFFER = 2


class ChapterType(Enum):
    DEFAULT = b'default'
    MARATHON = b'marathon'
    RESOURCE = b'resource'


class PackageItem(ViewModel):
    __slots__ = ()

    def __init__(self, properties=11, commands=0):
        super(PackageItem, self).__init__(properties=properties, commands=commands)
        return

    @property
    def compoundPrice(self):
        return self._getViewModel(0)

    @staticmethod
    def getCompoundPriceType():
        return UserCompoundPriceModel

    def getPackageID(self):
        return self._getNumber(1)

    def setPackageID(self, value):
        self._setNumber(1, value)
        return

    def getPrice(self):
        return self._getNumber(2)

    def setPrice(self, value):
        self._setNumber(2, value)
        return

    def getIsLocked(self):
        return self._getBool(3)

    def setIsLocked(self, value):
        self._setBool(3, value)
        return

    def getIsBought(self):
        return self._getBool(4)

    def setIsBought(self, value):
        self._setBool(4, value)
        return

    def getType(self):
        return PackageType(self._getNumber(5))

    def setType(self, value):
        self._setNumber(5, value.value)
        return

    def getChapterID(self):
        return self._getNumber(6)

    def setChapterID(self, value):
        self._setNumber(6, value)
        return

    def getChapterState(self):
        return ChapterStates(self._getNumber(7))

    def setChapterState(self, value):
        self._setNumber(7, value.value)
        return

    def getCurrentLevel(self):
        return self._getNumber(8)

    def setCurrentLevel(self, value):
        self._setNumber(8, value)
        return

    def getExpireTime(self):
        return self._getNumber(9)

    def setExpireTime(self, value):
        self._setNumber(9, value)
        return

    def getChapterType(self):
        return ChapterType(self._getString(10))

    def setChapterType(self, value):
        self._setString(10, value.value)
        return

    def _initialize(self):
        super(PackageItem, self)._initialize()
        self._addViewModelProperty(b'compoundPrice', UserCompoundPriceModel())
        self._addNumberProperty(b'packageID', 0)
        self._addNumberProperty(b'price', 0)
        self._addBoolProperty(b'isLocked', False)
        self._addBoolProperty(b'isBought', False)
        self._addNumberProperty(b'type')
        self._addNumberProperty(b'chapterID', 0)
        self._addNumberProperty(b'chapterState')
        self._addNumberProperty(b'currentLevel', 0)
        self._addNumberProperty(b'expireTime', 0)
        self._addStringProperty(b'chapterType')
        return
