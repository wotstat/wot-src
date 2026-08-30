import re
from debug_utils import LOG_CURRENT_EXCEPTION, LOG_WARNING
from gui.impl import backport
from gui.notify_center import notify_center_helpers
from helpers import i18n
_RE_FLAGS = re.M | re.U

class _TagFormatter(object):
    __slots__ = (b'_compiled',)

    def __init__(self, name):
        super(_TagFormatter, self).__init__()
        self._compiled = self._makePattern(name)
        return

    def format(self, text):
        try:
            results = re.findall(self._compiled, text)
        except re.error:
            return text

        for tag, formatted in self._prepare(results):
            text = text.replace(tag, formatted)

        return text

    def _prepare(self, results):
        raise NotImplementedError
        return

    def _makePattern(self, name):
        raise NotImplementedError
        return


class _ValueFormatter(_TagFormatter):

    def _prepare(self, results):
        for found in results:
            if len(found) != 2:
                continue
            tag, value = found
            if not value:
                LOG_WARNING(b'Value of tag is empty. It is ignored', tag)
                continue
            try:
                formatted = self._getValue(value)
            except (TypeError, ValueError):
                formatted = value
                LOG_CURRENT_EXCEPTION()

            yield (tag, formatted)

        return

    def _getValue(self, value):
        raise NotImplementedError
        return

    def _makePattern(self, name):
        return re.compile((b'(<{0}.*?>(.+?)</{0}>)').format(name), _RE_FLAGS)


class _GoldFormatter(_ValueFormatter):

    def __init__(self):
        super(_GoldFormatter, self).__init__(b'gold')
        return

    def _getValue(self, value):
        return backport.getGoldFormat(long(value))


class _IntegerFormatter(_ValueFormatter):

    def __init__(self):
        super(_IntegerFormatter, self).__init__(b'integer')
        return

    def _getValue(self, value):
        return backport.getIntegralFormat(long(value))


class _FloatFormatter(_ValueFormatter):

    def __init__(self):
        super(_FloatFormatter, self).__init__(b'float')
        return

    def _getValue(self, value):
        return backport.getFractionalFormat(float(value))


class _NiceNumberFormatter(_ValueFormatter):

    def __init__(self):
        super(_NiceNumberFormatter, self).__init__(b'nicenumber')
        return

    def _getValue(self, value):
        return backport.getNiceNumberFormat(float(value))


class _TimeFormatter(_ValueFormatter):

    def _getLocalTime(self, value):
        return float(value)


class _ShortTimeFormatter(_TimeFormatter):

    def __init__(self):
        super(_ShortTimeFormatter, self).__init__(b'shorttime')
        return

    def _getValue(self, value):
        return backport.getShortTimeFormat(self._getLocalTime(value))


class _LongTimeFormatter(_TimeFormatter):

    def __init__(self):
        super(_LongTimeFormatter, self).__init__(b'longtime')
        return

    def _getValue(self, value):
        return backport.getLongTimeFormat(self._getLocalTime(value))


class _ShortDateFormatter(_TimeFormatter):

    def __init__(self):
        super(_ShortDateFormatter, self).__init__(b'shortdate')
        return

    def _getValue(self, value):
        return backport.getShortDateFormat(self._getLocalTime(value))


class _LongDateFormatter(_TimeFormatter):

    def __init__(self):
        super(_LongDateFormatter, self).__init__(b'longdate')
        return

    def _getValue(self, value):
        return backport.getLongDateFormat(self._getLocalTime(value))


class _DateTimeFormatter(_TimeFormatter):

    def __init__(self):
        super(_DateTimeFormatter, self).__init__(b'datetime')
        return

    def _getValue(self, value):
        value = self._getLocalTime(value)
        return (u'{0:>s} {1:>s}').format(backport.getShortDateFormat(value), backport.getLongTimeFormat(value))


_LINK_HTML = b'<a href="event:{0}">{1}</a>'

class _LinkFormatter(_TagFormatter):

    def __init__(self):
        super(_LinkFormatter, self).__init__(b'link')
        return

    def _prepare(self, results):
        for found in results:
            if len(found) != 4:
                continue
            tag, _, actions, label = found
            label = label.strip()
            if not label:
                LOG_WARNING(b'Label is empty. It is ignored', tag)
                continue
            if not actions:
                LOG_WARNING(b'Actions are empty. It is removed', tag)
                yield (tag, b'')
            else:
                yield (
                 tag, _LINK_HTML.format(actions, label))

        return

    def _makePattern(self, name):
        return re.compile((b'(<{0} actions=(["|\\\']+?)(.+?)\\2>(.+?)</{0}>)').format(name), _RE_FLAGS)


class _LocalizationFormatter(_TagFormatter):

    def __init__(self):
        super(_LocalizationFormatter, self).__init__(b'')
        return

    def _prepare(self, results):
        for found in results:
            if len(found) != 2:
                continue
            tag, value = found
            if not value:
                LOG_WARNING(b'Value of tag is empty. It is ignored', tag)
                continue
            yield (tag, i18n.makeString(value))

        return

    def _makePattern(self, name):
        return re.compile(b'(\\_\\(([^)]+)\\))', _RE_FLAGS)


class _SpaFormater(_ValueFormatter):

    def __init__(self):
        super(_SpaFormater, self).__init__(b'spa')
        return

    def _getValue(self, value):
        return notify_center_helpers.spa2Nickname(int(value))


_formatters = (
 _GoldFormatter(),
 _IntegerFormatter(),
 _FloatFormatter(),
 _NiceNumberFormatter(),
 _ShortTimeFormatter(),
 _LongTimeFormatter(),
 _ShortDateFormatter(),
 _LongDateFormatter(),
 _DateTimeFormatter(),
 _LinkFormatter(),
 _LocalizationFormatter(),
 _SpaFormater())

def formatText(text):
    for formatter in _formatters:
        text = formatter.format(text)

    return text
