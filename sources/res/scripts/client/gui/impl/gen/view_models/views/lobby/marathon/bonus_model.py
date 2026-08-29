from frameworks.wulf import ViewModel

class BonusModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=6, commands=0):
        super(BonusModel, self).__init__(properties=properties, commands=commands)
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

    def getLabel(self):
        return self._getString(2)

    def setLabel(self, value):
        self._setString(2, value)
        return

    def getTooltipId(self):
        return self._getString(3)

    def setTooltipId(self, value):
        self._setString(3, value)
        return

    def getOverlayType(self):
        return self._getString(4)

    def setOverlayType(self, value):
        self._setString(4, value)
        return

    def getDescription(self):
        return self._getString(5)

    def setDescription(self, value):
        self._setString(5, value)
        return

    def _initialize(self):
        super(BonusModel, self)._initialize()
        self._addStringProperty(b'name', b'')
        self._addStringProperty(b'icon', b'')
        self._addStringProperty(b'label', b'')
        self._addStringProperty(b'tooltipId', b'')
        self._addStringProperty(b'overlayType', b'')
        self._addStringProperty(b'description', b'')
        return
