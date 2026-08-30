from enum import Enum
from frameworks.wulf import Array, ViewModel
from gui.impl.gen.view_models.views.lobby.achievements.achievement_model import AchievementModel
from gui.impl.gen.view_models.views.lobby.achievements.views.summary.background_model import BackgroundModel
from gui.impl.gen.view_models.views.lobby.achievements.views.summary.other_player_info_model import OtherPlayerInfoModel
from gui.impl.gen.view_models.views.lobby.achievements.views.summary.ribbon_model import RibbonModel
from gui.impl.gen.view_models.views.lobby.achievements.views.summary.statistic_item_model import StatisticItemModel

class EditState(Enum):
    AVAILABLE = b'available'
    NOT_ENOUGH_ACHIEVEMENTS = b'notEnoughAchievements'
    DISABLED = b'disabled'


class SummaryViewModel(ViewModel):
    __slots__ = (b'onAchievementsSettings', b'onCustomizationConfirmed', b'onCustomizationDiscard', b'onSetBackgroundDraft', b'onSetRibbonDraft', b'onSetIsInCustomizationMode')

    def __init__(self, properties=35, commands=6):
        super(SummaryViewModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def otherPlayerInfo(self):
        return self._getViewModel(0)

    @staticmethod
    def getOtherPlayerInfoType():
        return OtherPlayerInfoModel

    @property
    def background(self):
        return self._getViewModel(1)

    @staticmethod
    def getBackgroundType():
        return BackgroundModel

    @property
    def backgroundDraft(self):
        return self._getViewModel(2)

    @staticmethod
    def getBackgroundDraftType():
        return BackgroundModel

    @property
    def ribbon(self):
        return self._getViewModel(3)

    @staticmethod
    def getRibbonType():
        return RibbonModel

    @property
    def ribbonDraft(self):
        return self._getViewModel(4)

    @staticmethod
    def getRibbonDraftType():
        return RibbonModel

    def getIsSummaryEnabled(self):
        return self._getBool(5)

    def setIsSummaryEnabled(self, value):
        self._setBool(5, value)
        return

    def getIsWTREnabled(self):
        return self._getBool(6)

    def setIsWTREnabled(self, value):
        self._setBool(6, value)
        return

    def getIsEditOpened(self):
        return self._getBool(7)

    def setIsEditOpened(self, value):
        self._setBool(7, value)
        return

    def getIsOtherPlayer(self):
        return self._getBool(8)

    def setIsOtherPlayer(self, value):
        self._setBool(8, value)
        return

    def getCurrentRatingRank(self):
        return self._getNumber(9)

    def setCurrentRatingRank(self, value):
        self._setNumber(9, value)
        return

    def getPrevCurrentRatingRank(self):
        return self._getNumber(10)

    def setPrevCurrentRatingRank(self, value):
        self._setNumber(10, value)
        return

    def getCurrentRatingSubRank(self):
        return self._getNumber(11)

    def setCurrentRatingSubRank(self, value):
        self._setNumber(11, value)
        return

    def getPrevCurrentRatingSubRank(self):
        return self._getNumber(12)

    def setPrevCurrentRatingSubRank(self, value):
        self._setNumber(12, value)
        return

    def getPersonalScore(self):
        return self._getNumber(13)

    def setPersonalScore(self, value):
        self._setNumber(13, value)
        return

    def getPrevPersonalScore(self):
        return self._getNumber(14)

    def setPrevPersonalScore(self, value):
        self._setNumber(14, value)
        return

    def getRequiredNumberOfBattles(self):
        return self._getNumber(15)

    def setRequiredNumberOfBattles(self, value):
        self._setNumber(15, value)
        return

    def getBattlesLeftCount(self):
        return self._getNumber(16)

    def setBattlesLeftCount(self, value):
        self._setNumber(16, value)
        return

    def getStatistic(self):
        return self._getArray(17)

    def setStatistic(self, value):
        self._setArray(17, value)
        return

    @staticmethod
    def getStatisticType():
        return StatisticItemModel

    def getEditState(self):
        return EditState(self._getString(18))

    def setEditState(self, value):
        self._setString(18, value.value)
        return

    def getNumberOfUniqueAwards(self):
        return self._getNumber(19)

    def setNumberOfUniqueAwards(self, value):
        self._setNumber(19, value)
        return

    def getTotalAwards(self):
        return self._getNumber(20)

    def setTotalAwards(self, value):
        self._setNumber(20, value)
        return

    def getCurrentMastery(self):
        return self._getNumber(21)

    def setCurrentMastery(self, value):
        self._setNumber(21, value)
        return

    def getTotalMastery(self):
        return self._getNumber(22)

    def setTotalMastery(self, value):
        self._setNumber(22, value)
        return

    def getAchievementRibbonLength(self):
        return self._getNumber(23)

    def setAchievementRibbonLength(self, value):
        self._setNumber(23, value)
        return

    def getSignificantAchievements(self):
        return self._getArray(24)

    def setSignificantAchievements(self, value):
        self._setArray(24, value)
        return

    @staticmethod
    def getSignificantAchievementsType():
        return AchievementModel

    def getRegistrationDate(self):
        return self._getString(25)

    def setRegistrationDate(self, value):
        self._setString(25, value)
        return

    def getLastVisitDate(self):
        return self._getString(26)

    def setLastVisitDate(self, value):
        self._setString(26, value)
        return

    def getLastVisitTime(self):
        return self._getString(27)

    def setLastVisitTime(self, value):
        self._setString(27, value)
        return

    def getIsSuccessfullyEdited(self):
        return self._getBool(28)

    def setIsSuccessfullyEdited(self, value):
        self._setBool(28, value)
        return

    def getIsCustomizationButtonVisible(self):
        return self._getBool(29)

    def setIsCustomizationButtonVisible(self, value):
        self._setBool(29, value)
        return

    def getIsCustomizationButtonEnabled(self):
        return self._getBool(30)

    def setIsCustomizationButtonEnabled(self, value):
        self._setBool(30, value)
        return

    def getCustomizationButtonTooltip(self):
        return self._getString(31)

    def setCustomizationButtonTooltip(self, value):
        self._setString(31, value)
        return

    def getBackgroundOptions(self):
        return self._getArray(32)

    def setBackgroundOptions(self, value):
        self._setArray(32, value)
        return

    @staticmethod
    def getBackgroundOptionsType():
        return BackgroundModel

    def getRibbonOptions(self):
        return self._getArray(33)

    def setRibbonOptions(self, value):
        self._setArray(33, value)
        return

    @staticmethod
    def getRibbonOptionsType():
        return RibbonModel

    def getIsInCustomizationMode(self):
        return self._getBool(34)

    def setIsInCustomizationMode(self, value):
        self._setBool(34, value)
        return

    def _initialize(self):
        super(SummaryViewModel, self)._initialize()
        self._addViewModelProperty(b'otherPlayerInfo', OtherPlayerInfoModel())
        self._addViewModelProperty(b'background', BackgroundModel())
        self._addViewModelProperty(b'backgroundDraft', BackgroundModel())
        self._addViewModelProperty(b'ribbon', RibbonModel())
        self._addViewModelProperty(b'ribbonDraft', RibbonModel())
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
        self._addNumberProperty(b'currentMastery', 0)
        self._addNumberProperty(b'totalMastery', 0)
        self._addNumberProperty(b'achievementRibbonLength', 0)
        self._addArrayProperty(b'significantAchievements', Array())
        self._addStringProperty(b'registrationDate', b'')
        self._addStringProperty(b'lastVisitDate', b'')
        self._addStringProperty(b'lastVisitTime', b'')
        self._addBoolProperty(b'isSuccessfullyEdited', False)
        self._addBoolProperty(b'isCustomizationButtonVisible', False)
        self._addBoolProperty(b'isCustomizationButtonEnabled', False)
        self._addStringProperty(b'customizationButtonTooltip', b'')
        self._addArrayProperty(b'backgroundOptions', Array())
        self._addArrayProperty(b'ribbonOptions', Array())
        self._addBoolProperty(b'isInCustomizationMode', False)
        self.onAchievementsSettings = self._addCommand(b'onAchievementsSettings')
        self.onCustomizationConfirmed = self._addCommand(b'onCustomizationConfirmed')
        self.onCustomizationDiscard = self._addCommand(b'onCustomizationDiscard')
        self.onSetBackgroundDraft = self._addCommand(b'onSetBackgroundDraft')
        self.onSetRibbonDraft = self._addCommand(b'onSetRibbonDraft')
        self.onSetIsInCustomizationMode = self._addCommand(b'onSetIsInCustomizationMode')
        return
