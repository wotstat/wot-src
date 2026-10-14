from __future__ import absolute_import
import logging
from score_reasons_common.schemas.base import ExtensionSchema, ScoreReasonModel
from typing import Optional, List, Dict
import section2dict
from dict2model import exceptions
from extension_utils import ResMgr
_logger = logging.getLogger(__name__)
_g_manager = None
DEFAULT_XML = b'scripts/item_defs/score_reasons/score_reasons.xml'

def _readScoreReasonsXml(xmlPath):
    section = ResMgr.openSection(xmlPath)
    if section is None:
        _logger.error(b'Broken xml schemas source: %s.', xmlPath)
        return
    else:
        extensions = section2dict.parse(section).get(b'extension', [])
        extensions = extensions if isinstance(extensions, list) else [extensions]
        if not extensions:
            _logger.debug(b'File <%s> section [%s] empty or does not exist.', xmlPath, b'extension')
        ResMgr.purge(xmlPath, True)
        return extensions


class ScoreReasonsModelsManager(object):
    _UNIQUE_NAME_PARTS_COUNT = 3
    _UNIQUE_NAME_SCOPE_INDEX = 1
    __slots__ = (b'_reasons', b'_reasonsByScope')

    def __init__(self):
        self._reasons = {}
        self._reasonsByScope = {}
        self._registerFromXml(DEFAULT_XML)
        return

    def getScoreReasonModel(self, uniqueName):
        return self._reasons.get(uniqueName)

    def getAllUniqueNames(self):
        return list(self._reasons)

    @property
    def reasonsByScope(self):
        return self._reasonsByScope

    def getUniqueNamesByScope(self, scopeKey):
        return self._reasonsByScope.get(scopeKey, [])

    def isReasonInScope(self, uniqueName, scopeType):
        parts = uniqueName.split(b'.')
        return len(parts) >= self._UNIQUE_NAME_PARTS_COUNT and parts[self._UNIQUE_NAME_SCOPE_INDEX] == scopeType

    def _registerFromXml(self, xmlPath):
        errors = None
        for extIndex, rawExtData in enumerate(_readScoreReasonsXml(xmlPath)):
            try:
                extensionModel = ExtensionSchema.deserialize(rawExtData, silent=False)
                for scopeModel in extensionModel.scope:
                    scopeKey = (b'{}.{}').format(extensionModel.name, scopeModel.scopeType)
                    for reasonModel in scopeModel.reason:
                        uniqueName = (b'{}.{}').format(scopeKey, reasonModel.name)
                        if uniqueName in self._reasons:
                            raise exceptions.ValidationError((b'{} already exist.').format(uniqueName))
                        self._reasons[uniqueName] = reasonModel
                        self._reasonsByScope.setdefault(scopeKey, []).append(uniqueName)

            except exceptions.ValidationError as ve:
                error = exceptions.ValidationErrorMessage(ve.error.data, title=(b'Extension[{}]').format(extIndex))
                errors = errors + error if errors else error

        if errors:
            raise exceptions.ValidationError(errors)
        return


def init():
    global _g_manager
    if _g_manager is None:
        _g_manager = ScoreReasonsModelsManager()
        _logger.debug(b'Score reasons models manager created from: %s.', DEFAULT_XML)
    return


def get():
    if _g_manager is None:
        _logger.error(b'Score reasons models manager not initialized.')
    return _g_manager
