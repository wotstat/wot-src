from frameworks.wulf import ViewModel

class OfferRewardModel(ViewModel):
    __slots__ = (b'onClose', b'onAccept')

    def __init__(self, properties=7, commands=2):
        super(OfferRewardModel, self).__init__(properties=properties, commands=commands)
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

    def getTooltipTitle(self):
        return self._getString(2)

    def setTooltipTitle(self, value):
        self._setString(2, value)
        return

    def getTooltipDescription(self):
        return self._getString(3)

    def setTooltipDescription(self, value):
        self._setString(3, value)
        return

    def getCount(self):
        return self._getNumber(4)

    def setCount(self, value):
        self._setNumber(4, value)
        return

    def getBonusType(self):
        return self._getString(5)

    def setBonusType(self, value):
        self._setString(5, value)
        return

    def getHightlightType(self):
        return self._getString(6)

    def setHightlightType(self, value):
        self._setString(6, value)
        return

    def _initialize(self):
        super(OfferRewardModel, self)._initialize()
        self._addStringProperty(b'name', b'')
        self._addStringProperty(b'icon', b'')
        self._addStringProperty(b'tooltipTitle', b'')
        self._addStringProperty(b'tooltipDescription', b'')
        self._addNumberProperty(b'count', 0)
        self._addStringProperty(b'bonusType', b'')
        self._addStringProperty(b'hightlightType', b'')
        self.onClose = self._addCommand(b'onClose')
        self.onAccept = self._addCommand(b'onAccept')
        return
