import logging
from enum import IntEnum, Enum
_logger = logging.getLogger(__name__)
RESOURCE_WELL_PDATA_KEY = b'resourceWell'
UNAVAILABLE_REWARD_ERROR = b'UNAVAILABLE_REWARD_ERROR'
CHANNEL_NAME_PREFIX = b'suv_'

class ProgressionState(IntEnum):
    ACTIVE = 1
    NO_PROGRESS = 2
    NO_VEHICLES = 3
    FORBIDDEN = 4
    BEFORE_EVENT = 5


class ResourceType(Enum):
    BLUEPRINTS = b'blueprints'
    CURRENCY = b'currency'
    PREMIUMS = b'premiums'

    @classmethod
    def getMember(cls, value):
        if value in cls._value2member_map_:
            return cls(value)
        else:
            _logger.error(b'%s does not exist in ResourceType values', value)
            return


class ServerResourceType(Enum):
    BLUEPRINTS = b'blueprints'
    CURRENCY = b'currency'
    ENTITLEMENTS = b'entitlement'
