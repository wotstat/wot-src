from gui.shared.gui_items.Vehicle import Vehicle
from gui.shared.items_parameters.formatters import formatParameter, FORMAT_SETTINGS, _niceRangeFormat
from gui.shared.items_parameters.params import VehicleParams
from helpers import dependency
from skeletons.gui.game_control import IEpicBattleMetaGameController
from supply_shared import Supply
SUPPLY_PARAMS_KEYS = (b'avgDamage', b'avgPiercingPower', b'flameMaxDistance', b'clipFireRate', b'reloadTimeSecs', b'shotDispersionAngle', b'maxHealth', b'turretArmor', b'circularVisionRadius', b'captureTime', b'resurrectTime', b'cooldownTime', b'healTime', b'gunYawLimits')

def _generateSettings():
    s = {b'healTime': _niceRangeFormat}
    s.update(FORMAT_SETTINGS)
    return s


_FORMAT_SETTINGS = _generateSettings()

class SupplyParams(VehicleParams):
    __epicMetaController = dependency.descriptor(IEpicBattleMetaGameController)

    @property
    def resurrectTime(self):
        supplyID = Supply.getID(self._itemDescr.type)
        if supplyID != Supply.AIRSHIP:
            return self.__epicMetaController.getSupplyParams()[supplyID][b'resurrectTime']
        else:
            return

    @property
    def captureTime(self):
        supplyID = Supply.getID(self._itemDescr.type)
        if supplyID != Supply.AIRSHIP:
            return None
        else:
            return self.__epicMetaController.getSupplyParams()[supplyID][b'captureTime']

    @property
    def cooldownTime(self):
        supplyID = Supply.getID(self._itemDescr.type)
        if supplyID != Supply.AIRSHIP:
            return None
        else:
            return self.__epicMetaController.getSupplyParams()[supplyID][b'cooldownTime']


def getSupplyParameters(vehicle):
    params = SupplyParams(vehicle).getParamsDict()
    filteredParams = {key: formatParameter(key, params.get(key), formatSettings=_FORMAT_SETTINGS) for key in SUPPLY_PARAMS_KEYS}
    return filteredParams


def getArmorDamageFactors(descriptor):
    hullDamageFactor = min(matInfo.vehicleDamageFactor for matInfo in descriptor.hull.materials.itervalues())
    turretDamageFactor = min(matInfo.vehicleDamageFactor for matInfo in descriptor.turret.materials.itervalues())
    return (hullDamageFactor, turretDamageFactor)
