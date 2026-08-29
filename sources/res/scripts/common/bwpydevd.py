import os, sys, ResMgr, BigWorld, threading, bwdebug
REPLACE_PATHS = []
HAS_BW_CONFIG = False
if os.name == b'posix':
    try:
        import BWConfig
        HAS_BW_CONFIG = True
    except ImportError:
        HAS_BW_CONFIG = False

else:

    class BWConfig:
        debugConfig = None

        @staticmethod
        def readString(key, default=b''):
            return BWConfig.debugConfig.readString(key, default)

        @staticmethod
        def readBool(key, default=False):
            return BWConfig.debugConfig.readBool(key, default)

        @staticmethod
        def readInt(key, default=0):
            return BWConfig.debugConfig.readInt(key, default)

        @staticmethod
        def getSections(key):
            sections = []
            for sectName, sect in BWConfig.debugConfig.items():
                if sectName == key:
                    sections.append(sect)

            return sections


def BWConfigWrapper(fn):

    def wrapped(*args, **kwargs):
        global HAS_BW_CONFIG
        if os.name == b'posix':
            return fn(*args, **kwargs)
        else:
            prefsConfig = ResMgr.openSection(b'../../bin/client/preferences.xml')
            if prefsConfig and prefsConfig.has_key(b'scriptsPreferences/development/pydevd'):
                BWConfig.debugConfig = prefsConfig[b'scriptsPreferences/development']
            else:
                BWConfig.debugConfig = ResMgr.openSection(b'scripts_config.xml')
            if BWConfig.debugConfig is not None:
                HAS_BW_CONFIG = True
            fn(*args, **kwargs)
            BWConfig.debugConfig = None
            return

    return wrapped


@BWConfigWrapper
def startDebug(isStartUp=False, host=None, port=None, ide=None):
    if not HAS_BW_CONFIG:
        return
    if isStartUp and not BWConfig.readBool(b'pydevd/autoConnect/%s' % BigWorld.component, False):
        return
    for pydevdSect in BWConfig.getSections(b'pydevd'):
        for sectName, sect in pydevdSect.items():
            if sectName == b'replacePath':
                REPLACE_PATHS.append((sect.readString(b'to'), sect.readString(b'from')))

    ide = ide or BWConfig.readString(b'pydevd/ide', b'pycharm')
    host = host or BWConfig.readString(b'pydevd/host', b'localhost')
    port = port or BWConfig.readInt(b'pydevd/port', 5678)
    suspend = BWConfig.readBool(b'pydevd/suspend', False)
    traceOnlyCurrentThread = BWConfig.readBool(b'pydevd/traceOnlyCurrentThread', False)
    inspectDoubleUnderscore = BWConfig.readBool(b'pydevd/inspectDoubleUnderscore', True)
    startPyDevD(ide, host, port, suspend, traceOnlyCurrentThread, inspectDoubleUnderscore)
    return


bwPyDevDStarted = False

def startPyDevD(ide, host=b'127.0.0.1', port=5678, suspend=False, traceOnlyCurrentThread=False, inspectDoubleUnderscore=False):
    global bwPyDevDStarted
    if not bwPyDevDStarted:
        bwPyDevDStarted = True
        pydevDir = b'scripts/common/pydev/%s/pydev' % ide
        absPydevDir = ResMgr.resolveToAbsolutePath(pydevDir)
        if not os.path.isdir(absPydevDir):
            bwdebug.ERROR_MSG(b'Unable to find pydevd directory for IDE %s (at %s)' % (ide, absPydevDir))
        sys.path.append(pydevDir)
        try:
            import pydevd
            bwdebug.INFO_MSG(b'PyDevD connecting to %s:%d' % (host, port))
            pydevd.settrace(host=host, port=port, suspend=suspend, stdoutToServer=True, stderrToServer=True, trace_only_current_thread=traceOnlyCurrentThread, inspect_double_underscore=inspectDoubleUnderscore)
            threading.currentThread().__pydevd_id__ = BigWorld.component
        except Exception as e:
            from traceback import print_exc
            print_exc()
            bwdebug.ERROR_MSG(b'Failed to load pydevd: %s' % repr(e))
            bwPyDevDStarted = False

    return


def stopPyDevD():
    global bwPyDevDStarted
    if bwPyDevDStarted:
        bwPyDevDStarted = False
        try:
            import pydevd
            pydevd.stoptrace()
            del threading.currentThread().__pydevd_id__
            bwdebug.INFO_MSG(b'PyDevD debug has stopped')
        except Exception as e:
            from traceback import print_exc
            print_exc()
            bwdebug.ERROR_MSG(b'Failed to stop pydevd: %s' % repr(e))

    return
