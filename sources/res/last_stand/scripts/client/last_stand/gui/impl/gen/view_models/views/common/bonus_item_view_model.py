from frameworks.wulf import ViewModel

class BonusItemViewModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=8, commands=0):
        super(BonusItemViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getUserName(self):
        return self._getString(0)

    def setUserName(self, value):
        self._setString(0, value)
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

    def getIcon(self):
        return self._getString(3)

    def setIcon(self, value):
        self._setString(3, value)
        return

    def getOverlayType(self):
        return self._getString(4)

    def setOverlayType(self, value):
        self._setString(4, value)
        return

    def getTooltipId(self):
        return self._getString(5)

    def setTooltipId(self, value):
        self._setString(5, value)
        return

    def getTooltipContentId(self):
        return self._getString(6)

    def setTooltipContentId(self, value):
        self._setString(6, value)
        return

    def getLabel(self):
        return self._getString(7)

    def setLabel(self, value):
        self._setString(7, value)
        return

    def _initialize(self):
        super(BonusItemViewModel, self)._initialize()
        self._addStringProperty(b'userName', b'')
        self._addStringProperty(b'name', b'')
        self._addStringProperty(b'value', b'')
        self._addStringProperty(b'icon', b'')
        self._addStringProperty(b'overlayType', b'')
        self._addStringProperty(b'tooltipId', b'')
        self._addStringProperty(b'tooltipContentId', b'')
        self._addStringProperty(b'label', b'')
        return
