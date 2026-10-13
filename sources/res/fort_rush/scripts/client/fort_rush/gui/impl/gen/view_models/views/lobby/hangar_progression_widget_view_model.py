from frameworks.wulf import ViewModel

class HangarProgressionWidgetViewModel(ViewModel):
    __slots__ = (b'onClick',)

    def __init__(self, properties=6, commands=1):
        super(HangarProgressionWidgetViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getIsAvailable(self):
        return self._getBool(0)

    def setIsAvailable(self, value):
        self._setBool(0, value)
        return

    def getAllCollected(self):
        return self._getBool(1)

    def setAllCollected(self, value):
        self._setBool(1, value)
        return

    def getIsNewItem(self):
        return self._getBool(2)

    def setIsNewItem(self, value):
        self._setBool(2, value)
        return

    def getCurrentProgression(self):
        return self._getNumber(3)

    def setCurrentProgression(self, value):
        self._setNumber(3, value)
        return

    def getTotalProgression(self):
        return self._getNumber(4)

    def setTotalProgression(self, value):
        self._setNumber(4, value)
        return

    def getCurrentProgressionStage(self):
        return self._getNumber(5)

    def setCurrentProgressionStage(self, value):
        self._setNumber(5, value)
        return

    def _initialize(self):
        super(HangarProgressionWidgetViewModel, self)._initialize()
        self._addBoolProperty(b'isAvailable', False)
        self._addBoolProperty(b'allCollected', False)
        self._addBoolProperty(b'isNewItem', False)
        self._addNumberProperty(b'currentProgression', 0)
        self._addNumberProperty(b'totalProgression', 0)
        self._addNumberProperty(b'currentProgressionStage', 0)
        self.onClick = self._addCommand(b'onClick')
        return
