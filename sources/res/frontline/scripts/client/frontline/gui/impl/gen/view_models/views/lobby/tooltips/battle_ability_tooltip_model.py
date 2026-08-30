from frameworks.wulf import Array, ViewModel
from frontline.gui.impl.gen.view_models.views.lobby.tooltips.battle_ability_tooltip_levels_model import BattleAbilityTooltipLevelsModel
from frontline.gui.impl.gen.view_models.views.lobby.tooltips.battle_ability_tooltip_param_model import BattleAbilityTooltipParamModel

class BattleAbilityTooltipModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=6, commands=0):
        super(BattleAbilityTooltipModel, self).__init__(properties=properties, commands=commands)
        return

    def getCategory(self):
        return self._getString(0)

    def setCategory(self, value):
        self._setString(0, value)
        return

    def getName(self):
        return self._getString(1)

    def setName(self, value):
        self._setString(1, value)
        return

    def getImageName(self):
        return self._getString(2)

    def setImageName(self, value):
        self._setString(2, value)
        return

    def getIsPurchased(self):
        return self._getBool(3)

    def setIsPurchased(self, value):
        self._setBool(3, value)
        return

    def getCharacteristics(self):
        return self._getArray(4)

    def setCharacteristics(self, value):
        self._setArray(4, value)
        return

    @staticmethod
    def getCharacteristicsType():
        return BattleAbilityTooltipParamModel

    def getLevelsInfo(self):
        return self._getArray(5)

    def setLevelsInfo(self, value):
        self._setArray(5, value)
        return

    @staticmethod
    def getLevelsInfoType():
        return BattleAbilityTooltipLevelsModel

    def _initialize(self):
        super(BattleAbilityTooltipModel, self)._initialize()
        self._addStringProperty(b'category', b'')
        self._addStringProperty(b'name', b'')
        self._addStringProperty(b'imageName', b'')
        self._addBoolProperty(b'isPurchased', False)
        self._addArrayProperty(b'characteristics', Array())
        self._addArrayProperty(b'levelsInfo', Array())
        return
