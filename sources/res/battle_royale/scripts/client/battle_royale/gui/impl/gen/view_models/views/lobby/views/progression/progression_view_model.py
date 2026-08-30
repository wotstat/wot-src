from enum import Enum
from frameworks.wulf import Array, ViewModel
from battle_royale.gui.impl.gen.view_models.views.lobby.views.battle_quests_model import BattleQuestsModel
from battle_royale.gui.impl.gen.view_models.views.lobby.views.battle_royale_event_model import BattleRoyaleEventModel
from battle_royale.gui.impl.gen.view_models.views.lobby.views.progression.progress_level_model import ProgressLevelModel

class ProgressionState(Enum):
    INPROGRESS = b'inProgress'
    COMPLETED = b'completed'


class ProgressionViewModel(ViewModel):
    __slots__ = (b'onClose', b'pollServerTime')

    def __init__(self, properties=11, commands=2):
        super(ProgressionViewModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def battleQuests(self):
        return self._getViewModel(0)

    @staticmethod
    def getBattleQuestsType():
        return BattleQuestsModel

    @property
    def eventInfo(self):
        return self._getViewModel(1)

    @staticmethod
    def getEventInfoType():
        return BattleRoyaleEventModel

    def getState(self):
        return ProgressionState(self._getString(2))

    def setState(self, value):
        self._setString(2, value.value)
        return

    def getCurProgressPoints(self):
        return self._getNumber(3)

    def setCurProgressPoints(self, value):
        self._setNumber(3, value)
        return

    def getPrevProgressPoints(self):
        return self._getNumber(4)

    def setPrevProgressPoints(self, value):
        self._setNumber(4, value)
        return

    def getPointsForLevel(self):
        return self._getNumber(5)

    def setPointsForLevel(self, value):
        self._setNumber(5, value)
        return

    def getProgressLevels(self):
        return self._getArray(6)

    def setProgressLevels(self, value):
        self._setArray(6, value)
        return

    @staticmethod
    def getProgressLevelsType():
        return ProgressLevelModel

    def getStartTimestamp(self):
        return self._getNumber(7)

    def setStartTimestamp(self, value):
        self._setNumber(7, value)
        return

    def getEndTimestamp(self):
        return self._getNumber(8)

    def setEndTimestamp(self, value):
        self._setNumber(8, value)
        return

    def getServerTimestamp(self):
        return self._getNumber(9)

    def setServerTimestamp(self, value):
        self._setNumber(9, value)
        return

    def getCalendarTooltipId(self):
        return self._getString(10)

    def setCalendarTooltipId(self, value):
        self._setString(10, value)
        return

    def _initialize(self):
        super(ProgressionViewModel, self)._initialize()
        self._addViewModelProperty(b'battleQuests', BattleQuestsModel())
        self._addViewModelProperty(b'eventInfo', BattleRoyaleEventModel())
        self._addStringProperty(b'state')
        self._addNumberProperty(b'curProgressPoints', 0)
        self._addNumberProperty(b'prevProgressPoints', 0)
        self._addNumberProperty(b'pointsForLevel', 0)
        self._addArrayProperty(b'progressLevels', Array())
        self._addNumberProperty(b'startTimestamp', 0)
        self._addNumberProperty(b'endTimestamp', 0)
        self._addNumberProperty(b'serverTimestamp', 0)
        self._addStringProperty(b'calendarTooltipId', b'')
        self.onClose = self._addCommand(b'onClose')
        self.pollServerTime = self._addCommand(b'pollServerTime')
        return
