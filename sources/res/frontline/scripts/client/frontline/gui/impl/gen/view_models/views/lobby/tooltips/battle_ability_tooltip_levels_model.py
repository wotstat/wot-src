from frameworks.wulf import Array, ViewModel
from frontline.gui.impl.gen.view_models.views.lobby.tooltips.battle_ability_tooltip_param_model import BattleAbilityTooltipParamModel

class BattleAbilityTooltipLevelsModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(BattleAbilityTooltipLevelsModel, self).__init__(properties=properties, commands=commands)
        return

    def getLevel(self):
        return self._getNumber(0)

    def setLevel(self, value):
        self._setNumber(0, value)
        return

    def getParams(self):
        return self._getArray(1)

    def setParams(self, value):
        self._setArray(1, value)
        return

    @staticmethod
    def getParamsType():
        return BattleAbilityTooltipParamModel

    def _initialize(self):
        super(BattleAbilityTooltipLevelsModel, self)._initialize()
        self._addNumberProperty(b'level', 0)
        self._addArrayProperty(b'params', Array())
        return
