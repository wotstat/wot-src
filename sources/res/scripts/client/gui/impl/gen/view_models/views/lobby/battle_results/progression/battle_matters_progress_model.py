from frameworks.wulf import Array, ViewModel
from gui.impl.gen.view_models.views.lobby.battle_matters.quest_view_model import QuestViewModel

class BattleMattersProgressModel(ViewModel):
    __slots__ = (b'onNavigate',)
    PATH = b'coui://gui/gameface/_dist/production/mono/plugins/post_battle/battle_matters/battle_matters.js'

    def __init__(self, properties=2, commands=1):
        super(BattleMattersProgressModel, self).__init__(properties=properties, commands=commands)
        return

    def getNavigationEnabled(self):
        return self._getBool(0)

    def setNavigationEnabled(self, value):
        self._setBool(0, value)
        return

    def getBattleMatters(self):
        return self._getArray(1)

    def setBattleMatters(self, value):
        self._setArray(1, value)
        return

    @staticmethod
    def getBattleMattersType():
        return QuestViewModel

    def _initialize(self):
        super(BattleMattersProgressModel, self)._initialize()
        self._addBoolProperty(b'navigationEnabled', False)
        self._addArrayProperty(b'battleMatters', Array())
        self.onNavigate = self._addCommand(b'onNavigate')
        return
