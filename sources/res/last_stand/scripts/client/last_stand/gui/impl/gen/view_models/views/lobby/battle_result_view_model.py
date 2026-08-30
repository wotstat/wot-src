from frameworks.wulf import Array, ViewModel
from last_stand.gui.impl.gen.view_models.views.common.bonus_item_view_model import BonusItemViewModel
from last_stand.gui.impl.gen.view_models.views.lobby.battle_info_model import BattleInfoModel
from last_stand.gui.impl.gen.view_models.views.lobby.player_info_model import PlayerInfoModel

class BattleResultViewModel(ViewModel):
    __slots__ = (b'onClose',)

    def __init__(self, properties=10, commands=1):
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

    def getPhasesCount(self):
        return self._getNumber(3)

    def setPhasesCount(self, value):
        self._setNumber(3, value)
        return

    def getIsWin(self):
        return self._getBool(4)

    def setIsWin(self, value):
        self._setBool(4, value)
        return

    def getNewRecord(self):
        return self._getBool(5)

    def setNewRecord(self, value):
        self._setBool(5, value)
        return

    def getDifficultyLevel(self):
        return self._getNumber(6)

    def setDifficultyLevel(self, value):
        self._setNumber(6, value)
        return

    def getTime(self):
        return self._getNumber(7)

    def setTime(self, value):
        self._setNumber(7, value)
        return

    def getCompletedMissions(self):
        return self._getString(8)

    def setCompletedMissions(self, value):
        self._setString(8, value)
        return

    def getRewards(self):
        return self._getArray(9)

    def setRewards(self, value):
        self._setArray(9, value)
        return

    @staticmethod
    def getRewardsType():
        return BonusItemViewModel

    def _initialize(self):
        super(BattleResultViewModel, self)._initialize()
        self._addViewModelProperty(b'battleInfo', BattleInfoModel())
        self._addViewModelProperty(b'playerInfo', PlayerInfoModel())
        self._addNumberProperty(b'currentPhase', 0)
        self._addNumberProperty(b'phasesCount', 0)
        self._addBoolProperty(b'isWin', False)
        self._addBoolProperty(b'newRecord', False)
        self._addNumberProperty(b'difficultyLevel', 0)
        self._addNumberProperty(b'time', 0)
        self._addStringProperty(b'completedMissions', b'')
        self._addArrayProperty(b'rewards', Array())
        self.onClose = self._addCommand(b'onClose')
        return
