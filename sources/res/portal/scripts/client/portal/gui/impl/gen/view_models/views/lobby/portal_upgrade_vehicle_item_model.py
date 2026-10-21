from frameworks.wulf import Array
from frameworks.wulf import ViewModel
from portal.gui.impl.gen.view_models.views.lobby.portal_upgrade_ability_item_model import PortalUpgradeAbilityItemModel

class PortalUpgradeVehicleItemModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=5, commands=0):
        super(PortalUpgradeVehicleItemModel, self).__init__(properties=properties, commands=commands)
        return

    def getName(self):
        return self._getString(0)

    def setName(self, value):
        self._setString(0, value)
        return

    def getLvl(self):
        return self._getNumber(1)

    def setLvl(self, value):
        self._setNumber(1, value)
        return

    def getPoints(self):
        return self._getNumber(2)

    def setPoints(self, value):
        self._setNumber(2, value)
        return

    def getVehicleType(self):
        return self._getString(3)

    def setVehicleType(self, value):
        self._setString(3, value)
        return

    def getAbilities(self):
        return self._getArray(4)

    def setAbilities(self, value):
        self._setArray(4, value)
        return

    @staticmethod
    def getAbilitiesType():
        return PortalUpgradeAbilityItemModel

    def _initialize(self):
        super(PortalUpgradeVehicleItemModel, self)._initialize()
        self._addStringProperty(b'name', b'')
        self._addNumberProperty(b'lvl', 0)
        self._addNumberProperty(b'points', 0)
        self._addStringProperty(b'vehicleType', b'')
        self._addArrayProperty(b'abilities', Array())
        return
