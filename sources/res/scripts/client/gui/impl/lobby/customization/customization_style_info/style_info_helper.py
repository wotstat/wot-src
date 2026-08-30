import nations
from gui import GUI_NATIONS_ORDER_INDICES
from gui.impl.lobby.customization.shared import makeVehiclesShortNamesString
from gui.shared.gui_items.Vehicle import VEHICLE_TAGS, VEHICLE_TYPES_ORDER
from gui.shared.gui_items.customization.c11n_items import SpecialEvents
from helpers import int2roman
from items.components.c11n_constants import CustomizationDisplayType

class Parameters(object):
    PO_ID = b'po_id'
    ICON = b'icon'
    VALUE = b'value'


TAG_TO_PO_NAME = {(SpecialEvents.NY): b'ny', 
   (SpecialEvents.NY18): b'ny18', 
   (SpecialEvents.NY19): b'ny19', 
   (SpecialEvents.NY20): b'ny20', 
   (SpecialEvents.NY21): b'ny21', 
   (SpecialEvents.NY22): b'ny22', 
   (SpecialEvents.NY23): b'ny23', 
   (SpecialEvents.FOOTBALL18): b'football18', 
   (SpecialEvents.WINTER_HUNT): b'winter_hunt', 
   (SpecialEvents.KURSK_BATTLE): b'kursk_battle', 
   (SpecialEvents.HALLOWEEN): b'halloween', 
   (CustomizationDisplayType.HISTORICAL): b'historical', 
   (CustomizationDisplayType.NON_HISTORICAL): b'nonhistorical', 
   (CustomizationDisplayType.FANTASTICAL): b'fantastical', 
   b'rentable': b'rentable', 
   b'bonus': b'bonus'}

def getSuitable(item, currentVehicle=None):
    result = []
    for node in item.descriptor.filter.include:
        conditions = {}
        if node.nations:
            conditions[b'nations'] = []
            sortedNations = sorted(node.nations, key=GUI_NATIONS_ORDER_INDICES.get)
            for nation in sortedNations:
                conditions[b'nations'].append(nations.NAMES[nation])

        if node.tags:
            vehTypes = [vt for vt in VEHICLE_TYPES_ORDER if vt in node.tags]
            if vehTypes:
                conditions[b'vehType'] = vehTypes
            if VEHICLE_TAGS.PREMIUM in node.tags:
                conditions[b'isPremium'] = True
            if VEHICLE_TAGS.PREMIUM_IGR in node.tags:
                conditions[b'isPremiumIGR'] = True
        if node.levels:
            conditions[b'levels'] = []
            for level in node.levels:
                conditions[b'levels'].append(int2roman(level))

        if node.vehicles:
            vehicleName = makeVehiclesShortNamesString(set(node.vehicles), currentVehicle, flat=True)
            conditions[b'tankNames'] = vehicleName
        result.append(conditions)

    return result
