from __future__ import absolute_import
import copy, typing
from builtins import filter
from future.utils import viewvalues
from helpers import dependency
from constants import SwitchState
from account_helpers import AccountSettings
from gui import GUI_NATIONS_ORDER_INDICES
from gui.Scaleform.daapi.view.lobby.storage import storage_helpers
from gui.Scaleform.daapi.view.lobby.storage.inventory.inventory_view import IN_GROUP_SORT_KEYS
from gui.Scaleform.daapi.view.lobby.storage.inventory.inventory_view import TABS_SORT_ORDER
from gui.Scaleform.daapi.view.meta.ItemsWithTypeFilterTabViewMeta import ItemsWithTypeFilterTabViewMeta
from gui.impl import backport
from gui.impl.gen import R
from gui.impl.gen_utils import DynAccessor
from gui.shared.event_dispatcher import showBattleBoosterSellDialog
from gui.shared.gui_items import GUI_ITEM_TYPE
from gui.shared.utils.functions import makeTooltip
from gui.shared.utils.requesters.ItemsRequester import REQ_CRITERIA
from items import UNDEFINED_ITEM_CD
from skeletons.gui.lobby_context import ILobbyContext
from gui.shared.event_dispatcher import showSellDialog
if typing.TYPE_CHECKING:
    from typing import Dict, Union, Callable

def processFilterEntry(item, field, calculator):
    entry = item.get(field, b'')
    if isinstance(entry, DynAccessor):
        item[field] = calculator(entry)
    return


class FiltrableInventoryCategoryByTypeTabView(ItemsWithTypeFilterTabViewMeta):
    filterItems = None

    def __init__(self):
        super(FiltrableInventoryCategoryByTypeTabView, self).__init__()
        self._filterMask = 0
        self._totalCount = -1
        self._currentCount = -1
        self.__loadFilters()
        return

    def setActiveState(self, isActive):
        self.setActive(isActive)
        return

    def sellItem(self, itemId):
        dataCompactId = int(itemId)
        typeID = self._itemsCache.items.getItemByCD(dataCompactId).itemTypeID if dataCompactId else UNDEFINED_ITEM_CD
        if typeID == GUI_ITEM_TYPE.BATTLE_BOOSTER:
            showBattleBoosterSellDialog(dataCompactId)
        else:
            showSellDialog(dataCompactId)
        return

    def onFiltersChange(self, filters):
        self._filterMask = filters
        self._buildItems()
        return

    def resetFilter(self):
        self._filterMask = 0
        self.as_resetFilterS(self._filterMask)
        self._buildItems()
        return

    def _parseLoadedFilters(self, filterDict):
        self._filterMask = filterDict[b'filterMask']
        return

    def _prepareDataForFilterSaving(self):
        return {b'filterMask': (self._filterMask)}

    def _getClientSectionKey(self):
        raise NotImplementedError
        return

    def _getFilteredCriteria(self):
        return REQ_CRITERIA.EMPTY

    def _initFilter(self):
        items = self._getInitFilterItems()
        for item in items:
            processFilterEntry(item, b'tooltip', (lambda da: makeTooltip(body=backport.text(da()))))
            processFilterEntry(item, b'icon', (lambda da: backport.image(da())))
            if self._filterMask & item[b'filterValue'] == item[b'filterValue']:
                item.update({b'selected': True})

        typeFilters = self._getTypeFilters(items)
        self.as_initTypeFilterS(typeFilters)
        return

    def _getTypeFilters(self, items):
        return {b'items': items, 
           b'minSelectedItems': 0}

    def _populate(self):
        super(FiltrableInventoryCategoryByTypeTabView, self)._populate()
        self._initFilter()
        self._itemsCache.onSyncCompleted += self.__onCacheResync
        self._buildItems()
        return

    def _dispose(self):
        self.__saveFilters()
        self._itemsCache.onSyncCompleted -= self.__onCacheResync
        super(FiltrableInventoryCategoryByTypeTabView, self)._dispose()
        return

    def _buildItems(self):
        super(FiltrableInventoryCategoryByTypeTabView, self)._buildItems()
        self.__updateUI()
        return

    def _getVO(self, item):
        return storage_helpers.getItemVo(item)

    def _getVoList(self):
        totalItems = self._getItemList()
        self._totalCount = len(totalItems.values())
        filterCriteria = self._getFilteredCriteria()
        dataProviderListVoItems = []
        for item in sorted(viewvalues(totalItems), key=self._getItemSortKey):
            if filterCriteria(item):
                dataProviderListVoItems.append(self._getVO(item))

        self._currentCount = len(dataProviderListVoItems)
        return dataProviderListVoItems

    def containItemType(self, itemType):
        values = filter(self._getFilteredCriteria(), self._getItemList().values())
        return next((item for item in values if item.itemTypeID == itemType), None) is not None

    def _getItemSortKey(self, item):
        return (
         TABS_SORT_ORDER[item.itemTypeID],
         GUI_NATIONS_ORDER_INDICES[item.nationID],
         IN_GROUP_SORT_KEYS[item.itemTypeID](item))

    def _getInitFilterItems(self):
        if self.filterItems is not None:
            return copy.deepcopy(self.filterItems)
        else:
            return []

    def _shouldShowCounter(self):
        return self._filterMask != 0

    def __loadFilters(self):
        if storage_helpers.isStorageSessionTimeout():
            return
        self._parseLoadedFilters(AccountSettings.getSessionSettings(self._getClientSectionKey()))
        return

    def __saveFilters(self):
        AccountSettings.setSessionSettings(self._getClientSectionKey(), self._prepareDataForFilterSaving())
        return

    def __updateUI(self):
        self.__updateFilterCounter()
        self.__updateScreen()
        return

    def __updateFilterCounter(self):
        if self._totalCount != -1 and self._currentCount != -1:
            shouldShow = self._shouldShowCounter()
            if shouldShow:
                countString = self._formatCountString(self._currentCount, self._totalCount)
            else:
                countString = self._formatTotalCountString(self._totalCount)
            self.as_updateCounterS(shouldShow, countString, self._currentCount == 0)
        return

    def __updateScreen(self):
        hasNoItems = self._totalCount == 0
        hasNoFilterResults = not hasNoItems and self._currentCount == 0
        filterWarningVO = None
        if hasNoFilterResults:
            filterWarningVO = self._makeFilterWarningVO(backport.text(R.strings.storage.filter.warningMessage()), backport.text(R.strings.storage.filter.noResultsBtn.label()), None)
        self.as_showDummyScreenS(hasNoItems)
        self.as_showFilterWarningS(filterWarningVO)
        return

    def __onCacheResync(self, *args):
        self._buildItems()
        return


class FiltrableRegularCategoryByTypeTabView(FiltrableInventoryCategoryByTypeTabView):
    _lobbyContext = dependency.descriptor(ILobbyContext)

    def _getItemList(self):
        criteria = self._getRequestCriteria(self._invVehicles)
        items = {}
        for itemType in self._getItemTypeIDs():
            if itemType == GUI_ITEM_TYPE.DEMOUNT_KIT:
                items.update(self._goodiesCache.getDemountKits(REQ_CRITERIA.DEMOUNT_KIT.IN_ACCOUNT | REQ_CRITERIA.DEMOUNT_KIT.IS_ENABLED))
            elif itemType == GUI_ITEM_TYPE.MENTORING_LICENSE:
                items.update(self._goodiesCache.getMentoringLicenses(REQ_CRITERIA.MENTORING_LICENSE.IN_ACCOUNT | REQ_CRITERIA.MENTORING_LICENSE.IS_ENABLED))
            elif itemType == GUI_ITEM_TYPE.RECERTIFICATION_FORM:
                if SwitchState.DISABLED.value == self._lobbyContext.getServerSettings().recertificationFormState():
                    continue
                items.update(self._goodiesCache.getRecertificationForms(REQ_CRITERIA.RECERTIFICATION_FORM.IN_ACCOUNT | REQ_CRITERIA.RECERTIFICATION_FORM.IS_ENABLED))
            else:
                items.update(self._itemsCache.items.getItems(itemType, criteria, nationID=None))

        return items
