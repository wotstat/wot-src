from __future__ import absolute_import
import logging
LOGGER_NAME = b'NewbieBattleHints'

def getLogger(*names):
    return logging.getLogger((b'{}').format((b':').join((LOGGER_NAME,) + names)))
