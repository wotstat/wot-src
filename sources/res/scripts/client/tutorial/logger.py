from constants import IS_DEVELOPMENT
from debug_utils import _doLog, LOG_CURRENT_EXCEPTION

class LOG_LEVEL(object):
    ERROR = 1
    WARNING = 2
    DEBUG = 4
    MEMORY = 8
    REQUEST = 16


CURRENT_LOG_LEVEL = LOG_LEVEL.ERROR
if IS_DEVELOPMENT:
    CURRENT_LOG_LEVEL |= LOG_LEVEL.WARNING
    CURRENT_LOG_LEVEL |= LOG_LEVEL.REQUEST

def LOG_DEBUG(msg, *args):
    if CURRENT_LOG_LEVEL & LOG_LEVEL.DEBUG:
        _doLog(b'TUTORIAL DEBUG', msg, args)
    return


def LOG_WARNING(msg, *args):
    if CURRENT_LOG_LEVEL & LOG_LEVEL.WARNING:
        _doLog(b'TUTORIAL WARNING', msg, args)
    return


def LOG_ERROR(msg, *args):
    if CURRENT_LOG_LEVEL & LOG_LEVEL.ERROR:
        _doLog(b'TUTORIAL ERROR', msg, args)
    return


def LOG_MEMORY(msg, *args):
    if CURRENT_LOG_LEVEL & LOG_LEVEL.MEMORY:
        _doLog(b'TUTORIAL MEMORY', msg, args)
    return


def LOG_REQUEST(msg, *args):
    if CURRENT_LOG_LEVEL & LOG_LEVEL.REQUEST:
        _doLog(b'TUTORIAL REQUEST', msg, args)
    return


__all__ = (b'LOG_DEBUG', b'LOG_WARNING', b'LOG_ERROR', b'LOG_MEMORY', b'LOG_REQUEST', b'LOG_CURRENT_EXCEPTION')
