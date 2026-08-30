import BigWorld
from CurrentVehicle import g_currentPreviewVehicle
from gui.Scaleform.daapi.view.lobby.vehicle_preview.vehicle_preview import VehiclePreview
from gui.Scaleform.daapi.view.meta.VehiclePreviewBottomPanelWotPlusMeta import VehiclePreviewBottomPanelWotPlusMeta
from gui.Scaleform.genConsts.VEHPREVIEW_CONSTANTS import VEHPREVIEW_CONSTANTS
from gui.impl import backport
from gui.impl.gen import R
import th_async as future_async
from gui.Scaleform.daapi.view.lobby.event_boards.formaters import formatDate
from gui.shared.event_dispatcher import showTelecomRentDialog
from gui.shared.gui_items.Vehicle import getIconResourceName, getNationLessName
from gui.shop import showRentProductOverlay

class RentalVehiclePreview(VehiclePreview):

    def setBottomPanel(self):
        self.as_setBottomPanelS(VEHPREVIEW_CONSTANTS.BOTTOM_PANEL_WOT_PLUS_LINKAGE)
        return


class VehiclePreviewBottomPanelRental(VehiclePreviewBottomPanelWotPlusMeta):

    def _populate(self):
        super(VehiclePreviewBottomPanelRental, self)._populate()
        self.as_setDataS({b'rentButtonLabel': (backport.text(R.strings.subscription.rentButton.label())), 
           b'isRentButtonEnable': True})
        return

    def onRentClick(self):
        self.__purchaseSubRent()
        return

    def setOffers(self, offers):
        self.__buyParams = offers[0].buyParams
        return

    @future_async.th_async
    def __purchaseSubRent(self):

        def successCallback():
            showRentProductOverlay(self.__buyParams)
            return

        title = backport.text(R.strings.dialogs.wotPlusRental.title())
        vehicleName = g_currentPreviewVehicle.item.userName
        vehicleName = vehicleName.replace(b'(', b'%((')
        vehicleName = vehicleName.replace(b')', b'))')
        title %= vehicleName
        date = formatDate(BigWorld.player().telecomRentals.getRosterExpirationTime())
        description = backport.text(R.strings.dialogs.wotPlusRental.description()) % date
        iconName = getIconResourceName(getNationLessName(g_currentPreviewVehicle.item.name))
        icon = R.images.gui.maps.shop.vehicles.c_360x270.dyn(iconName)()
        yield future_async.th_await(showTelecomRentDialog(title, description, icon, successCallback))
        return
