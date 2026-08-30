from frameworks.wulf import ViewModel

class BattleMattersTokenTooltipViewModel(ViewModel):
    __slots__ = ()
    ARG_REWARD_TOKEN = b'rewardToken'

    def __init__(self, properties=2, commands=0):
        super(BattleMattersTokenTooltipViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getEndDate(self):
        return self._getNumber(0)

    def setEndDate(self, value):
        self._setNumber(0, value)
        return

    def getVehiclesLevel(self):
        return self._getNumber(1)

    def setVehiclesLevel(self, value):
        self._setNumber(1, value)
        return

    def _initialize(self):
        super(BattleMattersTokenTooltipViewModel, self)._initialize()
        self._addNumberProperty(b'endDate', 0)
        self._addNumberProperty(b'vehiclesLevel', 0)
        return
