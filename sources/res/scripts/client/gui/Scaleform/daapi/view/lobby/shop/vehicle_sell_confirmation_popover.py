from __future__ import absolute_import
import logging
from gui.Scaleform.daapi.view.meta.VehicleSellConfirmationPopoverMeta import VehicleSellConfirmationPopoverMeta
from gui.Scaleform.locale.STORE import STORE
from gui.impl import backport
from gui.shared.event_bus import EVENT_BUS_SCOPE
from gui.shared.events import ShopEvent
from gui.shared.formatters import text_styles
from helpers import dependency
from helpers.i18n import makeString as _ms
from skeletons.gui.shared import IItemsCache
_logger = logging.getLogger(__name__)

class VehicleSellConfirmationPopover(VehicleSellConfirmationPopoverMeta):
    itemsCache = dependency.descriptor(IItemsCache)

    def __init__(self, ctx=None):
        super(VehicleSellConfirmationPopover, self).__init__(ctx)
        data = ctx.get(b'data')
        self.__confirmGoldPrice = int(data.confirmGoldPrice)
        self.__tradeOffVehicleIntCD = int(data.tradeOffVehicleIntCD)
        return

    def confirmTradeIn(self):
        self.fireEvent(ShopEvent(ShopEvent.CONFIRM_TRADE_IN), EVENT_BUS_SCOPE.LOBBY)
        self.destroy()
        return

    def _populate(self):
        super(VehicleSellConfirmationPopover, self)._populate()
        self.as_setInitDataS(self.__getInitialVO())
        return

    def __getInitialVO(self):
        tradeOffVehicle = self.itemsCache.items.getItemByCD(self.__tradeOffVehicleIntCD)
        if tradeOffVehicle:
            dataVO = {b'titleLabel': (text_styles.main(_ms(STORE.SELLCONFIRMATIONPOPOVER_TITLELABEL, vehName=tradeOffVehicle.shortUserName))), 
               b'priceLabel': (text_styles.main(_ms(STORE.SELLCONFIRMATIONPOPOVER_PRICELABEL, price=text_styles.highlightText(backport.getIntegralFormat(self.__confirmGoldPrice))))), 
               b'priceValue': (self.__confirmGoldPrice)}
            return dataVO
        else:
            _logger.error(b'Invalid trade off vehicle CD.')
            return
