import logging

def getLogger(loggerName):
    return logging.getLogger((b'GameLoading:{}').format(loggerName))


def getSequencesViewHistoryLogger():
    return getLogger(b'SequencesViewHistory')


def getCdnConfigLogger():
    return getLogger(b'CdnConfig')


def getCdnCacheLogger():
    return getLogger(b'CdnCache')


def getResourcesLogger():
    return getLogger(b'Resources')


def getStatesLogger():
    return getLogger(b'States')


def getStateMachineLogger():
    return getLogger(b'StateMachine')


def getLoaderSettingsLogger():
    return getLogger(b'LoaderSettings')


def getLoaderLogger():
    return getLogger(b'Loader')
