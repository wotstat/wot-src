from frameworks.wulf import ViewModel

class HangarProgressionViewModel(ViewModel):
    __slots__ = (b'onClick',)

    def __init__(self, properties=4, commands=1):
        super(HangarProgressionViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getAllCollected(self):
        return self._getBool(0)

    def setAllCollected(self, value):
        self._setBool(0, value)
        return

    def getIsNewItem(self):
        return self._getBool(1)

    def setIsNewItem(self, value):
        self._setBool(1, value)
        return

    def getCurrentProgression(self):
        return self._getNumber(2)

    def setCurrentProgression(self, value):
        self._setNumber(2, value)
        return

    def getTotalProgression(self):
        return self._getNumber(3)

    def setTotalProgression(self, value):
        self._setNumber(3, value)
        return

    def _initialize(self):
        super(HangarProgressionViewModel, self)._initialize()
        self._addBoolProperty(b'allCollected', False)
        self._addBoolProperty(b'isNewItem', False)
        self._addNumberProperty(b'currentProgression', 0)
        self._addNumberProperty(b'totalProgression', 0)
        self.onClick = self._addCommand(b'onClick')
        return
