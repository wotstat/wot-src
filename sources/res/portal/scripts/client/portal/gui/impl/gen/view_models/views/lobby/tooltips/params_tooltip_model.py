from frameworks.wulf import ViewModel

class ParamsTooltipModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=1, commands=0):
        super(ParamsTooltipModel, self).__init__(properties=properties, commands=commands)
        return

    def getName(self):
        return self._getString(0)

    def setName(self, value):
        self._setString(0, value)
        return

    def _initialize(self):
        super(ParamsTooltipModel, self)._initialize()
        self._addStringProperty(b'name', b'')
        return
