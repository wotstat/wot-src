from __future__ import absolute_import
import logging, typing
from collections import namedtuple
from enum import Enum
from future.utils import lmap, viewitems
from items import vehicles
from renewable_subscription_common.settings_constants import OptionalDevicesUsageConst
from soft_exception import SoftException
if typing.TYPE_CHECKING:
    from ResMgr import DataSection
    from typing import Dict, List
_logger = logging.getLogger(__name__)
VehicleLoadout = namedtuple(b'VehicleLoadout', (b'devices', b'percentage'))
VehicleLevelClassRoleGroup = namedtuple(b'VehicleLevelClassRoleGroup', (b'level', b'vehClass', b'role'))

class GenericOptionalDevice(Enum):
    STEREOSCOPE = 1
    TURBOCHARGER = 2
    ENHANCED_AIM_DRIVES = 3
    GROUSERS = 4
    AIMING_STABILIZER = 5
    ANTIFRAGMENTATION_LINING = 6
    CAMOUFLAGE_NET = 7
    IMPROVED_SIGHTS = 8
    VENTILATION = 9
    HEALTH_RESERVE = 10
    ROTATION_MECHANISM = 11
    RAMMER = 12
    COATED_OPTICS = 13
    ADDIT_INVISIBILITY_DEVICE = 14
    IMPROVED_CONFIGURATION = 15
    RADIO_COMMUNICATION = 16
    COMMANDERS_VIEW = 17
    MODERNIZED_EXTRA_HEALTH_RESERVE_ANTIFRAGMENTATION_LINING = 18
    MODERNIZED_TURBOCHARGER_ROTATION_MECHANISM = 19
    MODERNIZED_AIM_DRIVES_AIMING_STABILIZER = 20
    MODERNIZED_IMPROVED_SIGHTS_ENHANCED_AIM_DRIVES = 21


EQUIPMENT_NAME_TO_GENERIC_OPTIONAL_DEVICE_MAP = {b'stereoscope': (GenericOptionalDevice.STEREOSCOPE), 
   b'turbocharger': (GenericOptionalDevice.TURBOCHARGER), 
   b'enhancedAimDrives': (GenericOptionalDevice.ENHANCED_AIM_DRIVES), 
   b'grousers': (GenericOptionalDevice.GROUSERS), 
   b'aimingStabilizer': (GenericOptionalDevice.AIMING_STABILIZER), 
   b'antifragmentationLining': (GenericOptionalDevice.ANTIFRAGMENTATION_LINING), 
   b'camouflageNet': (GenericOptionalDevice.CAMOUFLAGE_NET), 
   b'improvedSights': (GenericOptionalDevice.IMPROVED_SIGHTS), 
   b'ventilation': (GenericOptionalDevice.VENTILATION), 
   b'healthReserve': (GenericOptionalDevice.HEALTH_RESERVE), 
   b'rotationMechanism': (GenericOptionalDevice.ROTATION_MECHANISM), 
   b'rammer': (GenericOptionalDevice.RAMMER), 
   b'coatedOptics': (GenericOptionalDevice.COATED_OPTICS), 
   b'additInvisibilityDevice': (GenericOptionalDevice.ADDIT_INVISIBILITY_DEVICE), 
   b'improvedConfiguration': (GenericOptionalDevice.IMPROVED_CONFIGURATION), 
   b'radioCommunication': (GenericOptionalDevice.RADIO_COMMUNICATION), 
   b'commandersView': (GenericOptionalDevice.COMMANDERS_VIEW), 
   b'improvedVentilation': (GenericOptionalDevice.VENTILATION), 
   b'tankRammer': (GenericOptionalDevice.RAMMER), 
   b'additionalInvisibilityDevice': (GenericOptionalDevice.ADDIT_INVISIBILITY_DEVICE), 
   b'extraHealthReserve': (GenericOptionalDevice.HEALTH_RESERVE), 
   b'improvedRadioCommunication': (GenericOptionalDevice.RADIO_COMMUNICATION), 
   b'improvedRotationMechanism': (GenericOptionalDevice.ROTATION_MECHANISM), 
   b'modernizedExtraHealthReserveAntifragmentationLining': (GenericOptionalDevice.MODERNIZED_EXTRA_HEALTH_RESERVE_ANTIFRAGMENTATION_LINING), 
   b'modernizedAimDrivesAimingStabilizer': (GenericOptionalDevice.MODERNIZED_AIM_DRIVES_AIMING_STABILIZER), 
   b'modernizedTurbochargerRotationMechanism': (GenericOptionalDevice.MODERNIZED_TURBOCHARGER_ROTATION_MECHANISM), 
   b'modernizedImprovedSightsEnhancedAimDrives': (GenericOptionalDevice.MODERNIZED_IMPROVED_SIGHTS_ENHANCED_AIM_DRIVES)}
GENERIC_OPTIONAL_DEVICE_MAP_TO_EQUIPMENT_NAME = {v: k for k, v in viewitems(EQUIPMENT_NAME_TO_GENERIC_OPTIONAL_DEVICE_MAP)}

def _readOptionalDevicesUsage(section):
    tempConfig = {}
    vehicleName = section.readString(b'vehicle')
    vehTypeCompDescr = _getVehicleTypeCompDescr(vehicleName)
    tempConfig[vehTypeCompDescr] = _parseDevicesLoadouts(section)
    return tempConfig


def _parseDevicesLoadouts(reader):
    section = reader[b'loadouts']
    loadouts = []
    for _, values in section.items():
        devices = []
        for device in values.readString(b'devices').split():
            device = device.strip()
            if device not in EQUIPMENT_NAME_TO_GENERIC_OPTIONAL_DEVICE_MAP:
                _logger.warning(b'Unknown device %s in optional device assistant config.', device)
                continue
            devices.append(EQUIPMENT_NAME_TO_GENERIC_OPTIONAL_DEVICE_MAP.get(device).value)

        percentage = values.readFloat(b'percentage', 0.0)
        loadouts.append((devices, percentage))

    return loadouts


def _getVehicleTypeCompDescr(vehicleName):
    try:
        return vehicles.makeVehicleTypeCompDescrByName(vehicleName)
    except SoftException:
        _logger.warning(b'Vehicle %s does not exist! Check optional devices assistant configs to fix it.', vehicleName)

    return -1


def convertServerDiffToRichTypes(configDict):
    updateConfig = configDict.get(OptionalDevicesUsageConst.UPDATE, {})
    for vehicle, loadoutList in viewitems(updateConfig):
        newLoadoutList = []
        for loadout in loadoutList:
            devicesList = lmap(GenericOptionalDevice, loadout[0])
            percentage = loadout[1]
            newLoadoutList.append(VehicleLoadout(devicesList, percentage))

        updateConfig[vehicle] = newLoadoutList

    return configDict


def _validateOverrideConfig(configDict):
    removedVehicles = set(configDict.get(OptionalDevicesUsageConst.REMOVE, []))
    updatedEquipmentUsages = set(configDict.get(OptionalDevicesUsageConst.UPDATE, {}).keys())
    copiedVehiclesFrom = configDict.get(OptionalDevicesUsageConst.COPY, {}).values()
    copiedVehiclesTo = configDict.get(OptionalDevicesUsageConst.COPY, {}).keys()
    if -1 in removedVehicles or -1 in updatedEquipmentUsages or -1 in copiedVehiclesFrom or -1 in copiedVehiclesTo:
        raise SoftException(b'There is at least one nonexistent vehicle in optional_devices_usage_override_config.xml. See warnings.')
    removedUpdated = removedVehicles.intersection(updatedEquipmentUsages)
    if removedUpdated:
        raise SoftException((b'There are removed AND updated vehicles in optional_devices_usage_override_config.xml. {}').format([vehicles.getVehicleType(removedVehicle).name for removedVehicle in removedUpdated]))
    removedCopied = removedVehicles.intersection(copiedVehiclesFrom)
    if removedCopied:
        raise SoftException((b'There are removed vehicles as "vehicleFrom" in copy config. {}').format([vehicles.getVehicleType(removedVehicle).name for removedVehicle in removedCopied]))
    wrongDeviceLenVehicles = []
    for vehicleCD, data in configDict.get(OptionalDevicesUsageConst.UPDATE, {}).items():
        if len(data) > 3:
            wrongDeviceLenVehicles.append(vehicleCD)

    if wrongDeviceLenVehicles:
        raise SoftException((b'Invalid number of popular setups for vehicles: {}').format([vehicles.getVehicleType(vehicle).name for vehicle in wrongDeviceLenVehicles]))
    return
