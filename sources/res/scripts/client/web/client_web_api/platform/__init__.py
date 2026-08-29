import typing
from helpers import dependency
from skeletons.helpers.platform import IPublishPlatform
from web.client_web_api.api import C2WHandler, c2w

class PlatformEventHandler(C2WHandler):
    __platform = dependency.descriptor(IPublishPlatform)

    def init(self):
        super(PlatformEventHandler, self).init()
        self.__platform.onPayment += self.__onPayment
        self.__platform.onOverlay += self.__onOverlay
        return

    def fini(self):
        self.__platform.onPayment -= self.__onPayment
        self.__platform.onOverlay -= self.__onOverlay
        super(PlatformEventHandler, self).fini()
        return

    @c2w(name=b'on_platform_payment')
    def __onPayment(self, orderID, authorized):
        return {b'orderID': orderID, 
           b'authorized': (bool(authorized))}

    @c2w(name=b'on_overlay_activated')
    def __onOverlay(self, active):
        return {b'isActive': active}
