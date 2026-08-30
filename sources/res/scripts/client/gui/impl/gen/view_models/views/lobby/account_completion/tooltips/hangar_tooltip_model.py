from frameworks.wulf import Array, ViewModel
from gui.impl.gen.view_models.common.missions.bonuses.bonus_model import BonusModel

class HangarTooltipModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(HangarTooltipModel, self).__init__(properties=properties, commands=commands)
        return

    def getEmail(self):
        return self._getString(0)

    def setEmail(self, value):
        self._setString(0, value)
        return

    def getBonuses(self):
        return self._getArray(1)

    def setBonuses(self, value):
        self._setArray(1, value)
        return

    @staticmethod
    def getBonusesType():
        return BonusModel

    def _initialize(self):
        super(HangarTooltipModel, self)._initialize()
        self._addStringProperty(b'email', b'')
        self._addArrayProperty(b'bonuses', Array())
        return
