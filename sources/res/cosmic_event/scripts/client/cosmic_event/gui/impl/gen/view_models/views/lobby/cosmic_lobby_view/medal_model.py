from frameworks.wulf import ViewModel

class MedalModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=4, commands=0):
        super(MedalModel, self).__init__(properties=properties, commands=commands)
        return

    def getName(self):
        return self._getString(0)

    def setName(self, value):
        self._setString(0, value)
        return

    def getTooltipId(self):
        return self._getString(1)

    def setTooltipId(self, value):
        self._setString(1, value)
        return

    def getTooltipContentId(self):
        return self._getString(2)

    def setTooltipContentId(self, value):
        self._setString(2, value)
        return

    def getIsReceived(self):
        return self._getBool(3)

    def setIsReceived(self, value):
        self._setBool(3, value)
        return

    def _initialize(self):
        super(MedalModel, self)._initialize()
        self._addStringProperty(b'name', b'')
        self._addStringProperty(b'tooltipId', b'')
        self._addStringProperty(b'tooltipContentId', b'')
        self._addBoolProperty(b'isReceived', False)
        return
