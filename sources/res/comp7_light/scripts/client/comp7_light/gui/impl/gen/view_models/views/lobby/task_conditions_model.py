from frameworks.wulf import ViewModel

class TaskConditionsModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=4, commands=0):
        super(TaskConditionsModel, self).__init__(properties=properties, commands=commands)
        return

    def getCondition(self):
        return self._getString(0)

    def setCondition(self, value):
        self._setString(0, value)
        return

    def getLastValue(self):
        return self._getNumber(1)

    def setLastValue(self, value):
        self._setNumber(1, value)
        return

    def getCurrentValue(self):
        return self._getNumber(2)

    def setCurrentValue(self, value):
        self._setNumber(2, value)
        return

    def getMaxValue(self):
        return self._getNumber(3)

    def setMaxValue(self, value):
        self._setNumber(3, value)
        return

    def _initialize(self):
        super(TaskConditionsModel, self)._initialize()
        self._addStringProperty(b'condition', b'')
        self._addNumberProperty(b'lastValue', 0)
        self._addNumberProperty(b'currentValue', 0)
        self._addNumberProperty(b'maxValue', 0)
        return
