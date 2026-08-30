from __future__ import absolute_import
import logging, typing
from future.utils import listvalues
from dict2model import exceptions
from hints_common.battle.schemas.base import HMCType, CommonHintSchema
from hints_common.common.manager import BaseHintsModelsManager
from py2to3 import patched_typing
_logger = logging.getLogger(__name__)
_g_manager = None
DEFAULT_XML = b'scripts/item_defs/hints/battle_hints.xml'

class CommonBattleHintsModelsManager(BaseHintsModelsManager, patched_typing.Generic[HMCType]):
    __slots__ = (b'_hints', b'_hintsBySchemas')

    def __init__(self, schemaTag, defaultSchema):
        self._hints = {}
        self._hintsBySchemas = {}
        super(CommonBattleHintsModelsManager, self).__init__(DEFAULT_XML, defaultSchema, schemaTag=schemaTag)
        return

    def get(self, uniqueName):
        return self._hints.get(uniqueName)

    def getAll(self):
        return listvalues(self._hints)

    def getBySchema(self, schema):
        return self._hintsBySchemas.get(schema, [])

    def _addToStorage(self, schema, model):
        if model.uniqueName in self._hints:
            raise exceptions.ValidationError((b'{} already exist.').format(model.uniqueName))
        model.prepare(schema)
        self._hints[model.uniqueName] = model
        self._hintsBySchemas.setdefault(schema, []).append(model)
        return

    def _checkSchemaType(self, schema):
        if not isinstance(schema, CommonHintSchema):
            raise exceptions.ValidationError((b'Schema type must be {} or inherited.').format(CommonHintSchema))
        return


def init(schemaTag, defaultSchema):
    global _g_manager
    if _g_manager is None:
        _g_manager = CommonBattleHintsModelsManager(schemaTag=schemaTag, defaultSchema=defaultSchema)
        _logger.debug(b'Battle hints models manager created from: %s.', DEFAULT_XML)
    return


def get():
    if _g_manager is None:
        _logger.error(b'Battle hints models manager not initialized.')
    return _g_manager
