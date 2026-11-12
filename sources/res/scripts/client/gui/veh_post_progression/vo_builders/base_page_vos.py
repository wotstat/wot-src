import typing
from account_helpers.settings_core.settings_constants import GAME
from gui.impl import backport
from gui.impl.gen import R
from gui.shared.formatters import text_styles, getRoleTextWithIcon
from gui.shared.gui_items.Vehicle import getNationLessName, getIconResourceName
from gui.shared.gui_items.artefacts import getAbilityVO
from helpers import dependency
from skeletons.account_helpers.settings_core import ISettingsCore
if typing.TYPE_CHECKING:
    from typing import Dict
    from gui.shared.gui_items.Vehicle import Vehicle

def getBaseButtonsVO(vehicle):
    iconName = getIconResourceName(getNationLessName(vehicle.name))
    return {b'shopIconPath': (backport.image(R.images.gui.maps.shop.vehicles.c_360x270.dyn(iconName)())), 
       b'compareBtnVisible': True, 
       b'goToVehicleViewBtnVisible': True, 
       b'isPremium': (vehicle.isPremium), 
       b'vehicleId': (vehicle.intCD), 
       b'isEarlyAccess': (vehicle.isEarlyAccess)}


def getBaseDataVO(vehicle):
    return {b'showDemountAllPairsBtn': False, 
       b'showExpBlock': False, 
       b'vehicleButton': {}, b'vehicleInfo': {}, b'nation': (vehicle.nationName)}


@dependency.replace_none_kwargs(settingsCore=ISettingsCore)
def getBaseTitleVO(vehicle, settingsCore=None):
    tankUserName = vehicle.userName
    difficulty = vehicle.difficulty
    if not settingsCore.getSetting(GAME.SHOW_VEHICLE_DIFFICULTY_IN_RESEARCH):
        difficulty = 0
    return {b'intCD': (vehicle.intCD), 
       b'tankNameStr': (text_styles.grandTitle(tankUserName)), 
       b'tankNameStrSmall': (text_styles.promoTitle(tankUserName)), 
       b'statusStr': b'', 
       b'roleText': (getRoleTextWithIcon(vehicle.role, vehicle.roleLabel)), 
       b'difficulty': difficulty, 
       b'showInfoIcon': False, 
       b'ability': (getAbilityVO(vehicle))}
