from frameworks.wulf import ViewModel

class NodeTechTreeModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=15, commands=0):
        super(NodeTechTreeModel, self).__init__(properties=properties, commands=commands)
        return

    def getId(self):
        return self._getNumber(0)

    def setId(self, value):
        self._setNumber(0, value)
        return

    def getState(self):
        return self._getNumber(1)

    def setState(self, value):
        self._setNumber(1, value)
        return

    def getExtendedState(self):
        return self._getNumber(2)

    def setExtendedState(self, value):
        self._setNumber(2, value)
        return

    def getItemLevel(self):
        return self._getNumber(3)

    def setItemLevel(self, value):
        self._setNumber(3, value)
        return

    def getBlueprintCanConvert(self):
        return self._getBool(4)

    def setBlueprintCanConvert(self, value):
        self._setBool(4, value)
        return

    def getBlueprintMaxCount(self):
        return self._getNumber(5)

    def setBlueprintMaxCount(self, value):
        self._setNumber(5, value)
        return

    def getBlueprintBalance(self):
        return self._getNumber(6)

    def setBlueprintBalance(self, value):
        self._setNumber(6, value)
        return

    def getEarnedXP(self):
        return self._getNumber(7)

    def setEarnedXP(self, value):
        self._setNumber(7, value)
        return

    def getIsRemovable(self):
        return self._getBool(8)

    def setIsRemovable(self, value):
        self._setBool(8, value)
        return

    def getItemType(self):
        return self._getString(9)

    def setItemType(self, value):
        self._setString(9, value)
        return

    def getColumn(self):
        return self._getNumber(10)

    def setColumn(self, value):
        self._setNumber(10, value)
        return

    def getRow(self):
        return self._getNumber(11)

    def setRow(self, value):
        self._setNumber(11, value)
        return

    def getNation(self):
        return self._getString(12)

    def setNation(self, value):
        self._setString(12, value)
        return

    def getEarlyAccessPrice(self):
        return self._getNumber(13)

    def setEarlyAccessPrice(self, value):
        self._setNumber(13, value)
        return

    def getIsEarlyAccessLocked(self):
        return self._getBool(14)

    def setIsEarlyAccessLocked(self, value):
        self._setBool(14, value)
        return

    def _initialize(self):
        super(NodeTechTreeModel, self)._initialize()
        self._addNumberProperty(b'id', 0)
        self._addNumberProperty(b'state', 0)
        self._addNumberProperty(b'extendedState', 0)
        self._addNumberProperty(b'itemLevel', 0)
        self._addBoolProperty(b'blueprintCanConvert', False)
        self._addNumberProperty(b'blueprintMaxCount', 0)
        self._addNumberProperty(b'blueprintBalance', 0)
        self._addNumberProperty(b'earnedXP', 0)
        self._addBoolProperty(b'isRemovable', False)
        self._addStringProperty(b'itemType', b'')
        self._addNumberProperty(b'column', 0)
        self._addNumberProperty(b'row', 0)
        self._addStringProperty(b'nation', b'')
        self._addNumberProperty(b'earlyAccessPrice', 0)
        self._addBoolProperty(b'isEarlyAccessLocked', False)
        return
