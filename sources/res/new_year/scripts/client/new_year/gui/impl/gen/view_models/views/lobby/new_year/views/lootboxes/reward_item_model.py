from frameworks.wulf import ViewModel

class RewardItemModel(ViewModel):
    __slots__ = ()
    SIZE_ADAPTIVE = 0
    SIZE_SMALL = 1
    SIZE_BIG = 2

    def __init__(self, properties=17, commands=0):
        super(RewardItemModel, self).__init__(properties=properties, commands=commands)
        return

    def getItem(self):
        return self._getString(0)

    def setItem(self, value):
        self._setString(0, value)
        return

    def getName(self):
        return self._getString(1)

    def setName(self, value):
        self._setString(1, value)
        return

    def getIcon(self):
        return self._getString(2)

    def setIcon(self, value):
        self._setString(2, value)
        return

    def getValue(self):
        return self._getString(3)

    def setValue(self, value):
        self._setString(3, value)
        return

    def getBigIcon(self):
        return self._getString(4)

    def setBigIcon(self, value):
        self._setString(4, value)
        return

    def getHighlightType(self):
        return self._getString(5)

    def setHighlightType(self, value):
        self._setString(5, value)
        return

    def getBigHighlightType(self):
        return self._getString(6)

    def setBigHighlightType(self, value):
        self._setString(6, value)
        return

    def getOverlayType(self):
        return self._getString(7)

    def setOverlayType(self, value):
        self._setString(7, value)
        return

    def getBigOverlayType(self):
        return self._getString(8)

    def setBigOverlayType(self, value):
        self._setString(8, value)
        return

    def getHighlightIcon(self):
        return self._getString(9)

    def setHighlightIcon(self, value):
        self._setString(9, value)
        return

    def getBigHighlightIcon(self):
        return self._getString(10)

    def setBigHighlightIcon(self, value):
        self._setString(10, value)
        return

    def getOverlayIcon(self):
        return self._getString(11)

    def setOverlayIcon(self, value):
        self._setString(11, value)
        return

    def getBigOverlayIcon(self):
        return self._getString(12)

    def setBigOverlayIcon(self, value):
        self._setString(12, value)
        return

    def getLabel(self):
        return self._getString(13)

    def setLabel(self, value):
        self._setString(13, value)
        return

    def getAlign(self):
        return self._getString(14)

    def setAlign(self, value):
        self._setString(14, value)
        return

    def getTooltipId(self):
        return self._getNumber(15)

    def setTooltipId(self, value):
        self._setNumber(15, value)
        return

    def getSize(self):
        return self._getNumber(16)

    def setSize(self, value):
        self._setNumber(16, value)
        return

    def _initialize(self):
        super(RewardItemModel, self)._initialize()
        self._addStringProperty(b'item', b'')
        self._addStringProperty(b'name', b'')
        self._addStringProperty(b'icon', b'')
        self._addStringProperty(b'value', b'')
        self._addStringProperty(b'bigIcon', b'')
        self._addStringProperty(b'highlightType', b'')
        self._addStringProperty(b'bigHighlightType', b'')
        self._addStringProperty(b'overlayType', b'')
        self._addStringProperty(b'bigOverlayType', b'')
        self._addStringProperty(b'highlightIcon', b'')
        self._addStringProperty(b'bigHighlightIcon', b'')
        self._addStringProperty(b'overlayIcon', b'')
        self._addStringProperty(b'bigOverlayIcon', b'')
        self._addStringProperty(b'label', b'')
        self._addStringProperty(b'align', b'')
        self._addNumberProperty(b'tooltipId', 0)
        self._addNumberProperty(b'size', 0)
        return
