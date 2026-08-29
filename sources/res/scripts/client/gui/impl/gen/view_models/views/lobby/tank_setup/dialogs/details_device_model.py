from frameworks.wulf import ViewModel

class DetailsDeviceModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(DetailsDeviceModel, self).__init__(properties=properties, commands=commands)
        return

    def getOverlayType(self):
        return self._getString(0)

    def setOverlayType(self, value):
        self._setString(0, value)
        return

    def getLevel(self):
        return self._getNumber(1)

    def setLevel(self, value):
        self._setNumber(1, value)
        return

    def getDeviceName(self):
        return self._getString(2)

    def setDeviceName(self, value):
        self._setString(2, value)
        return

    def _initialize(self):
        super(DetailsDeviceModel, self)._initialize()
        self._addStringProperty(b'overlayType', b'')
        self._addNumberProperty(b'level', 0)
        self._addStringProperty(b'deviceName', b'')
        return
