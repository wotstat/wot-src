from gui.impl.gen.view_models.common.battle_player import VehicleTypeEnum
from frameworks.wulf import ViewModel

class FortRushHudTeamUnitModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(FortRushHudTeamUnitModel, self).__init__(properties=properties, commands=commands)
        return

    def getId(self):
        return self._getString(0)

    def setId(self, value):
        self._setString(0, value)
        return

    def getType(self):
        return VehicleTypeEnum(self._getString(1))

    def setType(self, value):
        self._setString(1, value.value)
        return

    def getIsDestroyed(self):
        return self._getBool(2)

    def setIsDestroyed(self, value):
        self._setBool(2, value)
        return

    def _initialize(self):
        super(FortRushHudTeamUnitModel, self)._initialize()
        self._addStringProperty(b'id', b'')
        self._addStringProperty(b'type', VehicleTypeEnum.UNDEFINED.value)
        self._addBoolProperty(b'isDestroyed', False)
        return
