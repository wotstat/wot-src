from enum import Enum
from frameworks.wulf import Array
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.views.lobby.personal_missions.pages.pm3_quests_card_model import Pm3QuestsCardModel

class QuestLineType(Enum):
    HIT = b'hit'
    KILLS = b'kills'
    ASSIST = b'assist'
    BATTLE = b'battle'
    MASTER = b'master'


class Pm3QuestsLineModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(Pm3QuestsLineModel, self).__init__(properties=properties, commands=commands)
        return

    def getType(self):
        return QuestLineType(self._getString(0))

    def setType(self, value):
        self._setString(0, value.value)
        return

    def getId(self):
        return self._getNumber(1)

    def setId(self, value):
        self._setNumber(1, value)
        return

    def getCards(self):
        return self._getArray(2)

    def setCards(self, value):
        self._setArray(2, value)
        return

    @staticmethod
    def getCardsType():
        return Pm3QuestsCardModel

    def _initialize(self):
        super(Pm3QuestsLineModel, self)._initialize()
        self._addStringProperty(b'type')
        self._addNumberProperty(b'id', 0)
        self._addArrayProperty(b'cards', Array())
        return
