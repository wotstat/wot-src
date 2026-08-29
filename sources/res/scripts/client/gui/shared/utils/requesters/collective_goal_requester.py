import logging, typing
from th_async import th_async, th_await
from Event import Event
from gui.game_control.reactive_comm import Subscription
from helpers import dependency
from skeletons.gui.game_control import IReactiveCommunicationService
_logger = logging.getLogger(__name__)

class CollectiveGoalRequester(object):
    __slots__ = (b'onUpdated', b'__subscription', b'__message')
    __reactiveCommunication = dependency.descriptor(IReactiveCommunicationService)

    def __init__(self):
        super(CollectiveGoalRequester, self).__init__()
        self.onUpdated = Event()
        self.__subscription = None
        self.__message = None
        return

    @th_async
    def start(self, channelName):
        _logger.debug(b'Trying to subscribe channel: <%s>', channelName)
        if self.__subscription is not None:
            _logger.error(b'Requester is already subscribed to channel: <%s>', channelName)
            return
        else:
            if not self.__reactiveCommunication.isChannelSubscriptionAvailable:
                _logger.error(b'Channel subscription is unavailable! Please check reactive communication settings')
                return
            self.__message = None
            self.__subscription = Subscription(channelName)
            status = yield th_await(self.__reactiveCommunication.subscribeToChannel(self.__subscription))
            _logger.debug(b'Subscription status for channel <%s>: %s', channelName, status)
            if status:
                self.__subscription.onClosed += self.__onClosed
                self.__subscription.onMessage += self.__onMessage
                _logger.debug(b'Sending get_last request for channel <%s>', channelName)
                self.__reactiveCommunication.getLastMessageFromChannel(self.__subscription)
            else:
                self.__subscription = None
            return

    def stop(self):
        if self.__subscription is not None:
            _logger.debug(b'Trying to unsubscribe channel: <%s>', self.__subscription.channel)
            self.__subscription.onClosed -= self.__onClosed
            self.__subscription.onMessage -= self.__onMessage
            self.__reactiveCommunication.unsubscribeFromChannel(self.__subscription)
            self.__subscription = None
        return

    def clear(self):
        self.stop()
        self.onUpdated.clear()
        self.__message = None
        return

    @property
    def isActive(self):
        return self.__subscription is not None

    def getMessage(self):
        return self.__message

    def __onMessage(self, message):
        _logger.debug(b'Message: %s', message)
        if message:
            self.__message = message
            self.onUpdated()
        return

    def __onClosed(self, reason):
        _logger.debug(b'Subscription is closed with reason %s', reason)
        self.stop()
        return
