from enum import Enum
from gui.impl.gen.view_models.views.lobby.user_missions.widget.base_battle_pass_model import BaseBattlePassModel

class WidgetState(Enum):
    INTRO = b'intro'
    PROGRESSION = b'progression'
    COMPLETED = b'completed'


class AppearAnimationState(Enum):
    WAITING = b'waiting'
    READY = b'ready'
    PLAYED = b'played'


class BattlePassModel(BaseBattlePassModel):
    __slots__ = (b'onOpenBattlePass', b'onIntroAnimationPlayed')

    def __init__(self, properties=17, commands=2):
        super(BattlePassModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def lastSeenState(self):
        return self._getViewModel(3)

    @staticmethod
    def getLastSeenStateType():
        return BaseBattlePassModel

    def getWidgetState(self):
        return WidgetState(self._getString(4))

    def setWidgetState(self, value):
        self._setString(4, value.value)
        return

    def getLevelPoints(self):
        return self._getNumber(5)

    def setLevelPoints(self, value):
        self._setNumber(5, value)
        return

    def getTooltipID(self):
        return self._getNumber(6)

    def setTooltipID(self, value):
        self._setNumber(6, value)
        return

    def getChapterID(self):
        return self._getNumber(7)

    def setChapterID(self, value):
        self._setNumber(7, value)
        return

    def getSeason(self):
        return self._getNumber(8)

    def setSeason(self, value):
        self._setNumber(8, value)
        return

    def getIsBought(self):
        return self._getBool(9)

    def setIsBought(self, value):
        self._setBool(9, value)
        return

    def getIsExtraChapter(self):
        return self._getBool(10)

    def setIsExtraChapter(self, value):
        self._setBool(10, value)
        return

    def getIsHoliday(self):
        return self._getBool(11)

    def setIsHoliday(self, value):
        self._setBool(11, value)
        return

    def getIsPaused(self):
        return self._getBool(12)

    def setIsPaused(self, value):
        self._setBool(12, value)
        return

    def getHasExtraChapter(self):
        return self._getBool(13)

    def setHasExtraChapter(self, value):
        self._setBool(13, value)
        return

    def getIsExtraChapterHighlighted(self):
        return self._getBool(14)

    def setIsExtraChapterHighlighted(self, value):
        self._setBool(14, value)
        return

    def getAppearAnimationState(self):
        return AppearAnimationState(self._getString(15))

    def setAppearAnimationState(self, value):
        self._setString(15, value.value)
        return

    def getTimeLeft(self):
        return self._getNumber(16)

    def setTimeLeft(self, value):
        self._setNumber(16, value)
        return

    def _initialize(self):
        super(BattlePassModel, self)._initialize()
        self._addViewModelProperty(b'lastSeenState', BaseBattlePassModel())
        self._addStringProperty(b'widgetState')
        self._addNumberProperty(b'levelPoints', 0)
        self._addNumberProperty(b'tooltipID', 0)
        self._addNumberProperty(b'chapterID', -1)
        self._addNumberProperty(b'season', 0)
        self._addBoolProperty(b'isBought', False)
        self._addBoolProperty(b'isExtraChapter', False)
        self._addBoolProperty(b'isHoliday', False)
        self._addBoolProperty(b'isPaused', False)
        self._addBoolProperty(b'hasExtraChapter', False)
        self._addBoolProperty(b'isExtraChapterHighlighted', False)
        self._addStringProperty(b'appearAnimationState')
        self._addNumberProperty(b'timeLeft', 0)
        self.onOpenBattlePass = self._addCommand(b'onOpenBattlePass')
        self.onIntroAnimationPlayed = self._addCommand(b'onIntroAnimationPlayed')
        return
