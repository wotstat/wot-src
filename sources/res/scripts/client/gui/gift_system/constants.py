from enum import unique, Enum, IntEnum
DEV_STAMP_CODE = b'giftSystem_1_devStamp'
MAX_CACHED_PLAYERS = 5000

@unique
class GifterResponseState(Enum):
    WEB_FAILURE = b'webFailure'
    WEB_SUCCESS = b'webSuccess'
    REQUESTS_DISABLED = b'requestsDisabled'
    CLIENTGW_NOT_AVAILABLE = b'clientgwNotAvailable'
    REQUEST_IN_PROGRESS = b'requestInProgress'
    CENTER_DISCONNECTED = b'centerDisconnected'
    GIFT_SYSTEM_LIMIT_REACHED = b'giftSystemLimitReached'


@unique
class GiftMessageType(IntEnum):
    INCOME = 0
    OUTCOME = 1
    HISTORY = 2
    LIMITS = 4


@unique
class HubUpdateReason(IntEnum):
    HISTORY = 0
    SETTINGS = 1
    WEB_STATE = 2
    INCOME_GIFT = 3
    OUTCOME_GIFT = 4
    KEEPER_CLEAR = 5
    STAMPER_UPDATE = 6
    WAIT_RESPONSE_RECEIVED = 7
