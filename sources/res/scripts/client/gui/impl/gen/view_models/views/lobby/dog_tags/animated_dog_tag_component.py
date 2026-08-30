from gui.impl.gen.view_models.views.lobby.achievements.advanced_achievement_model import AdvancedAchievementModel
from gui.impl.gen.view_models.views.lobby.dog_tags.dt_dog_tag import DtDogTag

class AnimatedDogTagComponent(DtDogTag):
    __slots__ = ()

    def __init__(self, properties=8, commands=0):
        super(AnimatedDogTagComponent, self).__init__(properties=properties, commands=commands)
        return

    @property
    def requiredAchievement(self):
        return self._getViewModel(4)

    @staticmethod
    def getRequiredAchievementType():
        return AdvancedAchievementModel

    def getAnimation(self):
        return self._getString(5)

    def setAnimation(self, value):
        self._setString(5, value)
        return

    def getIsSelected(self):
        return self._getBool(6)

    def setIsSelected(self, value):
        self._setBool(6, value)
        return

    def getIsShowInPrebattle(self):
        return self._getBool(7)

    def setIsShowInPrebattle(self, value):
        self._setBool(7, value)
        return

    def _initialize(self):
        super(AnimatedDogTagComponent, self)._initialize()
        self._addViewModelProperty(b'requiredAchievement', AdvancedAchievementModel())
        self._addStringProperty(b'animation', b'')
        self._addBoolProperty(b'isSelected', False)
        self._addBoolProperty(b'isShowInPrebattle', False)
        return
