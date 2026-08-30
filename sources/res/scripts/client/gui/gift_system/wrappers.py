from collections import namedtuple
from functools import wraps
OpenedGiftData = namedtuple(b'OpenedGiftData', b'senderID, metaInfo')
GiftsHistoryData = namedtuple(b'GiftsHistoryData', (b'aggregated', b'detailed'))
GiftsWebState = namedtuple(b'GiftsWebState', (b'sendLimit', b'expireTime', b'expireDelta', b'executionTime', b'state'))
IncomeSysMessage = namedtuple(b'IncomeSysMessage', (b'eventID', b'senderID', b'giftItemID', b'meta', b'executionTime'))
SendGiftResponse = namedtuple(b'SendGiftResponse', (b'state', b'receiverID', b'outCount', b'entitlementCode', b'meta', b'executionTime'))

def ifMessagesEnabled(method):

    @wraps(method)
    def wrapper(messenger, *args, **kwargs):
        if messenger.isMessagesEnabled():
            method(messenger, *args, **kwargs)
        return

    return wrapper


def ifMessagesAllowed(msgType, useQueue=True):

    def decorator(method):

        @wraps(method)
        def wrapper(messenger, *args, **kwargs):
            if not messenger.isMessagesSuspended(*args, **kwargs):
                method(messenger, *args, **kwargs)
            elif useQueue:
                messenger.addToQueue(msgType, *args, **kwargs)
            return

        return wrapper

    return decorator


def hasGiftEventHub(method):

    @wraps(method)
    def wrapper(hubContainer, *args, **kwargs):
        if hubContainer.getGiftEventHub() is not None:
            method(hubContainer, *args, **kwargs)
        return

    return wrapper


def skipNoHubsAction(method):

    @wraps(method)
    def wrapper(controller, hubsToAction, *args, **kwargs):
        if hubsToAction:
            method(controller, hubsToAction, *args, **kwargs)
        return

    return wrapper


def filterGiftHubsAction(eventID):

    def decorator(method):

        @wraps(method)
        def wrapper(listener, hubsToAction, *args, **kwargs):
            if eventID in hubsToAction:
                method(listener, hubsToAction, *args, **kwargs)
            return

        return wrapper

    return decorator
