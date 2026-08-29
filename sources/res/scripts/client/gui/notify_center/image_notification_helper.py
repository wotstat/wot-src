import logging
from adisp import adisp_process, adisp_async
from gui import SystemMessages
from gui.impl import backport
from gui.impl.gen import R
from gui.shared.image_helper import getTextureLinkByID
from helpers.CallbackDelayer import CallbackDelayer
from MTWebBrowser import getWebCache
_logger = logging.getLogger(__name__)

class WebImageHelper(object):
    __slots__ = (b'__callbackMethod', b'__imageUrl', b'__callbackDelayer', b'__webCache', b'__defLocalDirPath')
    __DEFAULT_TIMEOUT = 10.0

    def __init__(self, defLocalDirPath=b'notifications'):
        self.__callbackMethod = None
        self.__imageUrl = b''
        self.__callbackDelayer = CallbackDelayer()
        self.__webCache = None
        self.__defLocalDirPath = defLocalDirPath
        return

    @adisp_async
    def getLocalPath(self, imageUrl, callback=lambda x: None):
        self.__imageUrl = imageUrl
        self.__callbackMethod = callback
        self.__webCache = getWebCache()
        if self.__webCache is None:
            _logger.error(b'Failed to get web cache. Using empty image path.')
            self.__callbackDelayer.destroy()
            self.__callMethod(b'')
            return
        else:
            localPath = self.__webCache.get(self.__imageUrl)
            if localPath is not None:
                _logger.debug(b'Got image path %s for url %s', localPath, self.__imageUrl)
                self.__callbackDelayer.destroy()
                self.__webCache = None
                self.__callMethod(str(localPath))
                return
            _logger.debug(b'Failed to get image from web cache by url %s. Downloading initialized.', self.__imageUrl)
            self.__webCache.loadCustomUrls([self.__imageUrl], self.__defLocalDirPath)
            self.__webCache.onDownloadFinished += self.__stop
            self.__callbackDelayer.delayCallback(self.__DEFAULT_TIMEOUT, self.__stop)
            return

    def __stop(self):
        self.__callbackDelayer.destroy()
        self.__webCache.onDownloadFinished -= self.__stop
        localPath = self.__webCache.get(self.__imageUrl) or b''
        _logger.debug(b'Got image path %s for url %s', localPath, self.__imageUrl)
        self.__webCache = None
        self.__callMethod(str(localPath))
        return

    def __onTimer(self):
        _logger.warning(b'Web Cache download timed out. Failed to load image from url: %s', self.__imageUrl)
        self.__stop()
        return

    def __callMethod(self, localPath):
        callback = self.__callbackMethod
        self.__callbackMethod = None
        if callback is not None and callable(callback):
            callback(localPath)
        return


@adisp_process
def showPaymentMethodLinkNotification(method, imageUrl):
    helper = WebImageHelper()
    localPath = yield helper.getLocalPath(imageUrl)
    SystemMessages.pushMessage(text=backport.text(R.strings.messenger.serviceChannelMessages.sysMsg.titles.paymentMethodLink(), method=method), type=SystemMessages.SM_TYPE.PaymentMethodLinkNotifyCenter, messageData={b'imageBlock': (_packImageBlock(localPath))})
    return


@adisp_process
def showPaymentMethodUnlinkNotification(method, imageUrl):
    helper = WebImageHelper()
    localPath = yield helper.getLocalPath(imageUrl)
    SystemMessages.pushMessage(text=backport.text(R.strings.messenger.serviceChannelMessages.sysMsg.titles.paymentMethodUnlink(), method=method), type=SystemMessages.SM_TYPE.PaymentMethodUnlinkNotifyCenter, messageData={b'imageBlock': (_packImageBlock(localPath))})
    return


def _packImageBlock(imagePath):
    if not imagePath:
        return b''
    return (b"<br/><br/><img src='{path}'/>").format(path=getTextureLinkByID(imagePath))
