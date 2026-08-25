from enum import Enum
from gui.impl.gen.view_models.views.lobby.crew.common.skill.skill_simple_model import SkillSimpleModel

class BattleBooster(Enum):
    NONE = b'none'
    LEARNED = b'learned'
    IMPROVED = b'Improved'


class SkillModel(SkillSimpleModel):
    __slots__ = ()

    def __init__(self, properties=7, commands=0):
        super(SkillModel, self).__init__(properties=properties, commands=commands)
        return

    def getIsZero(self):
        return self._getBool(4)

    def setIsZero(self, value):
        self._setBool(4, value)
        return

    def getIsIrrelevant(self):
        return self._getBool(5)

    def setIsIrrelevant(self, value):
        self._setBool(5, value)
        return

    def getBattleBooster(self):
        return BattleBooster(self._getString(6))

    def setBattleBooster(self, value):
        self._setString(6, value.value)
        return

    def _initialize(self):
        super(SkillModel, self)._initialize()
        self._addBoolProperty(b'isZero', False)
        self._addBoolProperty(b'isIrrelevant', False)
        self._addStringProperty(b'battleBooster', BattleBooster.NONE.value)
        return
