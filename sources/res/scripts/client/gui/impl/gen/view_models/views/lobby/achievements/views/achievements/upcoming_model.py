from gui.impl.gen.view_models.views.lobby.achievements.advanced_achievement_model import AdvancedAchievementModel

class UpcomingModel(AdvancedAchievementModel):
    __slots__ = ()

    def __init__(self, properties=18, commands=0):
        super(UpcomingModel, self).__init__(properties=properties, commands=commands)
        return

    def getSpecificItemName(self):
        return self._getString(15)

    def setSpecificItemName(self, value):
        self._setString(15, value)
        return

    def getSpecificItemLevel(self):
        return self._getNumber(16)

    def setSpecificItemLevel(self, value):
        self._setNumber(16, value)
        return

    def getIsResearchable(self):
        return self._getBool(17)

    def setIsResearchable(self, value):
        self._setBool(17, value)
        return

    def _initialize(self):
        super(UpcomingModel, self)._initialize()
        self._addStringProperty(b'specificItemName', b'')
        self._addNumberProperty(b'specificItemLevel', 0)
        self._addBoolProperty(b'isResearchable', False)
        return
