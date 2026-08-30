from frameworks.wulf import ViewModel

class Pm3OperationsTooltipRewardsModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(Pm3OperationsTooltipRewardsModel, self).__init__(properties=properties, commands=commands)
        return

    def getName(self):
        return self._getString(0)

    def setName(self, value):
        self._setString(0, value)
        return

    def getIcon(self):
        return self._getString(1)

    def setIcon(self, value):
        self._setString(1, value)
        return

    def _initialize(self):
        super(Pm3OperationsTooltipRewardsModel, self)._initialize()
        self._addStringProperty(b'name', b'')
        self._addStringProperty(b'icon', b'')
        return
