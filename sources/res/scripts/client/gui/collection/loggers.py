import logging

def getLogger(loggerName):
    return logging.getLogger((b'Collections:{}').format(loggerName))


def getCdnCacheLogger():
    return getLogger(b'CdnCache')


def getLocalCacheLogger():
    return getLogger(b'LocalCache')
