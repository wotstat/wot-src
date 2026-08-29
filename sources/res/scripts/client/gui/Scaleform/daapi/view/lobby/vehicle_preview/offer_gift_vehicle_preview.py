import logging
from functools import partial
import typing
from CurrentVehicle import g_currentPreviewVehicle
from constants import RentType
from gui.Scaleform.daapi.view.lobby.vehicle_preview.items_kit_helper import getDataOneVehicle, addBuiltInEquipment
from gui.Scaleform.daapi.view.lobby.vehicle_preview.vehicle_preview import VehiclePreview
from gui.Scaleform.framework.entities import BaseDAAPIComponent
from gui.Scaleform.genConsts.STORAGE_CONSTANTS import STORAGE_CONSTANTS
from gui.Scaleform.genConsts.VEHPREVIEW_CONSTANTS import VEHPREVIEW_CONSTANTS
from gui.Scaleform.locale.VEHICLE_PREVIEW import VEHICLE_PREVIEW
from gui.impl.lobby.offers.offer_gift_dialog import RENT_VALUE_DESCR_BY_TYPE
from gui.shared import event_dispatcher, formatters
from helpers import dependency
from skeletons.gui.lobby_context import ILobbyContext
from skeletons.gui.offers import IOffersDataProvider
from web.web_client_api.common import ItemPackEntry, ItemPackType, ItemPackTypeGroup
from gui.impl import backport
from gui.impl.gen import R
_logger = logging.getLogger(__name__)
CREW_LVL_BY_TYPE = {(ItemPackType.CREW_50): b'50%', 
   (ItemPackType.CREW_75): b'75%', 
   (ItemPackType.CREW_100): b'100%', 
   (ItemPackType.CUSTOM_CREW_100): b'100%'}

class OfferGiftVehiclePreview(VehiclePreview):
    __offersProvider = dependency.descriptor(IOffersDataProvider)
    __lobbyContext = dependency.descriptor(ILobbyContext)

    def __init__(self, ctx):
        if any(key not in ctx for key in [b'offerID', b'giftID', b'confirmCallback']):
            _logger.error(b'Wrong context for offer preview window: %s', ctx)
        self._offer = self.__offersProvider.getOffer(ctx[b'offerID'])
        self._gift = self._offer.getGift(ctx[b'giftID'])
        self._vehicle = self._gift.bonus.displayedItem
        customCallbacks = ctx.get(b'customCallbacks', {})
        self._customCallbacks = customCallbacks if customCallbacks is not None else {}
        self._COMMON_SOUND_SPACE = ctx.get(b'soundSpace', self._COMMON_SOUND_SPACE)
        ctx[b'itemCD'] = self._vehicle.intCD
        ctx[b'previewBackCb'] = self._customCallbacks.get(b'previewBackCb', partial(event_dispatcher.showOfferGiftsWindow, self._offer.id))
        super(OfferGiftVehiclePreview, self).__init__(ctx)
        self._confirmCallback = ctx.get(b'confirmCallback')
        self.__itemsPack = self._generateItemsPack()
        addBuiltInEquipment(self.__itemsPack, self._itemsCache, self._vehicleCD)
        return

    def setBottomPanel(self):
        self.as_setBottomPanelS(VEHPREVIEW_CONSTANTS.BOTTOM_PANEL_OFFER_GIFT_LINKAGE)
        return

    def _generateItemsPack(self):
        itemsPack = []
        if self._gift.isWithSlotBonus:
            itemsPack.append(ItemPackEntry(type=ItemPackType.CUSTOM_SLOT, count=1, groupID=1))
        if self._gift.bonus.isWithCrew:
            lvl = self._gift.bonus.getTmanRoleLevel(self._gift.bonus.displayedVehicleInfo)
            crewType = getattr(ItemPackType, (b'CREW_{}').format(lvl), ItemPackType.CREW_50)
            itemsPack.append(ItemPackEntry(type=crewType, count=1, groupID=1))
        return itemsPack

    def _onRegisterFlashComponent(self, viewPy, alias):
        super(OfferGiftVehiclePreview, self)._onRegisterFlashComponent(viewPy, alias)
        if alias == VEHPREVIEW_CONSTANTS.BOTTOM_PANEL_OFFER_GIFT_PY_ALIAS:
            itemsData = getDataOneVehicle(itemsPack=self.__itemsPack, vehicle=g_currentPreviewVehicle.item, vehicleGroupId=1)
            for item in self.__itemsPack:
                if item.type in ItemPackTypeGroup.CREW:
                    itemsData.insert(0, self.__getCrewItemPackEntry(item))

            viewPy.setData(itemsPack=self.__itemsPack, panelDataVO=self._getBuyingPanelData(), packedItemsVO={b'items': itemsData}, confirmCallback=self._confirmCallback)
        elif alias == VEHPREVIEW_CONSTANTS.CREW_LINKAGE:
            viewPy.setVehicleCrews((
             ItemPackEntry(id=g_currentPreviewVehicle.item.intCD, groupID=1),), [item for item in self.__itemsPack if item.type in ItemPackTypeGroup.CREW])
        return

    def _getPreviewDescription(self):
        tankName = self._gift.bonus.displayedItem.shortUserName
        if self._gift.rentType == RentType.NO_RENT:
            noRentRes = R.strings.offers.tankPreview.description.noRent
            if self._gift.bonus.isWithCrew and self._gift.isWithSlotBonus:
                res = noRentRes.withCrewAndSlot()
            elif self._gift.bonus.isWithCrew:
                res = noRentRes.withCrew()
            elif self._gift.isWithSlotBonus:
                res = noRentRes.withSlot()
            else:
                res = noRentRes.noItems()
            description = backport.text(res, tankName=tankName)
        else:
            if self._vehicle.isRented:
                base = R.strings.offers.tankPreview.description.prolongRent()
            else:
                base = R.strings.offers.tankPreview.description.newRent()
            valueRes = RENT_VALUE_DESCR_BY_TYPE[self._gift.rentType]
            rentValue = backport.text(valueRes, value=self._gift.rentValue)
            description = backport.text(base, tankName=tankName, rentValue=rentValue)
        return description

    def _getButtonLabel(self):
        if self._gift.rentType != RentType.NO_RENT and self._vehicle.isRented:
            buttonLabel = R.strings.offers.tankPreview.buttonLabel.prolongRent()
        else:
            buttonLabel = R.strings.offers.tankPreview.buttonLabel.default()
        return buttonLabel

    def _getBuyingPanelData(self):
        return {b'title': (formatters.text_styles.superPromoTitle(self._getPreviewDescription())), 
           b'buyButtonLabel': (backport.text(self._getButtonLabel()))}

    def _getBackBtnLabel(self):
        return self._backBtnLabel or VEHICLE_PREVIEW.HEADER_BACKBTN_DESCRLABEL_REFERRALPROGRAM

    def _populate(self):
        super(OfferGiftVehiclePreview, self)._populate()
        self.__offersProvider.onOffersUpdated += self.__onOffersUpdated
        self.__lobbyContext.getServerSettings().onServerSettingsChange += self.__onServerSettingsChange
        return

    def _dispose(self):
        super(OfferGiftVehiclePreview, self)._dispose()
        self.__offersProvider.onOffersUpdated -= self.__onOffersUpdated
        self.__lobbyContext.getServerSettings().onServerSettingsChange -= self.__onServerSettingsChange
        return

    def _getExitEvent(self):
        exitEvent = super(OfferGiftVehiclePreview, self)._getExitEvent()
        exitEvent.ctx.update({b'confirmCallback': (self._confirmCallback), b'offerID': (self._offer.id), b'giftID': (self._gift.id)})
        return exitEvent

    def _onInventoryChanged(self, *_):
        return

    def __onServerSettingsChange(self, *args, **kwargs):
        if not self.__lobbyContext.getServerSettings().isOffersEnabled():
            event_dispatcher.showHangar()
        return

    def __onOffersUpdated(self):
        offer = self.__offersProvider.getOffer(self._offer.id)
        if offer is None or not offer.isOfferAvailable:
            if self.__offersProvider.getAvailableOffers(onlyVisible=True):
                event_dispatcher.showStorage(defaultSection=STORAGE_CONSTANTS.OFFERS)
            else:
                self._customCallbacks.get(b'offerEndedCb', event_dispatcher.showHangar)()
        return

    @classmethod
    def __getCrewItemPackEntry(cls, item):
        return {b'isEnabled': True, 
           b'topTitle': b'', 
           b'topTitleSmall': b'', 
           b'items': [
                    {b'count': (CREW_LVL_BY_TYPE.get(item.type, b'')), 
                       b'hasCompensation': False, 
                       b'icon': (backport.image(R.images.gui.maps.shop.rewards.c_48x48.prizeCrew())), 
                       b'iconAlt': (backport.image(R.images.gui.maps.icons.artefact.notFound())), 
                       b'id': b'None', 
                       b'overlayType': b'', 
                       b'rawData': None, 
                       b'slotIndex': 0, 
                       b'type': (item.type)}]}
