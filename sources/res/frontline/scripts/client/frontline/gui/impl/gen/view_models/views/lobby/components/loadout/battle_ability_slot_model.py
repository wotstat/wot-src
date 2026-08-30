from frameworks.wulf import Array
from frontline.gui.impl.gen.view_models.views.lobby.components.loadout.battle_ability_by_rank_model import BattleAbilityByRankModel
from gui.impl.gen.view_models.views.lobby.tank_setup.sub_views.base_slot_model import BaseSlotModel

class BattleAbilitySlotModel(BaseSlotModel):
    __slots__ = ()

    def __init__(self, properties=30, commands=0):
        super(BattleAbilitySlotModel, self).__init__(properties=properties, commands=commands)
        return

    def getLevel(self):
        return self._getNumber(21)

    def setLevel(self, value):
        self._setNumber(21, value)
        return

    def getCost(self):
        return self._getNumber(22)

    def setCost(self, value):
        self._setNumber(22, value)
        return

    def getTargetSlotId(self):
        return self._getNumber(23)

    def setTargetSlotId(self, value):
        self._setNumber(23, value)
        return

    def getSkillId(self):
        return self._getNumber(24)

    def setSkillId(self, value):
        self._setNumber(24, value)
        return

    def getRank(self):
        return self._getNumber(25)

    def setRank(self, value):
        self._setNumber(25, value)
        return

    def getDescription(self):
        return self._getString(26)

    def setDescription(self, value):
        self._setString(26, value)
        return

    def getCategory(self):
        return self._getString(27)

    def setCategory(self, value):
        self._setString(27, value)
        return

    def getRanks(self):
        return self._getArray(28)

    def setRanks(self, value):
        self._setArray(28, value)
        return

    @staticmethod
    def getRanksType():
        return unicode

    def getAbilitiesByRank(self):
        return self._getArray(29)

    def setAbilitiesByRank(self, value):
        self._setArray(29, value)
        return

    @staticmethod
    def getAbilitiesByRankType():
        return BattleAbilityByRankModel

    def _initialize(self):
        super(BattleAbilitySlotModel, self)._initialize()
        self._addNumberProperty(b'level', 0)
        self._addNumberProperty(b'cost', 0)
        self._addNumberProperty(b'targetSlotId', 0)
        self._addNumberProperty(b'skillId', 0)
        self._addNumberProperty(b'rank', 0)
        self._addStringProperty(b'description', b'')
        self._addStringProperty(b'category', b'')
        self._addArrayProperty(b'ranks', Array())
        self._addArrayProperty(b'abilitiesByRank', Array())
        return
