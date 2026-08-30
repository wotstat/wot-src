from enum import IntEnum
from frameworks.wulf import Array
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.views.lobby.battle_pass.game_mode_card_model import GameModeCardModel
from gui.impl.gen.view_models.views.lobby.battle_pass.game_mode_rows_model import GameModeRowsModel

class ArenaBonusType(IntEnum):
    REGULAR = 1
    SORTIE_2 = 20
    FORT_BATTLE_2 = 21
    RANKED = 22
    EPIC_BATTLE = 27
    BATTLE_ROYALE_SOLO = 29
    BATTLE_ROYALE_SQUAD = 30
    COMP7 = 43
    VERSUS_AI = 50


class GameModeModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=5, commands=0):
        super(GameModeModel, self).__init__(properties=properties, commands=commands)
        return

    def getTitle(self):
        return self._getString(0)

    def setTitle(self, value):
        self._setString(0, value)
        return

    def getText(self):
        return self._getString(1)

    def setText(self, value):
        self._setString(1, value)
        return

    def getArenaBonusType(self):
        return ArenaBonusType(self._getNumber(2))

    def setArenaBonusType(self, value):
        self._setNumber(2, value.value)
        return

    def getTableRows(self):
        return self._getArray(3)

    def setTableRows(self, value):
        self._setArray(3, value)
        return

    @staticmethod
    def getTableRowsType():
        return GameModeRowsModel

    def getCards(self):
        return self._getArray(4)

    def setCards(self, value):
        self._setArray(4, value)
        return

    @staticmethod
    def getCardsType():
        return GameModeCardModel

    def _initialize(self):
        super(GameModeModel, self)._initialize()
        self._addStringProperty(b'title', b'')
        self._addStringProperty(b'text', b'')
        self._addNumberProperty(b'arenaBonusType')
        self._addArrayProperty(b'tableRows', Array())
        self._addArrayProperty(b'cards', Array())
        return
