from frameworks.wulf import ViewModel

class BootcampRewardItemModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(BootcampRewardItemModel, self).__init__(properties=properties, commands=commands)
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

    def getTooltipId(self):
        return self._getNumber(2)

    def setTooltipId(self, value):
        self._setNumber(2, value)
        return

    def _initialize(self):
        super(BootcampRewardItemModel, self)._initialize()
        self._addStringProperty(b'name', b'')
        self._addStringProperty(b'icon', b'')
        self._addNumberProperty(b'tooltipId', 0)
        return
