from constants import MIN_VEHICLE_LEVEL, MAX_VEHICLE_LEVEL
from nations import INDICES
from gui import GUI_NATIONS, GUI_NATIONS_ORDER_INDEX
from gui.Scaleform import getVehicleTypeAssetPath, getNationsFilterAssetPath, getLevelsAssetPath
from gui.Scaleform.locale.MENU import MENU
from gui.shared.gui_items.Vehicle import VEHICLE_TYPES_ORDER, VEHICLE_TYPES_ORDER_INDICES

def packIntVehicleTypesFilter(defaultVehType=-1):
    result = [
     {b'label': (MENU.CAROUSEL_TANK_FILTER_ALL), 
        b'data': defaultVehType, 
        b'icon': (getVehicleTypeAssetPath(b'all'))}]
    for idx, vehicleType in enumerate(VEHICLE_TYPES_ORDER):
        result.append({b'label': (b'#menu:carousel_tank_filter/' + vehicleType), 
           b'data': idx, 
           b'icon': (getVehicleTypeAssetPath(vehicleType))})

    return result


def packVehicleTypesFilter(defaultVehType, types=VEHICLE_TYPES_ORDER):
    if types is not VEHICLE_TYPES_ORDER:
        types = sorted(types, key=(lambda _type: VEHICLE_TYPES_ORDER_INDICES[_type]))
    result = [
     {b'label': (MENU.CAROUSEL_TANK_FILTER_ALL), 
        b'data': defaultVehType, 
        b'icon': (getVehicleTypeAssetPath(b'all'))}]
    for vehicleType in types:
        result.append({b'label': (b'#menu:carousel_tank_filter/' + vehicleType), 
           b'data': vehicleType, 
           b'icon': (getVehicleTypeAssetPath(vehicleType))})

    return result


def packNationsFilter(nations=GUI_NATIONS):
    if nations is not GUI_NATIONS:
        nations = sorted(nations, key=(lambda nation: GUI_NATIONS_ORDER_INDEX[nation]))
    result = [
     {b'label': (MENU.NATIONS_ALL), 
        b'data': (-1), 
        b'icon': (getNationsFilterAssetPath(b'all'))}]
    for nation in nations:
        result.append({b'label': (MENU.nations(nation)), 
           b'data': (INDICES[nation]), 
           b'icon': (getNationsFilterAssetPath(nation))})

    return result


def packVehicleLevelsFilter(levelRange=range(MIN_VEHICLE_LEVEL, MAX_VEHICLE_LEVEL + 1)):
    result = [
     {b'label': (MENU.LEVELS_ALL), 
        b'data': (-1), 
        b'icon': (getLevelsAssetPath(b'level_all'))}]
    for level in levelRange:
        result.append({b'label': (b'#menu:levels/%d' % level), 
           b'data': level, 
           b'icon': (getLevelsAssetPath(b'level_%d' % level))})

    return result
