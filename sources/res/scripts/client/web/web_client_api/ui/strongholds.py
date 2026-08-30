from gui.clans.clan_helpers import getStrongholdUrl
from gui.impl.lobby.clan_supply.clan_supply_helpers import showClanSupplyView
from gui.shared import event_dispatcher as shared_events
from uilogging.clan_supply.constants import ClanSupplyLogKeys
from web.web_client_api import w2c, W2CSchema

class StrongholdsWebApiMixin(object):

    @w2c(W2CSchema, b'strongholds')
    def openStrongholds(self, cmd):
        url = getStrongholdUrl() + cmd.custom_parameters.get(b'url', b'')
        shared_events.showStrongholds(url)
        return

    @w2c(W2CSchema, b'clan_supply')
    def openClanSupply(self, cmd):
        tabID = cmd.custom_parameters.get(b'page')
        showClanSupplyView(tabId=tabID, parentScreenLog=ClanSupplyLogKeys.CLAN_LANDING)
        return
