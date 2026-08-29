import adisp, th_async
from gui.game_control.reactive_comm import Subscription, SubscriptionClientStatus, SubscriptionServerStatus
from helpers import dependency
from skeletons.gui.game_control import IReactiveCommunicationService
from web.web_client_api import w2c, w2capi, Field, W2CSchema

class _SubscriptionSchema(W2CSchema):
    channel_name = Field(required=True, type=basestring)
    get_last_message = Field(required=False, type=bool)


class _UnsubscriptionSchema(W2CSchema):
    channel_name = Field(required=True, type=basestring)


@w2capi(name=b'reactive_communication_service', key=b'action', finiHandlerName=b'_finiSubscriptionsHandler')
class ReactiveCommunicationWebApi(object):
    __service = dependency.descriptor(IReactiveCommunicationService)

    def __init__(self):
        super(ReactiveCommunicationWebApi, self).__init__()
        self.__subscriptions = {}
        return

    @w2c(W2CSchema, name=b'is_channel_subscription_available')
    def isSubscriptionAvailable(self, _):
        return self.__service.isChannelSubscriptionAvailable

    @w2c(_SubscriptionSchema, b'subscribe_to_channel')
    def subscribe(self, cmd):
        name = cmd.channel_name.encode(b'utf-8')
        if name not in self.__subscriptions:
            self.__subscriptions[name] = subscription = Subscription(name)
            self.__service.onSubscriptionClosed += self.__onSubscriptionClosed
            status = yield self.__doSubscribe(subscription)
            if not status:
                self.__subscriptions.pop(name, None)
            elif cmd.get_last_message:
                self.__getLastMessage(subscription)
            yield {b'channel_name': name, 
               b'subscription_id': (id(subscription)), 
               b'status': {b'client': (status.client.value), 
                           b'server': (status.server.value)}}
        elif cmd.get_last_message:
            self.__getLastMessage(self.__subscriptions[name])
        yield {b'channel_name': name, 
           b'status': {b'client': (SubscriptionClientStatus.AlreadySubscribed.value), 
                       b'server': (SubscriptionServerStatus.Subscribed.value)}}
        return

    @w2c(_UnsubscriptionSchema, b'unsubscribe_from_channel')
    def unsubscribe(self, cmd):
        name = cmd.channel_name.encode(b'utf-8')
        success = False
        subscriptionID = 0
        if name in self.__subscriptions:
            subscription = self.__subscriptions.pop(name)
            subscriptionID = id(subscription)
            success = self.__service.unsubscribeFromChannel(subscription)
        return {b'channel_name': name, 
           b'subscription_id': subscriptionID, 
           b'success': success}

    def _finiSubscriptionsHandler(self):
        self.__service.onSubscriptionClosed -= self.__onSubscriptionClosed
        for subscription in self.__subscriptions.values():
            self.__service.unsubscribeFromChannel(subscription)

        self.__subscriptions.clear()
        return

    @adisp.adisp_async
    @th_async.th_async
    def __doSubscribe(self, subscription, callback):
        status = yield th_async.th_await(self.__service.subscribeToChannel(subscription))
        callback(status)
        return

    def __getLastMessage(self, subscription):
        return self.__service.getLastMessageFromChannel(subscription)

    def __onSubscriptionClosed(self, subscription, _):
        self.__subscriptions.pop(subscription, None)
        return
