from frameworks.wulf import ViewModel

class BootcampRewardsTooltipModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=1, commands=0):
        super(BootcampRewardsTooltipModel, self).__init__(properties=properties, commands=commands)
        return

    def getIsNeedAwarding(self):
        return self._getBool(0)

    def setIsNeedAwarding(self, value):
        self._setBool(0, value)
        return

    def _initialize(self):
        super(BootcampRewardsTooltipModel, self)._initialize()
        self._addBoolProperty(b'isNeedAwarding', False)
        return
