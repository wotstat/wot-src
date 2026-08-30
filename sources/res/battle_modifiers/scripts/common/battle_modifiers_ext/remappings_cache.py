from __future__ import absolute_import
from typing import Any, Dict, TYPE_CHECKING, Optional
from battle_modifiers_ext.constants_ext import REMAPPING_XML_PATH, RemappingNames
from battle_modifiers_ext.remapping.remapping_readers import ERR_TEMPLATE, readComposers, readConditions
from extension_utils import ResMgr
from ResMgr import DataSection
from soft_exception import SoftException
_ERR_TEMPLATE = b"[Remapping] {} for remapping '{}'"
if TYPE_CHECKING:
    from battle_modifiers_common import ModifiersContext
    from battle_modifiers_ext.remapping.remapping_composers import IComposer
g_cache = None

class RemappingCache(object):
    __slots__ = (b'__remapping',)

    def __init__(self):
        self.__readConfig()
        return

    def __repr__(self):
        return (b'RemappingCache({})').format(self.__remapping)

    def getValue(self, modifierName, remappingName, oldValue, ctx):
        composer = self.__remapping.get(remappingName, {}).get(modifierName)
        if composer is not None:
            return composer.getValue(ctx, oldValue)
        else:
            return

    def getValues(self, modifierName, remappingName, oldValue):
        composer = self.__remapping.get(remappingName, {}).get(modifierName)
        if composer is not None:
            return composer.getValues(oldValue)
        else:
            return

    def reloadCache(self, configPath=b''):
        self.__readConfig(configPath)
        return

    def __readConfig(self, configPath=b''):
        configPath = configPath or REMAPPING_XML_PATH
        config = ResMgr.openSection(configPath)
        if config is None:
            raise SoftException((b"[Remapping] Cannot open or read '{}'").format(configPath))
        self.__remapping = {}
        for remappingName, remappingSection in config.items():
            if remappingName == b'xmlns:xmlref':
                continue
            if remappingName not in RemappingNames.ALL:
                raise SoftException((b"[Remapping] Invalid remapping name '{}'").format(remappingName))
            self.__remapping[remappingName] = self.__readRemappingSection(remappingSection)

        return

    def __readRemappingSection(self, config):
        remappingName = config.name
        if not config.has_key(b'conditions'):
            raise SoftException(ERR_TEMPLATE.format(b'Missing conditions', remappingName))
        conditions = readConditions(config[b'conditions'], remappingName)
        if not config.has_key(b'composers'):
            raise SoftException(ERR_TEMPLATE.format(b'Missing composers', remappingName))
        return readComposers(config[b'composers'], remappingName, conditions)


def init():
    global g_cache
    g_cache = RemappingCache()
    return
