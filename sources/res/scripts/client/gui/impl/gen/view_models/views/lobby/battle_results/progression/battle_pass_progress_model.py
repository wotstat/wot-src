from frameworks.wulf import Array, ViewModel
from gui.impl.wrappers.user_list_model import UserListModel
from gui.impl.gen.view_models.views.lobby.battle_pass.reward_item_model import RewardItemModel
from gui.impl.gen.view_models.views.lobby.battle_results.progression.external_points_model import ExternalPointsModel

class BattlePassProgressModel(ViewModel):
    __slots__ = (b'onNavigate',)
    PATH = b'coui://gui/gameface/_dist/production/mono/plugins/post_battle/battle_pass/battle_pass.js'

    def __init__(self, properties=28, commands=1):
        super(BattlePassProgressModel, self).__init__(properties=properties, commands=commands)
        return

    def getPreviousChapterID(self):
        return self._getNumber(0)

    def setPreviousChapterID(self, value):
        self._setNumber(0, value)
        return

    def getCurrentChapterID(self):
        return self._getNumber(1)

    def setCurrentChapterID(self, value):
        self._setNumber(1, value)
        return

    def getHasBattlePass(self):
        return self._getBool(2)

    def setHasBattlePass(self, value):
        self._setBool(2, value)
        return

    def getBattlePassComplete(self):
        return self._getBool(3)

    def setBattlePassComplete(self, value):
        self._setBool(3, value)
        return

    def getAvailablePoints(self):
        return self._getNumber(4)

    def setAvailablePoints(self, value):
        self._setNumber(4, value)
        return

    def getBpTopPoints(self):
        return self._getNumber(5)

    def setBpTopPoints(self, value):
        self._setNumber(5, value)
        return

    def getBpTopExternalPoints(self):
        return self._getArray(6)

    def setBpTopExternalPoints(self, value):
        self._setArray(6, value)
        return

    @staticmethod
    def getBpTopExternalPointsType():
        return ExternalPointsModel

    def getPointsAux(self):
        return self._getNumber(7)

    def setPointsAux(self, value):
        self._setNumber(7, value)
        return

    def getQuestPoints(self):
        return self._getNumber(8)

    def setQuestPoints(self, value):
        self._setNumber(8, value)
        return

    def getBonusCapPoints(self):
        return self._getNumber(9)

    def setBonusCapPoints(self, value):
        self._setNumber(9, value)
        return

    def getCurrentLevelPoints(self):
        return self._getNumber(10)

    def setCurrentLevelPoints(self, value):
        self._setNumber(10, value)
        return

    def getMaxLevelPoints(self):
        return self._getNumber(11)

    def setMaxLevelPoints(self, value):
        self._setNumber(11, value)
        return

    def getCurrentLevel(self):
        return self._getNumber(12)

    def setCurrentLevel(self, value):
        self._setNumber(12, value)
        return

    def getPreviousLevel(self):
        return self._getNumber(13)

    def setPreviousLevel(self, value):
        self._setNumber(13, value)
        return

    def getPointsDiff(self):
        return self._getNumber(14)

    def setPointsDiff(self, value):
        self._setNumber(14, value)
        return

    def getLevelReached(self):
        return self._getBool(15)

    def setLevelReached(self, value):
        self._setBool(15, value)
        return

    def getLevelMax(self):
        return self._getBool(16)

    def setLevelMax(self, value):
        self._setBool(16, value)
        return

    def getNavigationEnabled(self):
        return self._getBool(17)

    def setNavigationEnabled(self, value):
        self._setBool(17, value)
        return

    def getHolidayBattlePass(self):
        return self._getBool(18)

    def setHolidayBattlePass(self, value):
        self._setBool(18, value)
        return

    def getLevelsInPostProgression(self):
        return self._getNumber(19)

    def setLevelsInPostProgression(self, value):
        self._setNumber(19, value)
        return

    def getPreviousMaxLevelPoints(self):
        return self._getNumber(20)

    def setPreviousMaxLevelPoints(self, value):
        self._setNumber(20, value)
        return

    def getLevelsInPreviousChapter(self):
        return self._getNumber(21)

    def setLevelsInPreviousChapter(self, value):
        self._setNumber(21, value)
        return

    def getExtraChapter(self):
        return self._getBool(22)

    def setExtraChapter(self, value):
        self._setBool(22, value)
        return

    def getPreviousChapterBought(self):
        return self._getBool(23)

    def setPreviousChapterBought(self, value):
        self._setBool(23, value)
        return

    def getCurrentFreeAwards(self):
        return self._getArray(24)

    def setCurrentFreeAwards(self, value):
        self._setArray(24, value)
        return

    @staticmethod
    def getCurrentFreeAwardsType():
        return RewardItemModel

    def getCurrentPaidAwards(self):
        return self._getArray(25)

    def setCurrentPaidAwards(self, value):
        self._setArray(25, value)
        return

    @staticmethod
    def getCurrentPaidAwardsType():
        return RewardItemModel

    def getPreviousFreeAwards(self):
        return self._getArray(26)

    def setPreviousFreeAwards(self, value):
        self._setArray(26, value)
        return

    @staticmethod
    def getPreviousFreeAwardsType():
        return UserListModel

    def getPreviousPaidAwards(self):
        return self._getArray(27)

    def setPreviousPaidAwards(self, value):
        self._setArray(27, value)
        return

    @staticmethod
    def getPreviousPaidAwardsType():
        return UserListModel

    def _initialize(self):
        super(BattlePassProgressModel, self)._initialize()
        self._addNumberProperty(b'previousChapterID', 0)
        self._addNumberProperty(b'currentChapterID', 0)
        self._addBoolProperty(b'hasBattlePass', False)
        self._addBoolProperty(b'battlePassComplete', False)
        self._addNumberProperty(b'availablePoints', 0)
        self._addNumberProperty(b'bpTopPoints', 0)
        self._addArrayProperty(b'bpTopExternalPoints', Array())
        self._addNumberProperty(b'pointsAux', 0)
        self._addNumberProperty(b'questPoints', 0)
        self._addNumberProperty(b'bonusCapPoints', 0)
        self._addNumberProperty(b'currentLevelPoints', 0)
        self._addNumberProperty(b'maxLevelPoints', 0)
        self._addNumberProperty(b'currentLevel', 0)
        self._addNumberProperty(b'previousLevel', 0)
        self._addNumberProperty(b'pointsDiff', 0)
        self._addBoolProperty(b'levelReached', False)
        self._addBoolProperty(b'levelMax', False)
        self._addBoolProperty(b'navigationEnabled', False)
        self._addBoolProperty(b'holidayBattlePass', False)
        self._addNumberProperty(b'levelsInPostProgression', 0)
        self._addNumberProperty(b'previousMaxLevelPoints', 0)
        self._addNumberProperty(b'levelsInPreviousChapter', 0)
        self._addBoolProperty(b'extraChapter', False)
        self._addBoolProperty(b'previousChapterBought', False)
        self._addArrayProperty(b'currentFreeAwards', Array())
        self._addArrayProperty(b'currentPaidAwards', Array())
        self._addArrayProperty(b'previousFreeAwards', Array())
        self._addArrayProperty(b'previousPaidAwards', Array())
        self.onNavigate = self._addCommand(b'onNavigate')
        return
