from frameworks.wulf import ViewModel

class CustomizationRarityRewardScreenModel(ViewModel):
    __slots__ = (b'goToExterior', b'goToGarage')

    def __init__(self, properties=5, commands=2):
        super(CustomizationRarityRewardScreenModel, self).__init__(properties=properties, commands=commands)
        return

    def getIsFirstAttachment(self):
        return self._getBool(0)

    def setIsFirstAttachment(self, value):
        self._setBool(0, value)
        return

    def getName(self):
        return self._getString(1)

    def setName(self, value):
        self._setString(1, value)
        return

    def getTitle(self):
        return self._getString(2)

    def setTitle(self, value):
        self._setString(2, value)
        return

    def getRarity(self):
        return self._getString(3)

    def setRarity(self, value):
        self._setString(3, value)
        return

    def getIsExteriorEnabled(self):
        return self._getBool(4)

    def setIsExteriorEnabled(self, value):
        self._setBool(4, value)
        return

    def _initialize(self):
        super(CustomizationRarityRewardScreenModel, self)._initialize()
        self._addBoolProperty(b'isFirstAttachment', False)
        self._addStringProperty(b'name', b'')
        self._addStringProperty(b'title', b'')
        self._addStringProperty(b'rarity', b'')
        self._addBoolProperty(b'isExteriorEnabled', False)
        self.goToExterior = self._addCommand(b'goToExterior')
        self.goToGarage = self._addCommand(b'goToGarage')
        return
