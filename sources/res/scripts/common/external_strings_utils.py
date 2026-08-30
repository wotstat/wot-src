from __future__ import absolute_import
import re, unicodedata
from builtins import chr
from future.utils import lrange
from past.builtins import unicode, xrange
from debug_utils import LOG_CURRENT_EXCEPTION
from constants import CREDENTIALS_RESTRICTION, CREDENTIALS_RESTRICTION_SET
from soft_exception import SoftException
from struct_helpers import unpackByte
_MAX_NORMALIZED_NAME_BYTES = 96

class TextRestrictionsBasic(object):
    __slots__ = (b'ACCOUNT_NAME_RE', b'ACCOUNT_NAME_MIN_LENGTH', b'ACCOUNT_NAME_MAX_LENGTH', b'ACCOUNT_NAME_MIN_LENGTH_REG', b'LOGIN_NAME_RE', b'LOGIN_NAME_MIN_LENGTH', b'LOGIN_NAME_MAX_LENGTH', b'UPPERCASE_CLAN_ABBREV', b'REQUIRE_NORMALIZED_CLAN_ABBREV', b'CLAN_ABBREV_RE', b'CLAN_NAME_MAX_LENGTH', b'CLAN_ABBREV_MAX_LENGTH', b'CLAN_DESCR_MAX_LENGTH', b'CLAN_MOTTO_MAX_LENGTH')

    def __init__(self):
        self.ACCOUNT_NAME_RE = re.compile(b'^[a-zA-Z0-9_]+$')
        self.ACCOUNT_NAME_MIN_LENGTH = 2
        self.ACCOUNT_NAME_MAX_LENGTH = 24
        self.ACCOUNT_NAME_MIN_LENGTH_REG = 3
        self.LOGIN_NAME_RE = re.compile(b'^[a-z0-9_-]+(\\.[a-z0-9_-]+)*@[a-z0-9-]+(\\.[a-z0-9-]+)*\\.([a-z]{2,4})$')
        self.LOGIN_NAME_MIN_LENGTH = 1
        self.LOGIN_NAME_MAX_LENGTH = 255
        self.UPPERCASE_CLAN_ABBREV = True
        self.REQUIRE_NORMALIZED_CLAN_ABBREV = True
        self.CLAN_ABBREV_RE = re.compile(b'^[A-Z0-9_\\-]+$')
        self.CLAN_NAME_MAX_LENGTH = 70
        self.CLAN_ABBREV_MAX_LENGTH = 5
        self.CLAN_DESCR_MAX_LENGTH = 1000
        self.CLAN_MOTTO_MAX_LENGTH = 100
        return


class TextRestrictionsChinese(TextRestrictionsBasic):
    __slots__ = TextRestrictionsBasic.__slots__

    def __init__(self):
        super(TextRestrictionsChinese, self).__init__()
        ACCOUNT_NAME_EXCLUDED_SYMBOLS = lrange(32) + [
         2, 3, 4, 5, 6, 
         7, 8, 9, 10]
        self.ACCOUNT_NAME_RE = re.compile(u'(?u)^[^' + (u'').join(u'\\x%0.2x' % n for n in ACCOUNT_NAME_EXCLUDED_SYMBOLS) + chr(65535) + chr(65534) + u']+$')
        self.ACCOUNT_NAME_MIN_LENGTH_REG = self.ACCOUNT_NAME_MIN_LENGTH
        self.LOGIN_NAME_RE = re.compile(b'^[_a-z0-9-+@.]+$')
        self.LOGIN_NAME_MIN_LENGTH = 4
        self.LOGIN_NAME_MAX_LENGTH = 50
        self.CLAN_ABBREV_RE = self.ACCOUNT_NAME_RE
        self.UPPERCASE_CLAN_ABBREV = False
        self.REQUIRE_NORMALIZED_CLAN_ABBREV = False
        return


class TextRestrictionsKorea(TextRestrictionsChinese):
    __slots__ = TextRestrictionsChinese.__slots__

    def __init__(self):
        super(TextRestrictionsKorea, self).__init__()
        self.LOGIN_NAME_MIN_LENGTH = 1
        self.LOGIN_NAME_MAX_LENGTH = 50
        self.LOGIN_NAME_RE = re.compile(b'^[a-z0-9_-]+(\\.[a-z0-9_-]+)*@([a-z0-9]([a-z0-9-]*[a-z0-9])?\\.)+[a-z]{2,4}$')
        self.ACCOUNT_NAME_RE = re.compile(u'^[a-zA-Z0-9_\uac00-\ud79d]+$')
        return


class TextRestrictionsSandbox(TextRestrictionsBasic):
    __slots__ = TextRestrictionsBasic.__slots__
    SANDBOX_POSTFIX_LENGTH = 5

    def __init__(self):
        super(TextRestrictionsSandbox, self).__init__()
        self.ACCOUNT_NAME_MAX_LENGTH += self.SANDBOX_POSTFIX_LENGTH
        return


class TextRestrictionsCT(TextRestrictionsBasic):
    __slots__ = TextRestrictionsBasic.__slots__
    CT_POSTFIX_LENGTH = 5

    def __init__(self):
        super(TextRestrictionsCT, self).__init__()
        self.ACCOUNT_NAME_MAX_LENGTH += self.CT_POSTFIX_LENGTH
        return


if CREDENTIALS_RESTRICTION_SET == CREDENTIALS_RESTRICTION.BASIC:
    textRestrictions = TextRestrictionsBasic()
elif CREDENTIALS_RESTRICTION_SET == CREDENTIALS_RESTRICTION.CHINESE:
    textRestrictions = TextRestrictionsChinese()
elif CREDENTIALS_RESTRICTION_SET == CREDENTIALS_RESTRICTION.KOREA:
    textRestrictions = TextRestrictionsKorea()
elif CREDENTIALS_RESTRICTION_SET == CREDENTIALS_RESTRICTION.SANDBOX:
    textRestrictions = TextRestrictionsSandbox()
elif CREDENTIALS_RESTRICTION_SET == CREDENTIALS_RESTRICTION.CT:
    textRestrictions = TextRestrictionsCT()
_ACCOUNT_NAME_RE = textRestrictions.ACCOUNT_NAME_RE
_ACCOUNT_NAME_MIN_LENGTH = textRestrictions.ACCOUNT_NAME_MIN_LENGTH
_ACCOUNT_NAME_MAX_LENGTH = textRestrictions.ACCOUNT_NAME_MAX_LENGTH
_ACCOUNT_NAME_MIN_LENGTH_REG = textRestrictions.ACCOUNT_NAME_MIN_LENGTH_REG
_LOGIN_NAME_RE = textRestrictions.LOGIN_NAME_RE
_LOGIN_NAME_MIN_LENGTH = textRestrictions.LOGIN_NAME_MIN_LENGTH
_LOGIN_NAME_MAX_LENGTH = textRestrictions.LOGIN_NAME_MAX_LENGTH
_CLAN_ABBREV_RE = textRestrictions.CLAN_ABBREV_RE
_CLAN_NAME_MAX_LENGTH = textRestrictions.CLAN_NAME_MAX_LENGTH
_CLAN_ABBREV_MAX_LENGTH = textRestrictions.CLAN_ABBREV_MAX_LENGTH
_UPPERCASE_CLAN_ABBREV = textRestrictions.UPPERCASE_CLAN_ABBREV
_REQUIRE_NORMALIZED_CLAN_ABBREV = textRestrictions.REQUIRE_NORMALIZED_CLAN_ABBREV
CLAN_DESCR_MAX_LENGTH = textRestrictions.CLAN_DESCR_MAX_LENGTH
CLAN_MOTTO_MAX_LENGTH = textRestrictions.CLAN_MOTTO_MAX_LENGTH

def getClanAbbrevMaxLength():
    return _CLAN_ABBREV_MAX_LENGTH


CLAN_DESCR_MAX_BYTES = CLAN_DESCR_MAX_LENGTH * 4
CLAN_MOTTO_MAX_BYTES = CLAN_MOTTO_MAX_LENGTH * 4

def unicode_from_utf8(utf8str, unicodeNormalForm=b'NFKC'):
    unicodeStr = utf8str
    if isinstance(unicodeStr, bytes):
        unicodeStr = unicode(unicodeStr, b'utf8')
    return (unicodedata.normalize(unicodeNormalForm, unicodeStr), unicodeStr)


def utf8_accepted(utf8str, regExp, minLen, maxLen, unicodeNormalForm=b'NFKC', checkBeforeNormalisation=True):
    nfkc, plain = unicode_from_utf8(utf8str, unicodeNormalForm)

    def matchFn(uniStr):
        return (regExp.match(uniStr)) and minLen <= len(uniStr) <= maxLen

    if checkBeforeNormalisation and not matchFn(plain):
        return False
    return matchFn(nfkc)


def normalized_unicode_trim(utf8str, length, unicodeNormalForm=b'NFKC'):
    try:
        unicodeStr, _ = unicode_from_utf8(utf8str, unicodeNormalForm)
        if len(unicodeStr) > max(0, length):
            unicodeStr = unicodeStr[:length]
        return unicodeStr.encode(b'utf8')
    except:
        LOG_CURRENT_EXCEPTION()
        return

    return


def normalized_unicode_trim_u(unicodeStr, length, unicodeNormalForm=b'NFKC'):
    try:
        unicodeStr = unicodedata.normalize(unicodeNormalForm, unicodeStr)
        if len(unicodeStr) > max(0, length):
            unicodeStr = unicodeStr[:length]
        return unicodeStr
    except:
        LOG_CURRENT_EXCEPTION()
        return

    return


def normalized_unicode_trim_and_lowercase(utf8str, length, unicodeNormalForm=b'NFKC'):
    try:
        unicodeStr, _ = unicode_from_utf8(utf8str, unicodeNormalForm)
        if len(unicodeStr) > max(0, length):
            unicodeStr = unicodeStr[:length]
        return unicodeStr.lower().encode(b'utf8')
    except:
        LOG_CURRENT_EXCEPTION()
        return

    return


def isAccountNameValid(text, minLength=_ACCOUNT_NAME_MIN_LENGTH):
    return utf8_accepted(text, _ACCOUNT_NAME_RE, minLength, _ACCOUNT_NAME_MAX_LENGTH)


def normalizedAccountName(text):
    return normalized_unicode_trim_and_lowercase(text, _ACCOUNT_NAME_MAX_LENGTH)


def isAccountLoginValid(text):
    return utf8_accepted(text, _LOGIN_NAME_RE, _LOGIN_NAME_MIN_LENGTH, _LOGIN_NAME_MAX_LENGTH)


def normalizedAccountLogin(text):
    try:
        text = normalize_utf8(text)
        if len(text) > _LOGIN_NAME_MAX_LENGTH:
            text = text[:_LOGIN_NAME_MAX_LENGTH]
        return text.lower()
    except:
        LOG_CURRENT_EXCEPTION()
        return

    return


def forgeAccountNormalizedName(origNormalizedName, centerID):
    ext = b'\x01' + str(centerID)
    return origNormalizedName[:_MAX_NORMALIZED_NAME_BYTES - len(ext)] + ext


def isClanNameValid(text):
    try:
        utext = unicode(text, b'utf8').strip()
        if utext.encode(b'utf8') != text:
            return False
        if not 2 <= len(utext) <= _CLAN_NAME_MAX_LENGTH:
            return False
        for word in utext.split(b' '):
            if not word or any(ord(c) < 32 for c in word):
                return False

        return True
    except:
        LOG_CURRENT_EXCEPTION()
        return False

    return


def normalizedClanName(text):
    try:
        utext, _ = unicode_from_utf8(text)
        if len(utext) > _CLAN_NAME_MAX_LENGTH:
            utext = utext[:_CLAN_NAME_MAX_LENGTH]
        return utext.lower().encode(b'utf8')
    except:
        LOG_CURRENT_EXCEPTION()
        return

    return


def isClanAbbrevValid(abbrev):
    return utf8_accepted(abbrev, _CLAN_ABBREV_RE, 2, _CLAN_ABBREV_MAX_LENGTH) and (not _REQUIRE_NORMALIZED_CLAN_ABBREV or abbrev == normalizedClanAbbrev(abbrev))


def normalizedClanAbbrev(abbrev):
    try:
        abbrev, _ = unicode_from_utf8(abbrev)
        if len(abbrev) > _CLAN_ABBREV_MAX_LENGTH:
            abbrev = abbrev[:_CLAN_ABBREV_MAX_LENGTH]
        if _UPPERCASE_CLAN_ABBREV:
            abbrev = abbrev.upper()
        return abbrev.encode(b'utf8')
    except:
        LOG_CURRENT_EXCEPTION()
        return

    return


def isChannelNameValid(channelName):
    test = channelName.strip()
    return test and test[0] not in b'[<{('


def escapeSQL(text, default=b'\\0'):
    if text is None:
        return default
    else:
        return text.replace(b'\\', b'\\\\').replace(b"'", b"\\'").replace(b'"', b'\\"').replace(b'\x00', b'\\0')


def normalize_utf8(utf8str):
    return unicode(utf8str, b'utf8').encode(b'utf8')


def truncate_utf8(utf8str, maxbytes):
    if len(utf8str) < maxbytes:
        return utf8str
    if maxbytes <= 0:
        return b''
    if _is_utf8_one_byte(utf8str[maxbytes - 1]):
        return utf8str[:maxbytes]
    for x in xrange(1, 5):
        if _is_utf8_first_byte(utf8str[maxbytes - x]):
            ut8_len = _decode_utf8_len_byte(utf8str[maxbytes - x])
            if x == ut8_len:
                break
            return utf8str[:maxbytes - x]

    return utf8str[:maxbytes]


def _is_utf8_one_byte(byte):
    o = unpackByte(byte)
    return 127 & o == o


def _is_utf8_first_byte(byte):
    o = unpackByte(byte)
    return 191 & o != o


def _decode_utf8_len_byte(byte):
    o = unpackByte(byte)
    v = 240 & o
    if v >= 240:
        return 4
    if v >= 224:
        return 3
    if v >= 192:
        return 2
    if v < 127:
        return 1
    return 0


def strtobool(val):
    val = val.lower()
    if val in (b'y', b'yes', b't', b'true', b'on', b'1'):
        return True
    if val in (b'n', b'no', b'f', b'false', b'off', b'0'):
        return False
    raise InvalidStringValueException(b'invalid truth value %r' % (val,))
    return


class InvalidStringValueException(SoftException):
    pass
