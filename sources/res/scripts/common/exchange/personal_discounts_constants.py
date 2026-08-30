from __future__ import absolute_import
from collections import namedtuple
from enum import Enum
EXCHANGE_RATE_GOLD_NAME = b'gold_exchange'
EXCHANGE_RATE_FREE_XP_NAME = b'experience_translation'
EXCHANGE_RATE_TYPES = (EXCHANGE_RATE_GOLD_NAME, EXCHANGE_RATE_FREE_XP_NAME)
MAX_DISCOUNT_VALUE = 2147483647L
MAX_TIMESTAMP_VALUE = 9007199254740991L
MAX_DISCOUNT_COEFFICIENT = 10
DIGITAL_TEMPLATE = b'([1-9]\\d*((_|\\.)\\d+)?)'
EXCHANGE_NAME_TO_GAME_PARAM_NAME = {EXCHANGE_RATE_GOLD_NAME: b'exchangeRate', 
   EXCHANGE_RATE_FREE_XP_NAME: b'freeXPConversion'}
ExchangeRate = namedtuple(b'ExchangeRate', [b'goldRateValue', b'resourceRateValue'])

class ExchangeDiscountType(Enum):
    LIMITED = b'limited'
    UNLIMITED = b'unlimited'


class ExchangeRateShowFormat(Enum):
    COEFFICIENT = b'coefficient'
    INTEGER = b'integer'
    TEMPORARY = b'temporary'
    LIMITED = b'limited'


class ExchangeRateCoefficientType(Enum):
    AMOUNT = b'increase'
    MULTIPLY = b'mul'


ExchangeDiscountInfo = namedtuple(b'ExchangeDiscountInfo', (b'isPersonal', b'exchangeType', b'discountType', b'goldRateValue', b'resourceRateValue', b'showFormat', b'amountOfDiscount', b'discountLifetime', b'tokenName'))

class ExchangeRateDiscountToken(Enum):
    LIMIT_TYPE = b'limit_type'
    SHOW_FORMAT = b'show_format'
    RATE_TYPE = b'rate_type'
    RATE_VALUE = b'change_on'
