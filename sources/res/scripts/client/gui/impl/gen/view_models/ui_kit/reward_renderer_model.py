from frameworks.wulf import ViewModel

class RewardRendererModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=8, commands=0):
        super(RewardRendererModel, self).__init__(properties=properties, commands=commands)
        return

    def getLabelStr(self):
        return self._getString(0)

    def setLabelStr(self, value):
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

    def getHighlightType(self):
        return self._getString(3)

    def setHighlightType(self, value):
        self._setString(3, value)
        return

    def getOverlayType(self):
        return self._getString(4)

    def setOverlayType(self, value):
        self._setString(4, value)
        return

    def getHasCompensation(self):
        return self._getBool(5)

    def setHasCompensation(self, value):
        self._setBool(5, value)
        return

    def getLabelAlign(self):
        return self._getString(6)

    def setLabelAlign(self, value):
        self._setString(6, value)
        return

    def getIconSize(self):
        return self._getString(7)

    def setIconSize(self, value):
        self._setString(7, value)
        return

    def _initialize(self):
        super(RewardRendererModel, self)._initialize()
        self._addStringProperty(b'labelStr', b'')
        self._addStringProperty(b'icon', b'')
        self._addNumberProperty(b'tooltipId', 0)
        self._addStringProperty(b'highlightType', b'')
        self._addStringProperty(b'overlayType', b'')
        self._addBoolProperty(b'hasCompensation', False)
        self._addStringProperty(b'labelAlign', b'center')
        self._addStringProperty(b'iconSize', b'small')
        return
