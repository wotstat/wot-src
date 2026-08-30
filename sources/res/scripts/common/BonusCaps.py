from __future__ import absolute_import
from typing import Dict, Optional, Set, FrozenSet

class BonusCapsConst(object):
    CONFIG_NAME = b'bonus_caps_override_config'
    REMOVE = b'remove'
    ADD = b'add'
    OVERRIDE = b'override'


class BonusCapsConfig(object):
    __slots__ = {
     b'__config'}
    __OPERATIONS = {(BonusCapsConst.REMOVE): (lambda x, y: x - y), 
       (BonusCapsConst.ADD): (lambda x, y: x | y), 
       (BonusCapsConst.OVERRIDE): (lambda x, y: y)}

    def __init__(self, config=None):
        if not config:
            config = {}
        self.__config = config
        return

    def __performOperations(self, arenaBonusType, defaultBonusCaps):
        configBonusCaps = self.__config[arenaBonusType]
        resultBonusCaps = set(defaultBonusCaps)
        for operation in configBonusCaps:
            resultBonusCaps = self.__OPERATIONS[operation](resultBonusCaps, configBonusCaps[operation])

        return resultBonusCaps

    def getModifiedBonusCaps(self, arenaBonusType, defaultBonusCaps):
        if self.__config.get(arenaBonusType, None) is None:
            return defaultBonusCaps
        else:
            return frozenset(self.__performOperations(arenaBonusType, defaultBonusCaps))
