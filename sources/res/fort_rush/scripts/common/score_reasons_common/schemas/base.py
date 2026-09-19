from __future__ import absolute_import
from typing import List
from dict2model import fields, models, schemas, validate

class ScoreReasonModel(models.Model):
    __slots__ = (b'name',)

    def __init__(self, name):
        super(ScoreReasonModel, self).__init__()
        self.name = name
        return

    def _reprArgs(self):
        return (b'name={}').format(self.name)


scoreReasonSchema = schemas.Schema[ScoreReasonModel](fields={b'name': (fields.String(required=True, deserializedValidators=validate.Length(minValue=1, maxValue=50)))}, checkUnknown=False, modelClass=ScoreReasonModel)

class ScopeType(object):
    TEAM = b'team'
    VEHICLE = b'vehicle'


class ScopeModel(models.Model):
    __slots__ = (b'scopeType', b'reason')

    def __init__(self, scopeType, reason):
        super(ScopeModel, self).__init__()
        self.scopeType = scopeType
        self.reason = reason
        return

    def _reprArgs(self):
        return (b'scopeType={}, reason={}').format(self.scopeType, self.reason)


ScopeSchema = schemas.Schema[ScopeModel](fields={b'scopeType': (fields.String(required=True, deserializedValidators=validate.OneOf([ScopeType.TEAM, ScopeType.VEHICLE]))), 
   b'reason': (fields.UniCapList(fields.Nested(schema=scoreReasonSchema), required=False, default=[]))}, checkUnknown=False, modelClass=ScopeModel)

class ExtensionModel(models.Model):
    __slots__ = (b'name', b'scope')

    def __init__(self, name, scope):
        super(ExtensionModel, self).__init__()
        self.name = name
        self.scope = scope
        return

    def _reprArgs(self):
        return (b'name={}, scope={}').format(self.name, self.scope)


ExtensionSchema = schemas.Schema[ExtensionModel](fields={b'name': (fields.String(required=True, deserializedValidators=validate.Length(minValue=1, maxValue=50))), 
   b'scope': (fields.UniCapList(fields.Nested(schema=ScopeSchema), required=False, default=[]))}, checkUnknown=False, modelClass=ExtensionModel)
