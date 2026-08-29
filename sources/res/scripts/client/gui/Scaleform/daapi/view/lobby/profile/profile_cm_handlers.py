from gui.Scaleform.framework.entities.EventSystemEntity import EventSystemEntity
from gui.Scaleform.framework.managers.context_menu import AbstractContextMenuHandler
from gui.Scaleform.locale.MENU import MENU
from gui.shared import event_dispatcher as shared_events
from helpers import dependency
from skeletons.gui.game_control import IVehicleComparisonBasket
from skeletons.gui.shared import IItemsCache

class PROFILE(object):
    VEHICLE_COMPARE = b'profileVehicleCompare'
    VEHICLE_INFO = b'profileVehicleInfo'


class ProfileVehicleCMHandler(AbstractContextMenuHandler, EventSystemEntity):
    itemsCache = dependency.descriptor(IItemsCache)
    comparisonBasket = dependency.descriptor(IVehicleComparisonBasket)

    def __init__(self, cmProxy, ctx=None):
        super(ProfileVehicleCMHandler, self).__init__(cmProxy, ctx, {(PROFILE.VEHICLE_COMPARE): b'compareVehicle', 
           (PROFILE.VEHICLE_INFO): b'showVehicleInfo'})
        return

    def compareVehicle(self):
        self.comparisonBasket.addVehicle(self.__vehCD)
        return

    def showVehicleInfo(self):
        shared_events.showVehicleInfo(self.__vehCD)
        return

    def _generateOptions(self, ctx=None):
        vehicle = self.itemsCache.items.getItemByCD(self.__vehCD)
        options = []
        if not vehicle.isSecret or vehicle.isInInventory:
            options.append(self._makeItem(PROFILE.VEHICLE_INFO, MENU.CONTEXTMENU_VEHICLEINFOEX))
        if self.comparisonBasket.isEnabled():
            options.append(self._makeItem(PROFILE.VEHICLE_COMPARE, MENU.contextmenu(PROFILE.VEHICLE_COMPARE), {b'enabled': (self.comparisonBasket.isReadyToAdd(vehicle))}))
        return options

    def _initFlashValues(self, ctx):
        self.__vehCD = int(ctx.id)
        return
