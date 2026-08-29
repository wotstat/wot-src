from enum import Enum
from frameworks.wulf import ViewModel

class SkillType(Enum):
    NEW = b'new'
    LEARNED = b'learned'
    LEARNING = b'learning'
    IRRELEVANT = b'irrelevant'
    POSSIBLE = b'possible'
    ZEROSKILL = b'zeroSkill'


class CrewWidgetTankmanSkillModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(CrewWidgetTankmanSkillModel, self).__init__(properties=properties, commands=commands)
        return

    def getName(self):
        return self._getString(0)

    def setName(self, value):
        self._setString(0, value)
        return

    def getIcon(self):
        return self._getString(1)

    def setIcon(self, value):
        self._setString(1, value)
        return

    def getType(self):
        return SkillType(self._getString(2))

    def setType(self, value):
        self._setString(2, value.value)
        return

    def _initialize(self):
        super(CrewWidgetTankmanSkillModel, self)._initialize()
        self._addStringProperty(b'name', b'')
        self._addStringProperty(b'icon', b'')
        self._addStringProperty(b'type')
        return
