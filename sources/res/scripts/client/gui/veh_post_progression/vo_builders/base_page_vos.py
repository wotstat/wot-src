import typing
from gui.impl import backport
from gui.impl.gen import R
from gui.shared.formatters import text_styles, getRoleTextWithIcon
from gui.shared.gui_items.Vehicle import getNationLessName, getIconResourceName
if typing.TYPE_CHECKING:
    from gui.shared.gui_items.Vehicle import Vehicle

def getBaseButtonsVO(vehicle):
    iconName = getIconResourceName(getNationLessName(vehicle.name))
    return {b'shopIconPath': (backport.image(R.images.gui.maps.shop.vehicles.c_360x270.dyn(iconName)())), 
       b'compareBtnVisible': True, 
       b'goToVehicleViewBtnVisible': True, 
       b'isPremium': (vehicle.isPremium or vehicle.buyPrices.itemPrice.isActionPrice()), 
       b'vehicleId': (vehicle.intCD)}


def getBaseDataVO(vehicle):
    return {b'showDemountAllPairsBtn': False, 
       b'showExpBlock': False, 
       b'vehicleButton': {}, b'vehicleInfo': {}, b'nation': (vehicle.nationName)}


def getBaseTitleVO(vehicle):
    tankUserName = vehicle.userName
    return {b'intCD': (vehicle.intCD), 
       b'tankNameStr': (text_styles.grandTitle(tankUserName)), 
       b'tankNameStrSmall': (text_styles.promoTitle(tankUserName)), 
       b'statusStr': b'', 
       b'roleText': (getRoleTextWithIcon(vehicle.role, vehicle.roleLabel)), 
       b'showInfoIcon': False}
