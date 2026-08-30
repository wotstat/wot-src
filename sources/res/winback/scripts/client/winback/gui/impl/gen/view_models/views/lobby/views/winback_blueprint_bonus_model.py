from gui.impl.gen.view_models.common.missions.bonuses.blueprint_bonus_model import BlueprintBonusModel

class WinbackBlueprintBonusModel(BlueprintBonusModel):
    __slots__ = ()

    def __init__(self, properties=11, commands=0):
        super(WinbackBlueprintBonusModel, self).__init__(properties=properties, commands=commands)
        return

    def getAmountInStorage(self):
        return self._getNumber(9)

    def setAmountInStorage(self, value):
        self._setNumber(9, value)
        return

    def getIsSelected(self):
        return self._getBool(10)

    def setIsSelected(self, value):
        self._setBool(10, value)
        return

    def _initialize(self):
        super(WinbackBlueprintBonusModel, self)._initialize()
        self._addNumberProperty(b'amountInStorage', 0)
        self._addBoolProperty(b'isSelected', False)
        return
