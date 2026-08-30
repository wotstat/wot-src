from __future__ import absolute_import
import logging
from enum import Enum
_logger = logging.getLogger(__name__)
UNAVAILABLE_REWARD_ERROR = b'UNAVAILABLE_REWARD_ERROR'
CHANNEL_NAME_PREFIX = b'suv_'
DEFAULT_SEASON_NUMBER = 0

class PurchaseMode(Enum):
    ONE_SERIAL_PRODUCT = b'ONE_SERIAL_PRODUCT'
    SEQUENTIAL_PRODUCT = b'SEQUENTIAL_PRODUCT'
    TWO_PARALLEL_PRODUCTS = b'TWO_PARALLEL_PRODUCTS'


class ResourceType(Enum):
    BLUEPRINTS = b'blueprints'
    CURRENCY = b'currency'

    @classmethod
    def getMember(cls, value):
        if value in cls._value2member_map_:
            return cls(value)
        else:
            _logger.error(b'%s does not exist in ResourceType values', value)
            return
