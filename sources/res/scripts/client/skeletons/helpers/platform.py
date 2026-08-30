from __future__ import absolute_import
import typing
if typing.TYPE_CHECKING:
    from Event import Event

class IPublishPlatform(object):
    onPayment = None
    onOverlay = None

    def init(self):
        raise NotImplementedError
        return

    def fini(self):
        raise NotImplementedError
        return

    def isInited(self):
        raise NotImplementedError
        return

    def isConnected(self):
        raise NotImplementedError
        return
