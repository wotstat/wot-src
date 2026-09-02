import logging
from collections import namedtuple
import typing
from ResMgr import DataSection
from bonus_readers import readBonusSection, SUPPORTED_BONUSES
from gui.server_events.bonuses import getNonQuestBonuses, splitBonuses
import resource_helper
from soft_exception import SoftException
_logger = logging.getLogger(__name__)
_EVENT_CONFIG_XML_PATH = b'gui/event_gui_settings.xml'
_EVENT_SETTINGS = None
_EventSettings = namedtuple(b'_EventSettings', (b'vehicleCharacteristics',))
_VehicleCharacteristics = namedtuple(b'VehicleCharacteristics', (b'pros', b'cons', b'role'))

def _readEventSettings():
    _, section = resource_helper.getRoot(_EVENT_CONFIG_XML_PATH)
    result = _EventSettings(_readVehicleCharacteristics(section[b'vehicleCharacteristics']))
    resource_helper.purgeResource(_EVENT_CONFIG_XML_PATH)
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
    for subsection in section.values():
        bonuses = []
        items = readBonusSection(SUPPORTED_BONUSES, subsection)
        for key, value in items.iteritems():
            bonuses.extend(getNonQuestBonuses(key, value))

        collection.extend(splitBonuses(bonuses))

    return collection


def getVehicleCharacteristics():
    data = getEventSettings().vehicleCharacteristics
    if data is None:
        _logger.error(b'There is not vehicle characteristics')
        return {}
    else:
        return data


def getEventSettings():
    global _EVENT_SETTINGS
    if _EVENT_SETTINGS is None:
        _EVENT_SETTINGS = _readEventSettings()
    return _EVENT_SETTINGS
