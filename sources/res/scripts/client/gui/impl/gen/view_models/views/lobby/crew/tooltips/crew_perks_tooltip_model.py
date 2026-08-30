from enum import Enum
from frameworks.wulf import Array
from gui.impl.gen.view_models.views.lobby.crew.common.skill.skill_extended_model import SkillExtendedModel
from gui.impl.gen.view_models.views.lobby.crew.tooltips.crew_perks_tooltip_booster_model import CrewPerksTooltipBoosterModel

class PerkType(Enum):
    EMPTY = b''
    MAIN = b'main'
    SITUATIONAL = b'situational'
    COMMON = b'common'
    COMMANDERSPECIAL = b'commanderSpecial'


class BoosterType(Enum):
    NONE = b'none'
    ORDINARY = b'ordinary'
    EXTRA = b'extra'


class CrewPerksTooltipModel(SkillExtendedModel):
    __slots__ = ()

    def __init__(self, properties=18, commands=0):
        super(CrewPerksTooltipModel, self).__init__(properties=properties, commands=commands)
        return

    def getSkillType(self):
        return self._getString(9)

    def setSkillType(self, value):
        self._setString(9, value)
        return

    def getRealLevel(self):
        return self._getReal(10)

    def setRealLevel(self, value):
        self._setReal(10, value)
        return

    def getIsAdvancedTooltipEnable(self):
        return self._getBool(11)

    def setIsAdvancedTooltipEnable(self, value):
        self._setBool(11, value)
        return

    def getIsGroupSkill(self):
        return self._getBool(12)

    def setIsGroupSkill(self, value):
        self._setBool(12, value)
        return

    def getIsAnyMemberWithLowEfficiency(self):
        return self._getBool(13)

    def setIsAnyMemberWithLowEfficiency(self, value):
        self._setBool(13, value)
        return

    def getIsAnyMemberUntrained(self):
        return self._getBool(14)

    def setIsAnyMemberUntrained(self, value):
        self._setBool(14, value)
        return

    def getBoosters(self):
        return self._getArray(15)

    def setBoosters(self, value):
        self._setArray(15, value)
        return

    @staticmethod
    def getBoostersType():
        return CrewPerksTooltipBoosterModel

    def getEfficiency(self):
        return self._getReal(16)

    def setEfficiency(self, value):
        self._setReal(16, value)
        return

    def getBoosterType(self):
        return BoosterType(self._getString(17))

    def setBoosterType(self, value):
        self._setString(17, value.value)
        return

    def _initialize(self):
        super(CrewPerksTooltipModel, self)._initialize()
        self._addStringProperty(b'skillType', b'')
        self._addRealProperty(b'realLevel', 0.0)
        self._addBoolProperty(b'isAdvancedTooltipEnable', False)
        self._addBoolProperty(b'isGroupSkill', False)
        self._addBoolProperty(b'isAnyMemberWithLowEfficiency', False)
        self._addBoolProperty(b'isAnyMemberUntrained', False)
        self._addArrayProperty(b'boosters', Array())
        self._addRealProperty(b'efficiency', 0.0)
        self._addStringProperty(b'boosterType', BoosterType.NONE.value)
        return
