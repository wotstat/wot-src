from frameworks.wulf import Array
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.common.missions.bonuses.icon_bonus_model import IconBonusModel

class WtEventAwardViewModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=5, commands=0):
        super(WtEventAwardViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getTitle(self):
        return self._getString(0)

    def setTitle(self, value):
        self._setString(0, value)
        return

    def getStatus(self):
        return self._getString(1)

    def setStatus(self, value):
        self._setString(1, value)
        return

    def getIsValuableReward(self):
        return self._getBool(2)

    def setIsValuableReward(self, value):
        self._setBool(2, value)
        return

    def getIsPostBattle(self):
        return self._getBool(3)

    def setIsPostBattle(self, value):
        self._setBool(3, value)
        return

    def getMainRewards(self):
        return self._getArray(4)

    def setMainRewards(self, value):
        self._setArray(4, value)
        return

    @staticmethod
    def getMainRewardsType():
        return IconBonusModel

    def _initialize(self):
        super(WtEventAwardViewModel, self)._initialize()
        self._addStringProperty(b'title', b'')
        self._addStringProperty(b'status', b'')
        self._addBoolProperty(b'isValuableReward', False)
        self._addBoolProperty(b'isPostBattle', False)
        self._addArrayProperty(b'mainRewards', Array())
        return
