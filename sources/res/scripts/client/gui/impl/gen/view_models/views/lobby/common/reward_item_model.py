from frameworks.wulf import ViewModel

class RewardItemModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=6, commands=0):
        super(RewardItemModel, self).__init__(properties=properties, commands=commands)
        return

    def getIcon(self):
        return self._getString(0)

    def setIcon(self, value):
        self._setString(0, value)
        return

    def getName(self):
        return self._getString(1)

    def setName(self, value):
        self._setString(1, value)
        return

    def getValue(self):
        return self._getNumber(2)

    def setValue(self, value):
        self._setNumber(2, value)
        return

    def getTooltipId(self):
        return self._getString(3)

    def setTooltipId(self, value):
        self._setString(3, value)
        return

    def getTooltipContentId(self):
        return self._getNumber(4)

    def setTooltipContentId(self, value):
        self._setNumber(4, value)
        return

    def getOverlayType(self):
        return self._getString(5)

    def setOverlayType(self, value):
        self._setString(5, value)
        return

    def _initialize(self):
        super(RewardItemModel, self)._initialize()
        self._addStringProperty(b'icon', b'')
        self._addStringProperty(b'name', b'')
        self._addNumberProperty(b'value', 0)
        self._addStringProperty(b'tooltipId', b'')
        self._addNumberProperty(b'tooltipContentId', 0)
        self._addStringProperty(b'overlayType', b'')
        return
