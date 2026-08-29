from frameworks.wulf import ViewModel

class LoadingResourceModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=4, commands=0):
        super(LoadingResourceModel, self).__init__(properties=properties, commands=commands)
        return

    def getType(self):
        return self._getString(0)

    def setType(self, value):
        self._setString(0, value)
        return

    def getSubType(self):
        return self._getString(1)

    def setSubType(self, value):
        self._setString(1, value)
        return

    def getCount(self):
        return self._getNumber(2)

    def setCount(self, value):
        self._setNumber(2, value)
        return

    def getTooltipId(self):
        return self._getString(3)

    def setTooltipId(self, value):
        self._setString(3, value)
        return

    def _initialize(self):
        super(LoadingResourceModel, self)._initialize()
        self._addStringProperty(b'type', b'')
        self._addStringProperty(b'subType', b'')
        self._addNumberProperty(b'count', 0)
        self._addStringProperty(b'tooltipId', b'')
        return
