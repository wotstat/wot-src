from enum import Enum, unique
MAX_CHANNEL_HISTORY = 10
CHANNEL_UNSUBSCRIPTION_DELAY = 60

@unique
class SubscriptionCommand(Enum):
    Subscribe = b'subscribe'
    Unsubscribe = b'unsubscribe'
    GetLast = b'get_last'


@unique
class SubscriptionServerStatus(Enum):
    Subscribed = b'subscribed'
    NotExists = b'not_exists'
    ChannelsLimit = b'channels_limit'
    Unsubscribed = b'unsubscribed'
    NotSubscribed = b'not_subscribed'
    ChannelDeleted = b'channel_deleted'
    UnknownCommand = b'unknown_command'
    NameNotAllowed = b'name_not_allowed'
    CachedMessage = b'cached_message'
    NoCachedMessage = b'no_cached_message'

    @classmethod
    def fromString(cls, value):
        if value in [item.value for item in cls]:
            return cls(value)
        return cls.UnknownCommand


@unique
class SubscriptionClientStatus(Enum):
    NotExists = b'not_exists'
    Unsubscribed = b'unsubscribed'
    Subscribing = b'subscribing'
    Subscribed = b'subscribed'
    Unsubscribing = b'unsubscribing'
    Disabled = b'disabled'
    InvalidObject = b'invalid_object'
    NameNotAllowed = b'name_not_allowed'
    AlreadySubscribed = b'already_subscribed'


@unique
class SubscriptionCloseReason(Enum):
    Request = b'request'
    Cancel = b'cancel'
    Deleted = b'deleted'
