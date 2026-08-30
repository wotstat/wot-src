from frameworks.wulf import ViewModel

class DailyExperienceViewModel(ViewModel):
    __slots__ = (b'onBackButtonClick', b'onWotPremiumUpgradeButtonClick', b'onWotPlusSubscribeButtonClick', b'onWotPremiumDetailsButtonClick', b'onWotPlusDetailsButtonClick')

    def __init__(self, properties=8, commands=5):
        super(DailyExperienceViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getIsWotPremium(self):
        return self._getBool(0)

    def setIsWotPremium(self, value):
        self._setBool(0, value)
        return

    def getIsWotPlus(self):
        return self._getBool(1)

    def setIsWotPlus(self, value):
        self._setBool(1, value)
        return

    def getIsWotPlusBonusEnabled(self):
        return self._getBool(2)

    def setIsWotPlusBonusEnabled(self, value):
        self._setBool(2, value)
        return

    def getMultiplier(self):
        return self._getNumber(3)

    def setMultiplier(self, value):
        self._setNumber(3, value)
        return

    def getLeftBonusCount(self):
        return self._getNumber(4)

    def setLeftBonusCount(self, value):
        self._setNumber(4, value)
        return

    def getTotalBonusCount(self):
        return self._getNumber(5)

    def setTotalBonusCount(self, value):
        self._setNumber(5, value)
        return

    def getWotPremiumMaxApplications(self):
        return self._getNumber(6)

    def setWotPremiumMaxApplications(self, value):
        self._setNumber(6, value)
        return

    def getWotPlusMaxApplications(self):
        return self._getNumber(7)

    def setWotPlusMaxApplications(self, value):
        self._setNumber(7, value)
        return

    def _initialize(self):
        super(DailyExperienceViewModel, self)._initialize()
        self._addBoolProperty(b'isWotPremium', False)
        self._addBoolProperty(b'isWotPlus', False)
        self._addBoolProperty(b'isWotPlusBonusEnabled', False)
        self._addNumberProperty(b'multiplier', 1)
        self._addNumberProperty(b'leftBonusCount', 0)
        self._addNumberProperty(b'totalBonusCount', 5)
        self._addNumberProperty(b'wotPremiumMaxApplications', 0)
        self._addNumberProperty(b'wotPlusMaxApplications', 0)
        self.onBackButtonClick = self._addCommand(b'onBackButtonClick')
        self.onWotPremiumUpgradeButtonClick = self._addCommand(b'onWotPremiumUpgradeButtonClick')
        self.onWotPlusSubscribeButtonClick = self._addCommand(b'onWotPlusSubscribeButtonClick')
        self.onWotPremiumDetailsButtonClick = self._addCommand(b'onWotPremiumDetailsButtonClick')
        self.onWotPlusDetailsButtonClick = self._addCommand(b'onWotPlusDetailsButtonClick')
        return
