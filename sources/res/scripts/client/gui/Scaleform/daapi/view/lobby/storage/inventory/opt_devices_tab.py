from __future__ import absolute_import
from collections import OrderedDict
from enum import IntEnum
from PlayerEvents import g_playerEvents
from gui.shared.event_dispatcher import showSellDialog
from gui.Scaleform.daapi.view.meta.StorageDevicesTabViewMeta import StorageDevicesTabViewMeta
from gui.Scaleform.daapi.view.lobby.storage.inventory.inventory_view import TABS_SORT_ORDER, IN_GROUP_SORT_KEYS
from gui.Scaleform.daapi.view.lobby.store.browser.shop_helpers import getBuyOptionalDevicesUrl
from gui.impl import backport
from gui.impl.gen import R
from gui.shared.money import Currency
from gui.shared.gui_items.items_actions import factory as ItemsActionsFactory
from gui.shared.event_dispatcher import showShop
from gui.shared.gui_items import GUI_ITEM_TYPE
from gui.shared.utils.requesters import REQ_CRITERIA

class _OptDeviceTypeFilter(IntEnum):
    ALL = 0
    SIMPLE = 1
    DELUXE = 2
    TROPHY = 4
    MODERNIZED = 8


_TYPE_FILTER_ITEMS = [
 {b'id': (int(_OptDeviceTypeFilter.ALL)), 
    b'label': (backport.text(R.strings.storage.devices.filters.all()))},
 {b'id': (int(_OptDeviceTypeFilter.SIMPLE)), 
    b'label': (backport.text(R.strings.storage.devices.filters.simple()))},
 {b'id': (int(_OptDeviceTypeFilter.TROPHY)), 
    b'label': (backport.text(R.strings.storage.devices.filters.trophy()))},
 {b'id': (int(_OptDeviceTypeFilter.DELUXE)), 
    b'label': (backport.text(R.strings.storage.devices.filters.deluxe()))},
 {b'id': (int(_OptDeviceTypeFilter.MODERNIZED)), 
    b'label': (backport.text(R.strings.storage.devices.filters.modernized()))}]
_BIT_TO_DEVICE_TYPE_MAP = OrderedDict((
 (
  _OptDeviceTypeFilter.SIMPLE, REQ_CRITERIA.OPTIONAL_DEVICE.SIMPLE),
 (
  _OptDeviceTypeFilter.TROPHY, REQ_CRITERIA.OPTIONAL_DEVICE.TROPHY),
 (
  _OptDeviceTypeFilter.DELUXE, REQ_CRITERIA.OPTIONAL_DEVICE.DELUXE),
 (
  _OptDeviceTypeFilter.MODERNIZED, REQ_CRITERIA.OPTIONAL_DEVICE.MODERNIZED)))

class OptDevicesTabView(StorageDevicesTabViewMeta):

    def _populate(self):
        super(OptDevicesTabView, self)._populate()
        self.__updateBalance()
        g_playerEvents.onClientUpdated += self.__onClientUpdate
        return

    def _dispose(self):
        g_playerEvents.onClientUpdated -= self.__onClientUpdate
        super(OptDevicesTabView, self)._dispose()
        return

    def _getTypeFilters(self, items):
        return {b'items': items, 
           b'minSelectedItems': 0, 
           b'filterTypeName': (backport.text(R.strings.storage.storage.tabs.devices.filter.type.label()))}

    def navigateToStore(self):
        showShop(getBuyOptionalDevicesUrl())
        return

    def upgradeItem(self, itemId):
        optDevice = self._itemsCache.items.getItemByCD(int(itemId))
        ItemsActionsFactory.doAction(ItemsActionsFactory.UPGRADE_OPT_DEVICE, optDevice, None, None, None)
        return

    def _initFilter(self):
        index = 0
        if self._filterMask in _BIT_TO_DEVICE_TYPE_MAP:
            index = list(_BIT_TO_DEVICE_TYPE_MAP).index(self._filterMask) + 1
        self.as_initModulesFilterS({b'enabled': True, b'selectedIndex': index, b'data': _TYPE_FILTER_ITEMS})
        return

    def _getClientSectionKey(self):
        return b'storage_opt_devices'

    def _getItemTypeID(self):
        return GUI_ITEM_TYPE.OPTIONALDEVICE

    def _getFilteredCriteria(self):
        criteria = _BIT_TO_DEVICE_TYPE_MAP.get(self._filterMask, REQ_CRITERIA.EMPTY)
        if self._selectedVehicle:
            if not self._selectedVehicle.optDevices.layout.getCapacity():
                criteria |= REQ_CRITERIA.NONE
            else:
                criteria |= REQ_CRITERIA.VEHICLE.SUITABLE([self._selectedVehicle], self._getItemTypeIDs())
        return criteria

    def _getRequestCriteria(self, invVehicles):
        return REQ_CRITERIA.INVENTORY

    def _getItemSortKey(self, item):
        return (
         TABS_SORT_ORDER[item.itemTypeID],
         IN_GROUP_SORT_KEYS[item.itemTypeID](item))

    def _buildItems(self):
        super(OptDevicesTabView, self)._buildItems()
        self.as_showDummyScreenS(not self._dataProvider.collection)
        return

    def sellItem(self, itemId):
        showSellDialog(int(itemId))
        return

    def __onClientUpdate(self, diff, _):
        if Currency.EQUIP_COIN in diff.get(b'stats', {}):
            self.__updateBalance()
        return

    def __updateBalance(self):
        money = self._itemsCache.items.stats.money
        balanceStr = backport.getIntegralFormat(money.get(Currency.EQUIP_COIN, 0))
        self.as_setBalanceValueS(balanceStr)
        return
