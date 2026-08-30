__all__ = [
 0, 
 1, 
 2, 
 3, 
 4, 
 5, 
 6, 
 7, 
 8, 
 9, 
 10, 
 11, 
 12]
import os, re, time, base64, random, socket, urllib, warnings
from email._parseaddr import quote
from email._parseaddr import AddressList as _AddressList
from email._parseaddr import mktime_tz
from email._parseaddr import parsedate as _parsedate
from email._parseaddr import parsedate_tz as _parsedate_tz
from quopri import decodestring as _qdecode
from email.encoders import _bencode, _qencode
COMMASPACE = b', '
EMPTYSTRING = b''
UEMPTYSTRING = u''
CRLF = b'\r\n'
TICK = b"'"
specialsre = re.compile(b'[][\\\\()<>@,:;".]')
escapesre = re.compile(b'[][\\\\()"]')

def _identity(s):
    return s


def _bdecode(s):
    if not s:
        return s
    return base64.decodestring(s)


def fix_eols(s):
    s = re.sub(b'(?<!\\r)\\n', CRLF, s)
    s = re.sub(b'\\r(?!\\n)', CRLF, s)
    return s


def formataddr(pair):
    name, address = pair
    if name:
        quotes = b''
        if specialsre.search(name):
            quotes = b'"'
        name = escapesre.sub(b'\\\\\\g<0>', name)
        return b'%s%s%s <%s>' % (quotes, name, quotes, address)
    return address


def getaddresses(fieldvalues):
    all = COMMASPACE.join(fieldvalues)
    a = _AddressList(all)
    return a.addresslist


ecre = re.compile(b'\n  =\\?                   # literal =?\n  (?P<charset>[^?]*?)   # non-greedy up to the next ? is the charset\n  \\?                    # literal ?\n  (?P<encoding>[qb])    # either a "q" or a "b", case insensitive\n  \\?                    # literal ?\n  (?P<atom>.*?)         # non-greedy up to the next ?= is the atom\n  \\?=                   # literal ?=\n  ', re.VERBOSE | re.IGNORECASE)

def formatdate(timeval=None, localtime=False, usegmt=False):
    if timeval is None:
        timeval = time.time()
    if localtime:
        now = time.localtime(timeval)
        if time.daylight and now[-1]:
            offset = time.altzone
        else:
            offset = time.timezone
        hours, minutes = divmod(abs(offset), 3600)
        if offset > 0:
            sign = b'-'
        else:
            sign = b'+'
        zone = b'%s%02d%02d' % (sign, hours, minutes // 60)
    else:
        now = time.gmtime(timeval)
        if usegmt:
            zone = b'GMT'
        else:
            zone = b'-0000'
    return b'%s, %02d %s %04d %02d:%02d:%02d %s' % (
     [
      11, 12, 13, 14, 15, 16, 17][now[6]],
     now[2],
     [
      20, 21, 22, 23, 24, 25, 
      26, 27, 28, 29, 30, 
      31][now[1] - 1],
     now[0], now[3], now[4], now[5],
     zone)


def make_msgid(idstring=None):
    timeval = int(time.time() * 100)
    pid = os.getpid()
    randint = random.getrandbits(64)
    if idstring is None:
        idstring = b''
    else:
        idstring = b'.' + idstring
    idhost = socket.getfqdn()
    msgid = b'<%d.%d.%d%s@%s>' % (timeval, pid, randint, idstring, idhost)
    return msgid


def parsedate(data):
    if not data:
        return None
    else:
        return _parsedate(data)


def parsedate_tz(data):
    if not data:
        return None
    else:
        return _parsedate_tz(data)


def parseaddr(addr):
    addrs = _AddressList(addr).addresslist
    if not addrs:
        return (b'', b'')
    return addrs[0]


def unquote(str):
    if len(str) > 1:
        if str.startswith(b'"') and str.endswith(b'"'):
            return str[1:-1].replace(b'\\\\', b'\\').replace(b'\\"', b'"')
        if str.startswith(b'<') and str.endswith(b'>'):
            return str[1:-1]
    return str


def decode_rfc2231(s):
    parts = s.split(TICK, 2)
    if len(parts) <= 2:
        return (None, None, s)
    else:
        return parts


def encode_rfc2231(s, charset=None, language=None):
    import urllib
    s = urllib.quote(s, safe=b'')
    if charset is None and language is None:
        return s
    else:
        if language is None:
            language = b''
        return b"%s'%s'%s" % (charset, language, s)


rfc2231_continuation = re.compile(b'^(?P<name>\\w+)\\*((?P<num>[0-9]+)\\*?)?$')

def decode_params(params):
    params = params[:]
    new_params = []
    rfc2231_params = {}
    name, value = params.pop(0)
    new_params.append((name, value))
    while params:
        name, value = params.pop(0)
        if name.endswith(b'*'):
            encoded = True
        else:
            encoded = False
        value = unquote(value)
        mo = rfc2231_continuation.match(name)
        if mo:
            name, num = mo.group(b'name', b'num')
            if num is not None:
                num = int(num)
            rfc2231_params.setdefault(name, []).append((num, value, encoded))
        else:
            new_params.append((name, b'"%s"' % quote(value)))

    if rfc2231_params:
        for name, continuations in rfc2231_params.items():
            value = []
            extended = False
            continuations.sort()
            for num, s, encoded in continuations:
                if encoded:
                    s = urllib.unquote(s)
                    extended = True
                value.append(s)

            value = quote(EMPTYSTRING.join(value))
            if extended:
                charset, language, value = decode_rfc2231(value)
                new_params.append((name, (charset, language, b'"%s"' % value)))
            else:
                new_params.append((name, b'"%s"' % value))

    return new_params


def collapse_rfc2231_value(value, errors=b'replace', fallback_charset=b'us-ascii'):
    if isinstance(value, tuple):
        rawval = unquote(value[2])
        charset = value[0] or b'us-ascii'
        try:
            return unicode(rawval, charset, errors)
        except LookupError:
            return unicode(rawval, fallback_charset, errors)

    else:
        return unquote(value)
    return
