from enum import Enum
from frameworks.wulf import Array
from frameworks.wulf import ViewModel
from portal.gui.impl.gen.view_models.views.lobby.tooltips.bonus_parameter import BonusParameter
from portal.gui.impl.gen.view_models.views.lobby.tooltips.modules_parameters import ModulesParameters

class ItemType(Enum):
    GUN = b'vehicleGun'
    ENGINE = b'vehicleEngine'
    TURRET = b'vehicleTurret'
    HULL = b'vehicleChassis'
    DAMAGEBONUS = b'damageBonus'
    KDBONUS = b'kdBonus'
    SMALLMOBILITYBONUS = b'smallMobilityBonus'
    SMALLKDBONUS = b'smallKDBonus'


class ModuleModifier(Enum):
    DAMAGEGUN = b'damageGun'
    QUICKFIREGUN = b'quickfireGun'
    DRUMGUN = b'drumGun'
    DUALGUN = b'dualGun'
    MAGAZINERELOADINGGUN = b'magazineReloadingGun'
    FASTHULL = b'fastHull'
    HPHULL = b'hpHull'
    ARMOREDHULL = b'armoredHull'
    FASTTURRET = b'fastTurret'
    HPTURRET = b'hpTurret'
    FASTENGINE = b'fastEngine'
    POWERENGINE = b'powerEngine'


class ModulesTooltipModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=7, commands=0):
        super(ModulesTooltipModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def bonusParameter(self):
        return self._getViewModel(0)

    @staticmethod
    def getBonusParameterType():
        return BonusParameter

    def getItemType(self):
        return ItemType(self._getString(1))

    def setItemType(self, value):
        self._setString(1, value.value)
        return

    def getModuleModifier(self):
        return ModuleModifier(self._getString(2))

    def setModuleModifier(self, value):
        self._setString(2, value.value)
        return

    def getModuleName(self):
        return self._getString(3)

    def setModuleName(self, value):
        self._setString(3, value)
        return

    def getNextLevel(self):
        return self._getNumber(4)

    def setNextLevel(self, value):
        self._setNumber(4, value)
        return

    def getIsModule(self):
        return self._getBool(5)

    def setIsModule(self, value):
        self._setBool(5, value)
        return

    def getParameters(self):
        return self._getArray(6)

    def setParameters(self, value):
        self._setArray(6, value)
        return

    @staticmethod
    def getParametersType():
        return ModulesParameters

    def _initialize(self):
        super(ModulesTooltipModel, self)._initialize()
        self._addViewModelProperty(b'bonusParameter', BonusParameter())
        self._addStringProperty(b'itemType')
        self._addStringProperty(b'moduleModifier')
        self._addStringProperty(b'moduleName', b'')
        self._addNumberProperty(b'nextLevel', 0)
        self._addBoolProperty(b'isModule', True)
        self._addArrayProperty(b'parameters', Array())
        return
