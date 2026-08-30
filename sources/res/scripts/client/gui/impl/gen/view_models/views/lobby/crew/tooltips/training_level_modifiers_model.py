from frameworks.wulf import ViewModel

class TrainingLevelModifiersModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(TrainingLevelModifiersModel, self).__init__(properties=properties, commands=commands)
        return

    def getValue(self):
        return self._getReal(0)

    def setValue(self, value):
        self._setReal(0, value)
        return

    def getReason(self):
        return self._getString(1)

    def setReason(self, value):
        self._setString(1, value)
        return

    def _initialize(self):
        super(TrainingLevelModifiersModel, self)._initialize()
        self._addRealProperty(b'value', 0.0)
        self._addStringProperty(b'reason', b'')
        return
