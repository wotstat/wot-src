from frameworks.wulf import ViewModel

class MessageModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=8, commands=0):
        super(MessageModel, self).__init__(properties=properties, commands=commands)
        return

    def getId(self):
        return self._getNumber(0)

    def setId(self, value):
        self._setNumber(0, value)
        return

    def getName(self):
        return self._getString(1)

    def setName(self, value):
        self._setString(1, value)
        return

    def getOrder(self):
        return self._getNumber(2)

    def setOrder(self, value):
        self._setNumber(2, value)
        return

    def getViewed(self):
        return self._getBool(3)

    def setViewed(self, value):
        self._setBool(3, value)
        return

    def getSelected(self):
        return self._getBool(4)

    def setSelected(self, value):
        self._setBool(4, value)
        return

    def getSystem(self):
        return self._getBool(5)

    def setSystem(self, value):
        self._setBool(5, value)
        return

    def getPrebattle(self):
        return self._getBool(6)

    def setPrebattle(self, value):
        self._setBool(6, value)
        return

    def getTooltipId(self):
        return self._getString(7)

    def setTooltipId(self, value):
        self._setString(7, value)
        return

    def _initialize(self):
        super(MessageModel, self)._initialize()
        self._addNumberProperty(b'id', 0)
        self._addStringProperty(b'name', b'')
        self._addNumberProperty(b'order', 0)
        self._addBoolProperty(b'viewed', False)
        self._addBoolProperty(b'selected', False)
        self._addBoolProperty(b'system', False)
        self._addBoolProperty(b'prebattle', False)
        self._addStringProperty(b'tooltipId', b'')
        return
