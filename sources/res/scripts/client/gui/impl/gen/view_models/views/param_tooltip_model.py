from frameworks.wulf import ViewModel

class ParamTooltipModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(ParamTooltipModel, self).__init__(properties=properties, commands=commands)
        return

    def getType(self):
        return self._getString(0)

    def setType(self, value):
        self._setString(0, value)
        return

    def getParams(self):
        return self._getString(1)

    def setParams(self, value):
        self._setString(1, value)
        return

    def getResId(self):
        return self._getNumber(2)

    def setResId(self, value):
        self._setNumber(2, value)
        return

    def _initialize(self):
        super(ParamTooltipModel, self)._initialize()
        self._addStringProperty(b'type', b'')
        self._addStringProperty(b'params', b'{}')
        self._addNumberProperty(b'resId', 0)
        return
