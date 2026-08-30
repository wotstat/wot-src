from typing import TYPE_CHECKING
from gui.wgcg.base.handlers import RequestHandlers
from gui.wgcg.settings import WebRequestDataType
if TYPE_CHECKING:
    from gui.wgcg.promo_screens.contexts import PromoGetTeaserRequestCtx, PromoSendTeaserShownRequestCtx, PromoGetUnreadCountRequestCtx, PromoSendActionLogCtx
    from typing import Callable

class PromoScreensRequestHandlers(RequestHandlers):

    def get(self):
        handlers = {(WebRequestDataType.PROMO_GET_TEASER): (self.__getTeaser), 
           (WebRequestDataType.PROMO_TEASER_SHOWN): (self.__sendShownTeaser), 
           (WebRequestDataType.PROMO_GET_UNREAD): (self.__getUnreadCount), 
           (WebRequestDataType.PROMO_SEND_LOG): (self.__sendActionLog)}
        return handlers

    def __getTeaser(self, ctx, callback):
        return self._requester.doRequestEx(ctx, callback, (b'promo_screens', b'get_teaser'), **ctx.getAdditionalData())

    def __sendShownTeaser(self, ctx, callback):
        return self._requester.doRequestEx(ctx, callback, (b'promo_screens', b'send_teaser'), ctx.getPromoID(), **ctx.getAdditionalData())

    def __getUnreadCount(self, ctx, callback):
        return self._requester.doRequestEx(ctx, callback, (b'promo_screens', b'get_unread_count'), **ctx.getAdditionalData())

    def __sendActionLog(self, ctx, callback):
        return self._requester.doRequestEx(ctx, callback, (b'promo_screens', b'client_promo_log'), ctx.getActionData())
