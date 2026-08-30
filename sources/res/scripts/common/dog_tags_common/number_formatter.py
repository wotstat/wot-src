import re
from collections import defaultdict
from math import floor
import typing
from dog_tags_common.config.common import ComponentNumberType

def formatComponentValue(locale, value, numberType, specialReplacements=True):
    if numberType == ComponentNumberType.PERCENTAGE:
        raw_value = formatPercentage(value)
    else:
        raw_value = formatNumber(locale, value, regionalPrefix=specialReplacements)
    if not specialReplacements:
        return raw_value
    return (b'').join(_replacements.get(c, c) for c in raw_value)


def formatPercentage(value):
    rounded = customRound(value, 2)
    formatted = (b'{:.2f}').format(rounded)
    formattedNoZeroes = _TRAILING_ZEROES_RE.sub(b'', formatted)
    return (b'{}%').format(formattedNoZeroes)


def formatNumber(locale, value, regionalPrefix=True):
    suffix = (b'{}_').format(locale) if regionalPrefix else b''
    suffix = suffix + b'{}'
    if regionalPrefix:
        suffix = (b'[{}]').format(suffix)
    if value < 100000:
        formatted = (b'{:,.2f}').format(customRound(value, 2))
        formatted = _TRAILING_ZEROES_RE.sub(b'', formatted)
    elif value < 999500:
        formatted = (b'{} {}').format(_formatThousands(value), suffix.format(b'k'))
    elif value < 1000000:
        formatted = (b'{} {}').format(_formatThousands(value, floor), suffix.format(b'k'))
    else:
        formatted = (b'{} {}').format(_formatMillions(locale, value), suffix.format(b'm'))
    return formatted.replace(b',', b' ')


def customRound(value, ndecimals=0):
    fact = 10 ** (ndecimals + 1)
    norm_value = float(value) * fact
    last = norm_value % 10
    if last >= 5:
        norm_value += 10
    return (norm_value - last) / fact


def _formatThousands(value, roundStrategy=customRound):
    shortValue = float(value) / 1000
    return (b'{:,d}').format(int(roundStrategy(shortValue)))


def _formatMillions(locale, value):
    shortValue = float(value) / _millionDivider[locale]
    return (b'{:,.1f}').format(customRound(shortValue, 1)).replace(b'.0', b'')


_TRAILING_ZEROES_RE = re.compile(b'\\.?0+$')
_millionDivider = defaultdict((lambda : 1000000))
for language in [b'ja', b'zh_cn', b'ko']:
    _millionDivider[language] = 10000

_replacements = {b'%': b'[percentage]', 
   b'.': b'[dot]'}
