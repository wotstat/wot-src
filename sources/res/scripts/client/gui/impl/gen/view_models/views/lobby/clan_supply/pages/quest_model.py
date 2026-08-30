from enum import Enum, IntEnum
from frameworks.wulf import Array, ViewModel
from gui.impl.gen.view_models.common.missions.bonuses.icon_bonus_model import IconBonusModel

class QuestStatus(IntEnum):
    DISABLED = 0
    IN_PROGRESS = 1
    REWARD_AVAILABLE = 2
    REWARD_PENDING = 3
    COMPLETE = 4


class QuestCondition(Enum):
    FRAGS = b'frags'
    FULL_DAMAGE = b'fullDamage'
    EXP = b'exp'
    WIN = b'win'


class QuestSquadState(Enum):
    SOLO = b'solo'
    PLATOON = b'platoon'
    SOLO_AND_PLATOON = b'soloAndPlatoon'
    DETACHMENT = b'detachment'


class QuestModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=10, commands=0):
        super(QuestModel, self).__init__(properties=properties, commands=commands)
        return

    def getLevel(self):
        return self._getNumber(0)

    def setLevel(self, value):
        self._setNumber(0, value)
        return

    def getCurrentProgress(self):
        return self._getNumber(1)

    def setCurrentProgress(self, value):
        self._setNumber(1, value)
        return

    def getRequiredProgress(self):
        return self._getNumber(2)

    def setRequiredProgress(self, value):
        self._setNumber(2, value)
        return

    def getMainCondition(self):
        return QuestCondition(self._getString(3))

    def setMainCondition(self, value):
        self._setString(3, value.value)
        return

    def getMainSquadState(self):
        return QuestSquadState(self._getString(4))

    def setMainSquadState(self, value):
        self._setString(4, value.value)
        return

    def getAlternativeCondition(self):
        return QuestCondition(self._getString(5))

    def setAlternativeCondition(self, value):
        self._setString(5, value.value)
        return

    def getAlternativeSquadState(self):
        return QuestSquadState(self._getString(6))

    def setAlternativeSquadState(self, value):
        self._setString(6, value.value)
        return

    def getConditionParams(self):
        return self._getString(7)

    def setConditionParams(self, value):
        self._setString(7, value)
        return

    def getStatus(self):
        return QuestStatus(self._getNumber(8))

    def setStatus(self, value):
        self._setNumber(8, value.value)
        return

    def getRewards(self):
        return self._getArray(9)

    def setRewards(self, value):
        self._setArray(9, value)
        return

    @staticmethod
    def getRewardsType():
        return IconBonusModel

    def _initialize(self):
        super(QuestModel, self)._initialize()
        self._addNumberProperty(b'level', 0)
        self._addNumberProperty(b'currentProgress', 0)
        self._addNumberProperty(b'requiredProgress', 0)
        self._addStringProperty(b'mainCondition')
        self._addStringProperty(b'mainSquadState')
        self._addStringProperty(b'alternativeCondition')
        self._addStringProperty(b'alternativeSquadState')
        self._addStringProperty(b'conditionParams', b'')
        self._addNumberProperty(b'status')
        self._addArrayProperty(b'rewards', Array())
        return
