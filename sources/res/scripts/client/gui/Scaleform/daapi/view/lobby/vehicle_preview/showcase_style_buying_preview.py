from __future__ import absolute_import
import typing
from CurrentVehicle import g_currentPreviewVehicle
from gui.impl import backport
from gui.impl.gen import R
from gui.Scaleform.daapi.view.lobby.vehicle_preview.style_preview import VehicleStylePreview
from gui.Scaleform.genConsts.VEHPREVIEW_CONSTANTS import VEHPREVIEW_CONSTANTS
from gui.shared.utils.requesters import REQ_CRITERIA
from helpers import dependency
from skeletons.gui.shared import IItemsCache
if typing.TYPE_CHECKING:
    from typing import Dict, Optional
    from gui.shared.gui_items.customization.c11n_items import Style

class VehicleShowcaseStyleBuyingPreview(VehicleStylePreview):
    __itemsCache = dependency.descriptor(IItemsCache)

    def __init__(self, ctx=None):
        super(VehicleShowcaseStyleBuyingPreview, self).__init__(ctx)
        self.__style = ctx.get(b'style')
        self.__price = ctx.get(b'price')
        self.__originalPrice = ctx.get(b'originalPrice')
        self.__discountPercent = ctx.get(b'discountPercent')
        self.__endTime = ctx.get(b'endTime')
        self.__buyParams = ctx.get(b'buyParams')
        self.__obtainingMethod = ctx.get(b'obtainingMethod')
        return

    def setBottomPanel(self, linkage=None):
        self.as_setBottomPanelS(linkage)
        return

    def _onRegisterFlashComponent(self, viewPy, alias):
        super(VehicleShowcaseStyleBuyingPreview, self)._onRegisterFlashComponent(viewPy, alias)
        if alias == VEHPREVIEW_CONSTANTS.BOTTOM_PANEL_SHOWCASE_STYLE_BUYING_PY_ALIAS:
            viewPy.setData(self.__style, self.__price, self.__endTime, self.__originalPrice, self.__buyParams, self.__discountPercent, self.__obtainingMethod)
            viewPy.update()
        return

    def _populate(self):
        self.setBottomPanel(VEHPREVIEW_CONSTANTS.BOTTOM_PANEL_SHOWCASE_STYLE_BUYING_LINKAGE)
        super(VehicleShowcaseStyleBuyingPreview, self)._populate()
        return

    def _getAdditionalInfoVO(self):
        vpAdditionalInfoVO = super(VehicleShowcaseStyleBuyingPreview, self)._getAdditionalInfoVO()
        if self._styleIsUnique():
            vpAdditionalInfoVO[b'vehicleInfoDesc'] = self.__getVehicleInfoDescVO()
        return vpAdditionalInfoVO

    def _styleIsUnique(self):
        suitableVehicles = self.__itemsCache.items.getVehicles(REQ_CRITERIA.VEHICLE.FOR_ITEM(self.__style))
        return len(suitableVehicles) == 1

    @staticmethod
    def __getVehicleInfoDescVO():
        vehicle = g_currentPreviewVehicle.item
        vehicleType = (b'{}_elite').format(vehicle.type) if vehicle.isElite or vehicle.isPremium else vehicle.type
        return {b'nationFlag': (backport.image(R.images.gui.maps.icons.filters.nations.dyn(vehicle.nationName)())), 
           b'level': (backport.text(R.strings.menu.header.level.num(vehicle.level)())), 
           b'typeImageSrc': (backport.image(R.images.gui.maps.icons.filters.tanks.dyn(vehicleType.replace(b'-', b'_'))())), 
           b'isElite': (vehicle.isElite or vehicle.isPremium), 
           b'name': (vehicle.descriptor.type.shortUserString)}
