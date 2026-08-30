from __future__ import absolute_import
import typing
from game_params_common.schema import GameParamsSchema
from constants import ARENA_BONUS_TYPE_IDS
from dict2model import models, validate
from dict2model.fields import Boolean, Integer, List, String
from dict2model.schemas import Schema
from soft_exception import SoftException
if typing.TYPE_CHECKING:
    from dict2model.types import ValidatorsType
    from dict2model.fields import Field

class BaseHintModel(models.Model):
    __slots__ = (b'hintType', b'viewClass')
    _VIEW_CLASS_DELIMITER = b':'

    def __init__(self, hintType, viewClass):
        super(BaseHintModel, self).__init__()
        self.hintType = hintType
        self.viewClass = viewClass
        return

    def isEnabledFor(self, arenaBonusType):
        raise NotImplementedError
        return

    def splitViewClass(self):
        return self.viewClass.split(self._VIEW_CLASS_DELIMITER)

    def _reprArgs(self):
        return (b'hintType={}, viewClass={}').format(self.hintType, self.viewClass)


_BHMType = typing.TypeVar(b'_BHMType', bound=BaseHintModel)

class BaseHintSchema(Schema[_BHMType]):

    def __init__(self, fields, modelClass, checkUnknown=True, serializedValidators=None, deserializedValidators=None):
        if not issubclass(modelClass, BaseHintModel):
            raise SoftException(b'modelClass should be a subclass of BaseHintModel')
        baseFields = {b'hintType': (String(required=True, default=b'', deserializedValidators=[
                       validate.Length(minValue=1, maxValue=100)])), 
           b'viewClass': (String(required=False, default=b''))}
        baseFields.update(fields)
        super(BaseHintSchema, self).__init__(fields=baseFields, checkUnknown=checkUnknown, serializedValidators=serializedValidators, deserializedValidators=deserializedValidators, modelClass=modelClass)
        return

    def validateRegistered(self, hints):
        return


class HintModel(BaseHintModel):
    __slots__ = (b'arenaBonusTypes',)

    def __init__(self, arenaBonusTypes, hintType, viewClass):
        super(HintModel, self).__init__(hintType, viewClass)
        self.arenaBonusTypes = arenaBonusTypes
        return

    def isEnabledFor(self, arenaBonusType):
        return arenaBonusType in self.arenaBonusTypes


class HintSchema(BaseHintSchema[HintModel]):

    def __init__(self):
        super(HintSchema, self).__init__(fields={b'arenaBonusTypes': (List(required=True, fieldOrSchema=Integer(deserializedValidators=[
                              validate.OneOf(ARENA_BONUS_TYPE_IDS.keys())])))}, checkUnknown=True, modelClass=HintModel)
        return


hintSchema = HintSchema()

class PrebattleHintsConfigModel(models.Model):
    __slots__ = (b'enabled', b'battleTimerThreshold')

    def __init__(self, enabled, battleTimerThreshold):
        super(PrebattleHintsConfigModel, self).__init__()
        self.enabled = enabled
        self.battleTimerThreshold = battleTimerThreshold
        return

    def _reprArgs(self):
        return (b'enabled={}, battleTimerThreshold={}').format(self.enabled, self.battleTimerThreshold)


configSchema = GameParamsSchema[PrebattleHintsConfigModel](gameParamsKey=b'prebattle_hints_config', fields={b'enabled': (Boolean(required=True)), 
   b'battleTimerThreshold': (Integer(required=True, deserializedValidators=validate.Range(minValue=0)))}, modelClass=PrebattleHintsConfigModel)
