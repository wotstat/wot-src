from __future__ import absolute_import
import typing
from collections import namedtuple
from functools import partial
from future.utils import viewvalues
import BigWorld
from CurrentVehicle import g_currentVehicle
from account_helpers.AccountSettings import AccountSettings, CUSTOMIZATION_SECTION, PROJECTION_DECAL_HINT_SHOWN_FIELD, CUSTOMIZATION_STYLE_ITEMS_VISITED, CUSTOMIZATION_TABS_VISITED
from account_helpers.settings_core.settings_constants import OnceOnlyHints
from gui import GUI_SETTINGS
from gui.ClientUpdateManager import g_clientUpdateManager
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS
from gui.Scaleform.daapi.view.lobby.customization.customization_carousel import CustomizationCarouselDataProvider, comparisonKey, FilterTypes, FilterAliases
from gui.Scaleform.daapi.view.lobby.customization.customization_item_vo import buildCustomizationItemDataVO
from gui.Scaleform.daapi.view.lobby.customization.shared import isItemUsedUp, CustomizationTabs, getMultiSlot, BillPopoverButtons, vehicleHasSlot, checkSlotsFilling
from gui.Scaleform.daapi.view.meta.CustomizationBottomPanelMeta import CustomizationBottomPanelMeta
from gui.Scaleform.locale.ITEM_TYPES import ITEM_TYPES
from gui.Scaleform.locale.RES_ICONS import RES_ICONS
from gui.Scaleform.locale.TOOLTIPS import TOOLTIPS
from gui.Scaleform.locale.VEHICLE_CUSTOMIZATION import VEHICLE_CUSTOMIZATION
from gui.customization.constants import CustomizationModes, CustomizationModeSource
from gui.customization.shared import getTotalPurchaseInfo, C11nId
from gui.impl import backport
from gui.impl.gen import R
from gui.shared.event_dispatcher import showBrowserOverlayView, showVehiclesSidebarDialogWindow
from gui.shared.formatters import text_styles, icons, getItemPricesVO, getMoneyVO
from gui.shared.gui_items import GUI_ITEM_TYPE
from gui.shared.gui_items.gui_item_economics import ITEM_PRICE_EMPTY
from gui.shared.money import Money
from gui.shared.utils.functions import makeTooltip
from gui.shared.utils.requesters.ItemsRequester import REQ_CRITERIA
from helpers import dependency
from helpers.i18n import makeString as _ms
from items.customizations import ProjectionDecalComponent
from skeletons.account_helpers.settings_core import ISettingsCore
from skeletons.gui.customization import ICustomizationService
from skeletons.gui.server_events import IEventsCache
from skeletons.gui.shared import IItemsCache
from vehicle_outfit.outfit import Area
from uilogging.customization_3d_objects.logger import CustomizationBottomPanelLogger
from uilogging.customization_3d_objects.logging_constants import CustomizationButtons, CustomizationViewKeys
if typing.TYPE_CHECKING:
    from typing import List, Callable
    from gui.shared.gui_items.customization.c11n_items import Customization
    from gui.shared.gui_items.gui_item import GUIItem
CustomizationCarouselDataVO = namedtuple(b'CustomizationCarouselDataVO', (b'displayString', b'isZeroCount', b'shouldShow', b'itemLayoutSize', b'bookmarks', b'arrows', b'showSeparators'))

class CustomizationBottomPanel(CustomizationBottomPanelMeta):
    itemsCache = dependency.descriptor(IItemsCache)
    eventsCache = dependency.descriptor(IEventsCache)
    service = dependency.descriptor(ICustomizationService)
    settingsCore = dependency.descriptor(ISettingsCore)

    def __init__(self):
        super(CustomizationBottomPanel, self).__init__()
        self.__ctx = None
        self._carouselDP = None
        self._selectedItem = None
        self.__cachedTabData = None
        self.__uiLogger = CustomizationBottomPanelLogger(CustomizationViewKeys.CUSTOMIZATION_BOTTOM_PANEL)
        return

    def _populate(self):
        super(CustomizationBottomPanel, self)._populate()
        self.__isInited = False
        self.__isEscHelpSeen = False
        self.__ctx = self.service.getCtx()
        self._carouselDP = CustomizationCarouselDataProvider(self._carouseItemWrapper)
        self._carouselDP.setFlashObject(self.getDp())
        self._carouselDP.setEnvironment(self.app)
        self.__ctx.events.onCarouselFiltered += self.__onCarouselFiltered
        self.__ctx.events.onCacheResync += self.__onCacheResync
        self.__ctx.events.onSeasonChanged += self.__onSeasonChanged
        self.__ctx.events.onItemInstalled += self.__onItemsInstalled
        self.__ctx.events.onTabChanged += self.__onTabChanged
        self.__ctx.events.onItemsRemoved += self.__onItemsRemoved
        self.__ctx.events.onModeChanged += self.__onModeChanged
        self.__ctx.events.onChangesCanceled += self.__onChangesCanceled
        self.__ctx.events.onComponentChanged += self.__onComponentChanged
        self.__ctx.events.onInstallNextCarouselItem += self.__onInstallNextCarouselItem
        self.__ctx.events.onItemSelected += self.__onItemSelected
        self.__ctx.events.onItemUnselected += self.__onItemUnselected
        self.__ctx.events.onSlotSelected += self.__onSlotSelected
        self.__ctx.events.onSlotUnselected += self.__onSlotUnselected
        self.__ctx.events.onFilterPopoverClosed += self.__onFilterPopoverClosed
        self.__ctx.events.onGetItemBackToHand += self.__onGetItemBackToHand
        g_currentVehicle.onChanged += self.__onVehicleChanged
        g_clientUpdateManager.addMoneyCallback(self.__setBottomPanelBillData)
        self.__setFooterInitData()
        self.__updatePopoverBtn()
        self.__updateHelpMessage()
        self.__c11nSettings = AccountSettings.getSettings(CUSTOMIZATION_SECTION)
        self.__serverSettings = self.settingsCore.serverSettings
        self.__stageSwitcherVisibility = False
        BigWorld.callback(0.0, (lambda : self.__onTabChanged(self.__ctx.mode.tabId)))
        BigWorld.callback(0.0, self.__setBottomPanelBillData)
        return

    def _dispose(self):
        g_clientUpdateManager.removeObjectCallbacks(self)
        self.__ctx.events.onComponentChanged -= self.__onComponentChanged
        self.__ctx.events.onChangesCanceled -= self.__onChangesCanceled
        self.__ctx.events.onModeChanged -= self.__onModeChanged
        self.__ctx.events.onItemsRemoved -= self.__onItemsRemoved
        self.__ctx.events.onTabChanged -= self.__onTabChanged
        self.__ctx.events.onItemInstalled -= self.__onItemsInstalled
        self.__ctx.events.onSeasonChanged -= self.__onSeasonChanged
        self.__ctx.events.onCacheResync -= self.__onCacheResync
        self.__ctx.events.onCarouselFiltered -= self.__onCarouselFiltered
        self.__ctx.events.onInstallNextCarouselItem -= self.__onInstallNextCarouselItem
        self.__ctx.events.onItemSelected -= self.__onItemSelected
        self.__ctx.events.onItemUnselected -= self.__onItemUnselected
        self.__ctx.events.onSlotSelected -= self.__onSlotSelected
        self.__ctx.events.onSlotUnselected -= self.__onSlotUnselected
        self.__ctx.events.onFilterPopoverClosed -= self.__onFilterPopoverClosed
        self.__ctx.events.onGetItemBackToHand -= self.__onGetItemBackToHand
        g_currentVehicle.onChanged -= self.__onVehicleChanged
        self._carouselDP._dispose()
        self._carouselDP = None
        self.__ctx = None
        self._selectedItem = None
        self.__c11nSettings = None
        self.__serverSettings = None
        self.__isInited = False
        self.__isEscHelpSeen = False
        self.__uiLogger = None
        self.__cachedTabData = None
        super(CustomizationBottomPanel, self)._dispose()
        return

    def getDp(self):
        return self.as_getDataProviderS()

    def returnToStyledMode(self):
        self.__ctx.returnToStyleMode()
        self.__updatePopoverBtn()
        return

    def switchMode(self, index):
        self.__changeMode(CustomizationModes.ALL[index])
        return

    def onSelectHotFilter(self, index, value):
        self.__uiLogger.onPrimaryFilterClick(index)
        filterType = (FilterTypes.INVENTORY, FilterTypes.APPLIED)[index]
        self._carouselDP.updateCarouselFilter(filterType, value)
        self.__rebuildCarousel()
        self.__updateHints()
        return

    def showGroupFromTab(self, groupId):
        tabIndex = groupId
        if tabIndex not in CustomizationTabs.MODES[self.__ctx.modeId]:
            self.__changeMode(CustomizationTabs.TAB_TO_MODE[tabIndex][0], tabIndex)
        else:
            self.__ctx.mode.changeTab(tabIndex)
        visitedSet = AccountSettings.getSettings(CUSTOMIZATION_TABS_VISITED)
        visitedSet.add(tabIndex)
        AccountSettings.setSettings(CUSTOMIZATION_TABS_VISITED, visitedSet)
        self.__setNotificationCounters()
        return

    def showVehiclesSideBar(self):
        isTutorial = self.__serverSettings.updateIsHintTutorial(OnceOnlyHints.C11N_VEHICLE_LIST_HINT)
        self.__uiLogger.onHintButtonClick(CustomizationButtons.VEHICLES_LIST, isTutorial)
        showVehiclesSidebarDialogWindow(self.__ctx.mode.tabId)
        return

    def onSelectItem(self, index, intCD, progressionLevel):
        if intCD != -1:
            self.__ctx.selectItem(intCD, progressionLevel)
            if self.__ctx.mode.tabId == CustomizationTabs.PROJECTION_DECALS:
                self.__onProjectionDecalOnlyOnceHintHidden(record=True)
        else:
            self.__ctx.unselectItem()
        return

    def onEditItem(self, intCD):
        self.__ctx.editStyle(intCD, source=CustomizationModeSource.CAROUSEL)
        self.__updatePopoverBtn()
        return

    def onItemIsNewAnimationShown(self, intCD):
        visitedSet = AccountSettings.getSettings(CUSTOMIZATION_STYLE_ITEMS_VISITED)
        visitedSet.add(intCD)
        AccountSettings.setSettings(CUSTOMIZATION_STYLE_ITEMS_VISITED, visitedSet)
        return

    def blinkCounter(self):
        self.as_playFilterBlinkS()
        return

    def resetFilter(self):
        self.__clearFilter()
        self.refreshFilterData()
        self.__rebuildCarousel()
        return

    def refreshFilterData(self):
        filterData = self._carouselDP.getFilterData()
        self.as_setFilterDataS(filterData)
        return

    @property
    def carouselItems(self):
        return self._carouselDP.collection

    def getVisibleTabs(self):
        return self._carouselDP.getVisibleTabs()

    def getEnabledTabs(self):
        return self._carouselDP.getEnabledTabs()

    def isItemUnsuitable(self, item):
        return self._carouselDP.processDependentParams(item)[1]

    def showVideo(self):
        self.__uiLogger.onButtonClick(CustomizationButtons.TO_THE_VIDEO)
        showBrowserOverlayView(GUI_SETTINGS.attachmentsEmptyVideo, VIEW_ALIAS.BROWSER_OVERLAY, forcedSkipEscape=True, callbackOnLoad=partial(self.__uiLogger.onViewOpen, CustomizationViewKeys.ATTACHMENTS_VIDEO), callbackOnClose=partial(self.__uiLogger.onViewClose, CustomizationViewKeys.ATTACHMENTS_VIDEO))
        return

    def __changeMode(self, modeId, tabId=None):
        self.__ctx.changeMode(modeId, tabId, CustomizationModeSource.BOTTOM_PANEL)
        self.__updatePopoverBtn()
        return

    def __updateStyleLabel(self):
        label = b''
        tooltip = None
        if self.__ctx.modeId in CustomizationModes.BASE_STYLES:
            label = text_styles.main(backport.text(R.strings.vehicle_customization.defaultStyle.label()))
        self.as_setCarouselInfoLabelDataS(label, tooltip)
        return

    def __onInstallNextCarouselItem(self, reverse):
        if self.__ctx.mode.selectedSlot is None:
            return
        else:
            item = self._carouselDP.getNextItem(reverse)
            if item is None:
                return
            self.__ctx.selectItem(item.intCD)
            return

    def __onSlotSelected(self, *_, **__):
        if self.__ctx.mode.tabId in (CustomizationTabs.PROJECTION_DECALS, CustomizationTabs.ATTACHMENTS):
            self.__rebuildCarousel(scroll=True)
        else:
            self._carouselDP.refresh()
            self.__updateSelection()
        self.__updatePopoverBtn()
        self.__updatefilterFallbackData()
        return

    def __onSlotUnselected(self, _):
        if self.__ctx.mode.tabId in (CustomizationTabs.PROJECTION_DECALS, CustomizationTabs.ATTACHMENTS):
            prevSelected = self._selectedItem
            self.__rebuildCarousel()
            if prevSelected is not None:
                self.__scrollToItem(prevSelected.intCD, True)
        else:
            self._carouselDP.refresh()
            self.__updateSelection()
        self.__updatefilterFallbackData()
        self.__updatePopoverBtn()
        return

    def __setNotificationCounters(self):
        vehicle = g_currentVehicle.item
        proxy = g_currentVehicle.itemsCache.items
        tabsCounters = []
        visibleTabs = self.getVisibleTabs()
        seenTabs = AccountSettings.getSettings(CUSTOMIZATION_TABS_VISITED)
        season = self.__ctx.season
        for tabId in visibleTabs:
            itemFilter = self.__getItemFilter(tabId)
            tabItemTypes = CustomizationTabs.ITEM_TYPES[tabId]
            tabsCounters.append(vehicle.getC11nItemsNoveltyCounter(proxy, itemTypes=tabItemTypes, season=season, itemFilter=itemFilter))

        unseenTabs = list(set(visibleTabs) - seenTabs)
        self.as_setNotificationCountersS({b'tabsCounters': tabsCounters, 
           b'unseenTabs': unseenTabs})
        return

    def __getItemFilter(self, tabId):
        if tabId == CustomizationTabs.STAT_TRACKERS:
            return None
        else:
            if self.__ctx.modeId == CustomizationModes.STYLE_2D_EDITABLE:
                return self.__ctx.mode.style.isItemInstallable
            if tabId == CustomizationTabs.STYLES_2D:
                return (lambda item: not item.is3D)
            if tabId == CustomizationTabs.STYLES_3D:
                return (lambda item: item.is3D)
            return (lambda item: not item.isStyleOnly)

    def __resetTabs(self):
        self.as_setBottomPanelTabsDataS({b'tabsDP': [], b'selectedTab': (-1)})
        return

    def __updateTabs(self):
        tabData = {b'tabsDP': (self.__getItemTabsData()), 
           b'selectedTab': (self.__ctx.mode.tabId)}
        if self.__cachedTabData != tabData:
            self.as_setBottomPanelTabsDataS(tabData)
            self.__cachedTabData = tabData
        return

    def __setFooterInitData(self):
        self.as_setBottomPanelInitDataS({b'filtersVO': {b'popoverAlias': (VIEW_ALIAS.CUSTOMIZATION_FILTER_POPOVER), 
                          b'mainBtn': {b'value': (RES_ICONS.MAPS_ICONS_BUTTONS_FILTER), 
                                       b'tooltip': (VEHICLE_CUSTOMIZATION.CAROUSEL_FILTER_MAINBTN)}, 
                          b'hotFilters': [
                                        {b'value': (RES_ICONS.MAPS_ICONS_CUSTOMIZATION_STORAGE_ICON), 
                                           b'tooltip': (VEHICLE_CUSTOMIZATION.CAROUSEL_FILTER_STORAGEBTN), 
                                           b'selected': (self._carouselDP.isFilterApplied(FilterTypes.INVENTORY))},
                                        {b'value': (RES_ICONS.MAPS_ICONS_BUTTONS_EQUIPPED_ICON), 
                                           b'tooltip': (VEHICLE_CUSTOMIZATION.CAROUSEL_FILTER_EQUIPPEDBTN), 
                                           b'selected': (self._carouselDP.isFilterApplied(FilterTypes.APPLIED))}]}})
        self.__setNotificationCounters()
        self.__updatefilterFallbackData()
        return

    def __updatefilterFallbackData(self):
        self.as_setFilterFallbackDataS(self.__getFallbackMessage())
        return

    def __getFilterMessage(self):
        return {b'message': ((b'{}{}\n{}').format(icons.makeImageTag(RES_ICONS.MAPS_ICONS_LIBRARY_ATTENTIONICONFILLED, vSpace=-3), text_styles.neutral(backport.text(R.strings.vehicle_customization.carousel.message.default.header())), text_styles.main(backport.text(R.strings.vehicle_customization.carousel.message.default.description()))))}

    def __getUnsupportAttachementMessage(self):
        return {b'message': ((b'{}{}').format(icons.makeImageTag(RES_ICONS.MAPS_ICONS_LIBRARY_ATTENTIONICONFILLED, vSpace=-3), text_styles.highlightText(backport.text(R.strings.vehicle_customization.carousel.message.attachment.unsapport.header(), name=g_currentVehicle.item.shortUserName)))), 
           b'hasVideo': True, 
           b'popoverBtnVisible': True}

    def __getNoAttachementMessage(self):
        return {b'message': ((b'{}\n{}').format(text_styles.middleTitle(backport.text(R.strings.vehicle_customization.carousel.message.attachment.default.header())), text_styles.main(backport.text(R.strings.vehicle_customization.carousel.message.attachment.default.description())))), 
           b'hasVideo': True}

    def __getNoDecalMessage(self):
        return {b'message': ((b'{}{}\n{}').format(icons.makeImageTag(RES_ICONS.MAPS_ICONS_LIBRARY_ATTENTIONICONFILLED, vSpace=-3), text_styles.neutral(backport.text(R.strings.vehicle_customization.carousel.message.default.header())), text_styles.main(backport.text(R.strings.vehicle_customization.carousel.message.noProgressionDecals()))))}

    def __getDecalSlotMessage(self):
        return {b'message': ((b'{}{}\n{}').format(icons.makeImageTag(RES_ICONS.MAPS_ICONS_LIBRARY_ATTENTIONICONFILLED, vSpace=-3), text_styles.neutral(backport.text(R.strings.vehicle_customization.carousel.message.default.header())), text_styles.main(backport.text(R.strings.vehicle_customization.carousel.message.propertysheet()))))}

    def __getNoStatTrackersMessage(self):
        return {b'message': ((b'{}\n{}').format(text_styles.middleTitle(backport.text(R.strings.vehicle_customization.carousel.message.statTracker.default.header())), text_styles.main(backport.text(R.strings.vehicle_customization.carousel.message.statTracker.default.description()))))}

    def __getFallbackMessage(self):
        selectedSlot = self.__ctx.mode.selectedSlot
        isEmptyTab = not self._carouselDP.collection
        hasNoItemsForTab = not self._carouselDP.getItemsData()
        tabId = self.__ctx.mode.tabId
        if selectedSlot is not None:
            if selectedSlot.slotType == GUI_ITEM_TYPE.PROJECTION_DECAL:
                return self.__getDecalSlotMessage()
        if tabId == CustomizationTabs.ATTACHMENTS:
            attachments = g_currentVehicle.itemsCache.items.getItems(GUI_ITEM_TYPE.ATTACHMENT, REQ_CRITERIA.CUSTOMIZATION.ON_ACCOUNT | REQ_CRITERIA.CUSTOM((lambda item: not item.descriptor.isHiddenInUI())))
            if not attachments:
                return self.__getNoAttachementMessage()
            if not vehicleHasSlot(GUI_ITEM_TYPE.ATTACHMENT, g_currentVehicle.item):
                return self.__getUnsupportAttachementMessage()
            if hasNoItemsForTab:
                return self.__getNoAttachementMessage()
        if tabId == CustomizationTabs.PROJECTION_DECALS and isEmptyTab:
            return self.__getNoDecalMessage()
        else:
            if tabId == CustomizationTabs.STAT_TRACKERS and hasNoItemsForTab:
                return self.__getNoStatTrackersMessage()
            return self.__getFilterMessage()

    def __buildCustomizationCarouselDataVO(self):
        isZeroCount = self._carouselDP.itemCount == 0
        countStyle = text_styles.error if isZeroCount else text_styles.main
        displayString = text_styles.main((b'{} / {}').format(countStyle(str(self._carouselDP.itemCount)), str(self._carouselDP.totalItemCount)))
        shouldShow = self._carouselDP.hasAppliedFilter()
        return CustomizationCarouselDataVO(displayString, isZeroCount, shouldShow, itemLayoutSize=self._carouselDP.getItemSizeData(), bookmarks=self._carouselDP.getBookmarskData(), arrows=self._carouselDP.getArrowsData(), showSeparators=self._carouselDP.getShowSeparatorsData())._asdict()

    def __setBottomPanelBillData(self, *_):
        purchaseItems = self.__ctx.getPurchaseItems()
        purchaseItems = self.__processBillDataPurchaseItems(purchaseItems)
        cartInfo = getTotalPurchaseInfo(purchaseItems)
        totalPriceVO = getItemPricesVO(cartInfo.totalPrice)
        label = _ms(VEHICLE_CUSTOMIZATION.COMMIT_APPLY)
        fromStorageCount = 0
        hasLockedItemsInStyle = False
        toBuyCount = 0
        lockedCount = 0
        for pItem in purchaseItems:
            if not pItem.item.isHiddenInUI():
                if not pItem.item.isUnlockedByToken():
                    lockedCount += 1
                elif pItem.isFromInventory:
                    fromStorageCount += 1
                else:
                    toBuyCount += 1
                curItem = pItem.item
                if curItem.isQuestsProgression and curItem.itemTypeID == GUI_ITEM_TYPE.STYLE:
                    totalItems = curItem.descriptor.questsProgression.getTotalCount()
                    itemsOpened = sum([curItem.descriptor.questsProgression.getUnlockedCount(token, self.eventsCache.questsProgress.getTokenCount(token)) for token in curItem.descriptor.questsProgression.getGroupTokens()])
                    hasLockedItemsInStyle = totalItems != itemsOpened

        for pItem in purchaseItems:
            if pItem.item.itemTypeID != GUI_ITEM_TYPE.PERSONAL_NUMBER:
                continue
            if not pItem.component.isFilled():
                hasEmptyNumber = True
                break
        else:
            hasEmptyNumber = False

        hasLockedItems = self.__ctx.mode.isOutfitsHasLockedItems()
        outfitsModified = buyBtnEnabled = self.__ctx.isOutfitsModified()
        if buyBtnEnabled and cartInfo.totalPrice != ITEM_PRICE_EMPTY:
            label = _ms(VEHICLE_CUSTOMIZATION.COMMIT_BUY)
        if hasEmptyNumber:
            tooltip = VEHICLE_CUSTOMIZATION.CUSTOMIZATION_EMPTYPERSONALNUMBER
        elif hasLockedItems:
            tooltip = VEHICLE_CUSTOMIZATION.CUSTOMIZATION_LOCKEDITEMSAPPLY
        elif self.__ctx.mode.isOutfitsEmpty():
            tooltip = VEHICLE_CUSTOMIZATION.CUSTOMIZATION_NOTSELECTEDITEMS
        else:
            tooltip = VEHICLE_CUSTOMIZATION.CUSTOMIZATION_ALREADYAPPLIED
        if outfitsModified:
            if fromStorageCount > 0 or toBuyCount > 0:
                self.__showBill()
            else:
                self.__hideBill()
        else:
            self.__hideBill()
        compoundPrice = totalPriceVO[0]
        if not compoundPrice[b'price']:
            compoundPrice[b'price'] = getMoneyVO(Money(gold=0))
        fromStorageCount = text_styles.stats((b'({})').format(fromStorageCount))
        toBuyCount = text_styles.stats((b'({})').format(toBuyCount))
        billLines = [
         self.__makeBillLine(text_styles.main((b'{} {}').format(_ms(VEHICLE_CUSTOMIZATION.BUYPOPOVER_PRICE), toBuyCount)), compoundPrice=compoundPrice, isEnoughStatuses=getMoneyVO(Money(True, True, True))),
         self.__makeBillLine(text_styles.main((b'{} {}').format(_ms(VEHICLE_CUSTOMIZATION.BUYPOPOVER_FROMSTORAGE), fromStorageCount)), icon=RES_ICONS.MAPS_ICONS_CUSTOMIZATION_STORAGE_ICON)]
        buttons = [
         self.__makeButton(_ms(VEHICLE_CUSTOMIZATION.BUYPOPOVER_BTNCLEARALL), BillPopoverButtons.CUSTOMIZATION_CLEAR, RES_ICONS.MAPS_ICONS_CUSTOMIZATION_ICON_CROSS)]
        if hasLockedItems or hasLockedItemsInStyle:
            lockedCountText = text_styles.stats((b'({})').format(lockedCount))
            billLines.append(self.__makeBillLine(text_styles.main((b'{} {}').format(_ms(VEHICLE_CUSTOMIZATION.BUYPOPOVER_LOCKED), lockedCountText)), icon=RES_ICONS.MAPS_ICONS_CUSTOMIZATION_LOCK_ICON))
            buttons.append(self.__makeButton(_ms(VEHICLE_CUSTOMIZATION.BUYPOPOVER_BTNCLEARLOCKED), BillPopoverButtons.CUSTOMIZATION_CLEAR_LOCKED, enabled=lockedCount > 0))
        self.as_setBottomPanelPriceStateS({b'buyBtnEnabled': (buyBtnEnabled and not hasLockedItems), 
           b'buyBtnLabel': label, 
           b'buyBtnTooltip': tooltip, 
           b'customizationDisplayType': (self.__ctx.mode.currentOutfit.customizationDisplayType()), 
           b'billVO': {b'title': (text_styles.highlightText(_ms(VEHICLE_CUSTOMIZATION.BUYPOPOVER_RESULT))), 
                       b'lines': billLines, 
                       b'buttons': buttons}})
        return

    def __makeBillLine(self, label, icon=None, compoundPrice=None, isEnoughStatuses=None):
        return {b'label': label, 
           b'icon': icon, 
           b'compoundPrice': compoundPrice, 
           b'isEnoughStatuses': isEnoughStatuses}

    def __makeButton(self, label, event, icon=None, enabled=True):
        return {b'label': label, 
           b'icon': icon, 
           b'event': event, 
           b'enabled': enabled}

    def __showBill(self):
        self.as_showBillS()
        return

    def __hideBill(self):
        self.as_hideBillS()
        return

    def __refreshHotFilters(self):
        self.as_setCarouselFiltersDataS({b'hotFilters': [
                         self._carouselDP.isFilterApplied(FilterTypes.INVENTORY),
                         self._carouselDP.isFilterApplied(FilterTypes.APPLIED)]})
        return

    def __clearFilter(self):
        self._carouselDP.clearFilter()
        self.__refreshHotFilters()
        return

    def __rebuildCarousel(self, scroll=False):
        self._carouselDP.invalidateFilteredItems()
        self._carouselDP.buildList()
        self._carouselDP.refresh()
        self.__updateSelection(scroll)
        self.as_setCarouselDataS(self.__buildCustomizationCarouselDataVO())
        return

    def _carouseItemWrapper(self, itemCD):
        item = self.service.getItemByCD(itemCD)
        inventoryCount = self.__ctx.mode.getItemInventoryCount(item)
        purchaseLimit = self.__ctx.mode.getPurchaseLimit(item)
        isApplied = itemCD in self._carouselDP.getAppliedItems()
        isBaseStyleItem = itemCD in self._carouselDP.getBaseStyleItems()
        if item.isStyleOnly or isBaseStyleItem:
            isDarked = isUsedUp = False
        else:
            isDarked = purchaseLimit <= 0 and inventoryCount <= 0
            isUsedUp = isItemUsedUp(item)
        showEditableHint = False
        showEditBtnHint = False
        if item.itemTypeID == GUI_ITEM_TYPE.STYLE:
            autoRentEnabled = self.__ctx.mode.isAutoRentEnabled()
            if item.isProgressionRequired:
                showEditableHint = not bool(self.__serverSettings.getOnceOnlyHintsSetting(OnceOnlyHints.C11N_PROGRESSION_REQUIRED_STYLE_SLOT_HINT))
                showEditBtnHint = not bool(self.__serverSettings.getOnceOnlyHintsSetting(OnceOnlyHints.C11N_PROGRESSION_REQUIRED_STYLE_SLOT_BUTTON_HINT))
            elif item.isEditable:
                showEditableHint = not bool(self.__serverSettings.getOnceOnlyHintsSetting(OnceOnlyHints.C11N_EDITABLE_STYLE_SLOT_HINT))
                showEditBtnHint = not bool(self.__serverSettings.getOnceOnlyHintsSetting(OnceOnlyHints.C11N_EDITABLE_STYLE_SLOT_BUTTON_HINT))
        else:
            autoRentEnabled = False
        isChained, isUnsuitable = self._carouselDP.processDependentParams(item)
        return buildCustomizationItemDataVO(item=item, count=inventoryCount, isApplied=isApplied, isDarked=isDarked, isUsedUp=isUsedUp, autoRentEnabled=autoRentEnabled, vehicle=g_currentVehicle.item, showEditableHint=showEditableHint, showEditBtnHint=showEditBtnHint, isChained=isChained, isUnsuitable=isUnsuitable, isInProgress=item.isQuestInProgress(), rarity=item.rarity)

    def __getItemTabsData(self):
        tabsData = []
        visibleTabs = self.getVisibleTabs()
        enabledTabs = self.getEnabledTabs()
        tankName = g_currentVehicle.item.userName
        outfit = self.__ctx.mode.currentOutfit
        for tabId in visibleTabs:
            slotType = CustomizationTabs.SLOT_TYPES[tabId]
            itemTypeName = CustomizationTabs.TAB_NAMES[tabId]
            isActive = tabId in CustomizationTabs.MODES[self.__ctx.modeId]
            isEnabled = tabId in enabledTabs
            body = TOOLTIPS.customizationItemTab(itemTypeName)
            if not isEnabled:
                body = _ms(TOOLTIPS.customizationDisabledItemTab(itemTypeName), tankName=tankName)
            slotsCount, filledSlotsCount = checkSlotsFilling(outfit, slotType)
            if tabId in (CustomizationTabs.STYLES_3D, CustomizationTabs.STYLES_2D):
                showPlus = outfit.style is None
            else:
                showPlus = filledSlotsCount < slotsCount
            tabsData.append({b'label': (_ms(ITEM_TYPES.customizationPlural(itemTypeName))), 
               b'icon': (RES_ICONS.getCustomizationIcon(itemTypeName)), 
               b'tooltip': (makeTooltip(ITEM_TYPES.customizationPlural(itemTypeName), body)), 
               b'id': tabId, 
               b'isInActiveGroup': isActive, 
               b'isEnabled': isEnabled, 
               b'showPlus': (showPlus and isActive)})

        return tabsData

    def __onCarouselFiltered(self, **kwargs):
        if b'group' in kwargs:
            self._carouselDP.updateSelectedGroup(kwargs[b'group'], kwargs.get(b'isReset', False))
        if b'historic' in kwargs:
            self._carouselDP.updateCarouselFilter(FilterTypes.HISTORIC, kwargs[b'historic'], FilterAliases.HISTORIC)
        if b'nonHistoric' in kwargs:
            self._carouselDP.updateCarouselFilter(FilterTypes.HISTORIC, kwargs[b'nonHistoric'], FilterAliases.NON_HISTORIC)
        if b'fantastical' in kwargs:
            self._carouselDP.updateCarouselFilter(FilterTypes.HISTORIC, kwargs[b'fantastical'], FilterAliases.FANTASTICAL)
        if b'inventory' in kwargs:
            self._carouselDP.updateCarouselFilter(FilterTypes.INVENTORY, kwargs[b'inventory'])
        if b'applied' in kwargs:
            self._carouselDP.updateCarouselFilter(FilterTypes.APPLIED, kwargs[b'applied'])
        if b'formfactorGroups' in kwargs:
            self._carouselDP.updateCarouselFilter(FilterTypes.FORMFACTORS, kwargs[b'formfactorGroups'])
        if b'onAnotherVeh' in kwargs:
            self._carouselDP.updateCarouselFilter(FilterTypes.USED_UP, kwargs[b'onAnotherVeh'])
        if b'onlyProgressionDecals' in kwargs:
            self._carouselDP.updateCarouselFilter(FilterTypes.PROGRESSION, kwargs[b'onlyProgressionDecals'])
        if b'onlyEditableStyles' in kwargs:
            self._carouselDP.updateCarouselFilter(FilterTypes.EDITABLE_STYLES, kwargs[b'onlyEditableStyles'], FilterAliases.EDITABLE_STYLES)
        if b'onlyNonEditableStyles' in kwargs:
            self._carouselDP.updateCarouselFilter(FilterTypes.EDITABLE_STYLES, kwargs[b'onlyNonEditableStyles'], FilterAliases.NON_EDITABLE_STYLES)
        if b'raritiesGroup' in kwargs:
            self._carouselDP.updateCarouselFilter(FilterTypes.RARITY, kwargs[b'raritiesGroup'])
        self.__refreshHotFilters()
        self.__rebuildCarousel()
        self.__updateHints()
        return

    def __onCacheResync(self, reason, items):
        if not g_currentVehicle.isPresent():
            return
        typesForUpdate = {GUI_ITEM_TYPE.CUSTOMIZATION, GUI_ITEM_TYPE.CUSTOMIZATIONS}
        if not typesForUpdate & set(items):
            return
        self._carouselDP.invalidateItems()
        self.__updateTabs()
        self.__setBottomPanelBillData()
        self.__updatePopoverBtn()
        self.__rebuildCarousel()
        self.__updateStyleLabel()
        self.__setNotificationCounters()
        self.__updatefilterFallbackData()
        return

    def __onVehicleChanged(self):
        self._carouselDP.invalidateItems()
        self.__updateTabs()
        self.resetFilter()
        self.__updatePopoverBtn()
        self.__setBottomPanelBillData()
        self.__setFooterInitData()
        self.__scrollToNewItem()
        self.__updateStyleLabel()
        return

    def __onSeasonChanged(self, seasonType):
        self.__updateTabs()
        self.__rebuildCarousel()
        self.__updatePopoverBtn()
        self.__setBottomPanelBillData()
        self.__setNotificationCounters()
        self.__scrollToNewItem()
        return

    def __updateHelpMessage(self):
        tabId = self.__ctx.mode.tabId
        isEscHelpVisible = False
        if self.__ctx.mode.prevTabId == CustomizationTabs.STAT_TRACKERS:
            pass
        elif self.__ctx.modeId == CustomizationModes.STYLE_2D_EDITABLE or tabId == CustomizationTabs.STAT_TRACKERS:
            if not self.__isEscHelpSeen:
                self.__isEscHelpSeen = True
                isEscHelpVisible = True
            else:
                return
        self.as_updateEscHelpMessageS(isEscHelpVisible)
        return

    def __updatePopoverBtn(self):
        itemsPopoverBtnEnabled = False
        if self.__ctx.isInStyleMode(CustomizationModes.STYLE_3D):
            itemsPopoverBtnEnabled = self.__ctx.hasCommonItems()
        else:
            for outfit in viewvalues(self.__ctx.mode.outfits):
                for intCD, component, _, _, _ in outfit.itemsFull():
                    isMatchingProjection = component.customType == ProjectionDecalComponent.customType and component.matchingTag is not None
                    if component.isFilled() or isMatchingProjection:
                        item = self.service.getItemByCD(intCD)
                        if item.isHiddenInUI():
                            continue
                        itemsPopoverBtnEnabled = True
                        break

                if itemsPopoverBtnEnabled:
                    break

        self.as_setItemsPopoverBtnEnabledS(itemsPopoverBtnEnabled)
        imgSrc = RES_ICONS.MAPS_ICONS_CUSTOMIZATION_ITEMS_POPOVER_DEFAULT_LIST30X16
        if itemsPopoverBtnEnabled:
            tooltip = VEHICLE_CUSTOMIZATION.CUSTOMIZATION_ITEMSPOPOVER_BTN
        else:
            tooltip = VEHICLE_CUSTOMIZATION.CUSTOMIZATION_ITEMSPOPOVER_BTN_DISABLED
        if self.__ctx.modeId == CustomizationModes.CUSTOM:
            popoverAlias = VIEW_ALIAS.CUSTOMIZATION_ITEMS_POPOVER
        else:
            style = self.__ctx.mode.currentOutfit.style
            if style is None:
                popoverAlias = VIEW_ALIAS.CUSTOMIZATION_EDITED_KIT_POPOVER
            elif style.isQuestsProgression:
                popoverAlias = VIEW_ALIAS.CUSTOMIZATION_PROGRESSIVE_KIT_POPOVER
            elif style.isEditable:
                popoverAlias = VIEW_ALIAS.CUSTOMIZATION_EDITED_KIT_POPOVER
            else:
                popoverAlias = VIEW_ALIAS.CUSTOMIZATION_KIT_POPOVER
        self.as_showPopoverBtnS(popoverAlias, imgSrc, tooltip)
        return

    def __onItemsInstalled(self, item, slotId, season, component):
        self.__updateTabs()
        self.__setBottomPanelBillData()
        self.__updatePopoverBtn()
        self.__rebuildCarousel(scroll=True)
        return

    def __onTabChanged(self, tabIndex, itemCD=None):
        self.__updateTabs()
        self.__rebuildCarousel()
        self.__updateStyleLabel()
        self.__setNotificationCounters()
        self.__updateHints()
        self.__updatefilterFallbackData()
        self.__updateVehiclesSidebarBtn()
        self.__updateHelpMessage()
        if itemCD is not None:
            self.__scrollToItem(itemCD)
        elif self._selectedItem is None:
            if not self.__isInited:
                BigWorld.callback(0.0, self.__scrollToNewItem)
            else:
                self.__scrollToNewItem()
        self.__uiLogger.onTabOpened(tabIndex)
        self.__isInited = True
        return

    def __onItemsRemoved(self, *_, **__):
        self.__updateTabs()
        self.__setBottomPanelBillData()
        selectedItem = self._selectedItem
        self.__updatePopoverBtn()
        self.__rebuildCarousel()
        if selectedItem is not None:
            self.__scrollToItem(selectedItem.intCD, immediately=True)
        return

    def __onModeChanged(self, modeId, prevModeId):
        self._carouselDP.onModeChanged(modeId, prevModeId)
        self.__setBottomPanelBillData()
        self.__setFooterInitData()
        self.__refreshHotFilters()
        self.__updatePopoverBtn()
        return

    def __onChangesCanceled(self):
        self.__updateTabs()
        self.__setBottomPanelBillData()
        self.__updatePopoverBtn()
        self._carouselDP.invalidateFilteredItems()
        self.__rebuildCarousel()
        return

    def __onComponentChanged(self, slotId, refreshCarousel):
        self.__setBottomPanelBillData()
        self.__updatePopoverBtn()
        if refreshCarousel:
            self.__rebuildCarousel()
        return

    def __scrollToNewItem(self):
        itemsRequester = self.itemsCache.items
        inventoryRequester = itemsRequester.inventory
        carrouselItemCDs = self._carouselDP.getCarouselData()
        currentVehItemType = g_currentVehicle.item.typeDescr
        getItemByCD = itemsRequester.getItemByCD
        noveltyCounters = inventoryRequester.getC11nItemsNoveltyCounters(currentVehItemType)
        carrouselNoveltyItems = [getItemByCD(intCD) for intCD in carrouselItemCDs if intCD in noveltyCounters]
        carrouselNoveltyItems.sort(key=comparisonKey)
        season = self.__ctx.season
        itemTypes = CustomizationTabs.ITEM_TYPES[self.__ctx.mode.tabId]
        for item in carrouselNoveltyItems:
            if item.itemTypeID in itemTypes and item.season & season:
                self.__scrollToItem(item.intCD)
                break

        return

    def __scrollToItem(self, itemCD, immediately=False):
        self.as_scrollToSlotS(itemCD, immediately)
        return

    def __onFilterPopoverClosed(self):
        self.blinkCounter()
        return

    def __onGetItemBackToHand(self, item, progressionLevel=-1, scrollToItem=False):
        if scrollToItem:
            self.__scrollToItem(item.intCD, immediately=True)
        return

    def __onItemSelected(self, *_):
        self.__updateSelection()
        return

    def __onItemUnselected(self):
        self.__updateSelection()
        return

    def __updateSelection(self, scroll=False):
        if self.__ctx.mode.selectedItem is not None:
            self._selectedItem = self.__ctx.mode.selectedItem
        elif self.__ctx.mode.selectedSlot is not None:
            slotId = self.__ctx.mode.selectedSlot
            if slotId.slotType == GUI_ITEM_TYPE.STYLE:
                self._selectedItem = self.__ctx.mode.modifiedStyle
            else:
                self._selectedItem = self.__ctx.mode.getItemFromSlot(slotId)
        else:
            self._selectedItem = None
        self._carouselDP.selectItem(self._selectedItem)
        if self._selectedItem is not None and scroll:
            self.__scrollToItem(self._selectedItem.intCD, True)
        self.__updateStageSwitcherVisibility()
        self.__updatePopoverBtn()
        return

    def __updateHints(self):
        if self.__ctx.mode.tabId == CustomizationTabs.PROJECTION_DECALS:
            self.__onProjectionDecalOnlyOnceHintShown()
        else:
            self.__onProjectionDecalOnlyOnceHintHidden()
        return

    def __onProjectionDecalOnlyOnceHintShown(self):
        if self.__c11nSettings.get(PROJECTION_DECAL_HINT_SHOWN_FIELD, False):
            return
        else:
            isCarouselEmpty = not self._carouselDP.collection
            slotId = C11nId(Area.MISC, GUI_ITEM_TYPE.PROJECTION_DECAL, -1)
            multiSlot = getMultiSlot(self.__ctx.mode.currentOutfit, slotId)
            isSlotEmpty = multiSlot is not None and multiSlot.isEmpty()
            visible = isSlotEmpty and not isCarouselEmpty
            self.as_setProjectionDecalHintVisibilityS(visible)
            return

    def __onProjectionDecalOnlyOnceHintHidden(self, record=False):
        if record and not self.__c11nSettings.get(PROJECTION_DECAL_HINT_SHOWN_FIELD, False):
            self.__c11nSettings[PROJECTION_DECAL_HINT_SHOWN_FIELD] = True
            AccountSettings.setSettings(CUSTOMIZATION_SECTION, self.__c11nSettings)
        self.as_setProjectionDecalHintVisibilityS(False)
        return

    def __processBillDataPurchaseItems(self, purchseItems):
        if self.__ctx.modeId not in CustomizationModes.STYLES:
            return purchseItems
        result = purchseItems[:1]
        for pItem in purchseItems[1:]:
            if pItem.isEdited:
                result.append(pItem)

        return result

    def __updateStageSwitcherVisibility(self):
        newVisibility = False
        if self.__ctx.mode.tabId in CustomizationTabs.STYLES:
            styleItem = self.__ctx.mode.currentOutfit.style
            if styleItem:
                newVisibility = styleItem.isProgression
        if self.__stageSwitcherVisibility != newVisibility:
            self.__stageSwitcherVisibility = newVisibility
            self.as_setStageSwitcherVisibilityS(self.__stageSwitcherVisibility)
        return

    def __updateVehiclesSidebarBtn(self):
        self.as_setVehiclesSidebarBtnVisibilityS(self.__ctx.mode.tabId == CustomizationTabs.ATTACHMENTS)
        return
