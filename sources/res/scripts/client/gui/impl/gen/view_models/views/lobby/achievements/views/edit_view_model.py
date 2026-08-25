from frameworks.wulf import Array, ViewModel
from gui.impl.gen.view_models.views.lobby.achievements.achievement_model import AchievementModel
from gui.impl.gen.view_models.views.lobby.achievements.views.achievement_section_model import AchievementSectionModel

class EditViewModel(ViewModel):
    __slots__ = (b'onChangeAutoSelect', b'onReplaceAchievement', b'onSave', b'onCancel', b'onExitConfirm', b'onHideFirstEntryState')

    def __init__(self, properties=8, commands=6):
        super(EditViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getIsAutoSelect(self):
        return self._getBool(0)

    def setIsAutoSelect(self, value):
        self._setBool(0, value)
        return

    def getIsFirstEntry(self):
        return self._getBool(1)

    def setIsFirstEntry(self, value):
        self._setBool(1, value)
        return

    def getHasChanges(self):
        return self._getBool(2)

    def setHasChanges(self, value):
        self._setBool(2, value)
        return

    def getSelectedAchievements(self):
        return self._getArray(3)

    def setSelectedAchievements(self, value):
        self._setArray(3, value)
        return

    @staticmethod
    def getSelectedAchievementsType():
        return AchievementModel

    def getAchievementSections(self):
        return self._getArray(4)

    def setAchievementSections(self, value):
        self._setArray(4, value)
        return

    @staticmethod
    def getAchievementSectionsType():
        return AchievementSectionModel

    def getRibbonSmall(self):
        return self._getString(5)

    def setRibbonSmall(self, value):
        self._setString(5, value)
        return

    def getRibbonNormal(self):
        return self._getString(6)

    def setRibbonNormal(self, value):
        self._setString(6, value)
        return

    def getRibbonLarge(self):
        return self._getString(7)

    def setRibbonLarge(self, value):
        self._setString(7, value)
        return

    def _initialize(self):
        super(EditViewModel, self)._initialize()
        self._addBoolProperty(b'isAutoSelect', False)
        self._addBoolProperty(b'isFirstEntry', False)
        self._addBoolProperty(b'hasChanges', False)
        self._addArrayProperty(b'selectedAchievements', Array())
        self._addArrayProperty(b'achievementSections', Array())
        self._addStringProperty(b'ribbonSmall', b'')
        self._addStringProperty(b'ribbonNormal', b'')
        self._addStringProperty(b'ribbonLarge', b'')
        self.onChangeAutoSelect = self._addCommand(b'onChangeAutoSelect')
        self.onReplaceAchievement = self._addCommand(b'onReplaceAchievement')
        self.onSave = self._addCommand(b'onSave')
        self.onCancel = self._addCommand(b'onCancel')
        self.onExitConfirm = self._addCommand(b'onExitConfirm')
        self.onHideFirstEntryState = self._addCommand(b'onHideFirstEntryState')
        return
