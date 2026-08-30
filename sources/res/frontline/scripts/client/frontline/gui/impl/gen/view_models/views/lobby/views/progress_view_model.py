from frameworks.wulf import Array
from frameworks.wulf import ViewModel
from frontline.gui.impl.gen.view_models.views.lobby.views.frontline_reward_model import FrontlineRewardModel

class ProgressViewModel(ViewModel):
    __slots__ = (b'onShopClick',)

    def __init__(self, properties=9, commands=1):
        super(ProgressViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getFrontlineState(self):
        return self._getString(0)

    def setFrontlineState(self, value):
        self._setString(0, value)
        return

    def getCountdownSeconds(self):
        return self._getNumber(1)

    def setCountdownSeconds(self, value):
        self._setNumber(1, value)
        return

    def getPendingDate(self):
        return self._getNumber(2)

    def setPendingDate(self, value):
        self._setNumber(2, value)
        return

    def getLevel(self):
        return self._getNumber(3)

    def setLevel(self, value):
        self._setNumber(3, value)
        return

    def getIsMaxLevel(self):
        return self._getBool(4)

    def setIsMaxLevel(self, value):
        self._setBool(4, value)
        return

    def getIsShopBannerVisible(self):
        return self._getBool(5)

    def setIsShopBannerVisible(self, value):
        self._setBool(5, value)
        return

    def getCurrentPoints(self):
        return self._getNumber(6)

    def setCurrentPoints(self, value):
        self._setNumber(6, value)
        return

    def getNeededPoints(self):
        return self._getNumber(7)

    def setNeededPoints(self, value):
        self._setNumber(7, value)
        return

    def getRewards(self):
        return self._getArray(8)

    def setRewards(self, value):
        self._setArray(8, value)
        return

    @staticmethod
    def getRewardsType():
        return FrontlineRewardModel

    def _initialize(self):
        super(ProgressViewModel, self)._initialize()
        self._addStringProperty(b'frontlineState', b'')
        self._addNumberProperty(b'countdownSeconds', 0)
        self._addNumberProperty(b'pendingDate', 0)
        self._addNumberProperty(b'level', 0)
        self._addBoolProperty(b'isMaxLevel', False)
        self._addBoolProperty(b'isShopBannerVisible', False)
        self._addNumberProperty(b'currentPoints', 0)
        self._addNumberProperty(b'neededPoints', 0)
        self._addArrayProperty(b'rewards', Array())
        self.onShopClick = self._addCommand(b'onShopClick')
        return
