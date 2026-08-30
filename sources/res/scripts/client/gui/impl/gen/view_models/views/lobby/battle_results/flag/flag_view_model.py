from frameworks.wulf import Array, ViewModel
from gui.impl.gen.view_models.views.lobby.battle_results.postbattle_achievement_model import PostbattleAchievementModel
from gui.impl.gen.view_models.views.lobby.common.router_model import RouterModel

class FlagViewModel(ViewModel):
    __slots__ = ()
    WIN = b'win'
    DRAW = b'tie'
    LOSE = b'lose'

    def __init__(self, properties=3, commands=0):
        super(FlagViewModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def router(self):
        return self._getViewModel(0)

    @staticmethod
    def getRouterType():
        return RouterModel

    def getWinStatus(self):
        return self._getString(1)

    def setWinStatus(self, value):
        self._setString(1, value)
        return

    def getAchievements(self):
        return self._getArray(2)

    def setAchievements(self, value):
        self._setArray(2, value)
        return

    @staticmethod
    def getAchievementsType():
        return PostbattleAchievementModel

    def _initialize(self):
        super(FlagViewModel, self)._initialize()
        self._addViewModelProperty(b'router', RouterModel())
        self._addStringProperty(b'winStatus', b'')
        self._addArrayProperty(b'achievements', Array())
        return
