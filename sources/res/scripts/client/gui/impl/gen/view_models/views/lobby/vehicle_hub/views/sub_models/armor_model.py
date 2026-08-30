from enum import Enum
from frameworks.wulf import Array, ViewModel
from gui.impl.gen import R
from gui.impl.gen.view_models.views.lobby.vehicle_hub.views.sub_models.armor_attacker import ArmorAttacker
from gui.impl.gen.view_models.views.lobby.vehicle_hub.views.sub_models.armor_value_model import ArmorValueModel
from gui.impl.gen.view_models.views.lobby.vehicle_hub.views.sub_models.armor_vehicle import ArmorVehicle

class Modes(Enum):
    NOMINAL = b'nominal'
    PENETRATION = b'penetration'
    NO_ARMOR = b'no_armor'


class DCCType(Enum):
    PENETRATION = b'penetration'
    RICOCHET = b'ricochet'
    NO_DAMAGE = b'no_damage'


class MinorShortTooltipTypes(Enum):
    MAIN_ARMOR = b'mainArmor'
    SPACED_ARMOR = b'spacedArmor'
    DEALING_DAMAGE_CHANCE = b'dealingDamageChance'
    NO_DAMAGE = b'noDamage'
    RICOCHET = b'ricochet'
    ATTACKING_CONFIGURATION = b'attackingConfiguration'


class ArmorModel(ViewModel):
    __slots__ = (b'onDragModule', b'onDragStateChanged', b'onModeChanged', b'onAttackerClicked', b'onGunItemClick', b'onTurretItemClick', b'onAttackerGunItemClick', b'onAttackerShellItemClick')

    def __init__(self, properties=11, commands=8):
        super(ArmorModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def attacker(self):
        return self._getViewModel(0)

    @staticmethod
    def getAttackerType():
        return ArmorAttacker

    @property
    def vehicle(self):
        return self._getViewModel(1)

    @staticmethod
    def getVehicleType():
        return ArmorVehicle

    def getMainArmor(self):
        return self._getArray(2)

    def setMainArmor(self, value):
        self._setArray(2, value)
        return

    @staticmethod
    def getMainArmorType():
        return ArmorValueModel

    def getSpacedArmor(self):
        return self._getArray(3)

    def setSpacedArmor(self, value):
        self._setArray(3, value)
        return

    @staticmethod
    def getSpacedArmorType():
        return ArmorValueModel

    def getMainGradient(self):
        return self._getResource(4)

    def setMainGradient(self, value):
        self._setResource(4, value)
        return

    def getSpacedGradient(self):
        return self._getResource(5)

    def setSpacedGradient(self, value):
        self._setResource(5, value)
        return

    def getPenetrationChance(self):
        return self._getArray(6)

    def setPenetrationChance(self, value):
        self._setArray(6, value)
        return

    @staticmethod
    def getPenetrationChanceType():
        return ArmorValueModel

    def getNoDamage(self):
        return self._getArray(7)

    def setNoDamage(self, value):
        self._setArray(7, value)
        return

    @staticmethod
    def getNoDamageType():
        return ArmorValueModel

    def getPenetrationGradient(self):
        return self._getResource(8)

    def setPenetrationGradient(self, value):
        self._setResource(8, value)
        return

    def getDragModuleMode(self):
        return self._getBool(9)

    def setDragModuleMode(self, value):
        self._setBool(9, value)
        return

    def getSelectedMode(self):
        return self._getString(10)

    def setSelectedMode(self, value):
        self._setString(10, value)
        return

    def _initialize(self):
        super(ArmorModel, self)._initialize()
        self._addViewModelProperty(b'attacker', ArmorAttacker())
        self._addViewModelProperty(b'vehicle', ArmorVehicle())
        self._addArrayProperty(b'mainArmor', Array())
        self._addArrayProperty(b'spacedArmor', Array())
        self._addResourceProperty(b'mainGradient', R.invalid())
        self._addResourceProperty(b'spacedGradient', R.invalid())
        self._addArrayProperty(b'penetrationChance', Array())
        self._addArrayProperty(b'noDamage', Array())
        self._addResourceProperty(b'penetrationGradient', R.invalid())
        self._addBoolProperty(b'dragModuleMode', False)
        self._addStringProperty(b'selectedMode', b'')
        self.onDragModule = self._addCommand(b'onDragModule')
        self.onDragStateChanged = self._addCommand(b'onDragStateChanged')
        self.onModeChanged = self._addCommand(b'onModeChanged')
        self.onAttackerClicked = self._addCommand(b'onAttackerClicked')
        self.onGunItemClick = self._addCommand(b'onGunItemClick')
        self.onTurretItemClick = self._addCommand(b'onTurretItemClick')
        self.onAttackerGunItemClick = self._addCommand(b'onAttackerGunItemClick')
        self.onAttackerShellItemClick = self._addCommand(b'onAttackerShellItemClick')
        return
