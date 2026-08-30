import logging, BigWorld
from account_helpers.telecom_rentals import TelecomRentals
from gui import SystemMessages
from gui.impl import backport
from gui.impl.gen import R
from gui.shared.gui_items.Vehicle import getUserName
from items.vehicles import getVehicleType
from web.web_client_api import W2CSchema, w2c, Field
_logger = logging.getLogger(__name__)

class _TelecomRentalsRentVehicleInfoSchema(W2CSchema):
    vehCD = Field(required=True, type=int)


class TelecomRentalsWebApiMixin(object):

    @w2c(W2CSchema, b'get_telecom_rentals_info')
    def getTelecomRentalsInfo(self, cmd):
        helper = BigWorld.player().telecomRentals
        return {b'active': (helper.isActive()), 
           b'rent_token_total': (helper.getTotalRentCount()), 
           b'rent_token_count': (0 if helper.isBlocked() else helper.getAvailableRentCount()), 
           b'expiration_date': (helper.getRosterExpirationTime())}

    @w2c(_TelecomRentalsRentVehicleInfoSchema, b'telecom_rent_delayed')
    def telecomRentDelayed(self, cmd):
        if cmd.vehCD:
            BigWorld.player().telecomRentals.setRentPending(cmd.vehCD)
            vehName = getUserName(getVehicleType(cmd.vehCD))
            SystemMessages.pushMessage(b'', messageData={b'header': (backport.text(R.strings.messenger.serviceChannelMessages.wotPlus.tankRental.isPending.title())), 
               b'text': (backport.text(R.strings.messenger.serviceChannelMessages.wotPlus.tankRental.isPending.text(), vehicle=vehName))}, type=SystemMessages.SM_TYPE.MessageHeader)
        return
