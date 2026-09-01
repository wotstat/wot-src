from __future__ import absolute_import
import logging
from collections import namedtuple
import typing
from future.utils import viewitems
from ResMgr import DataSection
from bonus_readers import readBonusSection, getSupportedBonuses
from gui.server_events.bonuses import getNonQuestBonuses, splitBonuses
import resource_helper
from soft_exception import SoftException
_logger = logging.getLogger(__name__)
_WT_GUI_CONFIG_XML_PATH = b'white_tiger/gui/gui_settings.xml'
_WT_GUI_SETTINGS = None
_WTGuiSettings = namedtuple(b'_WTGuiSettings', b'vehicleCharacteristics')
_VehicleCharacteristics = namedtuple(b'VehicleCharacteristics', (b'pros', b'cons', b'role'))

def _readWTGuiSettings():
    _, section = resource_helper.getRoot(_WT_GUI_CONFIG_XML_PATH)
    result = _WTGuiSettings(_readVehicleCharacteristics(section[b'vehicleCharacteristics']))
    resource_helper.purgeResource(_WT_GUI_CONFIG_XML_PATH)
    return result


def _readVehicleCharacteristics(section):
    properties = frozenset(section[b'properties'].asString.split(b' '))
    result = {}
    for subsection in section[b'vehicles'].values():
        vehicle = subsection[b'name'].asString
        result[vehicle] = _VehicleCharacteristics(_readProperties(subsection[b'pros'], properties), _readProperties(subsection[b'cons'], properties), role=subsection[b'role'].asString)

    return result


def _readProperties(section, allProperties):
    properties = section.asString.split(b' ')
    for prop in properties:
        if prop not in allProperties:
            raise SoftException(b'Incorrect vehicle property "%s" in the event settings' % prop)

    return properties


def _readCollection(section):
    collection = []
    supportedBonuses = getSupportedBonuses()
    for subsection in section.values():
        bonuses = []
        items = readBonusSection(supportedBonuses, subsection)
        for key, value in viewitems(items):
            bonuses.extend(getNonQuestBonuses(key, value))

        collection.extend(splitBonuses(bonuses))

    return collection


def getVehicleCharacteristics():
    data = getWTGuiSettings().vehicleCharacteristics
    if data is None:
        _logger.error(b'There is not vehicle characteristics')
        return {}
    else:
        return data


def getWTGuiSettings():
    global _WT_GUI_SETTINGS
    if _WT_GUI_SETTINGS is None:
        _WT_GUI_SETTINGS = _readWTGuiSettings()
    return _WT_GUI_SETTINGS
