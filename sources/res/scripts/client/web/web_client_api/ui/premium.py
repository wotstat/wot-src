from web.web_client_api import w2c, W2CSchema
from gui.shared import event_dispatcher as shared_events

class PremiumViewsWebApiMixin(object):

    @w2c(W2CSchema, b'premium_dashboard')
    def openPremiumDashboardWindow(self, _):
        shared_events.showDashboardView()
        return

    @w2c(W2CSchema, b'maps_blacklist')
    def openMapsBlacklistView(self, _):
        shared_events.showMapsBlacklistView()
        return
