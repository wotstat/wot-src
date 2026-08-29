from frameworks.wulf import ViewModel

class Pm3QuestItemPartProgressModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=5, commands=0):
        super(Pm3QuestItemPartProgressModel, self).__init__(properties=properties, commands=commands)
        return

    def getTo(self):
        return self._getNumber(0)

    def setTo(self, value):
        self._setNumber(0, value)
        return

    def getCurrentValue(self):
        return self._getNumber(1)

    def setCurrentValue(self, value):
        self._setNumber(1, value)
        return

    def getPreviousValue(self):
        return self._getNumber(2)

    def setPreviousValue(self, value):
        self._setNumber(2, value)
        return

    def getIcon(self):
        return self._getString(3)

    def setIcon(self, value):
        self._setString(3, value)
        return

    def getIsFailed(self):
        return self._getBool(4)

    def setIsFailed(self, value):
        self._setBool(4, value)
        return

    def _initialize(self):
        super(Pm3QuestItemPartProgressModel, self)._initialize()
        self._addNumberProperty(b'to', 0)
        self._addNumberProperty(b'currentValue', 0)
        self._addNumberProperty(b'previousValue', 0)
        self._addStringProperty(b'icon', b'')
        self._addBoolProperty(b'isFailed', False)
        return
