from collections import namedtuple
from customization_resource_common import getCustomizationResourceExchangePrice
from gui.customization.shared import getGroupHelper
from gui.impl.lobby.customization.shared import CustomizationTabs, getTabByItem
from gui.shared.gui_items import GUI_ITEM_TYPE
from gui.shared.utils.requesters import REQ_CRITERIA
from helpers import dependency
from skeletons.gui.shared import IItemsCache
from items.customizations import CustomizationItemSelector
EXCHANGE_TABS = (
 CustomizationTabs.PAINTS,
 CustomizationTabs.INSCRIPTIONS,
 CustomizationTabs.EMBLEMS,
 CustomizationTabs.CAMOUFLAGES,
 CustomizationTabs.PROJECTION_DECALS,
 CustomizationTabs.MODIFICATIONS,
 CustomizationTabs.STYLED_2D,
 CustomizationTabs.STYLED_3D)
EXCHANGE_PRICE_KEYS = {(CustomizationTabs.PAINTS): b'paints', 
   (CustomizationTabs.INSCRIPTIONS): b'inscriptions', 
   (CustomizationTabs.EMBLEMS): b'emblems', 
   (CustomizationTabs.CAMOUFLAGES): b'camouflages', 
   (CustomizationTabs.PROJECTION_DECALS): b'projectionDecals', 
   (CustomizationTabs.MODIFICATIONS): b'modifications', 
   (CustomizationTabs.STYLED_2D): b'styles2D', 
   (CustomizationTabs.STYLED_3D): b'styles3D'}
_LOCATION_INVENTORY = 0
_LOCATION_INVENTORY_AND_VEHICLE = 1
_LOCATION_VEHICLE = 2
ExchangeItem = namedtuple(b'ExchangeItem', (b'tabId', b'intCD', b'vehicleCD', b'name', b'icon', b'vehicleName', b'inventoryCount', b'installedCount', b'availableCount', b'isWide', b'exchangePrice', b'locationPriority', b'orderingNumber', b'itemId', b'groupName', b'displayType', b'isFavorite', b'isProgressive', b'formfactor', b'isEditable'))

def getExchangeItemKey(item):
    return (
     item.intCD, item.vehicleCD)


class CustomizationResourceExchangeDataProvider(object):
    __itemsCache = dependency.descriptor(IItemsCache)
    __slots__ = (b'__blacklist', b'__priceGroups', b'__itemsByTab', b'__itemsByKey', b'__selectors')

    def __init__(self, blacklist, priceGroups=None, items=None):
        self.__blacklist = blacklist
        self.__priceGroups = priceGroups or ()
        self.__itemsByTab = {}
        self.__itemsByKey = {}
        self.__selectors = None
        self.rebuild(items)
        return

    def rebuild(self, items=None):
        self.__itemsByTab = {tabId: [] for tabId in EXCHANGE_TABS}
        self.__itemsByKey = {}
        self.__selectors = []
        for blacklist in self.__blacklist:
            self.__selectors.append(CustomizationItemSelector.fromString(blacklist))

        if items is None:
            items = self.__itemsCache.items.getItems(itemTypeID=GUI_ITEM_TYPE.CUSTOMIZATIONS, criteria=REQ_CRITERIA.CUSTOMIZATION.ON_ACCOUNT).itervalues()
        for customization in items:
            exchangeItem = self.__makeExchangeItem(customization)
            if exchangeItem is None:
                continue
            self.__itemsByTab[exchangeItem.tabId].append(exchangeItem)
            self.__itemsByKey[getExchangeItemKey(exchangeItem)] = exchangeItem

        for tabItems in self.__itemsByTab.itervalues():
            tabItems.sort(key=(lambda item: (
             item.locationPriority,
             item.orderingNumber,
             item.itemId)))

        return

    def getTabs(self):
        return tuple(tabId for tabId in EXCHANGE_TABS if self.__itemsByTab.get(tabId))

    def updateConfig(self, priceGroups, blacklist):
        self.__priceGroups = priceGroups or ()
        self.__blacklist = blacklist
        self.rebuild()
        return

    def isAnyItemsToExchange(self):
        return any(self.__itemsByKey)

    def getItems(self, tabId):
        return tuple(self.__itemsByTab.get(tabId, ()))

    def getItem(self, key):
        return self.__itemsByKey.get(key)

    def getCategoryMap(self, items):
        result = {}
        for itemCD, vehicleCD, _ in items:
            key = (itemCD, vehicleCD)
            item = self.getItem(key)
            if item is not None:
                result[itemCD] = item.tabId

        return result

    def getFirstNonEmptyTab(self):
        tabs = self.getTabs()
        if tabs:
            return tabs[0]
        return CustomizationTabs.DEFAULT

    def getAvailableCount(self, tabId):
        return sum(item.availableCount for item in self.getItems(tabId))

    def getTotalCount(self, tabId):
        return sum(item.inventoryCount + item.installedCount for item in self.getItems(tabId))

    def hasAvailableItems(self):
        return self.getFirstNonEmptyTab() != CustomizationTabs.DEFAULT

    def __makeExchangeItem(self, item):
        try:
            tabId = getTabByItem(item)
        except KeyError:
            return

        if tabId not in EXCHANGE_TABS:
            return
        else:
            if any(selector.matches(item.descriptor) for selector in self.__selectors):
                return
            exchangePrice = getCustomizationResourceExchangePrice(self.__priceGroups, item.descriptor.priceGroupTags)
            if exchangePrice <= 0:
                return
            inventoryCount = item.fullInventoryCount()
            installedCount = item.installedCount()
            availableCount = inventoryCount
            if item.isProgressive:
                availableCount = max(0, availableCount - item.descriptor.progression.autoGrantCount)
            if inventoryCount > 0:
                locationPriority = _LOCATION_INVENTORY_AND_VEHICLE if installedCount > 0 else _LOCATION_INVENTORY
            else:
                locationPriority = _LOCATION_VEHICLE
            groupHelper = getGroupHelper(item)
            return ExchangeItem(tabId=tabId, intCD=item.intCD, vehicleCD=0, name=item.userName, icon=item.iconUrl if item.itemTypeID == GUI_ITEM_TYPE.CAMOUFLAGE else item.icon, vehicleName=b'', inventoryCount=inventoryCount, installedCount=installedCount, availableCount=availableCount, isWide=item.isWide(), exchangePrice=exchangePrice, locationPriority=locationPriority, orderingNumber=item.orderingNumber, itemId=item.id, groupName=groupHelper.getGroupName(), displayType=item.customizationDisplayType(), isFavorite=item.markedAsFavorite, isProgressive=item.isProgressive or item.isQuestsProgression, formfactor=getattr(item, b'formfactor', b''), isEditable=bool(getattr(item, b'isEditable', False)))
