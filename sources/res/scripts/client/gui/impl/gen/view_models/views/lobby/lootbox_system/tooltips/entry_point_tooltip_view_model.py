from frameworks.wulf import ViewModel

class EntryPointTooltipViewModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(EntryPointTooltipViewModel, self).__init__(properties=properties, commands=commands)
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

    def getEventExpireTime(self):
        return self._getNumber(2)

    def setEventExpireTime(self, value):
        self._setNumber(2, value)
        return

    def _initialize(self):
        super(EntryPointTooltipViewModel, self)._initialize()
        self._addStringProperty(b'eventName', b'')
        self._addBoolProperty(b'isEnabled', False)
        self._addNumberProperty(b'eventExpireTime', 0)
        return
