from frameworks.wulf import ViewModel

class WotPlusSubscriptionBonusModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(WotPlusSubscriptionBonusModel, self).__init__(properties=properties, commands=commands)
        return

    def getLabel(self):
        return self._getString(0)

    def setLabel(self, value):
        self._setString(0, value)
        return

    def getType(self):
        return self._getString(1)

    def setType(self, value):
        self._setString(1, value)
        return

    def _initialize(self):
        super(WotPlusSubscriptionBonusModel, self)._initialize()
        self._addStringProperty(b'label', b'')
        self._addStringProperty(b'type', b'')
        return
