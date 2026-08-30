from frameworks.wulf import Array, ViewModel
from gui.impl.gen.view_models.views.lobby.battle_results.progression.weekly_quest_progress_model import WeeklyQuestProgressModel

class WeeklyQuestsProgressModel(ViewModel):
    __slots__ = (b'onNavigate',)
    PATH = b'coui://gui/gameface/_dist/production/mono/plugins/post_battle/weekly_quests/weekly_quests.js'

    def __init__(self, properties=1, commands=1):
        super(WeeklyQuestsProgressModel, self).__init__(properties=properties, commands=commands)
        return

    def getWeeklyQuests(self):
        return self._getArray(0)

    def setWeeklyQuests(self, value):
        self._setArray(0, value)
        return

    @staticmethod
    def getWeeklyQuestsType():
        return WeeklyQuestProgressModel

    def _initialize(self):
        super(WeeklyQuestsProgressModel, self)._initialize()
        self._addArrayProperty(b'weeklyQuests', Array())
        self.onNavigate = self._addCommand(b'onNavigate')
        return
