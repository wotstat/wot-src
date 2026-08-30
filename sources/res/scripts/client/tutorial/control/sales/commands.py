from account_helpers.AccountSettings import AccountSettings
from gui.Scaleform.daapi.view.lobby.store.browser import shop_helpers
from gui.Scaleform.genConsts.STORE_CONSTANTS import STORE_CONSTANTS
from gui.impl.dialogs.dialogs import showEnlargeBarracksDialog
from gui.server_events.events_dispatcher import showMissionsMarathon
from gui.shared import g_eventBus
from gui.shared.event_dispatcher import showShop
from gui.shared.events import OpenLinkEvent
from gui.shared.gui_items.items_actions import factory as ActionsFactory
from wg_async import wg_await, wg_async

def buySlots():
    ActionsFactory.doAction(ActionsFactory.BUY_VEHICLE_SLOT)
    return


@wg_async
def buyBerths():
    yield wg_await(showEnlargeBarracksDialog())
    return


def createClan():
    g_eventBus.handleEvent(OpenLinkEvent(OpenLinkEvent.CLAN_CREATE))
    return


def showMarathonPage():
    showMissionsMarathon()
    return


def showShopPremium():
    showShop(shop_helpers.getBuyPremiumUrl())
    return


def showShopEquipment():
    showShop(shop_helpers.getBuyEquipmentUrl())
    return


def showShopOptionalDevice():
    showShop(shop_helpers.getBuyOptionalDevicesUrl())
    return


def showShopPersonalReserves():
    showShop(shop_helpers.getBuyPersonalReservesUrl())
    return


def showShopVehicles():
    showShop(shop_helpers.getBuyVehiclesUrl())
    return


def showShopVehiclesRent():
    showShop(shop_helpers.getBuyVehiclesUrl())
    return


def showShopVehiclesTradeIn():
    showShop(shop_helpers.getTradeInVehiclesUrl())
    return


def configureShopForShells():
    AccountSettings.setFilter(b'shop_current', (-1, STORE_CONSTANTS.SHELL, True))
    shellsFilter = AccountSettings.getFilter(b'shop_shell')
    shellsFilter[b'fitsType'] = STORE_CONSTANTS.OTHER_VEHICLES_SHELL_FIT
    shellsFilter[b'itemTypes'] = [
     STORE_CONSTANTS.ARMOR_PIERCING_SHELL,
     STORE_CONSTANTS.ARMOR_PIERCING_CR_SHELL,
     STORE_CONSTANTS.HOLLOW_CHARGE_SHELL,
     STORE_CONSTANTS.HIGH_EXPLOSIVE_SHELL]
    AccountSettings.setFilter(b'shop_shell', shellsFilter)
    return
