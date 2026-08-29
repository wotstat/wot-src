from enum import Enum
from frameworks.wulf import ViewModel

class QuestsType(Enum):
    HIT = b'hit'
    KILLS = b'kills'
    ASSIST = b'assist'
    BATTLE = b'battle'
    MASTER = b'master'


class PersonalMissionsQuestsTypeTooltipModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(PersonalMissionsQuestsTypeTooltipModel, self).__init__(properties=properties, commands=commands)
        return

    def getQuestsType(self):
        return QuestsType(self._getString(0))

    def setQuestsType(self, value):
        self._setString(0, value.value)
        return

    def getQuestType(self):
        return self._getString(1)

    def setQuestType(self, value):
        self._setString(1, value)
        return

    def _initialize(self):
        super(PersonalMissionsQuestsTypeTooltipModel, self)._initialize()
        self._addStringProperty(b'questsType')
        self._addStringProperty(b'questType', b'')
        return
