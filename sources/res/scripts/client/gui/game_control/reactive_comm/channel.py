import logging, re, zlib
from collections import deque
import typing, Event, websocket
from gui.game_control.reactive_comm import constants
from gui.game_control.reactive_comm import packer
_logger = logging.getLogger(__name__)
_channelRegExp = re.compile(b'^[a-zA-Z0-9_-]{2,36}$')

def isChannelNameValid(name):
    if isinstance(name, str):
        return _channelRegExp.match(name) is not None
    else:
        return False


class ChannelsEventsSender(object):

    def __init__(self):
        super(ChannelsEventsSender, self).__init__()
        self.__em = Event.EventManager()
        self.onChannelMessage = Event.Event(self.__em)
        self.onChannelClosed = Event.Event(self.__em)
        self.onSubscriptionClosed = Event.Event(self.__em)
        return

    def clear(self):
        self.__em.clear()
        return


class Channel(object):
    __slots__ = (b'__weakref__', b'__name', b'__clientStatus', b'__serverStatus', b'__messages', b'__subscriptions', b'__eventsSender')

    def __init__(self, name, eventsSender=None):
        super(Channel, self).__init__()
        self.__name = name
        self.__clientStatus = constants.SubscriptionClientStatus.Unsubscribed
        self.__serverStatus = constants.SubscriptionServerStatus.Unsubscribed
        self.__messages = deque(maxlen=constants.MAX_CHANNEL_HISTORY)
        self.__subscriptions = []
        self.__eventsSender = eventsSender
        return

    @property
    def name(self):
        return self.__name

    @property
    def status(self):
        return SubscriptionStatus(self.__clientStatus, self.__serverStatus)

    @property
    def isSubscribed(self):
        return self.__clientStatus == constants.SubscriptionClientStatus.Subscribed

    @property
    def hasSubscription(self):
        return len(self.__subscriptions) > 0

    @property
    def messages(self):
        return deque(self.__messages)

    @property
    def lastMessage(self):
        if self.__messages:
            return self.__messages[-1]
        else:
            return

    def clear(self):
        self.__clientStatus = constants.SubscriptionClientStatus.Unsubscribed
        self.__clearSubscriptions(reason=constants.SubscriptionCloseReason.Cancel)
        self.__eventsSender = None
        return

    def close(self):
        self.__clientStatus = constants.SubscriptionClientStatus.Unsubscribed
        return

    def subscribe(self, client):
        if self.__clientStatus == constants.SubscriptionClientStatus.Subscribed:
            _logger.warning(b'Client is already subscribed to channel <%s>', self.__name)
            return
        if client.status == websocket.ConnectionStatus.Opened:
            if self.__clientStatus != constants.SubscriptionClientStatus.Subscribing:
                _logger.debug(b'Request to subscribe to channel <%s> is sending', self.__name)
                self.__clientStatus = constants.SubscriptionClientStatus.Subscribing
                client.sendBinary(packer.packCommand(self.__name, constants.SubscriptionCommand.Subscribe))
        else:
            _logger.error(b'Request to subscribe to channel <%s> can not be invoked, connection is not opened', self.__name)
        return

    def unsubscribe(self, client):
        if self.__clientStatus == constants.SubscriptionClientStatus.Unsubscribed:
            _logger.warning(b'Client is already unsubscribed from channel <%s>', self.__name)
            return
        if client.status == websocket.ConnectionStatus.Opened:
            if self.__clientStatus != constants.SubscriptionClientStatus.Unsubscribing:
                _logger.debug(b'Request to unsubscribe from channel <%s> is sending', self.__name)
                self.__clientStatus = constants.SubscriptionClientStatus.Unsubscribing
                client.sendBinary(packer.packCommand(self.__name, constants.SubscriptionCommand.Unsubscribe))
        else:
            self.__clientStatus = constants.SubscriptionClientStatus.Unsubscribed
        return

    def getLastMessage(self, client):
        if self.__clientStatus == constants.SubscriptionClientStatus.Unsubscribed:
            _logger.warning(b'Client is unsubscribed from channel <%s>', self.__name)
            return
        if client.status == websocket.ConnectionStatus.Opened:
            if self.__clientStatus == constants.SubscriptionClientStatus.Subscribed:
                client.sendBinary(packer.packCommand(self.__name, constants.SubscriptionCommand.GetLast))
        return

    def addSubscription(self, subscription):
        if isinstance(subscription, Subscription) and subscription not in self.__subscriptions and subscription.channel == self.__name:
            self.__subscriptions.append(subscription)
            return True
        return False

    def removeSubscription(self, subscription):
        if subscription in self.__subscriptions:
            self.__subscriptions.remove(subscription)
            reason = constants.SubscriptionCloseReason.Request
            if self.__eventsSender is not None:
                self.__eventsSender.onSubscriptionClosed(subscription, reason)
            subscription.onClosed(reason)
            subscription.clear()
            return True
        else:
            return False

    def setStatus(self, status):
        if status == constants.SubscriptionServerStatus.ChannelDeleted:
            _logger.debug(b'Channel <%s> is deleted in subscriptions service', self.__name)
            self.__clientStatus = constants.SubscriptionClientStatus.Unsubscribed
            self.__messages.clear()
            self.__clearSubscriptions(reason=constants.SubscriptionCloseReason.Deleted)
        elif self.__clientStatus == constants.SubscriptionClientStatus.Subscribing:
            if status == constants.SubscriptionServerStatus.Subscribed:
                _logger.debug(b'Request to subscribe to channel <%s> is success', self.__name)
                self.__clientStatus = constants.SubscriptionClientStatus.Subscribed
            else:
                _logger.error(b'Request to subscribe to channel <%s> is failed: %r', self.__name, status)
                self.__clientStatus = constants.SubscriptionClientStatus.Unsubscribed
        elif self.__clientStatus == constants.SubscriptionClientStatus.Unsubscribing:
            if status == constants.SubscriptionServerStatus.Unsubscribed:
                _logger.debug(b'Request to unsubscribe from channel <%s> is success', self.__name)
                self.__clientStatus = constants.SubscriptionClientStatus.Unsubscribed
                self.__messages.clear()
            else:
                _logger.error(b'Request to unsubscribe from channel <%s> is failed: %r', self.__name, status)
                self.__clientStatus = constants.SubscriptionClientStatus.Unsubscribed
                self.__messages.clear()
            self.__clearSubscriptions(reason=constants.SubscriptionCloseReason.Request)
        elif status == constants.SubscriptionServerStatus.CachedMessage:
            _logger.debug(b'Request to get last message from channel <%s> is success', self.__name)
        elif status == constants.SubscriptionServerStatus.NoCachedMessage:
            _logger.debug(b'Channel <%s> doesnt have cached messages', self.__name)
        else:
            _logger.warning(b'Channel response <%s> is not handled: %r, %r', self.__name, self.__clientStatus, status)
        self.__serverStatus = status
        return

    def addMessage(self, message):
        if self.__clientStatus == constants.SubscriptionClientStatus.Subscribed:
            if message.seqid is not None and self.lastMessage and self.lastMessage.seqid > message.seqid:
                return False
            message.data = self.__tryDecompressZip(message.data)
            self.__messages.append(message)
            for subscription in self.__subscriptions:
                subscription.onMessage(message.data)

            if self.__eventsSender is not None:
                self.__eventsSender.onChannelMessage(self.__name, message.data)
            return True
        return False

    @staticmethod
    def __tryDecompressZip(data):
        try:
            result = zlib.decompress(data)
        except zlib.error:
            result = data

        return result

    def __clearSubscriptions(self, reason=constants.SubscriptionCloseReason.Cancel):
        for subscription in self.__subscriptions:
            if self.__eventsSender is not None:
                self.__eventsSender.onSubscriptionClosed(subscription, reason)
            subscription.onClosed(reason)
            subscription.clear()

        if self.__eventsSender is not None:
            self.__eventsSender.onChannelClosed(self.__name, reason)
        del self.__subscriptions[:]
        return


class Subscription(object):
    __slots__ = (b'__channel', b'__em', b'onMessage', b'onClosed')

    def __init__(self, channel):
        super(Subscription, self).__init__()
        self.__channel = channel
        self.__em = Event.EventManager()
        self.onMessage = Event.Event(self.__em)
        self.onClosed = Event.Event(self.__em)
        return

    @property
    def channel(self):
        return self.__channel

    def clear(self):
        self.__channel = b''
        self.__em.clear()
        return


class SubscriptionStatus(object):
    __slots__ = (b'__clientStatus', b'__serverStatus')

    def __init__(self, clientStatus=constants.SubscriptionClientStatus.Unsubscribed, serverStatus=constants.SubscriptionServerStatus.Unsubscribed):
        super(SubscriptionStatus, self).__init__()
        self.__clientStatus = clientStatus
        self.__serverStatus = serverStatus
        return

    def __repr__(self):
        return (b'{}(client={}, server={})').format(self.__class__.__name__, self.__clientStatus, self.__serverStatus)

    def __nonzero__(self):
        return self.isSubscribed

    @property
    def isSubscribed(self):
        return self.__clientStatus == constants.SubscriptionClientStatus.Subscribed

    @property
    def client(self):
        return self.__clientStatus

    @property
    def server(self):
        return self.__serverStatus
