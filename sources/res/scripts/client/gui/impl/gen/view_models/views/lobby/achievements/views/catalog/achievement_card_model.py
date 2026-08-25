from gui.impl.gen.view_models.views.lobby.achievements.views.catalog.details_model import DetailsModel

class AchievementCardModel(DetailsModel):
    __slots__ = ()

    def __init__(self, properties=26, commands=0):
        super(AchievementCardModel, self).__init__(properties=properties, commands=commands)
        return

    def getIsProgressive(self):
        return self._getBool(18)

    def setIsProgressive(self, value):
        self._setBool(18, value)
        return

    def getIsSingleStage(self):
        return self._getBool(19)

    def setIsSingleStage(self, value):
        self._setBool(19, value)
        return

    def getSpecificItemName(self):
        return self._getString(20)

    def setSpecificItemName(self, value):
        self._setString(20, value)
        return

    def getSpecificItemIconName(self):
        return self._getString(21)

    def setSpecificItemIconName(self, value):
        self._setString(21, value)
        return

    def getSpecificItemLevel(self):
        return self._getNumber(22)

    def setSpecificItemLevel(self, value):
        self._setNumber(22, value)
        return

    def getSpecificItemId(self):
        return self._getNumber(23)

    def setSpecificItemId(self, value):
        self._setNumber(23, value)
        return

    def getNewItemsCount(self):
        return self._getNumber(24)

    def setNewItemsCount(self, value):
        self._setNumber(24, value)
        return

    def getIsResearchable(self):
        return self._getBool(25)

    def setIsResearchable(self, value):
        self._setBool(25, value)
        return

    def _initialize(self):
        super(AchievementCardModel, self)._initialize()
        self._addBoolProperty(b'isProgressive', True)
        self._addBoolProperty(b'isSingleStage', False)
        self._addStringProperty(b'specificItemName', b'')
        self._addStringProperty(b'specificItemIconName', b'')
        self._addNumberProperty(b'specificItemLevel', 0)
        self._addNumberProperty(b'specificItemId', 0)
        self._addNumberProperty(b'newItemsCount', 0)
        self._addBoolProperty(b'isResearchable', False)
        return
