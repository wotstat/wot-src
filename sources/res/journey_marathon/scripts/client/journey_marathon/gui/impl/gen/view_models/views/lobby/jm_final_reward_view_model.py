from frameworks.wulf import Array, ViewModel
from gui.impl.gen.view_models.common.missions.bonuses.icon_bonus_model import IconBonusModel
from journey_marathon.gui.impl.gen.view_models.views.lobby.jm_bonus_model import JmBonusModel

class JmFinalRewardViewModel(ViewModel):
    __slots__ = (b'onClose',)

    def __init__(self, properties=2, commands=1):
        super(JmFinalRewardViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getMainRewards(self):
        return self._getArray(0)

    def setMainRewards(self, value):
        self._setArray(0, value)
        return

    @staticmethod
    def getMainRewardsType():
        return JmBonusModel

    def getAdditionalRewards(self):
        return self._getArray(1)

    def setAdditionalRewards(self, value):
        self._setArray(1, value)
        return

    @staticmethod
    def getAdditionalRewardsType():
        return IconBonusModel

    def _initialize(self):
        super(JmFinalRewardViewModel, self)._initialize()
        self._addArrayProperty(b'mainRewards', Array())
        self._addArrayProperty(b'additionalRewards', Array())
        self.onClose = self._addCommand(b'onClose')
        return
