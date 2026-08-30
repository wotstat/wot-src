import sys, re, subprocess, BigWorld, excepthook, time, traceback
from GarbageCollectionDebug import gcDump, getGarbageGraph
from functools import wraps
from collections import defaultdict
from warnings import warn_explicit
from traceback import format_exception
from constants import IS_CLIENT, IS_CELLAPP, IS_BASEAPP, CURRENT_REALM, IS_DEVELOPMENT, IS_BOT, GAME_ROOT_DIR_NAME
from constants import LEAKS_DETECTOR_MAX_EXECUTION_TIME
from contextlib import contextmanager
from threading import RLock
from soft_exception import SoftException
_src_file_trim_to = re.compile(b'res/(?:%s|%s_ext)/(?:.*/)?scripts/' % (GAME_ROOT_DIR_NAME, GAME_ROOT_DIR_NAME))
_g_trimmedFilenameByFullFilename = {}

def _getTrimmedFilename(filename):
    if filename in _g_trimmedFilenameByFullFilename:
        return _g_trimmedFilenameByFullFilename[filename]
    splitPaths = _src_file_trim_to.split(filename)
    if len(splitPaths) == 2:
        trimmedFilename = splitPaths[1]
    else:
        trimmedFilename = filename
    _g_trimmedFilenameByFullFilename[filename] = trimmedFilename
    return trimmedFilename


_g_logMapping = {}
_g_logLock = RLock()
GCDUMP_CROWBAR_SWITCH = False

class LOG_LEVEL:
    DEV = 1
    ST = 2
    CT = 3
    SVR_RELEASE = 4
    RELEASE = 5


class LOG_TAGS:
    BOOTCAMP = b'[BOOTCAMP]'
    STATISTIC = b'[STATISTIC]'


if CURRENT_REALM == b'DEV':
    _logLevel = LOG_LEVEL.DEV
elif CURRENT_REALM == b'ST':
    _logLevel = LOG_LEVEL.ST
elif CURRENT_REALM in (b'CT', b'SB'):
    _logLevel = LOG_LEVEL.CT
elif IS_CLIENT:
    _logLevel = LOG_LEVEL.RELEASE
else:
    _logLevel = LOG_LEVEL.SVR_RELEASE

class _LogWrapper(object):

    def __init__(self, logLevel):
        self.__lvl = logLevel
        return

    def __call__(self, func):
        if self.__lvl >= _logLevel:
            return func
        else:
            return (lambda *args, **kwargs: None)

        return


class CriticalError(BaseException):
    pass


@contextmanager
def suppress(*exceptions):
    try:
        yield
    except exceptions:
        pass

    return


def init():
    global _g_logMapping
    if not (IS_CLIENT or IS_BOT):

        def splitMessageIntoChunks(prefix, msg, func):
            if prefix not in (b'EXCEPTION', b'CRITICAL'):
                msg = msg[:8960]
            blockSize = 1792
            with _g_logLock:
                for m in msg.splitlines(False)[:100]:
                    idx = 0
                    while idx < len(m):
                        func(prefix, m[idx:idx + blockSize], None)
                        idx += blockSize

            return

        bwLogTrace = BigWorld.logTrace
        BigWorld.logTrace = lambda prefix, msg, *args: splitMessageIntoChunks(prefix, msg, bwLogTrace)
        bwLogDebug = BigWorld.logDebug
        BigWorld.logDebug = lambda prefix, msg, *args: splitMessageIntoChunks(prefix, msg, bwLogDebug)
        bwLogInfo = BigWorld.logInfo
        BigWorld.logInfo = lambda prefix, msg, *args: splitMessageIntoChunks(prefix, msg, bwLogInfo)
        bwLogNotice = BigWorld.logNotice
        BigWorld.logNotice = lambda prefix, msg, *args: splitMessageIntoChunks(prefix, msg, bwLogNotice)
        bwLogWarning = BigWorld.logWarning
        BigWorld.logWarning = lambda prefix, msg, *args: splitMessageIntoChunks(prefix, msg, bwLogWarning)
        bwLogError = BigWorld.logError
        BigWorld.logError = lambda prefix, msg, *args: splitMessageIntoChunks(prefix, msg, bwLogError)
        bwLogCritical = BigWorld.logCritical
        BigWorld.logCritical = lambda prefix, msg, *args: splitMessageIntoChunks(prefix, msg, bwLogCritical)
        bwLogHack = BigWorld.logHack
        BigWorld.logHack = lambda prefix, msg, *args: splitMessageIntoChunks(prefix, msg, bwLogHack)
    _g_logMapping = {b'TRACE': (BigWorld.logTrace), 
       b'DEBUG': (BigWorld.logDebug), 
       b'INFO': (BigWorld.logInfo), 
       b'NOTE': (BigWorld.logNotice), 
       b'NOTICE': (BigWorld.logNotice), 
       b'WARNING': (BigWorld.logWarning), 
       b'ERROR': (BigWorld.logError), 
       b'CRITICAL': (BigWorld.logCritical), 
       b'HACK': (BigWorld.logHack), 
       b'OBSOLETE': (BigWorld.logWarning)}
    excepthook.init(not IS_CLIENT and _logLevel < LOG_LEVEL.SVR_RELEASE, _getTrimmedFilename)
    return


@_LogWrapper(LOG_LEVEL.RELEASE)
def CRITICAL_ERROR(msg, *kargs, **kwargs):
    msg = (b'{0}:{1}:{2}:{3}').format(_makeMsgHeader(sys._getframe(1)), msg, kargs, kwargs)
    BigWorld.logCritical(b'CRITICAL', msg, None)
    if IS_CLIENT:
        BigWorld.quit()
    elif IS_CELLAPP or IS_BASEAPP:
        BigWorld.shutDownApp()
        raise CriticalError(msg)
    else:
        sys.exit()
    return


@_LogWrapper(LOG_LEVEL.RELEASE)
def LOG_CURRENT_EXCEPTION(tags=None, frame=1):
    msg = _makeMsgHeader(sys._getframe(frame)) + b'\n'
    etype, value, tb = sys.exc_info()
    msg += (b'').join(format_exception(etype, value, tb, None))
    with _g_logLock:
        BigWorld.logError(b'EXCEPTION', _addTagsToMsg(tags, msg), None)
        extMsg = excepthook.extendedTracebackAsString(_getTrimmedFilename, None, None, etype, value, tb)
        if extMsg:
            BigWorld.logError(b'EXCEPTION', _addTagsToMsg(tags, extMsg), None)
    return


LOG_EXPECTED_EXCEPTION = LOG_CURRENT_EXCEPTION

@_LogWrapper(LOG_LEVEL.RELEASE)
def LOG_WRAPPED_CURRENT_EXCEPTION(wrapperName, orgName, orgSource, orgLineno):
    sys.stderr.write(b'[%s] (%s, %d):' % (b'EXCEPTION', orgSource, orgLineno))
    from sys import exc_info
    from traceback import format_tb, format_exception_only
    etype, value, tb = exc_info()
    if tb:
        list = [
         b'Traceback (most recent call last):\n']
        list = list + format_tb(tb)
    else:
        list = []
    list = list
    for ln in list:
        if ln.find(wrapperName) == -1:
            sys.stderr.write(ln)

    list = format_exception_only(etype, value)
    for ln in list:
        sys.stderr.write(ln.replace(wrapperName, orgName))

    extMsg = excepthook.extendedTracebackAsString(_getTrimmedFilename, wrapperName, orgName, etype, value, tb)
    if extMsg:
        BigWorld.logError(b'EXCEPTION', extMsg, None)
    return


@_LogWrapper(LOG_LEVEL.RELEASE)
def LOG_CODEPOINT_WARNING(*kargs, **kwargs):
    _doLog(b'WARNING', b'this code point should have never been reached', kargs, kwargs)
    return


@_LogWrapper(LOG_LEVEL.RELEASE)
def LOG_ERROR(msg, *kargs, **kwargs):
    _doLog(b'ERROR', msg, kargs, kwargs)
    return


@_LogWrapper(LOG_LEVEL.RELEASE)
def LOG_SENTRY(msg, *kargs, **kwargs):
    try:
        raise SoftException((b'{} {} {}').format(msg, kargs, kwargs))
    except:
        LOG_CURRENT_EXCEPTION(frame=2)

    return


@_LogWrapper(LOG_LEVEL.DEV)
def LOG_ERROR_DEV(msg, *kargs, **kwargs):
    _doLog(b'ERROR', msg, kargs, kwargs)
    return


@_LogWrapper(LOG_LEVEL.DEV)
def LOG_ACHTUNG(msg, *kargs, **kwargs):
    _doLog(b'ACHTUNG', msg, kargs, kwargs)
    return


@_LogWrapper(LOG_LEVEL.RELEASE)
def LOG_WARNING(msg, *kargs, **kwargs):
    _doLog(b'WARNING', msg, kargs, kwargs)
    return


def LOG_OBSOLETE(msg, *kargs, **kwargs):
    _doLog(b'OBSOLETE', msg, kargs, kwargs)
    return


@_LogWrapper(LOG_LEVEL.RELEASE)
def LOG_NOTE(msg, *kargs, **kwargs):
    _doLog(b'NOTE', msg, kargs, kwargs)
    return


@_LogWrapper(LOG_LEVEL.SVR_RELEASE)
def LOG_DEBUG(msg, *kargs, **kwargs):
    _doLog(b'DEBUG', msg, kargs, kwargs)
    return


@_LogWrapper(LOG_LEVEL.DEV)
def LOG_DEBUG_DEV(msg, *kargs, **kwargs):
    _doLog(b'DEBUG', msg, kargs, kwargs)
    return


@_LogWrapper(LOG_LEVEL.DEV)
def LOG_DEBUG_DEV_NICE(msg, *kargs, **kwargs):
    kwargs[b'nice'] = True
    _doLog(b'DEBUG', msg, kargs, kwargs)
    return


@_LogWrapper(LOG_LEVEL.RELEASE)
def LOG_UNEXPECTED(msg, *kargs, **kwargs):
    _doLog(b'LOG_UNEXPECTED', msg, kargs, kwargs)
    return


@_LogWrapper(LOG_LEVEL.RELEASE)
def LOG_WRONG_CLIENT(entity, *kargs, **kwargs):
    entity = getattr(entity, b'id', entity)
    BigWorld.logError(b'WRONG_CLIENT', (b' ').join(map(str, [_makeMsgHeader(sys._getframe(1)), entity, kargs, kwargs])), None)
    return


@_LogWrapper(LOG_LEVEL.RELEASE)
def LOG_WRONG_CLIENT_SHORT(entity, attributeName, attribute, entityId, funcName, *_, **__):
    entity = getattr(entity, b'id', entity)
    BigWorld.logError(b'WRONG_CLIENT', (b' ').join(map(str, [entity, attributeName, attribute, entityId, funcName])), None)
    return


def _doLog(category, msg, args=None, kwargs={}, frameDepth=2):
    header = _makeMsgHeader(sys._getframe(frameDepth))
    logFunc = _g_logMapping.get(category, None)
    if not logFunc:
        logFunc = BigWorld.logDebug
    if args:
        if kwargs.get(b'nice'):
            parts = [header, u' ', msg]
            parts.extend(args)
            output = (u'').join(map(unicode, parts))
        else:
            output = (u' ').join(map(unicode, [header, msg, args]))
    else:
        output = (u' ').join(map(unicode, [header, msg]))
    tags = kwargs.pop(b'tags', None)
    logFunc(category, _addTagsToMsg(tags, output), None)
    if kwargs.get(b'stack', False):
        traceback.print_stack(file=sys.stdout)
    return


def _makeMsgHeader(frame):
    return (b'({}, {})').format(_getTrimmedFilename(frame.f_code.co_filename), frame.f_lineno)


def _doLogFmt(prefix, fmt, *args):
    msg = _makeMsgHeader(sys._getframe(2))
    msg += fmt.format(*args) if args else fmt
    BigWorld.logInfo(prefix, msg, None)
    return


def _addTagsToMsg(tags, msg):
    if tags:
        return (u'{0} {1}').format((u' ').join(tags), msg)
    return msg


def makeFuncLocationString(func):
    return excepthook.formatLocation(*excepthook.getLocationFromCode(_getTrimmedFilename, func.func_code))


def trace(func):
    argnames = func.func_code.co_varnames[:func.func_code.co_argcount]
    fname = func.func_name
    frame = sys._getframe(1)

    @wraps(func)
    def wrapper(*args, **kwds):
        BigWorld.logDebug((b' ').join(b'(%s, %d) call %s:' % (frame.f_code.co_filename, frame.f_lineno, fname), b':', (b', ').join(b'%s=%r' % entry for entry in zip(argnames, args) + kwds.items())))
        ret = func(*args, **kwds)
        BigWorld.logDebug((b' ').join(b'(%s, %d) return from %s:' % (frame.f_code.co_filename, frame.f_lineno, fname), b':', repr(ret)))
        return ret

    return wrapper


def deprecated(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        warn_explicit(b'Call to deprecated function %(funcname)s.' % {b'funcname': (func.__name__)}, category=DeprecationWarning, filename=func.func_code.co_filename, lineno=func.func_code.co_firstlineno + 1)
        return func(*args, **kwargs)

    return wrapper


def disabled(func):

    def empty_func(*args, **kargs):
        return

    return empty_func


def disabled_if(checker, msg=b''):

    def disable_func(func):

        @wraps(func)
        def wrapped(*args, **kwargs):
            if checker():
                return disabled(func)
            return func(*args, **kwargs)

        return wrapped

    return disable_func


def dump_garbage(source=False):
    import inspect, gc
    print b'\nCollecting GARBAGE:'
    gc.collect()
    print b'\nCollecting GARBAGE:'
    gc.collect()
    print b'\nGARBAGE OBJECTS:'
    for x in gc.garbage:
        try:
            s = str(x)
            if len(s) > 80:
                s = b'%s...' % s[:80]
            print b'::', s
            print b'        type:', type(x)
            print b'   referrers:', len(gc.get_referrers(x))
            print b'    is class:', inspect.isclass(type(x))
            print b'      module:', inspect.getmodule(x)
            if source:
                lines, line_num = inspect.getsourcelines(type(x))
                print b'    line num:', line_num
                for l in lines:
                    print b'        line:', l.rstrip(b'\n')

        except:
            pass

    return


def dump_garbage_2(verbose=True, generation=2):
    import gc
    from weakref import ProxyType, ReferenceType
    gc.set_debug(gc.DEBUG_LEAK | gc.DEBUG_STATS)
    if generation is None:
        gc.collect()
    elif generation in xrange(0, 3):
        gc.collect(generation)
    else:
        LOG_ERROR(b'Value of generation is invalid. Generation may be an integer specifying which generation to collect (from 0 to 2)')
        return
    if verbose:
        BigWorld.logInfo(b'', b'=========================================', None)
        BigWorld.logInfo(b'', b'##DUMPSTART', None)
    del gc.garbage[:]
    d = defaultdict((lambda : 0))
    for i in gc.get_objects():
        if not isinstance(i, ProxyType) and not isinstance(i, ReferenceType):
            if hasattr(i, b'__class__'):
                t = i.__class__
            else:
                t = type(i)
            d[t] += 1

    if verbose:
        for t, cnt in d.iteritems():
            msg = b'%d %s' % (cnt, t)
            if isinstance(msg, unicode):
                msg = msg.encode()
            BigWorld.logInfo(b'', msg, None)

    d.clear()
    del gc.garbage[:]
    del d
    if verbose:
        BigWorld.logInfo(b'', b'##DUMPEND', None)
        BigWorld.logInfo(b'', b'=========================================', None)
    return


def memoryLeaksSafeDump(id, _):
    curTime = time.time()
    if not GCDUMP_CROWBAR_SWITCH:
        gcDump()
    if time.time() - curTime > LEAKS_DETECTOR_MAX_EXECUTION_TIME or GCDUMP_CROWBAR_SWITCH:
        BigWorld.delTimer(id)
    return


def printConnections(ports):
    portsRE = (b'\\|').join(map((lambda p: str(p)), ports))
    ns = subprocess.Popen([b'netstat', b'-atupn'], stdout=subprocess.PIPE)
    gr = subprocess.Popen([b'grep', portsRE], stdin=ns.stdout, stdout=subprocess.PIPE)
    output = gr.communicate()[0].splitlines()
    for line in output:
        LOG_DEBUG(b'Connection: ', line)

    return


def printProcesses():
    ps = subprocess.Popen([
     1, 2, 3, 4, 5], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    procs = ps.communicate()[0].splitlines()
    procsCnt = 0
    for proc in procs:
        if b'app' in proc and b'bigworld' in proc:
            LOG_DEBUG(b'Process: ', proc)
            procsCnt += 1

    LOG_DEBUG(b'Total processes: ', procsCnt)
    return


def initMemoryLeaksLogging(repeatOffset=300):

    def detectMemoryLeaksTimerCallback(id, userArg):
        if userArg == 0:
            BigWorld.addTimer(memoryLeaksSafeDump, 1, repeatOffset, 1)
        return

    BigWorld.addTimer(detectMemoryLeaksTimerCallback, 1, 0, 0)
    return


def verify(expression):
    try:
        pass
    except AssertionError:
        LOG_CURRENT_EXCEPTION()

    return


def traceCalls(func):
    if not IS_DEVELOPMENT:
        return func
    argnames = func.func_code.co_varnames[:func.func_code.co_argcount]
    fname = func.func_name
    frame = sys._getframe(1)

    @wraps(func)
    def wrapper(*args, **kwds):
        entID = b' [id=%s]' % str(args[0].id) if len(args) > 0 and hasattr(args[0], b'id') else b''
        BigWorld.logDebug(b'traceCalls', b'(%s, %d)%s call %s(%s)' % (
         frame.f_code.co_filename, frame.f_lineno, entID, fname,
         (b', ').join(b'%s=%r' % entry for entry in zip(argnames, args) + kwds.items())), None)
        ret = func(*args, **kwds)
        BigWorld.logDebug(b'traceCalls', b'%s returned %s' % (fname, repr(ret)), None)
        return ret

    return wrapper


def wg_extract_stack(f=None, limit=None):
    if f is None:
        f = sys._getframe().f_back
    if limit is None:
        if hasattr(sys, b'tracebacklimit'):
            limit = sys.tracebacklimit
    list = []
    n = 0
    while f is not None and (limit is None or n < limit):
        lineno = f.f_lineno
        co = f.f_code
        filename = co.co_filename
        name = co.co_name
        list.append((filename, lineno, name))
        f = f.f_back
        n = n + 1

    list.reverse()
    return list


def traceMethodCalls(obj, *names):
    if not IS_DEVELOPMENT:
        return
    for name in names:
        func = getattr(obj, name)
        setattr(obj, name, traceCalls(func))

    return


init()
