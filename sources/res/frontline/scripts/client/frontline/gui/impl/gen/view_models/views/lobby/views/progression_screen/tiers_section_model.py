from frameworks.wulf import Array, ViewModel
from frontline.gui.impl.gen.view_models.views.lobby.views.frontline_reward_model import FrontlineRewardModel

class TiersSectionModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(TiersSectionModel, self).__init__(properties=properties, commands=commands)
        return

    def getStart(self):
        return self._getNumber(0)

    def setStart(self, value):
        self._setNumber(0, value)
        return

    def getEnd(self):
        return self._getNumber(1)

    def setEnd(self, value):
        self._setNumber(1, value)
        return

    def getRewards(self):
        return self._getArray(2)

    def setRewards(self, value):
        self._setArray(2, value)
        return

    @staticmethod
    def getRewardsType():
        return FrontlineRewardModel

    def _initialize(self):
        super(TiersSectionModel, self)._initialize()
        self._addNumberProperty(b'start', 0)
        self._addNumberProperty(b'end', 0)
        self._addArrayProperty(b'rewards', Array())
        return
