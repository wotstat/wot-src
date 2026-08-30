from frameworks.wulf import Array, ViewModel
from gui.impl.gen.view_models.views.lobby.battle_results.progression.daily_quest_progress_model import DailyQuestProgressModel

class DailyQuestsProgressModel(ViewModel):
    __slots__ = (b'onNavigate',)
    PATH = b'coui://gui/gameface/_dist/production/mono/plugins/post_battle/daily_quests/daily_quests.js'

    def __init__(self, properties=1, commands=1):
        super(DailyQuestsProgressModel, self).__init__(properties=properties, commands=commands)
        return

    def getDailyQuests(self):
        return self._getArray(0)

    def setDailyQuests(self, value):
        self._setArray(0, value)
        return

    @staticmethod
    def getDailyQuestsType():
        return DailyQuestProgressModel

    def _initialize(self):
        super(DailyQuestsProgressModel, self)._initialize()
        self._addArrayProperty(b'dailyQuests', Array())
        self.onNavigate = self._addCommand(b'onNavigate')
        return
