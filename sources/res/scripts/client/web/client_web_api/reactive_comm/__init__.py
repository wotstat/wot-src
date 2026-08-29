from helpers import dependency
from skeletons.gui.game_control import IReactiveCommunicationService
from web.client_web_api.api import C2WHandler, c2w

class ReactiveCommunicationEventHandler(C2WHandler):
    __service = dependency.descriptor(IReactiveCommunicationService)

    @property
    def preventIdentical(self):
        return False

    def init(self):
        super(ReactiveCommunicationEventHandler, self).init()
        self.__service.onChannelMessage += self.__onChannelMessage
        self.__service.onSubscriptionClosed += self.__onSubscriptionClosed
        return

    def fini(self):
        self.__service.onChannelMessage -= self.__onChannelMessage
        self.__service.onSubscriptionClosed -= self.__onSubscriptionClosed
        super(ReactiveCommunicationEventHandler, self).fini()
        return

    @c2w(name=b'on_reactive_communication_channel_message')
    def __onChannelMessage(self, name, message):
        return {b'channel_name': name, 
           b'data': message}

    @c2w(name=b'on_reactive_communication_subscription_closed')
    def __onSubscriptionClosed(self, subscription, reason):
        return {b'channel_name': (subscription.channel), 
           b'subscription_id': (id(subscription)), 
           b'reason': (reason.value)}
