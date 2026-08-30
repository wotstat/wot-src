from frameworks.wulf import Array, ViewModel
from gui.impl.gen.view_models.views.lobby.achievements.subcategory_advanced_achievement_model import SubcategoryAdvancedAchievementModel
from gui.impl.gen.view_models.views.lobby.achievements.views.achievements.upcoming_model import UpcomingModel

class AdvancedAchievementsViewModel(ViewModel):
    __slots__ = (b'onOpenTrophies', b'onOpenDetails', b'onCupClick', b'onAnimationInProgress', b'onAllAnimationEnd', b'onAchievementHover')

    def __init__(self, properties=12, commands=6):
        super(AdvancedAchievementsViewModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def trophy(self):
        return self._getViewModel(0)

    @staticmethod
    def getTrophyType():
        return SubcategoryAdvancedAchievementModel

    def getPrevAchievementsScore(self):
        return self._getNumber(1)

    def setPrevAchievementsScore(self, value):
        self._setNumber(1, value)
        return

    def getAchievementsScore(self):
        return self._getNumber(2)

    def setAchievementsScore(self, value):
        self._setNumber(2, value)
        return

    def getMaxAchievementsScore(self):
        return self._getNumber(3)

    def setMaxAchievementsScore(self, value):
        self._setNumber(3, value)
        return

    def getIsOtherPlayer(self):
        return self._getBool(4)

    def setIsOtherPlayer(self, value):
        self._setBool(4, value)
        return

    def getCategoryProgress(self):
        return self._getNumber(5)

    def setCategoryProgress(self, value):
        self._setNumber(5, value)
        return

    def getPrevCategoryProgress(self):
        return self._getNumber(6)

    def setPrevCategoryProgress(self, value):
        self._setNumber(6, value)
        return

    def getCategoryName(self):
        return self._getString(7)

    def setCategoryName(self, value):
        self._setString(7, value)
        return

    def getCategoryBackgroundName(self):
        return self._getString(8)

    def setCategoryBackgroundName(self, value):
        self._setString(8, value)
        return

    def getIsSkipAnimation(self):
        return self._getBool(9)

    def setIsSkipAnimation(self, value):
        self._setBool(9, value)
        return

    def getUpcomingAchievements(self):
        return self._getArray(10)

    def setUpcomingAchievements(self, value):
        self._setArray(10, value)
        return

    @staticmethod
    def getUpcomingAchievementsType():
        return UpcomingModel

    def getSubcategories(self):
        return self._getArray(11)

    def setSubcategories(self, value):
        self._setArray(11, value)
        return

    @staticmethod
    def getSubcategoriesType():
        return SubcategoryAdvancedAchievementModel

    def _initialize(self):
        super(AdvancedAchievementsViewModel, self)._initialize()
        self._addViewModelProperty(b'trophy', SubcategoryAdvancedAchievementModel())
        self._addNumberProperty(b'prevAchievementsScore', 0)
        self._addNumberProperty(b'achievementsScore', 0)
        self._addNumberProperty(b'maxAchievementsScore', 0)
        self._addBoolProperty(b'isOtherPlayer', False)
        self._addNumberProperty(b'categoryProgress', 0)
        self._addNumberProperty(b'prevCategoryProgress', 0)
        self._addStringProperty(b'categoryName', b'')
        self._addStringProperty(b'categoryBackgroundName', b'')
        self._addBoolProperty(b'isSkipAnimation', False)
        self._addArrayProperty(b'upcomingAchievements', Array())
        self._addArrayProperty(b'subcategories', Array())
        self.onOpenTrophies = self._addCommand(b'onOpenTrophies')
        self.onOpenDetails = self._addCommand(b'onOpenDetails')
        self.onCupClick = self._addCommand(b'onCupClick')
        self.onAnimationInProgress = self._addCommand(b'onAnimationInProgress')
        self.onAllAnimationEnd = self._addCommand(b'onAllAnimationEnd')
        self.onAchievementHover = self._addCommand(b'onAchievementHover')
        return
