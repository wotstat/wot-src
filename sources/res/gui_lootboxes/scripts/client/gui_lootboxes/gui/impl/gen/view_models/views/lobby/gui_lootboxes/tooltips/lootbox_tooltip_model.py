from frameworks.wulf import ViewModel

class LootboxTooltipModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=4, commands=0):
        super(LootboxTooltipModel, self).__init__(properties=properties, commands=commands)
        return

    def getUserNameKey(self):
        return self._getString(0)

    def setUserNameKey(self, value):
        self._setString(0, value)
        return

    def getDescriptionKey(self):
        return self._getString(1)

    def setDescriptionKey(self, value):
        self._setString(1, value)
        return

    def getTier(self):
        return self._getNumber(2)

    def setTier(self, value):
        self._setNumber(2, value)
        return

    def getCount(self):
        return self._getNumber(3)

    def setCount(self, value):
        self._setNumber(3, value)
        return

    def _initialize(self):
        super(LootboxTooltipModel, self)._initialize()
        self._addStringProperty(b'userNameKey', b'')
        self._addStringProperty(b'descriptionKey', b'')
        self._addNumberProperty(b'tier', 0)
        self._addNumberProperty(b'count', -1)
        return
