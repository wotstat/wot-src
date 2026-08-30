from __future__ import absolute_import
from CurrentVehicle import g_currentPreviewVehicle
from gui.Scaleform.daapi.view.lobby.vehicle_preview.items_kit_helper import OFFER_CHANGED_EVENT
from gui.Scaleform.daapi.view.meta.VehiclePreviewBrowseTabMeta import VehiclePreviewBrowseTabMeta
from gui.Scaleform.locale.RES_ICONS import RES_ICONS
from gui.Scaleform.locale.VEHICLE_PREVIEW import VEHICLE_PREVIEW
from gui.shared import g_eventBus, events
from gui.shared.formatters import text_styles, icons
from gui.shared.money import Currency
from gui.impl import backport
from gui.impl.gen import R
from helpers import dependency
from helpers.i18n import makeString as _ms
from skeletons.gui.shared import IItemsCache
_MAX_LENGTH_FULL_DESCRIPTION_NO_KPI = 400
_MAX_LENGTH_FULL_DESCRIPTION_WITH_KPI = 280

class VehiclePreviewBrowseTab(VehiclePreviewBrowseTabMeta):
    itemsCache = dependency.descriptor(IItemsCache)

    def __init__(self):
        super(VehiclePreviewBrowseTab, self).__init__()
        self.__isHeroTank = False
        self.__offer = None
        return

    def _populate(self):
        super(VehiclePreviewBrowseTab, self)._populate()
        g_currentPreviewVehicle.onComponentInstalled += self.update
        g_currentPreviewVehicle.onChanged += self.update
        g_eventBus.addListener(OFFER_CHANGED_EVENT, self.__onOfferChanged)
        self.update()
        return

    def _dispose(self):
        g_currentPreviewVehicle.onComponentInstalled -= self.update
        g_currentPreviewVehicle.onChanged -= self.update
        g_eventBus.removeListener(OFFER_CHANGED_EVENT, self.__onOfferChanged)
        super(VehiclePreviewBrowseTab, self)._dispose()
        return

    def setActiveState(self, isActive):
        return

    def onDisclaimerClick(self):
        if g_currentPreviewVehicle.isPresent():
            vehicle = g_currentPreviewVehicle.item
            g_eventBus.handleEvent(events.OpenLinkEvent(events.OpenLinkEvent.SPECIFIED, vehicle.getDisclaimerUrl()))
        return

    def setHeroTank(self, isHeroTank):
        self.__isHeroTank = isHeroTank
        self.update()
        return

    def setActiveOffer(self, offer):
        self.__offer = offer
        self.update()
        return

    def update(self, *_):
        self._update()
        return

    def _update(self):
        if g_currentPreviewVehicle.isPresent():
            item = g_currentPreviewVehicle.item
            if item.buyPrices.itemPrice.defPrice.get(Currency.GOLD):
                maxDescriptionLength = _MAX_LENGTH_FULL_DESCRIPTION_WITH_KPI
                bonuses = []
                if not (self.__isFrontlineCreditsOffer() or item.isOnlyForEpicBattles):
                    bonuses.append({b'iconSrc': (backport.image(R.images.gui.maps.shop.kpi.star_icon_benefits())), 
                       b'labelStr': (text_styles.concatStylesToMultiLine(text_styles.highTitle(backport.text(R.strings.vehicle_preview.infoPanel.premium.freeExpMultiplier())), text_styles.main(backport.text(R.strings.vehicle_preview.infoPanel.premium.freeExpText()))))})
                if not (item.isSpecial or self.__isFrontlineCreditsOffer() or item.isOnlyForEpicBattles):
                    bonuses.append({b'iconSrc': (backport.image(R.images.gui.maps.shop.kpi.money_benefits())), 
                       b'labelStr': (text_styles.concatStylesToMultiLine(text_styles.highTitle(backport.text(R.strings.vehicle_preview.infoPanel.premium.creditsMultiplier())), text_styles.main(backport.text(R.strings.vehicle_preview.infoPanel.premium.creditsText()))))})
                if item.isEarnCrystals:
                    bonuses.append({b'iconSrc': (backport.image(R.images.gui.maps.shop.kpi.bons_benefits())), 
                       b'labelStr': (text_styles.concatStylesToMultiLine(text_styles.highTitle(backport.text(R.strings.vehicle_preview.infoPanel.premium.bonsTitle())), text_styles.main(backport.text(R.strings.vehicle_preview.infoPanel.premium.bonsText()))))})
                if not item.isCrewLocked:
                    text = R.strings.vehicle_preview.infoPanel.premium.crewTransferText()
                    if item.ignoreRoleIncompatibility:
                        text = R.strings.vehicle_preview.infoPanel.premium.noCrewTransferPenaltyText()
                    bonuses.append({b'iconSrc': (backport.image(R.images.gui.maps.shop.kpi.crow_benefits())), 
                       b'labelStr': (text_styles.concatStylesToMultiLine(text_styles.highTitle(backport.text(R.strings.vehicle_preview.infoPanel.premium.crewTransferTitle())), text_styles.main(backport.text(text))))})
                builtInEquipmentIDs = item.getBuiltInEquipmentIDs()
                builtInCount = len(builtInEquipmentIDs) if builtInEquipmentIDs else 0
                if builtInCount > 0:
                    if builtInCount == 1:
                        equipment = self.itemsCache.items.getItemByCD(builtInEquipmentIDs[0])
                        mainText = equipment.userName
                    else:
                        mainText = backport.text(R.strings.vehicle_preview.infoPanel.premium.builtInEqupmentText(), value=builtInCount)
                    bonuses.append({b'iconSrc': (backport.image(R.images.gui.maps.shop.kpi.infinity_benefits())), 
                       b'labelStr': (text_styles.concatStylesToMultiLine(text_styles.highTitle(backport.text(R.strings.vehicle_preview.infoPanel.premium.builtInEqupmentTitle())), text_styles.main(mainText)))})
            else:
                maxDescriptionLength = _MAX_LENGTH_FULL_DESCRIPTION_NO_KPI
                bonuses = None
            description = item.fullDescription.decode(b'utf-8')
            hasTooltip = len(description) > maxDescriptionLength
            if hasTooltip:
                description = description[:maxDescriptionLength - 3] + b'...'
            icon = icons.makeImageTag(RES_ICONS.MAPS_ICONS_LIBRARY_INFO, 24, 24, -7, -4)
            self.as_setDataS({b'historicReferenceTxt': (text_styles.main(description)), 
               b'needDisclaimer': (item.hasDisclaimer()), 
               b'showTooltip': hasTooltip, 
               b'vehicleType': (g_currentPreviewVehicle.getVehiclePreviewType()), 
               b'titleInfo': (b'%s%s' % (_ms(VEHICLE_PREVIEW.INFOPANEL_TAB_ELITEFACTSHEET_INFO), icon)), 
               b'benefitsData': bonuses})
        return

    def __onOfferChanged(self, event):
        ctx = event.ctx
        self.setActiveOffer(ctx.get(b'offer'))
        return

    def __isFrontlineCreditsOffer(self):
        return self.__offer is not None and self.__offer.eventType == b'frontline' and self.__offer.buyPrice.credits
