from __future__ import absolute_import
import logging, re
from backports.functools_lru_cache import lru_cache
import typing
from exchange.personal_discounts_constants import EXCHANGE_RATE_GOLD_NAME, ExchangeRateCoefficientType, ExchangeDiscountInfo, ExchangeDiscountType, ExchangeRateShowFormat, ExchangeRateDiscountToken, EXCHANGE_RATE_FREE_XP_NAME, DIGITAL_TEMPLATE
from exchange.personal_discounts_helper import isExchangeRateDiscountAvailable
from exchange.personal_discounts_validator import isDiscountValuesCorrect
from math_common import decimal_round
if typing.TYPE_CHECKING:
    from typing import Tuple, Dict, Union, List, Optional, Any
_logger = logging.getLogger(__name__)

def convertTokensToExchangeDiscounts(tokens, defCourse, currentTime):
    discounts = []
    defGoldRateVal, defResRateVal = (defCourse[1], defCourse[0]) if isinstance(defCourse, tuple) else (1, defCourse)
    for token, tokenInfo in tokens.items():
        discount = _getDiscountFromTokensInfo(token, tokenInfo, defGoldRateVal, defResRateVal, currentTime)
        if discount is not None:
            discounts.append(discount)

    return discounts or None


def _getDiscountFromTokensInfo(tokenName, tokenInfo, defaultGoldRateValue, defaultResourceRateValue, currentTime):
    tokenExpirationTime, tokenAmount = tokenInfo
    if not (tokenAmount > 0 and tokenExpirationTime > currentTime):
        return
    else:
        parsedToken = _parseToken(tokenName)
        if parsedToken is None:
            _logger.warning(b'Token is invalid - %s', tokenName)
            return
        parsedToken.update({b'leftAmount': tokenAmount, 
           b'expiryTime': tokenExpirationTime, 
           b'tokenName': tokenName})
        _calculateDiscountRate(parsedToken, defaultGoldRateValue, defaultResourceRateValue)
        updateDiscountLimitResult = _updateDiscountLimit(parsedToken)
        if not updateDiscountLimitResult:
            _logger.warning(b'Discount token limit is incorrect, limit for xp translation must be divided to the exchange rate without remainder')
            return
        discount = _createDiscountInfoFromDict(parsedToken)
        isValuesCorrect = isDiscountValuesCorrect(discount, defaultGoldRateValue, defaultResourceRateValue)
        if not isValuesCorrect:
            _logger.warning(b'Discount token values are incorrect, tokenName=%s, expiration=%d, leftAmount=%d', tokenName, tokenExpirationTime, tokenAmount)
        if isValuesCorrect and isExchangeRateDiscountAvailable(discount, currentTime):
            return discount
        return


@lru_cache()
def __getTokenPattern(isLimited=False):

    def getSettingOptions(setting):
        return (b'|').join((b'{}').format(formatName.value) for formatName in setting)

    tokenKeyParamsTemplate = b'{name}:(?P<{name}>{value})'
    tokenKeyValueTemplate = b'{name}:(?P<{name}>{value})'
    exchangeType = (b'(?P<exchangeType>{}|{})').format(EXCHANGE_RATE_GOLD_NAME, EXCHANGE_RATE_FREE_XP_NAME)
    limitTypePattern = tokenKeyParamsTemplate.format(name=ExchangeRateDiscountToken.LIMIT_TYPE.value, value=getSettingOptions(ExchangeDiscountType))
    showFormatPattern = tokenKeyParamsTemplate.format(name=ExchangeRateDiscountToken.SHOW_FORMAT.value, value=getSettingOptions(ExchangeRateShowFormat))
    rateTypePattern = tokenKeyParamsTemplate.format(name=ExchangeRateDiscountToken.RATE_TYPE.value, value=getSettingOptions(ExchangeRateCoefficientType))
    rateChangerPattern = tokenKeyValueTemplate.format(name=ExchangeRateDiscountToken.RATE_VALUE.value, value=DIGITAL_TEMPLATE)
    formatSequence = [
     exchangeType, 
     limitTypePattern, 
     showFormatPattern, 
     rateTypePattern, 
     rateChangerPattern]
    full_pattern = (b':').join([b'{}'] * len(formatSequence)) + b':id:[0-9]+$'
    full_pattern = full_pattern.format(*formatSequence)
    return re.compile(full_pattern)


def _parseToken(tokenName):
    isLimited = ExchangeDiscountType.UNLIMITED.value not in tokenName
    pattern = __getTokenPattern(isLimited)
    matches = pattern.search(tokenName)
    if matches is None:
        return
    else:
        placeholder_values = {}
        params = [b'exchangeType',
         ExchangeRateDiscountToken.LIMIT_TYPE.value,
         ExchangeRateDiscountToken.SHOW_FORMAT.value,
         ExchangeRateDiscountToken.RATE_TYPE.value,
         ExchangeRateDiscountToken.RATE_VALUE.value]
        for param in params:
            value = matches.group(param)
            if param == ExchangeRateDiscountToken.RATE_VALUE.value and value:
                value = value.replace(b'_', b'.')
            placeholder_values[param] = value

        return placeholder_values


def _calculateDiscountRate(parsedToken, defaultGoldRateValue, defaultResourceRateValue):
    rateType = parsedToken.get(ExchangeRateDiscountToken.RATE_TYPE.value, b'')
    newExchangeCourse = float(parsedToken.get(ExchangeRateDiscountToken.RATE_VALUE.value, 0))
    newRate = decimal_round(defaultResourceRateValue + newExchangeCourse if rateType == ExchangeRateCoefficientType.AMOUNT.value else defaultResourceRateValue * newExchangeCourse)
    parsedToken[b'goldRateValue'] = defaultGoldRateValue
    parsedToken[b'resourceRateValue'] = newRate
    return


def _updateDiscountLimit(tokenInfo):
    exchangeType = tokenInfo.get(b'exchangeType', b'')
    tokenType = tokenInfo.get(ExchangeRateDiscountToken.LIMIT_TYPE.value, b'')
    if ExchangeDiscountType(tokenType) == ExchangeDiscountType.UNLIMITED or exchangeType == EXCHANGE_RATE_GOLD_NAME:
        return True
    amount = tokenInfo.get(b'leftAmount', 0)
    rate = int(tokenInfo[b'resourceRateValue'])
    if amount % rate != 0 or not amount:
        return False
    tokenInfo[b'leftAmount'] = amount // rate
    return True


def _createDiscountInfoFromDict(tokenInfo):
    return ExchangeDiscountInfo(isPersonal=True, exchangeType=tokenInfo.get(b'exchangeType', EXCHANGE_RATE_GOLD_NAME), discountType=ExchangeDiscountType(tokenInfo.get(ExchangeRateDiscountToken.LIMIT_TYPE.value)), showFormat=ExchangeRateShowFormat(tokenInfo.get(ExchangeRateDiscountToken.SHOW_FORMAT.value)), goldRateValue=tokenInfo.get(b'goldRateValue', 1), resourceRateValue=tokenInfo.get(b'resourceRateValue', 1), amountOfDiscount=tokenInfo.get(b'leftAmount', 0), discountLifetime=tokenInfo.get(b'expiryTime', 0), tokenName=tokenInfo.get(b'tokenName', None))
