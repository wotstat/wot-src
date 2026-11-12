from helpers import dependency
from skeletons.gui.app_loader import IAppLoader
from web.web_client_api import W2CSchema, w2c, w2capi, webApiCollection
from web.web_client_api.request.spa_id import SpaIdWebApiMixin
from web.web_client_api.sound import SoundWebApi
from web.web_client_api.ui.waiting import WaitingWebApiMixin

@w2capi(name=b'request', key=b'request_id')
class _LeaderboardRequestWebApi(SpaIdWebApiMixin):
    pass


@w2capi(name=b'util', key=b'action')
class _LeaderboardUtilWebApi(WaitingWebApiMixin):

    @w2c(W2CSchema, b'hide_tooltip')
    def hideToolTip(self, _):
        dependency.instance(IAppLoader).getApp().getToolTipMgr().hide()
        return


def createComp7LeaderboardWebHandlers():
    return webApiCollection(_LeaderboardRequestWebApi, SoundWebApi, _LeaderboardUtilWebApi)
