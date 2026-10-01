from frameworks.wulf import ViewModel

class AbilityTooltipExtraParamItemModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(AbilityTooltipExtraParamItemModel, self).__init__(properties=properties, commands=commands)
        return

    def getParamKey(self):
        return self._getString(0)

    def setParamKey(self, value):
        self._setString(0, value)
        return

    def getValue(self):
        return self._getString(1)

    def setValue(self, value):
        self._setString(1, value)
        return

    def getDescription(self):
        return self._getString(2)

    def setDescription(self, value):
        self._setString(2, value)
        return

    def _initialize(self):
        super(AbilityTooltipExtraParamItemModel, self)._initialize()
        self._addStringProperty(b'paramKey', b'')
        self._addStringProperty(b'value', b'')
        self._addStringProperty(b'description', b'')
        return
