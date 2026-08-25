from frameworks.wulf import ViewModel

class BuyVehicleSimpleTooltipModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(BuyVehicleSimpleTooltipModel, self).__init__(properties=properties, commands=commands)
        return

    def getTooltipId(self):
        return self._getString(0)

    def setTooltipId(self, value):
        self._setString(0, value)
        return

    def getHeader(self):
        return self._getString(1)

    def setHeader(self, value):
        self._setString(1, value)
        return

    def getBody(self):
        return self._getString(2)

    def setBody(self, value):
        self._setString(2, value)
        return

    def _initialize(self):
        super(BuyVehicleSimpleTooltipModel, self)._initialize()
        self._addStringProperty(b'tooltipId', b'')
        self._addStringProperty(b'header', b'')
        self._addStringProperty(b'body', b'')
        return
