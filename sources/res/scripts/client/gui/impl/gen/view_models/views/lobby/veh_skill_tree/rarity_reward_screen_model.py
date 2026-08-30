from frameworks.wulf import ViewModel

class RarityRewardScreenModel(ViewModel):
    __slots__ = (b'onClose',)

    def __init__(self, properties=3, commands=1):
        super(RarityRewardScreenModel, self).__init__(properties=properties, commands=commands)
        return

    def getName(self):
        return self._getString(0)

    def setName(self, value):
        self._setString(0, value)
        return

    def getTitle(self):
        return self._getString(1)

    def setTitle(self, value):
        self._setString(1, value)
        return

    def getRarity(self):
        return self._getString(2)

    def setRarity(self, value):
        self._setString(2, value)
        return

    def _initialize(self):
        super(RarityRewardScreenModel, self)._initialize()
        self._addStringProperty(b'name', b'')
        self._addStringProperty(b'title', b'')
        self._addStringProperty(b'rarity', b'')
        self.onClose = self._addCommand(b'onClose')
        return
