from frameworks.wulf import Array, ViewModel
from halloween.gui.impl.gen.view_models.views.lobby.battle_info_model import BattleInfoModel
from halloween.gui.impl.gen.view_models.views.lobby.player_info_model import PlayerInfoModel
from halloween.gui.impl.gen.view_models.views.lobby.reward_bonus_item_view_model import RewardBonusItemViewModel

class BattleResultViewModel(ViewModel):
    __slots__ = (b'onClose',)

    def __init__(self, properties=6, commands=1):
        super(BattleResultViewModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def battleInfo(self):
        return self._getViewModel(0)

    @staticmethod
    def getBattleInfoType():
        return BattleInfoModel

    @property
    def playerInfo(self):
        return self._getViewModel(1)

    @staticmethod
    def getPlayerInfoType():
        return PlayerInfoModel

    def getCurrentPhase(self):
        return self._getNumber(2)

    def setCurrentPhase(self, value):
        self._setNumber(2, value)
        return

    def getIsBossDefeated(self):
        return self._getBool(3)

    def setIsBossDefeated(self, value):
        self._setBool(3, value)
        return

    def getDifficultyLevel(self):
        return self._getNumber(4)

    def setDifficultyLevel(self, value):
        self._setNumber(4, value)
        return

    def getRewards(self):
        return self._getArray(5)

    def setRewards(self, value):
        self._setArray(5, value)
        return

    @staticmethod
    def getRewardsType():
        return RewardBonusItemViewModel

    def _initialize(self):
        super(BattleResultViewModel, self)._initialize()
        self._addViewModelProperty(b'battleInfo', BattleInfoModel())
        self._addViewModelProperty(b'playerInfo', PlayerInfoModel())
        self._addNumberProperty(b'currentPhase', 0)
        self._addBoolProperty(b'isBossDefeated', False)
        self._addNumberProperty(b'difficultyLevel', 0)
        self._addArrayProperty(b'rewards', Array())
        self.onClose = self._addCommand(b'onClose')
        return
