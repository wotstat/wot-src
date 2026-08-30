from frameworks.wulf import Array
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.common.missions.bonuses.bonus_model import BonusModel

class WtPortalRewardsBaseModel(ViewModel):
    __slots__ = (b'onClose', b'onBackToPortal', b'onPreview', b'onBuy')

    def __init__(self, properties=4, commands=4):
        super(WtPortalRewardsBaseModel, self).__init__(properties=properties, commands=commands)
        return

    def getIsBoxesEnabled(self):
        return self._getBool(0)

    def setIsBoxesEnabled(self, value):
        self._setBool(0, value)
        return

    def getFirstLaunchReward(self):
        return self._getNumber(1)

    def setFirstLaunchReward(self, value):
        self._setNumber(1, value)
        return

    def getIsFirstLaunch(self):
        return self._getBool(2)

    def setIsFirstLaunch(self, value):
        self._setBool(2, value)
        return

    def getRewards(self):
        return self._getArray(3)

    def setRewards(self, value):
        self._setArray(3, value)
        return

    @staticmethod
    def getRewardsType():
        return BonusModel

    def _initialize(self):
        super(WtPortalRewardsBaseModel, self)._initialize()
        self._addBoolProperty(b'isBoxesEnabled', True)
        self._addNumberProperty(b'firstLaunchReward', 100)
        self._addBoolProperty(b'isFirstLaunch', False)
        self._addArrayProperty(b'rewards', Array())
        self.onClose = self._addCommand(b'onClose')
        self.onBackToPortal = self._addCommand(b'onBackToPortal')
        self.onPreview = self._addCommand(b'onPreview')
        self.onBuy = self._addCommand(b'onBuy')
        return
