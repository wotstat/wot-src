from frameworks.wulf import ViewModel

class AbilitySlotModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=4, commands=0):
        super(AbilitySlotModel, self).__init__(properties=properties, commands=commands)
        return

    def getAbility(self):
        return self._getString(0)

    def setAbility(self, value):
        self._setString(0, value)
        return

    def getTooltipId(self):
        return self._getString(1)

    def setTooltipId(self, value):
        self._setString(1, value)
        return

    def getTooltipHeader(self):
        return self._getString(2)

    def setTooltipHeader(self, value):
        self._setString(2, value)
        return

    def getTooltipBody(self):
        return self._getString(3)

    def setTooltipBody(self, value):
        self._setString(3, value)
        return

    def _initialize(self):
        super(AbilitySlotModel, self)._initialize()
        self._addStringProperty(b'ability', b'')
        self._addStringProperty(b'tooltipId', b'')
        self._addStringProperty(b'tooltipHeader', b'')
        self._addStringProperty(b'tooltipBody', b'')
        return
