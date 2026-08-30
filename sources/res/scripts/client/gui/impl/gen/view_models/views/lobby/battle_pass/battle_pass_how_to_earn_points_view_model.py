from frameworks.wulf import Array, ViewModel
from gui.impl.gen.view_models.views.lobby.battle_pass.game_mode_model import GameModeModel

class BattlePassHowToEarnPointsViewModel(ViewModel):
    __slots__ = (b'onGoToMissions', b'onWotPlusClick')

    def __init__(self, properties=3, commands=2):
        super(BattlePassHowToEarnPointsViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getChapterID(self):
        return self._getNumber(0)

    def setChapterID(self, value):
        self._setNumber(0, value)
        return

    def getGameModes(self):
        return self._getArray(1)

    def setGameModes(self, value):
        self._setArray(1, value)
        return

    @staticmethod
    def getGameModesType():
        return GameModeModel

    def getIsWotPlusShown(self):
        return self._getBool(2)

    def setIsWotPlusShown(self, value):
        self._setBool(2, value)
        return

    def _initialize(self):
        super(BattlePassHowToEarnPointsViewModel, self)._initialize()
        self._addNumberProperty(b'chapterID', 0)
        self._addArrayProperty(b'gameModes', Array())
        self._addBoolProperty(b'isWotPlusShown', False)
        self.onGoToMissions = self._addCommand(b'onGoToMissions')
        self.onWotPlusClick = self._addCommand(b'onWotPlusClick')
        return
