from gui.Scaleform.daapi.view.lobby.rally.vo_converters import makeVehicleBasicVO
from gui.Scaleform.daapi.view.lobby.vehicle_compare.formatters import packHeaderColumnData
from gui.Scaleform.daapi.view.meta.TradeInPopupMeta import TradeInPopupMeta
from gui.Scaleform.framework.entities.DAAPIDataProvider import SortableDAAPIDataProvider
from gui.Scaleform.locale.DIALOGS import DIALOGS
from gui.Scaleform.locale.RES_ICONS import RES_ICONS
from gui.shared.items_cache import CACHE_SYNC_REASON
from gui.shared.gui_items import GUI_ITEM_TYPE
from gui.shared.gui_items.Vehicle import Vehicle
from gui.shared.utils.functions import makeTooltip
from gui.shared.money import Currency
from helpers import dependency
from skeletons.gui.game_control import ITradeInController
from gui.shared.tooltips.formatters import packItemActionTooltipData
from skeletons.gui.shared import IItemsCache
_INACCESSIBLE_FOR_TRADE_STATES = (
 Vehicle.VEHICLE_STATE.DAMAGED,
 Vehicle.VEHICLE_STATE.EXPLODED,
 Vehicle.VEHICLE_STATE.DESTROYED,
 Vehicle.VEHICLE_STATE.BATTLE,
 Vehicle.VEHICLE_STATE.IN_PREBATTLE,
 Vehicle.VEHICLE_STATE.LOCKED,
 Vehicle.VEHICLE_STATE.DISABLED)

class TradeInPopup(TradeInPopupMeta):
    itemsCache = dependency.descriptor(IItemsCache)
    tradeIn = dependency.descriptor(ITradeInController)

    def __init__(self, ctx=None):
        super(TradeInPopup, self).__init__(ctx)
        data = ctx[b'data']
        self.__tradeInDP = None
        self.__tradeInVehCD = int(data.tradeIn)
        self.__tradeOffVehCD = int(data.tradeOff)
        return

    def _populate(self):
        super(TradeInPopup, self)._populate()
        self.__tradeInDP = _TradeInDataProvider()
        self.__tradeInDP.setFlashObject(self.as_getDPS())
        self.__fillDP()
        self.itemsCache.onSyncCompleted += self.__onResync
        self.__initControls()
        return

    def _dispose(self):
        self.itemsCache.onSyncCompleted -= self.__onResync
        self.__tradeInDP.fini()
        self.__tradeInDP = None
        super(TradeInPopup, self)._dispose()
        return

    def __initControls(self):
        headers = [
         packHeaderColumnData(b'nationID', 49, 40, tooltip=DIALOGS.TRADEINPOPOVER_SORTING_NATION, icon=RES_ICONS.MAPS_ICONS_FILTERS_NATIONS_ALL, enabled=True),
         packHeaderColumnData(b'typeIndex', 45, 40, tooltip=DIALOGS.TRADEINPOPOVER_SORTING_VEHTYPE, icon=RES_ICONS.MAPS_ICONS_FILTERS_TANKS_ALL, enabled=True),
         packHeaderColumnData(b'level', 45, 40, tooltip=DIALOGS.TRADEINPOPOVER_SORTING_VEHLVL, icon=RES_ICONS.MAPS_ICONS_BUTTONS_TAB_SORT_BUTTON_LEVEL_6_8, enabled=True),
         packHeaderColumnData(b'shortUserName', 148, 40, label=DIALOGS.TRADEINPOPOVER_SORTING_VEHNAME_HEADER, tooltip=DIALOGS.TRADEINPOPOVER_SORTING_VEHNAME, enabled=True, verticalTextAlign=b'center'),
         packHeaderColumnData(b'price', 95, 40, label=DIALOGS.TRADEINPOPOVER_SORTING_SAVING_FORMATTED, tooltip=DIALOGS.TRADEINPOPOVER_SORTING_SAVING, enabled=True, verticalTextAlign=b'center')]
        self.as_setInitDataS({b'title': (DIALOGS.TRADEINPOPOVER_TITLE), 
           b'description': (DIALOGS.TRADEINPOPOVER_DESCR), 
           b'defaultSortField': b'price', 
           b'defaultSortDirection': b'descending', 
           b'tableHeaders': headers})
        return

    def onWindowClose(self):
        self.destroy()
        return

    def onSelectVehicle(self, vehicleCD):
        self.tradeIn.selectVehicleToSell(vehicleCD)
        self.onWindowClose()
        return

    def __onResync(self, reason, diff):
        if reason == CACHE_SYNC_REASON.SHOP_RESYNC or GUI_ITEM_TYPE.VEHICLE in diff:
            self.__tradeInDP.clear()
            self.__fillDP()
        return

    def __fillDP(self):
        self.__tradeInDP.setSelectedID(self.__tradeOffVehCD)
        self.__tradeInDP.buildList(self.tradeIn.getVehiclesToSell(True))
        self.__tradeInDP.refresh()
        return


class _TradeInDataProvider(SortableDAAPIDataProvider):

    def __init__(self):
        super(_TradeInDataProvider, self).__init__()
        self.__list = []
        self.__mapping = {}
        self.__selectedID = None
        return

    @property
    def collection(self):
        return self.__list

    def emptyItem(self):
        return

    def clear(self):
        self.__list = []
        self.__mapping.clear()
        self.__selectedID = None
        return

    def fini(self):
        self.clear()
        self.destroy()
        return

    def getSelectedIdx(self):
        if self.__selectedID in self.__mapping:
            return self.__mapping[self.__selectedID]
        return -1

    def setSelectedID(self, selId):
        self.__selectedID = selId
        return

    def buildList(self, changedVehsCDs):
        for idx, (vehCD, veh) in enumerate(changedVehsCDs.iteritems()):
            self.__list.append(self.__makeVO(veh))
            self.__mapping[vehCD] = idx

        return

    def pyGetSelectedIdx(self):
        return self.getSelectedIdx()

    def pySortOn(self, fields, order):
        super(_TradeInDataProvider, self).pySortOn(fields, order)
        self.__rebuildMapping()
        self.refresh()
        return

    def __rebuildMapping(self):
        self.__mapping = {item[b'intCD']: idx for idx, item in enumerate(self.sortedCollection)}
        return

    def __makeVO(self, vehicle):
        vehicleVO = makeVehicleBasicVO(vehicle)
        if vehicleVO is None:
            return
        else:
            vehicleVO[b'price'] = vehicle.tradeOffPrice.getSignValue(Currency.GOLD)
            vehicleVO[b'actionPrice'] = self._getItemPriceActionData(vehicle)
            vState, _ = vehicle.getState()
            if vState in _INACCESSIBLE_FOR_TRADE_STATES:
                vehicleVO[b'isReadyToFight'] = False
                vehicleVO[b'enabled'] = False
                vehicleVO[b'tooltip'] = makeTooltip(b'#tooltips:tradeInVehicleStatus/%s/header' % vState, b'#tooltips:tradeInVehicleStatus/%s/body' % vState)
            return vehicleVO

    def _getItemPriceActionData(self, vehicle):
        if vehicle.buyPrices.itemPrice.isActionPrice():
            return packItemActionTooltipData(vehicle)
        else:
            return
