from debug_utils import _doLog, _LogWrapper
from debug_utils import LOG_CURRENT_EXCEPTION, LOG_TAGS, LOG_LEVEL

@_LogWrapper(LOG_LEVEL.SVR_RELEASE)
def LOG_DEBUG_BOOTCAMP(msg, *kargs, **kwargs):
    kwargs.setdefault(b'tags', []).append(LOG_TAGS.BOOTCAMP)
    _doLog(b'DEBUG', msg, kargs, kwargs)
    return


@_LogWrapper(LOG_LEVEL.DEV)
def LOG_DEBUG_DEV_BOOTCAMP(msg, *kargs, **kwargs):
    kwargs.setdefault(b'tags', []).append(LOG_TAGS.BOOTCAMP)
    _doLog(b'DEBUG', msg, kargs, kwargs)
    return


@_LogWrapper(LOG_LEVEL.RELEASE)
def LOG_NOTE_BOOTCAMP(msg, *kargs, **kwargs):
    kwargs.setdefault(b'tags', []).append(LOG_TAGS.BOOTCAMP)
    _doLog(b'NOTE', msg, kargs, kwargs)
    return


@_LogWrapper(LOG_LEVEL.RELEASE)
def LOG_WARNING_BOOTCAMP(msg, *kargs, **kwargs):
    kwargs.setdefault(b'tags', []).append(LOG_TAGS.BOOTCAMP)
    _doLog(b'WARNING', msg, kargs, kwargs)
    return


@_LogWrapper(LOG_LEVEL.RELEASE)
def LOG_ERROR_BOOTCAMP(msg, *kargs, **kwargs):
    kwargs.setdefault(b'tags', []).append(LOG_TAGS.BOOTCAMP)
    _doLog(b'ERROR', msg, kargs, kwargs)
    return


@_LogWrapper(LOG_LEVEL.RELEASE)
def LOG_CODEPOINT_WARNING_BOOTCAMP(*kargs, **kwargs):
    kwargs.setdefault(b'tags', []).append(LOG_TAGS.BOOTCAMP)
    _doLog(b'WARNING', b'this code point should have never been reached', kargs, kwargs)
    return


def LOG_CURRENT_EXCEPTION_BOOTCAMP():
    LOG_CURRENT_EXCEPTION(tags=[LOG_TAGS.BOOTCAMP], frame=2)
    return


@_LogWrapper(LOG_LEVEL.RELEASE)
def LOG_STATISTIC(msg, *kargs, **kwargs):
    kwargs.setdefault(b'tags', []).append(LOG_TAGS.STATISTIC)
    _doLog(b'DEBUG', msg, kargs, kwargs)
    return
