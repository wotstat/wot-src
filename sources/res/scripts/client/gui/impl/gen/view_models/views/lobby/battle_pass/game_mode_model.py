from enum import IntEnum
from frameworks.wulf import Array, ViewModel
from gui.impl.gen.view_models.views.lobby.battle_pass.battle_royale_conditions_model import BattleRoyaleConditionsModel
from gui.impl.gen.view_models.views.lobby.battle_pass.game_mode_rows_model import GameModeRowsModel

class ArenaBonusType(IntEnum):
    REGULAR = 1
    RANKED = 22
    BATTLE_ROYALE_SOLO = 29
    EPIC_BATTLE = 27
    COMP7 = 43
    COMP7_LIGHT = 49


class PointsCardType(IntEnum):
    LIMIT = 0
    DAILY = 1


class GameModeModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=5, commands=0):
        super(GameModeModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def battleRoyaleCondtions(self):
        return self._getViewModel(0)

    @staticmethod
    def getBattleRoyaleCondtionsType():
        return BattleRoyaleConditionsModel

    def getArenaBonusType(self):
        return ArenaBonusType(self._getNumber(1))

    def setArenaBonusType(self, value):
        self._setNumber(1, value.value)
        return

    def getConditions(self):
        return self._getArray(2)

    def setConditions(self, value):
        self._setArray(2, value)
        return

    @staticmethod
    def getConditionsType():
        return GameModeRowsModel

    def getVehicles(self):
        return self._getArray(3)

    def setVehicles(self, value):
        self._setArray(3, value)
        return

    @staticmethod
    def getVehiclesType():
        return GameModeRowsModel

    def getCards(self):
        return self._getArray(4)

    def setCards(self, value):
        self._setArray(4, value)
        return

    @staticmethod
    def getCardsType():
        return PointsCardType

    def _initialize(self):
        super(GameModeModel, self)._initialize()
        self._addViewModelProperty(b'battleRoyaleCondtions', BattleRoyaleConditionsModel())
        self._addNumberProperty(b'arenaBonusType')
        self._addArrayProperty(b'conditions', Array())
        self._addArrayProperty(b'vehicles', Array())
        self._addArrayProperty(b'cards', Array())
        return
