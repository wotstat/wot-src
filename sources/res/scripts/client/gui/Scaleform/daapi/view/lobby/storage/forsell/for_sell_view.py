import nations
from account_helpers import getAccountDatabaseID
from gui.Scaleform.daapi.view.lobby.storage.category_view import StorageDataProvider
from gui.Scaleform.daapi.view.lobby.storage.storage_helpers import createStorageDefVO
from gui.Scaleform.daapi.view.lobby.storage.storage_helpers import getStorageItemDescr
from gui.Scaleform.daapi.view.lobby.storage.storage_helpers import getStorageItemIcon
from gui.Scaleform.daapi.view.lobby.storage.storage_helpers import getStorageItemName
from gui.Scaleform.daapi.view.lobby.storage.storage_helpers import getStorageShellsData
from gui.Scaleform.daapi.view.lobby.store.browser.shop_helpers import getShopURL
from gui.Scaleform.daapi.view.meta.StorageCategoryForSellViewMeta import StorageCategoryForSellViewMeta
from gui.Scaleform.genConsts.CONTEXT_MENU_HANDLER_TYPE import CONTEXT_MENU_HANDLER_TYPE
from gui.Scaleform.genConsts.STORE_CONSTANTS import STORE_CONSTANTS
from gui.Scaleform.locale.RES_SHOP import RES_SHOP
from gui.shared import events
from gui.shared.event_bus import EVENT_BUS_SCOPE
from gui.shared.event_dispatcher import showShop
from gui.shared.formatters import getItemPricesVO
from gui.shared.gui_items import GUI_ITEM_TYPE
from gui.shared.gui_items.items_actions import factory as ItemsActionsFactory
from gui.shared.gui_items.items_actions.actions import ItemSellSpec
from gui.shared.money import Money
from gui.shared.utils.requesters.ItemsRequester import REQ_CRITERIA
from helpers.local_cache import FileLocalCache
from items import parseIntCompactDescr
from gui.shared.event_dispatcher import showSellDialog
VERSION = 1
_FOR_SELL_SORT_ORDER = (GUI_ITEM_TYPE.TURRET, GUI_ITEM_TYPE.ENGINE, GUI_ITEM_TYPE.GUN,
 GUI_ITEM_TYPE.RADIO, GUI_ITEM_TYPE.CHASSIS, GUI_ITEM_TYPE.SHELL)

def _sortKey(item):
    itemPrice = item.getSellPrice().price
    if item.itemTypeID in _FOR_SELL_SORT_ORDER:
        itemTypeIndex = _FOR_SELL_SORT_ORDER.index(item.itemTypeID)
    else:
        itemTypeIndex = len(_FOR_SELL_SORT_ORDER)
    return (itemTypeIndex,
     -itemPrice.gold if itemPrice.gold is not None else 0,
     -itemPrice.credits if itemPrice.credits is not None else 0,
     getStorageItemName(item))


class _StorageForSellCache(FileLocalCache):

    def __init__(self, databaseID):
        super(_StorageForSellCache, self).__init__(b'storage_cache', (b'forbidden_for_sale', databaseID))
        self.__cache = set()
        return

    def __repr__(self):
        return (b'_StorageForSellCache({0:s}): {1!r:s}').format(hex(id(self)), self.__cache)

    def get(self):
        return self.__cache

    def set(self, itemsIDs):
        self.__cache = itemsIDs
        return

    def clear(self):
        self.__cache = None
        super(_StorageForSellCache, self).clear()
        return

    def _getCache(self):
        return (VERSION, self.__cache)

    def _setCache(self, data):
        if isinstance(data, (tuple, list)) and len(data) == 2:
            if VERSION == data[0]:
                self.__cache = data[1]
        return data


class _SelectableDataProvider(StorageDataProvider):

    def __init__(self):
        super(_SelectableDataProvider, self).__init__()
        self.__isAllSelected = False
        self.__unselectedIDs = set()
        self.__totalPrice = Money()
        self.__guiItems = []
        self._cache = self._createCache()
        if self._cache:
            self.__unselectedIDs = self._cache.get()
        return

    def writeCache(self):
        if self._cache:
            self._cache.set(self.__unselectedIDs)
            self._cache.write()
        return

    def isAllSelected(self):
        return self.__isAllSelected

    def getTotalPrice(self):
        return self.__totalPrice

    def getSelectedItemsCount(self):
        return len(self.collection) - len(self.__unselectedIDs)

    @property
    def collection(self):
        return self.__guiItems

    def fini(self):
        self.writeCache()
        if self._cache:
            self._cache.clear()
        self._cache = None
        self.__guiItems = None
        super(_SelectableDataProvider, self).fini()
        return

    def buildList(self, itemsVoList):
        newList = sorted(itemsVoList, key=_sortKey)
        self.__guiItems = []
        self.__totalPrice = Money()
        self.__isAllSelected = True
        approvedIDs = set()
        for item in newList:
            vo = self.__createVO(item)
            isSelected = item.intCD not in self.__unselectedIDs
            if not isSelected:
                approvedIDs.add(item.intCD)
                self.__isAllSelected = False
            else:
                self.__totalPrice += self.__getOriginalItemPrice(item)
            vo[b'selected'] = isSelected
            self.__guiItems.append(vo)

        self.__unselectedIDs = approvedIDs
        self._list = newList
        self.refresh()
        return

    def toggleItem(self, itemID):
        originalList = self._list
        voList = self.__guiItems
        self.__isAllSelected = True
        for i, item in enumerate(originalList):
            cItemID = item.intCD
            guiItem = voList[i]
            if cItemID == itemID:
                newSelected = not guiItem[b'selected']
                guiItem[b'selected'] = newSelected
                self.__updateSelectedSet(guiItem)
                self._refreshSingleItem(i, guiItem)
                if not newSelected:
                    self.__isAllSelected = False
                    self.__totalPrice -= self.__getOriginalItemPrice(item)
                else:
                    self.__totalPrice += self.__getOriginalItemPrice(item)
                    self.__isAllSelected = not self.__unselectedIDs
                break

        return

    def selectAll(self, isSelected):
        changedIndexes = []
        changedItems = []
        voList = self.__guiItems
        originalList = self._list
        self.__totalPrice = Money(0)
        for i, item in enumerate(originalList):
            guiItem = voList[i]
            if guiItem[b'selected'] != isSelected:
                guiItem[b'selected'] = isSelected
                self.__updateSelectedSet(guiItem)
                changedIndexes.append(i)
                changedItems.append(guiItem)
            if isSelected:
                self.__totalPrice += self.__getOriginalItemPrice(item)

        changedCount = len(changedIndexes)
        if changedCount:
            if changedCount == 1:
                self._refreshSingleItem(changedIndexes[0], changedItems[0])
            else:
                self._refreshItemsByIndexes(changedIndexes, changedItems)
        self.__isAllSelected = isSelected
        return

    def _refreshItemsByIndexes(self, indexes, voItems):
        self.flashObject.invalidateItems(indexes, voItems)
        return

    def _refreshSingleItem(self, index, itemVO):
        self.flashObject.invalidateItem(index, itemVO)
        return

    def _createCache(self):
        databaseID = getAccountDatabaseID()
        if databaseID:
            self._cache = _StorageForSellCache(databaseID)
            self._cache.read()
            return self._cache
        else:
            return

    def __updateSelectedSet(self, itemVO):
        itemID = itemVO[b'id']
        if itemVO[b'selected']:
            self.__unselectedIDs.remove(itemID)
        else:
            self.__unselectedIDs.add(itemID)
        return

    def __createVO(self, item):
        priceVO = getItemPricesVO(item.getSellPrice())[0]
        nationFlagIcon = RES_SHOP.getNationFlagIcon(nations.NAMES[item.nationID]) if item.nationID != nations.NONE_INDEX else b''
        return createStorageDefVO(item.intCD, getStorageItemName(item), getStorageItemDescr(item), item.inventoryCount, priceVO, getStorageItemIcon(item, STORE_CONSTANTS.ICON_SIZE_SMALL), b'altimage', itemType=item.getOverlayType(), nationFlagIcon=nationFlagIcon, contextMenuId=CONTEXT_MENU_HANDLER_TYPE.STORAGE_FOR_SELL_ITEM)

    def __getOriginalItemPrice(self, item):
        return item.getSellPrice().price * item.inventoryCount


class StorageCategoryForSellView(StorageCategoryForSellViewMeta):

    def sellItem(self, itemId):
        showSellDialog(int(itemId))
        return

    def sellAll(self):
        itemSellSpecs = []
        for item in self._dataProvider.collection:
            if item[b'selected']:
                intCD = item[b'id']
                count = item[b'count']
                typeIdx, _, _ = parseIntCompactDescr(intCD)
                itemSellSpecs.append(ItemSellSpec(typeIdx, intCD, count))

        ItemsActionsFactory.doAction(ItemsActionsFactory.SELL_MULTIPLE, itemSellSpecs)
        return

    def selectAll(self, isSelected):
        self._dataProvider.selectAll(isSelected)
        self.__updateUI()
        return

    def selectItem(self, itemId, _):
        self._dataProvider.toggleItem(itemId)
        self.__updateUI()
        return

    def navigateToStore(self):
        showShop(getShopURL())
        return

    def _populate(self):
        super(StorageCategoryForSellView, self)._populate()
        self.addListener(events.StorageEvent.SELECT_MODULE_FOR_SELL, self.__onSellModule, scope=EVENT_BUS_SCOPE.LOBBY)
        self._itemsCache.onSyncCompleted += self.__onCacheResync
        return

    def _dispose(self):
        self.removeListener(events.StorageEvent.SELECT_MODULE_FOR_SELL, self.__onSellModule, scope=EVENT_BUS_SCOPE.LOBBY)
        super(StorageCategoryForSellView, self)._dispose()
        self._itemsCache.onSyncCompleted -= self.__onCacheResync
        return

    def _createDataProvider(self):
        return _SelectableDataProvider()

    def _buildItems(self):
        super(StorageCategoryForSellView, self)._buildItems()
        self.as_showDummyScreenS(len(self._dataProvider.collection) == 0)
        self.__updateUI()
        return

    def _getVoList(self):
        modulesList = super(StorageCategoryForSellView, self)._getVoList()
        modulesList.extend(getStorageShellsData(self._invVehicles, False, self._getComparator()))
        return modulesList

    def _getVO(self, item):
        return item

    def _getComparator(self):

        def _comparator(a, b):
            result = cmp(b.getSellPrice().price, a.getSellPrice().price)
            return result

        return _comparator

    def _getItemTypeID(self):
        return GUI_ITEM_TYPE.VEHICLE_MODULES

    def _getRequestCriteria(self, invVehicles):
        criteria = super(StorageCategoryForSellView, self)._getRequestCriteria(invVehicles)
        requestTypeIds = self._getItemTypeID()
        criteria |= ~REQ_CRITERIA.VEHICLE.SUITABLE(invVehicles, requestTypeIds)
        criteria |= REQ_CRITERIA.INVENTORY
        return criteria

    def __updateUI(self):
        provider = self._dataProvider
        price = provider.getTotalPrice().credits
        self.as_initS({b'allItemsSelected': (provider.isAllSelected()), 
           b'sellButtonEnabled': (provider.getSelectedItemsCount() > 0), 
           b'price': [
                    b'credits', price]})
        return

    def __onCacheResync(self, *args):
        self._buildItems()
        return

    def __onSellModule(self, event):
        self._dataProvider.toggleItem(event.ctx[b'intCD'])
        self.__updateUI()
        return
