from frameworks.wulf import ViewModel

class TankSetupActionModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=7, commands=0):
        super(TankSetupActionModel, self).__init__(properties=properties, commands=commands)
        return

    def getActionType(self):
        return self._getString(0)

    def setActionType(self, value):
        self._setString(0, value)
        return

    def getIntCD(self):
        return self._getNumber(1)

    def setIntCD(self, value):
        self._setNumber(1, value)
        return

    def getInstalledSlotId(self):
        return self._getNumber(2)

    def setInstalledSlotId(self, value):
        self._setNumber(2, value)
        return

    def getLeftID(self):
        return self._getNumber(3)

    def setLeftID(self, value):
        self._setNumber(3, value)
        return

    def getRightID(self):
        return self._getNumber(4)

    def setRightID(self, value):
        self._setNumber(4, value)
        return

    def getLeftIntCD(self):
        return self._getNumber(5)

    def setLeftIntCD(self, value):
        self._setNumber(5, value)
        return

    def getRightIntCD(self):
        return self._getNumber(6)

    def setRightIntCD(self, value):
        self._setNumber(6, value)
        return

    def _initialize(self):
        super(TankSetupActionModel, self)._initialize()
        self._addStringProperty(b'actionType', b'')
        self._addNumberProperty(b'intCD', -1)
        self._addNumberProperty(b'installedSlotId', -1)
        self._addNumberProperty(b'leftID', -1)
        self._addNumberProperty(b'rightID', -1)
        self._addNumberProperty(b'leftIntCD', -1)
        self._addNumberProperty(b'rightIntCD', -1)
        return
