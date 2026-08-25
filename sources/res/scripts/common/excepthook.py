from __future__ import absolute_import
import sys, linecache
from functools import wraps
from future.utils import viewitems, viewvalues
from traceback import format_exception_only
import BigWorld
from constants import IS_BASEAPP
_MAX_OBJECT_SIZE = 16384
_MAX_DEPTH = 10
_SEQUENCE_TYPES = (
 list, set, tuple)
_LINE_LIMIT = 25
_ENABLE_EXTENDED_TRACEBACK = False

def getLocationFromCode(fileNameToTrim, code, lineno=None):
    filename = code.co_filename
    trim_match = fileNameToTrim.findall(filename)
    if trim_match:
        trim_path = trim_match[0]
        idx = filename.find(trim_path)
        filename = filename[idx + len(trim_path):]
    if lineno is None:
        lineno = code.co_firstlineno
    name = code.co_name
    return (filename, lineno, name)


def formatLocation(filename, lineno, name):
    return b'File "%s", line %d, in %s' % (filename, lineno, name)


def extendedTracebackAsString(fileNameToTrim, wrapperName, orgName, etype, value, tb):
    return (b'\n').join(extendedTracebackAsList(fileNameToTrim, wrapperName, orgName, etype, value, tb))


def extendedTracebackAsList(fileNameToTrim, wrapperName, orgName, exctype, value, traceback):
    global _ENABLE_EXTENDED_TRACEBACK
    if not _ENABLE_EXTENDED_TRACEBACK:
        return []
    else:
        try:
            lines = [
             b'[TRACEBACK EXT]']
            localsProcessorCache = {}
            parent = traceback
            n = 0
            while parent and n < _LINE_LIMIT:
                fm = parent.tb_frame
                filename, lineno, name = getLocationFromCode(fileNameToTrim, fm.f_code, parent.tb_lineno)
                parent = parent.tb_next
                n += 1
                linecache.checkcache(filename)
                line = linecache.getline(filename, lineno, fm.f_globals)
                if wrapperName is not None:
                    if line.find(wrapperName) != -1:
                        continue
                lines.append(b'  %s' % formatLocation(filename, lineno, name))
                line = line.strip()
                if line:
                    lines.append(b'    ' + line)
                lines.append((b'    locals: {0}').format(__processLocals(fm.f_locals, localsProcessorCache)))

            for line in format_exception_only(exctype, value):
                line = line.strip()
                if wrapperName is not None and orgName is not None:
                    line.replace(wrapperName, orgName)
                lines.append(line)

            lines.append(b'[/TRACEBACK EXT]')
        except:
            lines = []

        return lines


def __processVar(k, v, localsProcessorCache):
    varID = id(v)
    if varID in localsProcessorCache:
        return localsProcessorCache[varID]
    if k == b'self' or IS_BASEAPP and isinstance(v, (BigWorld.Base, BigWorld.Proxy)):
        res = {b'className': (v.__class__.__name__)}
        for field, alias in ((b'id', b'id'), (b'databaseID', b'dbID'), (b'className', b'entityType')):
            if hasattr(v, field):
                res[alias] = getattr(v, field)

    else:
        meta = {b'depth': 0, 
           b'size': 0, 
           b'cycleReferences': (set())}
        isSizeOK = __checkObjectSize(v, meta)
        if not isSizeOK:
            res = b'...skipped...'
        else:
            res = v
    localsProcessorCache[varID] = res
    return res


def __checkObjectSize(d, meta):
    try:
        meta[b'depth'] += 1
        if meta[b'depth'] >= _MAX_DEPTH:
            return False
        if id(d) in meta[b'cycleReferences']:
            return True
        meta[b'size'] += sys.getsizeof(d, 0)
        if meta[b'size'] >= _MAX_OBJECT_SIZE:
            return False
        meta[b'cycleReferences'].add(id(d))
        if isinstance(d, dict):
            for v in viewvalues(d):
                if not __checkObjectSize(v, meta):
                    return False

        elif isinstance(d, _SEQUENCE_TYPES):
            for v in d:
                if not __checkObjectSize(v, meta):
                    return False

        return True
    finally:
        meta[b'depth'] -= 1

    return


def __processLocals(locals, localsProcessorCache):
    return {k: __processVar(k, v, localsProcessorCache) for k, v in viewitems(locals)}


def __excepthook(excepthook, fileNameToTrim):

    @wraps(excepthook)
    def wrapper(exctype, value, traceback):
        excepthook(exctype, value, traceback)
        extMsg = extendedTracebackAsString(fileNameToTrim, None, None, exctype, value, traceback)
        BigWorld.logError(b'EXCEPTION', extMsg, None)
        return

    return wrapper


def init(enableExtendedTraceBack, fileNameToTrim):
    global _ENABLE_EXTENDED_TRACEBACK
    _ENABLE_EXTENDED_TRACEBACK = enableExtendedTraceBack
    if _ENABLE_EXTENDED_TRACEBACK:
        sys.excepthook = __excepthook(sys.excepthook, fileNameToTrim)
    return
