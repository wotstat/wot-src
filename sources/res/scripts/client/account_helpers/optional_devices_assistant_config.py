import csv, typing
from io import StringIO
import ResMgr
from constants import VEHICLE_CLASS_INDICES, ROLE_LABEL_TO_TYPE
from renewable_subscription_common.optional_devices_usage_config import VehicleLoadout, EQUIPMENT_NAME_TO_GENERIC_OPTIONAL_DEVICE_MAP, _getVehicleTypeCompDescr, VehicleLevelClassRoleGroup
from soft_exception import SoftException
if typing.TYPE_CHECKING:
    from typing import Dict
_USAGE_CONFIG_FILE = b'scripts/item_defs/optional_devices_assistance/optional_devices_usage.csv'
_USAGE_CONFIG_FILE_LEGENDARY = b'scripts/item_defs/optional_devices_assistance/optional_devices_usage_legendary.csv'
_FALLBACK_CONFIG_FILE = b'scripts/item_defs/optional_devices_assistance/optional_devices_fallback_usage.xml'
DEFAULT_ROLE = b'NotDefined'

def readOptionalDevicesUsageConfig(fileName):
    config = {}
    section = ResMgr.openSection(fileName)
    reader = csv.reader(StringIO(unicode(section.asString)), delimiter=b';')
    next(reader)
    for row in reader:
        if not row:
            continue
        if len(row) != 5:
            raise SoftException(b'Wrong data in optional devices usage config. %s', row)
        loadouts = config.setdefault(_getVehicleTypeCompDescr(row[0]), [])
        devices = []
        for device in row[1:4]:
            if not device:
                continue
            mappedDevice = EQUIPMENT_NAME_TO_GENERIC_OPTIONAL_DEVICE_MAP.get(device, None)
            if not mappedDevice:
                raise SoftException(b'Cannot map device from optional devices usage config. Unknown device. %s', device)
            devices.append(mappedDevice)

        percentage = float(row[4])
        loadouts.append(VehicleLoadout(devices, percentage))

    ResMgr.purge(fileName, True)
    return config


def readOptionalDevicesUsageFallbackConfig():
    config = {}
    section = ResMgr.openSection(_FALLBACK_CONFIG_FILE)[b'']
    if section is None:
        return config
    else:
        for _, subsection in section.items():
            config.update(_readOptionalDevicesFallbackUsage(subsection))

        return config


def _readOptionalDevicesFallbackUsage(section):
    tempConfig = {}
    level = section.readInt(b'level')
    type = section.readString(b'type')
    role = section.readString(b'role', DEFAULT_ROLE)
    vehicleName = section.readString(b'vehicleFrom')
    vehTypeCompDescr = _getVehicleTypeCompDescr(vehicleName)
    configKey = VehicleLevelClassRoleGroup(level, type, ROLE_LABEL_TO_TYPE.get(role))
    tempConfig[configKey] = vehTypeCompDescr
    return tempConfig
