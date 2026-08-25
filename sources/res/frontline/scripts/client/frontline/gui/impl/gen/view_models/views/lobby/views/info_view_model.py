from frameworks.wulf import Array, ViewModel
from frontline.gui.impl.gen.view_models.views.lobby.views.rank_item_model import RankItemModel
from frontline.gui.impl.gen.view_models.views.lobby.views.skill_category_base_model import SkillCategoryBaseModel

class InfoViewModel(ViewModel):
    __slots__ = (b'onClose',)

    def __init__(self, properties=8, commands=1):
        super(InfoViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getIsNinthLevelEnabled(self):
        return self._getBool(0)

    def setIsNinthLevelEnabled(self, value):
        self._setBool(0, value)
        return

    def getIsBattlePassAvailable(self):
        return self._getBool(1)

    def setIsBattlePassAvailable(self, value):
        self._setBool(1, value)
        return

    def getAutoscrollSection(self):
        return self._getString(2)

    def setAutoscrollSection(self, value):
        self._setString(2, value)
        return

    def getIsRandomReservesModeEnabled(self):
        return self._getBool(3)

    def setIsRandomReservesModeEnabled(self, value):
        self._setBool(3, value)
        return

    def getStartTimestamp(self):
        return self._getNumber(4)

    def setStartTimestamp(self, value):
        self._setNumber(4, value)
        return

    def getEndTimestamp(self):
        return self._getNumber(5)

    def setEndTimestamp(self, value):
        self._setNumber(5, value)
        return

    def getSkillsCategories(self):
        return self._getArray(6)

    def setSkillsCategories(self, value):
        self._setArray(6, value)
        return

    @staticmethod
    def getSkillsCategoriesType():
        return SkillCategoryBaseModel

    def getRanksWithPoints(self):
        return self._getArray(7)

    def setRanksWithPoints(self, value):
        self._setArray(7, value)
        return

    @staticmethod
    def getRanksWithPointsType():
        return RankItemModel

    def _initialize(self):
        super(InfoViewModel, self)._initialize()
        self._addBoolProperty(b'isNinthLevelEnabled', False)
        self._addBoolProperty(b'isBattlePassAvailable', False)
        self._addStringProperty(b'autoscrollSection', b'')
        self._addBoolProperty(b'isRandomReservesModeEnabled', False)
        self._addNumberProperty(b'startTimestamp', 0)
        self._addNumberProperty(b'endTimestamp', 0)
        self._addArrayProperty(b'skillsCategories', Array())
        self._addArrayProperty(b'ranksWithPoints', Array())
        self.onClose = self._addCommand(b'onClose')
        return
