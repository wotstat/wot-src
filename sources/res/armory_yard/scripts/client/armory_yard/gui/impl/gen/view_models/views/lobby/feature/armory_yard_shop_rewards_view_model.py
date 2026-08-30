from frameworks.wulf import ViewModel

class ArmoryYardShopRewardsViewModel(ViewModel):
    __slots__ = (b'onClose',)

    def __init__(self, properties=4, commands=1):
        super(ArmoryYardShopRewardsViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getDescription(self):
        return self._getString(0)

    def setDescription(self, value):
        self._setString(0, value)
        return

    def getIcon(self):
        return self._getString(1)

    def setIcon(self, value):
        self._setString(1, value)
        return

    def getCount(self):
        return self._getNumber(2)

    def setCount(self, value):
        self._setNumber(2, value)
        return

    def getItemType(self):
        return self._getString(3)

    def setItemType(self, value):
        self._setString(3, value)
        return

    def _initialize(self):
        super(ArmoryYardShopRewardsViewModel, self)._initialize()
        self._addStringProperty(b'description', b'')
        self._addStringProperty(b'icon', b'')
        self._addNumberProperty(b'count', 0)
        self._addStringProperty(b'itemType', b'')
        self.onClose = self._addCommand(b'onClose')
        return
