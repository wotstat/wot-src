from frameworks.wulf import ViewModel

class EntryPointViewModel(ViewModel):
    __slots__ = (b'onEntryClick',)

    def __init__(self, properties=5, commands=1):
        super(EntryPointViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getEventName(self):
        return self._getString(0)

    def setEventName(self, value):
        self._setString(0, value)
        return

    def getIsEnabled(self):
        return self._getBool(1)

    def setIsEnabled(self, value):
        self._setBool(1, value)
        return

    def getBoxesCount(self):
        return self._getNumber(2)

    def setBoxesCount(self, value):
        self._setNumber(2, value)
        return

    def getHasNew(self):
        return self._getBool(3)

    def setHasNew(self, value):
        self._setBool(3, value)
        return

    def getEventExpireTime(self):
        return self._getNumber(4)

    def setEventExpireTime(self, value):
        self._setNumber(4, value)
        return

    def _initialize(self):
        super(EntryPointViewModel, self)._initialize()
        self._addStringProperty(b'eventName', b'')
        self._addBoolProperty(b'isEnabled', False)
        self._addNumberProperty(b'boxesCount', 0)
        self._addBoolProperty(b'hasNew', False)
        self._addNumberProperty(b'eventExpireTime', 0)
        self.onEntryClick = self._addCommand(b'onEntryClick')
        return
