from frameworks.wulf import ViewModel

class LootBoxCategoryTooltipModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=1, commands=0):
        super(LootBoxCategoryTooltipModel, self).__init__(properties=properties, commands=commands)
        return

    def getCategory(self):
        return self._getString(0)

    def setCategory(self, value):
        self._setString(0, value)
        return

    def _initialize(self):
        super(LootBoxCategoryTooltipModel, self)._initialize()
        self._addStringProperty(b'category', b'')
        return
