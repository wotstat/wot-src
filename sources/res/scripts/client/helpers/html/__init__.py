import re
from debug_utils import LOG_CURRENT_EXCEPTION
from helpers import i18n
_getText_re = re.compile(b'\\_\\(([^)]+)\\)', re.U | re.M)

def _search(match):
    if match.group(1):
        return i18n.makeString(match.group(1))
    return b''


def escape(text):
    return text.replace(b'&', b'&amp;').replace(b'<', b'&lt;').replace(b'>', b'&gt;').replace(b'"', b'&quot;').replace(b"'", b'&apos;')


def translation(text):
    result = text
    try:
        result = _getText_re.sub(_search, text)
    except re.error:
        LOG_CURRENT_EXCEPTION()

    return result
