from frameworks.wulf import ViewModel

class LootDefRendererModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=14, commands=0):
        super(LootDefRendererModel, self).__init__(properties=properties, commands=commands)
        return

    def getLabelStr(self):
        return self._getString(0)

    def setLabelStr(self, value):
        self._setString(0, value)
        return

    def getBonusName(self):
        return self._getString(1)

    def setBonusName(self, value):
        self._setString(1, value)
        return

    def getIcon(self):
        return self._getString(2)

    def setIcon(self, value):
        self._setString(2, value)
        return

    def getTooltipId(self):
        return self._getNumber(3)

    def setTooltipId(self, value):
        self._setNumber(3, value)
        return

    def getRendererType(self):
        return self._getString(4)

    def setRendererType(self, value):
        self._setString(4, value)
        return

    def getIsSmall(self):
        return self._getBool(5)

    def setIsSmall(self, value):
        self._setBool(5, value)
        return

    def getIsEpic(self):
        return self._getBool(6)

    def setIsEpic(self, value):
        self._setBool(6, value)
        return

    def getHasCompensation(self):
        return self._getBool(7)

    def setHasCompensation(self, value):
        self._setBool(7, value)
        return

    def getLabelAlign(self):
        return self._getString(8)

    def setLabelAlign(self, value):
        self._setString(8, value)
        return

    def getHighlightType(self):
        return self._getString(9)

    def setHighlightType(self, value):
        self._setString(9, value)
        return

    def getOverlayType(self):
        return self._getString(10)

    def setOverlayType(self, value):
        self._setString(10, value)
        return

    def getIsEnabled(self):
        return self._getBool(11)

    def setIsEnabled(self, value):
        self._setBool(11, value)
        return

    def getRewardName(self):
        return self._getString(12)

    def setRewardName(self, value):
        self._setString(12, value)
        return

    def getSpecialAlias(self):
        return self._getString(13)

    def setSpecialAlias(self, value):
        self._setString(13, value)
        return

    def _initialize(self):
        super(LootDefRendererModel, self)._initialize()
        self._addStringProperty(b'labelStr', b'')
        self._addStringProperty(b'bonusName', b'')
        self._addStringProperty(b'icon', b'')
        self._addNumberProperty(b'tooltipId', 0)
        self._addStringProperty(b'rendererType', b'')
        self._addBoolProperty(b'isSmall', False)
        self._addBoolProperty(b'isEpic', False)
        self._addBoolProperty(b'hasCompensation', False)
        self._addStringProperty(b'labelAlign', b'center')
        self._addStringProperty(b'highlightType', b'')
        self._addStringProperty(b'overlayType', b'')
        self._addBoolProperty(b'isEnabled', True)
        self._addStringProperty(b'rewardName', b'')
        self._addStringProperty(b'specialAlias', b'')
        return
