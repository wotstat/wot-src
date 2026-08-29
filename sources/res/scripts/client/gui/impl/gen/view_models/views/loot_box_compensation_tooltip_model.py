from frameworks.wulf import ViewModel

class LootBoxCompensationTooltipModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=7, commands=0):
        super(LootBoxCompensationTooltipModel, self).__init__(properties=properties, commands=commands)
        return

    def getIconBefore(self):
        return self._getString(0)

    def setIconBefore(self, value):
        self._setString(0, value)
        return

    def getIconAfter(self):
        return self._getString(1)

    def setIconAfter(self, value):
        self._setString(1, value)
        return

    def getLabelBefore(self):
        return self._getString(2)

    def setLabelBefore(self, value):
        self._setString(2, value)
        return

    def getLabelAfter(self):
        return self._getString(3)

    def setLabelAfter(self, value):
        self._setString(3, value)
        return

    def getBonusName(self):
        return self._getString(4)

    def setBonusName(self, value):
        self._setString(4, value)
        return

    def getTooltipType(self):
        return self._getString(5)

    def setTooltipType(self, value):
        self._setString(5, value)
        return

    def getCountBefore(self):
        return self._getNumber(6)

    def setCountBefore(self, value):
        self._setNumber(6, value)
        return

    def _initialize(self):
        super(LootBoxCompensationTooltipModel, self)._initialize()
        self._addStringProperty(b'iconBefore', b'')
        self._addStringProperty(b'iconAfter', b'')
        self._addStringProperty(b'labelBefore', b'')
        self._addStringProperty(b'labelAfter', b'')
        self._addStringProperty(b'bonusName', b'')
        self._addStringProperty(b'tooltipType', b'base')
        self._addNumberProperty(b'countBefore', 1)
        return
