from frameworks.wulf import ViewModel

class BonusModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=8, commands=0):
        super(BonusModel, self).__init__(properties=properties, commands=commands)
        return

    def getIndex(self):
        return self._getNumber(0)

    def setIndex(self, value):
        self._setNumber(0, value)
        return

    def getName(self):
        return self._getString(1)

    def setName(self, value):
        self._setString(1, value)
        return

    def getValue(self):
        return self._getString(2)

    def setValue(self, value):
        self._setString(2, value)
        return

    def getIsCompensation(self):
        return self._getBool(3)

    def setIsCompensation(self, value):
        self._setBool(3, value)
        return

    def getTooltipId(self):
        return self._getString(4)

    def setTooltipId(self, value):
        self._setString(4, value)
        return

    def getTooltipContentId(self):
        return self._getString(5)

    def setTooltipContentId(self, value):
        self._setString(5, value)
        return

    def getLabel(self):
        return self._getString(6)

    def setLabel(self, value):
        self._setString(6, value)
        return

    def getProbability(self):
        return self._getNumber(7)

    def setProbability(self, value):
        self._setNumber(7, value)
        return

    def _initialize(self):
        super(BonusModel, self)._initialize()
        self._addNumberProperty(b'index', 0)
        self._addStringProperty(b'name', b'')
        self._addStringProperty(b'value', b'')
        self._addBoolProperty(b'isCompensation', False)
        self._addStringProperty(b'tooltipId', b'')
        self._addStringProperty(b'tooltipContentId', b'')
        self._addStringProperty(b'label', b'')
        self._addNumberProperty(b'probability', 0)
        return
