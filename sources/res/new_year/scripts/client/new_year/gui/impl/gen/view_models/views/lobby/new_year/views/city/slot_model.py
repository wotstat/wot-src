from gui.impl.gen import R
from frameworks.wulf import ViewModel

class SlotModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=8, commands=0):
        super(SlotModel, self).__init__(properties=properties, commands=commands)
        return

    def getSlotId(self):
        return self._getNumber(0)

    def setSlotId(self, value):
        self._setNumber(0, value)
        return

    def getToyId(self):
        return self._getNumber(1)

    def setToyId(self, value):
        self._setNumber(1, value)
        return

    def getRank(self):
        return self._getNumber(2)

    def setRank(self, value):
        self._setNumber(2, value)
        return

    def getIcon(self):
        return self._getResource(3)

    def setIcon(self, value):
        self._setResource(3, value)
        return

    def getType(self):
        return self._getString(4)

    def setType(self, value):
        self._setString(4, value)
        return

    def getIsBetterAvailable(self):
        return self._getBool(5)

    def setIsBetterAvailable(self, value):
        self._setBool(5, value)
        return

    def getIsEmpty(self):
        return self._getBool(6)

    def setIsEmpty(self, value):
        self._setBool(6, value)
        return

    def getIsSelected(self):
        return self._getBool(7)

    def setIsSelected(self, value):
        self._setBool(7, value)
        return

    def _initialize(self):
        super(SlotModel, self)._initialize()
        self._addNumberProperty(b'slotId', 0)
        self._addNumberProperty(b'toyId', 0)
        self._addNumberProperty(b'rank', 0)
        self._addResourceProperty(b'icon', R.invalid())
        self._addStringProperty(b'type', b'')
        self._addBoolProperty(b'isBetterAvailable', False)
        self._addBoolProperty(b'isEmpty', True)
        self._addBoolProperty(b'isSelected', False)
        return
