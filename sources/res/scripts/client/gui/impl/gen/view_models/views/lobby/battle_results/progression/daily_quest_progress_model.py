from enum import Enum
from gui.impl.gen.view_models.common.missions.daily_quest_model import DailyQuestModel

class DailyQuestTypes(Enum):
    EASY = b'easy'
    MEDIUM = b'medium'
    HARD = b'hard'
    BONUS = b'bonus'
    PREMIUM = b'premium'
    EPIC = b'epic'


class DailyQuestProgressModel(DailyQuestModel):
    __slots__ = ()

    def __init__(self, properties=14, commands=0):
        super(DailyQuestProgressModel, self).__init__(properties=properties, commands=commands)
        return

    def getLevel(self):
        return DailyQuestTypes(self._getString(12))

    def setLevel(self, value):
        self._setString(12, value.value)
        return

    def getNavigationEnabled(self):
        return self._getBool(13)

    def setNavigationEnabled(self, value):
        self._setBool(13, value)
        return

    def _initialize(self):
        super(DailyQuestProgressModel, self)._initialize()
        self._addStringProperty(b'level')
        self._addBoolProperty(b'navigationEnabled', False)
        return
