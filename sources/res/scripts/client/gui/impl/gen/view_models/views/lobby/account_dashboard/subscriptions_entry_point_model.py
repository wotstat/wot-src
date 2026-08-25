from frameworks.wulf import ViewModel

class SubscriptionsEntryPointModel(ViewModel):
    __slots__ = (b'onClick',)

    def __init__(self, properties=1, commands=1):
        super(SubscriptionsEntryPointModel, self).__init__(properties=properties, commands=commands)
        return

    def getIsEnabled(self):
        return self._getBool(0)

    def setIsEnabled(self, value):
        self._setBool(0, value)
        return

    def _initialize(self):
        super(SubscriptionsEntryPointModel, self)._initialize()
        self._addBoolProperty(b'isEnabled', True)
        self.onClick = self._addCommand(b'onClick')
        return
