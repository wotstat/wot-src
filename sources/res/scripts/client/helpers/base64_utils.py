import logging, base64, binascii, cPickle, typing
_logger = logging.getLogger(__name__)

def base64UrlDecode(encodedValue):
    if isinstance(encodedValue, unicode):
        encodedValue = encodedValue.encode(b'ascii')
    rem = len(encodedValue) % 4
    if rem > 0:
        encodedValue += b'=' * (4 - rem)
    return base64.urlsafe_b64decode(encodedValue)


def pack(raw):
    try:
        return base64.b64encode(cPickle.dumps(raw, cPickle.HIGHEST_PROTOCOL))
    except (binascii.Error, cPickle.PickleError, UnicodeError, TypeError, ValueError):
        _logger.exception(b'Packing data fail.')

    return


def unpack(packed, default=None):
    try:
        return cPickle.loads(base64.b64decode(packed))
    except (binascii.Error, cPickle.PickleError, UnicodeError, TypeError, ValueError, EOFError):
        _logger.exception(b'Unpacking data fail.')

    return default
