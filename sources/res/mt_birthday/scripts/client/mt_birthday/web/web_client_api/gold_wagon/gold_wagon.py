from gui.clientgw.gold_wagon.contexts import GoldWagonFetchInfoCtx
from helpers import dependency
from skeletons.gui.web import IWebController
from web.web_client_api import w2c, W2CSchema, w2capi
from mt_birthday.gui.shared.event_dispatcher import showMainView

class GoldWagonWebApiMixin(object):
    __webController = dependency.descriptor(IWebController)

    @w2c(W2CSchema, b'get_info')
    def getInfo(self, cmd):
        result = yield self.__webController.sendRequest(ctx=GoldWagonFetchInfoCtx())
        if result.isSuccess():
            yield {b'gold_daily_refill_amount': (result.data.get(b'gold_daily_refill_amount', 0)), b'gold_per_container': (result.data.get(b'gold_per_container', 0))}
        return

    @w2c(W2CSchema, b'show_birthday_main_view')
    def openBirthdayMainView(self, _):
        showMainView()
        return


@w2capi(name=b'gold_wagon', key=b'action')
class GoldWagonWebApi(GoldWagonWebApiMixin):
    pass
