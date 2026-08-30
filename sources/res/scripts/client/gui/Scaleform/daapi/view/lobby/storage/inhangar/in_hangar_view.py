from __future__ import absolute_import
from collections import namedtuple
from gui.Scaleform.daapi.view.common.filter_popover import VehiclesFilterPopover
from gui.Scaleform.daapi.view.meta.StorageCategoryInHangarViewMeta import StorageCategoryInHangarViewMeta
from gui.Scaleform.genConsts.STORAGE_CONSTANTS import STORAGE_CONSTANTS
from gui.Scaleform.locale.STORAGE import STORAGE
from gui.shared.gui_items import GUI_ITEM_TYPE
from gui.shared.utils.requesters import REQ_CRITERIA
from helpers import dependency
from skeletons.gui.shared import IItemsCache
StorageCategoryInHangarDataVO = namedtuple(b'StorageCategoryInHangarDataVO', (b'displayString', b'isZeroCount', b'shouldShow', b'searchInputLabel', b'searchInputName', b'searchInputTooltip', b'searchInputMaxChars'))
_SEARCH_INPUT_MAX_CHARS = 50
_TABS_DATA = (
 {b'id': (STORAGE_CONSTANTS.VEHICLES_TAB_ALL), 
    b'label': (STORAGE.INHANGAR_TABS_ALL), 
    b'linkage': (STORAGE_CONSTANTS.IN_HANGAR_ALL_VEHICLES_TAB), 
    b'selected': False},
 {b'id': (STORAGE_CONSTANTS.VEHICLES_TAB_RESTORE), 
    b'label': (STORAGE.INHANGAR_TABS_RESTORE), 
    b'linkage': (STORAGE_CONSTANTS.IN_HANGAR_RESTORE_VEHICLES_TAB), 
    b'selected': False})
_RENT_TAB_DATA = {b'id': (STORAGE_CONSTANTS.VEHICLES_TAB_RENT), 
   b'label': (STORAGE.INHANGAR_TABS_RENT), 
   b'linkage': (STORAGE_CONSTANTS.IN_HANGAR_RENT_VEHICLES_TAB), 
   b'selected': False}

class StorageVehicleFilterPopover(VehiclesFilterPopover):

    def _getInitialVO(self, filters, xpRateMultiplier):
        vo = super(StorageVehicleFilterPopover, self)._getInitialVO(filters, xpRateMultiplier)
        vo[b'searchSectionVisible'] = False
        return vo


class StorageCategoryInHangarView(StorageCategoryInHangarViewMeta):
    _itemsCache = dependency.descriptor(IItemsCache)

    def setActiveState(self, isActive):
        self.setActive(isActive)
        return

    def setActiveTab(self, tabId):
        tabsData = self.getTabsData()
        if tabId:
            for i, tab in enumerate(tabsData):
                tabsData[i][b'selected'] = False
                if tab.get(b'id') == tabId:
                    tabsData[i][b'selected'] = True

        self.as_setTabsDataS(tabsData)
        return

    def _populate(self):
        super(StorageCategoryInHangarView, self)._populate()
        self.setActiveTab(STORAGE_CONSTANTS.VEHICLES_TAB_ALL)
        return

    def getTabsData(self):
        if self.__canShowRentTab():
            return _TABS_DATA + (_RENT_TAB_DATA,)
        return _TABS_DATA

    def __canShowRentTab(self):
        criteria = REQ_CRITERIA.VEHICLE.RENT
        criteria |= ~REQ_CRITERIA.VEHICLE.IS_STORAGE_HIDDEN
        criteria |= ~REQ_CRITERIA.VEHICLE.BATTLE_ROYALE
        criteria |= ~REQ_CRITERIA.VEHICLE.EVENT_BATTLE
        criteria |= ~REQ_CRITERIA.VEHICLE.WOT_PLUS_VEHICLE
        return bool(self._itemsCache.items.getItems(GUI_ITEM_TYPE.VEHICLE, criteria))
