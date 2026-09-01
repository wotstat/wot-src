from frameworks.wulf import ViewModel

class LootboxEntryPointViewModel(ViewModel):
    __slots__ = (b'onEntryClick',)

    def __init__(self, properties=3, commands=1):
        super(LootboxEntryPointViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getIsEnabled(self):
        return self._getBool(0)

    def setIsEnabled(self, value):
        self._setBool(0, value)
        return

    def getBoxesCount(self):
        return self._getNumber(1)

    def setBoxesCount(self, value):
        self._setNumber(1, value)
        return

    def getEventName(self):
        return self._getString(2)

    def setEventName(self, value):
        self._setString(2, value)
        return

    def _initialize(self):
        super(LootboxEntryPointViewModel, self)._initialize()
        self._addBoolProperty(b'isEnabled', False)
        self._addNumberProperty(b'boxesCount', 0)
        self._addStringProperty(b'eventName', b'wt')
        self.onEntryClick = self._addCommand(b'onEntryClick')
        return
