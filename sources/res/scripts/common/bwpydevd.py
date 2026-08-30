from __future__ import absolute_import
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
    bwdebug.INFO_MSG(b'bwdebug start: %s - %s:%d for VS Code' % (ide, host, port))
    startPyDevD(ide, host, port, suspend, traceOnlyCurrentThread, inspectDoubleUnderscore)
    return


bwPyDevDStarted = False
bwActiveIde = None

def startPyDevD(ide, host=b'127.0.0.1', port=5678, suspend=False, traceOnlyCurrentThread=False, inspectDoubleUnderscore=False, pathMappings=None):
    global bwActiveIde
    global bwPyDevDStarted
    if not bwPyDevDStarted:
        bwPyDevDStarted = True
        bwActiveIde = ide
        if ide == b'vscode':
            pydevDir = b'scripts/common/pydev/vscode'
            sys.path.append(pydevDir)
            sys.path.append(pydevDir + b'/pydev')
        else:
            pydevDir = b'scripts/common/pydev/%s/pydev' % ide
            sys.path.append(pydevDir)
        try:
            if ide == b'vscode':
                import ptvsd
                activeMappings = pathMappings if pathMappings is not None else REPLACE_PATHS
                if activeMappings:
                    import pydevd_file_utils
                    pydevd_file_utils.setup_client_server_paths(activeMappings)
                    bwdebug.INFO_MSG(b'ptvsd path mappings: %s' % repr(activeMappings))
                bwdebug.INFO_MSG(b'ptvsd listening on %s:%d for VS Code' % (host, port))
                ptvsd.enable_attach(address=(host, port), redirect_output=True)
                if suspend:
                    ptvsd.wait_for_attach()
            else:
                import pydevd
                bwdebug.INFO_MSG(b'PyDevD connecting to %s:%d' % (host, port))
                pydevd.settrace(host=host, port=port, suspend=suspend, stdoutToServer=True, stderrToServer=True, trace_only_current_thread=traceOnlyCurrentThread, inspect_double_underscore=inspectDoubleUnderscore)
            threading.currentThread().__pydevd_id__ = BigWorld.component
        except Exception as e:
            from traceback import print_exc
            print_exc()
            bwdebug.ERROR_MSG(b'Failed to load pydevd: %s' % repr(e))

    return


def stopPyDevD():
    global bwActiveIde
    global bwPyDevDStarted
    if bwPyDevDStarted:
        bwPyDevDStarted = False
        try:
            if bwActiveIde == b'vscode':
                import ptvsd
                ptvsd.tracing(False)
            else:
                import pydevd
                pydevd.stoptrace()
            del threading.currentThread().__pydevd_id__
            bwdebug.INFO_MSG(b'PyDevD debug has stopped')
        except Exception as e:
            from traceback import print_exc
            print_exc()
            bwdebug.ERROR_MSG(b'Failed to stop pydevd: %s' % repr(e))

        bwActiveIde = None
    return
