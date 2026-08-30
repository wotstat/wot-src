from enum import Enum, IntEnum
from frameworks.wulf import ViewModel
from gui.impl.wrappers.user_compound_price_model import UserCompoundPriceModel

class ReserveType(Enum):
    PERSONAL = b'personal'
    CLAN = b'clan'
    EVENT = b'event'


class ReserveState(IntEnum):
    INACTIVE = 0
    ACTIVE = 1
    USED = 2


class ReserveKind(Enum):
    GOLD = b'booster_gold'
    CREDITS = b'booster_credits'
    XP = b'booster_xp'
    CREWXP = b'booster_crew_xp'
    FREEXP = b'booster_free_xp'
    FL_XP = b'booster_fl_xp'
    FREEXPCREWXP = b'booster_free_xp_and_crew_xp'
    FREEXPMAINXP = b'booster_free_xp_and_crew_xp'


class BoosterModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=18, commands=0):
        super(BoosterModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def price(self):
        return self._getViewModel(0)

    @staticmethod
    def getPriceType():
        return UserCompoundPriceModel

    def getBoosterID(self):
        return self._getNumber(1)

    def setBoosterID(self, value):
        self._setNumber(1, value)
        return

    def getReserveType(self):
        return ReserveType(self._getString(2))

    def setReserveType(self, value):
        self._setString(2, value.value)
        return

    def getInactivationTime(self):
        return self._getNumber(3)

    def setInactivationTime(self, value):
        self._setNumber(3, value)
        return

    def getInDepot(self):
        return self._getNumber(4)

    def setInDepot(self, value):
        self._setNumber(4, value)
        return

    def getMinBonus(self):
        return self._getNumber(5)

    def setMinBonus(self, value):
        self._setNumber(5, value)
        return

    def getMaxBonus(self):
        return self._getNumber(6)

    def setMaxBonus(self, value):
        self._setNumber(6, value)
        return

    def getTotalDuration(self):
        return self._getNumber(7)

    def setTotalDuration(self, value):
        self._setNumber(7, value)
        return

    def getIsPremium(self):
        return self._getBool(8)

    def setIsPremium(self, value):
        self._setBool(8, value)
        return

    def getState(self):
        return ReserveState(self._getNumber(9))

    def setState(self, value):
        self._setNumber(9, value.value)
        return

    def getIconId(self):
        return self._getString(10)

    def setIconId(self, value):
        self._setString(10, value)
        return

    def getNextExpirationAmount(self):
        return self._getNumber(11)

    def setNextExpirationAmount(self, value):
        self._setNumber(11, value)
        return

    def getNextExpirationTime(self):
        return self._getNumber(12)

    def setNextExpirationTime(self, value):
        self._setNumber(12, value)
        return

    def getWillExpireAfter(self):
        return self._getNumber(13)

    def setWillExpireAfter(self, value):
        self._setNumber(13, value)
        return

    def getInDepotExpirableAmount(self):
        return self._getNumber(14)

    def setInDepotExpirableAmount(self, value):
        self._setNumber(14, value)
        return

    def getReserveKind(self):
        return ReserveKind(self._getString(15))

    def setReserveKind(self, value):
        self._setString(15, value.value)
        return

    def getIsNew(self):
        return self._getBool(16)

    def setIsNew(self, value):
        self._setBool(16, value)
        return

    def getIsExpiringSoon(self):
        return self._getBool(17)

    def setIsExpiringSoon(self, value):
        self._setBool(17, value)
        return

    def _initialize(self):
        super(BoosterModel, self)._initialize()
        self._addViewModelProperty(b'price', UserCompoundPriceModel())
        self._addNumberProperty(b'boosterID', -1)
        self._addStringProperty(b'reserveType')
        self._addNumberProperty(b'inactivationTime', -1)
        self._addNumberProperty(b'inDepot', -1)
        self._addNumberProperty(b'minBonus', -1)
        self._addNumberProperty(b'maxBonus', 0)
        self._addNumberProperty(b'totalDuration', 60)
        self._addBoolProperty(b'isPremium', False)
        self._addNumberProperty(b'state')
        self._addStringProperty(b'iconId', b'')
        self._addNumberProperty(b'nextExpirationAmount', 0)
        self._addNumberProperty(b'nextExpirationTime', 0)
        self._addNumberProperty(b'willExpireAfter', 0)
        self._addNumberProperty(b'inDepotExpirableAmount', 0)
        self._addStringProperty(b'reserveKind')
        self._addBoolProperty(b'isNew', False)
        self._addBoolProperty(b'isExpiringSoon', False)
        return
