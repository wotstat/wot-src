from gui.impl.gen import R
from gui.impl.gen.view_models.views.lobby.tank_setup.common.base_ammunition_slot import BaseAmmunitionSlot

class BattleAbilityAmmunitionSlot(BaseAmmunitionSlot):
    __slots__ = ()

    def __init__(self, properties=15, commands=0):
        super(BattleAbilityAmmunitionSlot, self).__init__(properties=properties, commands=commands)
        return

    def getLevel(self):
        return self._getNumber(13)

    def setLevel(self, value):
        self._setNumber(13, value)
        return

    def getRank(self):
        return self._getResource(14)

    def setRank(self, value):
        self._setResource(14, value)
        return

    def _initialize(self):
        super(BattleAbilityAmmunitionSlot, self)._initialize()
        self._addNumberProperty(b'level', 0)
        self._addResourceProperty(b'rank', R.invalid())
        return
