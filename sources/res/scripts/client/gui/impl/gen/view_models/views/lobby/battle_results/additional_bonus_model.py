from enum import Enum, IntEnum
from frameworks.wulf import ViewModel

class PremiumXpBonusRestriction(IntEnum):
    NORESTRICTION = 0
    ISAPPLIED = 1
    INVALIDBATTLETYPE = 2
    ISNOTVICTORY = 3
    DEPRECATEDRESULTS = 4
    NOVEHICLE = 5
    NOCREW = 6
    FASTEREDUCATIONCREWNOTACTIVE = 7
    FASTEREDUCATIONCREWACTIVE = 8
    NOTAPPLYINGERROR = 9


class BonusStates(IntEnum):
    PREMIUMINFO = 0
    PREMIUMBONUS = 1
    PREMIUMEARNINGS = 2
    PREMIUMADVERTISING = 3
    PLUSINFO = 4
    PLUSEARNINGS = 5
    PLUSYOUROCK = 6


class WotPlusTypeEnum(Enum):
    NONE = b'none'
    CORE = b'core'
    PRO = b'pro'


class AdditionalBonusModel(ViewModel):
    __slots__ = (b'onPremiumXpBonusApplied', b'onLocalStorageUpdated', b'onShowDetails')

    def __init__(self, properties=16, commands=3):
        super(AdditionalBonusModel, self).__init__(properties=properties, commands=commands)
        return

    def getHasPremium(self):
        return self._getBool(0)

    def setHasPremium(self, value):
        self._setBool(0, value)
        return

    def getWasPremium(self):
        return self._getBool(1)

    def setWasPremium(self, value):
        self._setBool(1, value)
        return

    def getHasAnyPremium(self):
        return self._getBool(2)

    def setHasAnyPremium(self, value):
        self._setBool(2, value)
        return

    def getWotPlusType(self):
        return WotPlusTypeEnum(self._getString(3))

    def setWotPlusType(self, value):
        self._setString(3, value.value)
        return

    def getHasBasicPremium(self):
        return self._getBool(4)

    def setHasBasicPremium(self, value):
        self._setBool(4, value)
        return

    def getHasPenalties(self):
        return self._getBool(5)

    def setHasPenalties(self, value):
        self._setBool(5, value)
        return

    def getIsXpBonusEnabled(self):
        return self._getBool(6)

    def setIsXpBonusEnabled(self, value):
        self._setBool(6, value)
        return

    def getBonusMultiplier(self):
        return self._getNumber(7)

    def setBonusMultiplier(self, value):
        self._setNumber(7, value)
        return

    def getXpDiff(self):
        return self._getNumber(8)

    def setXpDiff(self, value):
        self._setNumber(8, value)
        return

    def getDailyAppliedAdditionalXP(self):
        return self._getNumber(9)

    def setDailyAppliedAdditionalXP(self, value):
        self._setNumber(9, value)
        return

    def getLeftBonusCount(self):
        return self._getNumber(10)

    def setLeftBonusCount(self, value):
        self._setNumber(10, value)
        return

    def getRestriction(self):
        return PremiumXpBonusRestriction(self._getNumber(11))

    def setRestriction(self, value):
        self._setNumber(11, value.value)
        return

    def getState(self):
        return BonusStates(self._getNumber(12))

    def setState(self, value):
        self._setNumber(12, value.value)
        return

    def getLocalStorage(self):
        return self._getString(13)

    def setLocalStorage(self, value):
        self._setString(13, value)
        return

    def getCreditsThreshold(self):
        return self._getNumber(14)

    def setCreditsThreshold(self, value):
        self._setNumber(14, value)
        return

    def getDurationInDays(self):
        return self._getNumber(15)

    def setDurationInDays(self, value):
        self._setNumber(15, value)
        return

    def _initialize(self):
        super(AdditionalBonusModel, self)._initialize()
        self._addBoolProperty(b'hasPremium', False)
        self._addBoolProperty(b'wasPremium', False)
        self._addBoolProperty(b'hasAnyPremium', False)
        self._addStringProperty(b'wotPlusType', WotPlusTypeEnum.NONE.value)
        self._addBoolProperty(b'hasBasicPremium', False)
        self._addBoolProperty(b'hasPenalties', False)
        self._addBoolProperty(b'isXpBonusEnabled', False)
        self._addNumberProperty(b'bonusMultiplier', 0)
        self._addNumberProperty(b'xpDiff', 0)
        self._addNumberProperty(b'dailyAppliedAdditionalXP', 0)
        self._addNumberProperty(b'leftBonusCount', 0)
        self._addNumberProperty(b'restriction', PremiumXpBonusRestriction.NORESTRICTION.value)
        self._addNumberProperty(b'state')
        self._addStringProperty(b'localStorage', b'')
        self._addNumberProperty(b'creditsThreshold', 0)
        self._addNumberProperty(b'durationInDays', 0)
        self.onPremiumXpBonusApplied = self._addCommand(b'onPremiumXpBonusApplied')
        self.onLocalStorageUpdated = self._addCommand(b'onLocalStorageUpdated')
        self.onShowDetails = self._addCommand(b'onShowDetails')
        return
