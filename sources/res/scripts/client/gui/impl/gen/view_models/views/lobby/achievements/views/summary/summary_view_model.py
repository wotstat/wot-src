from enum import Enum
from frameworks.wulf import Array
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.views.lobby.achievements.achievement_model import AchievementModel
from gui.impl.gen.view_models.views.lobby.achievements.views.summary.other_player_info_model import OtherPlayerInfoModel
from gui.impl.gen.view_models.views.lobby.achievements.views.summary.statistic_item_model import StatisticItemModel

class EditState(Enum):
    AVAILABLE = b'available'
    NOT_ENOUGH_ACHIEVEMENTS = b'notEnoughAchievements'
    DISABLED = b'disabled'


class SummaryViewModel(ViewModel):
    __slots__ = (b'onAchievementsSettings', b'onError')

    def __init__(self, properties=23, commands=2):
        super(SummaryViewModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def otherPlayerInfo(self):
        return self._getViewModel(0)

    @staticmethod
    def getOtherPlayerInfoType():
        return OtherPlayerInfoModel

    def getIsSummaryEnabled(self):
        return self._getBool(1)

    def setIsSummaryEnabled(self, value):
        self._setBool(1, value)
        return

    def getIsWTREnabled(self):
        return self._getBool(2)

    def setIsWTREnabled(self, value):
        self._setBool(2, value)
        return

    def getIsEditOpened(self):
        return self._getBool(3)

    def setIsEditOpened(self, value):
        self._setBool(3, value)
        return

    def getIsOtherPlayer(self):
        return self._getBool(4)

    def setIsOtherPlayer(self, value):
        self._setBool(4, value)
        return

    def getCurrentRatingRank(self):
        return self._getNumber(5)

    def setCurrentRatingRank(self, value):
        self._setNumber(5, value)
        return

    def getPrevCurrentRatingRank(self):
        return self._getNumber(6)

    def setPrevCurrentRatingRank(self, value):
        self._setNumber(6, value)
        return

    def getCurrentRatingSubRank(self):
        return self._getNumber(7)

    def setCurrentRatingSubRank(self, value):
        self._setNumber(7, value)
        return

    def getPrevCurrentRatingSubRank(self):
        return self._getNumber(8)

    def setPrevCurrentRatingSubRank(self, value):
        self._setNumber(8, value)
        return

    def getPersonalScore(self):
        return self._getNumber(9)

    def setPersonalScore(self, value):
        self._setNumber(9, value)
        return

    def getPrevPersonalScore(self):
        return self._getNumber(10)

    def setPrevPersonalScore(self, value):
        self._setNumber(10, value)
        return

    def getRequiredNumberOfBattles(self):
        return self._getNumber(11)

    def setRequiredNumberOfBattles(self, value):
        self._setNumber(11, value)
        return

    def getBattlesLeftCount(self):
        return self._getNumber(12)

    def setBattlesLeftCount(self, value):
        self._setNumber(12, value)
        return

    def getStatistic(self):
        return self._getArray(13)

    def setStatistic(self, value):
        self._setArray(13, value)
        return

    @staticmethod
    def getStatisticType():
        return StatisticItemModel

    def getEditState(self):
        return EditState(self._getString(14))

    def setEditState(self, value):
        self._setString(14, value.value)
        return

    def getNumberOfUniqueAwards(self):
        return self._getNumber(15)

    def setNumberOfUniqueAwards(self, value):
        self._setNumber(15, value)
        return

    def getTotalAwards(self):
        return self._getNumber(16)

    def setTotalAwards(self, value):
        self._setNumber(16, value)
        return

    def getAchievementRibbonLength(self):
        return self._getNumber(17)

    def setAchievementRibbonLength(self, value):
        self._setNumber(17, value)
        return

    def getSignificantAchievements(self):
        return self._getArray(18)

    def setSignificantAchievements(self, value):
        self._setArray(18, value)
        return

    @staticmethod
    def getSignificantAchievementsType():
        return AchievementModel

    def getRegistrationDate(self):
        return self._getString(19)

    def setRegistrationDate(self, value):
        self._setString(19, value)
        return

    def getLastVisitDate(self):
        return self._getString(20)

    def setLastVisitDate(self, value):
        self._setString(20, value)
        return

    def getLastVisitTime(self):
        return self._getString(21)

    def setLastVisitTime(self, value):
        self._setString(21, value)
        return

    def getIsSuccessfullyEdited(self):
        return self._getBool(22)

    def setIsSuccessfullyEdited(self, value):
        self._setBool(22, value)
        return

    def _initialize(self):
        super(SummaryViewModel, self)._initialize()
        self._addViewModelProperty(b'otherPlayerInfo', OtherPlayerInfoModel())
        self._addBoolProperty(b'isSummaryEnabled', True)
        self._addBoolProperty(b'isWTREnabled', True)
        self._addBoolProperty(b'isEditOpened', False)
        self._addBoolProperty(b'isOtherPlayer', False)
        self._addNumberProperty(b'currentRatingRank', 0)
        self._addNumberProperty(b'prevCurrentRatingRank', 0)
        self._addNumberProperty(b'currentRatingSubRank', 0)
        self._addNumberProperty(b'prevCurrentRatingSubRank', 0)
        self._addNumberProperty(b'personalScore', 0)
        self._addNumberProperty(b'prevPersonalScore', 0)
        self._addNumberProperty(b'requiredNumberOfBattles', 0)
        self._addNumberProperty(b'battlesLeftCount', 0)
        self._addArrayProperty(b'statistic', Array())
        self._addStringProperty(b'editState')
        self._addNumberProperty(b'numberOfUniqueAwards', 0)
        self._addNumberProperty(b'totalAwards', 0)
        self._addNumberProperty(b'achievementRibbonLength', 0)
        self._addArrayProperty(b'significantAchievements', Array())
        self._addStringProperty(b'registrationDate', b'')
        self._addStringProperty(b'lastVisitDate', b'')
        self._addStringProperty(b'lastVisitTime', b'')
        self._addBoolProperty(b'isSuccessfullyEdited', False)
        self.onAchievementsSettings = self._addCommand(b'onAchievementsSettings')
        self.onError = self._addCommand(b'onError')
        return
