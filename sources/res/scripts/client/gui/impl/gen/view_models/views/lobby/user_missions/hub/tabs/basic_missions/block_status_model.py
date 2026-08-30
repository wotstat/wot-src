from frameworks.wulf import ViewModel

class BlockStatusModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(BlockStatusModel, self).__init__(properties=properties, commands=commands)
        return

    def getIsEnabled(self):
        return self._getBool(0)

    def setIsEnabled(self, value):
        self._setBool(0, value)
        return

    def getDisabilityReason(self):
        return self._getString(1)

    def setDisabilityReason(self, value):
        self._setString(1, value)
        return

    def _initialize(self):
        super(BlockStatusModel, self)._initialize()
        self._addBoolProperty(b'isEnabled', False)
        self._addStringProperty(b'disabilityReason', b'')
        return
