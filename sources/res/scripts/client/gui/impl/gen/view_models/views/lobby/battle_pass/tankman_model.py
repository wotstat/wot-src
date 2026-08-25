from enum import Enum
from frameworks.wulf import Array, ViewModel
from gui.impl.gen.view_models.views.lobby.battle_pass.skill_model import SkillModel

class TankmanStates(Enum):
    RECEIVED = b'received'
    PROGRESSION = b'progression'
    IN_SHOP = b'inShop'
    NOT_FULL = b'notFull'
    UNAVAILABLE = b'unavailable'


class TankmanModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=9, commands=0):
        super(TankmanModel, self).__init__(properties=properties, commands=commands)
        return

    def getFullName(self):
        return self._getString(0)

    def setFullName(self, value):
        self._setString(0, value)
        return

    def getGroupName(self):
        return self._getString(1)

    def setGroupName(self, value):
        self._setString(1, value)
        return

    def getState(self):
        return TankmanStates(self._getString(2))

    def setState(self, value):
        self._setString(2, value.value)
        return

    def getChapterID(self):
        return self._getNumber(3)

    def setChapterID(self, value):
        self._setNumber(3, value)
        return

    def getProgressionLevel(self):
        return self._getNumber(4)

    def setProgressionLevel(self, value):
        self._setNumber(4, value)
        return

    def getCount(self):
        return self._getNumber(5)

    def setCount(self, value):
        self._setNumber(5, value)
        return

    def getAvailableCount(self):
        return self._getNumber(6)

    def setAvailableCount(self, value):
        self._setNumber(6, value)
        return

    def getHasVoiceover(self):
        return self._getBool(7)

    def setHasVoiceover(self, value):
        self._setBool(7, value)
        return

    def getSkills(self):
        return self._getArray(8)

    def setSkills(self, value):
        self._setArray(8, value)
        return

    @staticmethod
    def getSkillsType():
        return SkillModel

    def _initialize(self):
        super(TankmanModel, self)._initialize()
        self._addStringProperty(b'fullName', b'')
        self._addStringProperty(b'groupName', b'')
        self._addStringProperty(b'state')
        self._addNumberProperty(b'chapterID', 0)
        self._addNumberProperty(b'progressionLevel', 0)
        self._addNumberProperty(b'count', 1)
        self._addNumberProperty(b'availableCount', 0)
        self._addBoolProperty(b'hasVoiceover', False)
        self._addArrayProperty(b'skills', Array())
        return
