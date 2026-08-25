from frameworks.wulf import Array, ViewModel
from gui.impl.gen.view_models.common.missions.bonuses.icon_bonus_model import IconBonusModel

class JmRewardsViewModel(ViewModel):
    __slots__ = (b'onClose',)

    def __init__(self, properties=1, commands=1):
        super(JmRewardsViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getRewards(self):
        return self._getArray(0)

    def setRewards(self, value):
        self._setArray(0, value)
        return

    @staticmethod
    def getRewardsType():
        return IconBonusModel

    def _initialize(self):
        super(JmRewardsViewModel, self)._initialize()
        self._addArrayProperty(b'rewards', Array())
        self.onClose = self._addCommand(b'onClose')
        return
