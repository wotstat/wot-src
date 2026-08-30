from frameworks.wulf import ViewModel

class RewardOptionModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=6, commands=0):
        super(RewardOptionModel, self).__init__(properties=properties, commands=commands)
        return

    def getIconName(self):
        return self._getString(0)

    def setIconName(self, value):
        self._setString(0, value)
        return

    def getName(self):
        return self._getString(1)

    def setName(self, value):
        self._setString(1, value)
        return

    def getGiftId(self):
        return self._getNumber(2)

    def setGiftId(self, value):
        self._setNumber(2, value)
        return

    def getTooltipId(self):
        return self._getString(3)

    def setTooltipId(self, value):
        self._setString(3, value)
        return

    def getCount(self):
        return self._getNumber(4)

    def setCount(self, value):
        self._setNumber(4, value)
        return

    def getDescription(self):
        return self._getString(5)

    def setDescription(self, value):
        self._setString(5, value)
        return

    def _initialize(self):
        super(RewardOptionModel, self)._initialize()
        self._addStringProperty(b'iconName', b'')
        self._addStringProperty(b'name', b'')
        self._addNumberProperty(b'giftId', 0)
        self._addStringProperty(b'tooltipId', b'')
        self._addNumberProperty(b'count', 0)
        self._addStringProperty(b'description', b'')
        return
