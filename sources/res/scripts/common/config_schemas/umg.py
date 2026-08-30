from __future__ import absolute_import
from game_params_common.schema import GameParamsSchema
from dict2model import fields, models, schemas, validate
import typing

class WeightModel(models.Model):
    __slots__ = (b'name', b'weight')

    def __init__(self, name, weight):
        super(WeightModel, self).__init__()
        self.name = name
        self.weight = weight
        return

    def _reprArgs(self):
        return (b'name={}, weight={}').format(self.name, self.weight)


class WeightsModel(models.Model):
    __slots__ = (b'weights', b'_weightByName')

    def __init__(self, weights):
        super(WeightsModel, self).__init__()
        self.weights = weights
        self._weightByName = {p.name: p for p in self.weights}
        return

    def getWeightByName(self, name):
        return self._weightByName.get(name, None)

    def _reprArgs(self):
        return (b'weights={}').format(self.weights)


_weightSchema = schemas.Schema[WeightModel](modelClass=WeightModel, fields={b'name': (fields.String(deserializedValidators=validate.Length(minValue=2))), 
   b'weight': (fields.Integer(deserializedValidators=validate.Range(0, 1000)))})
umgMissionsConfigSchema = GameParamsSchema[WeightsModel](gameParamsKey=b'umgMissions', modelClass=WeightsModel, fields={b'weights': (fields.UniCapList(fieldOrSchema=_weightSchema, deserializedValidators=[
              validate.Length(minValue=1), validate.ValidateIterable([validate.IterableOfUnique(b'name')])]))})
umgEventsConfigSchema = GameParamsSchema[WeightsModel](gameParamsKey=b'umgEvents', modelClass=WeightsModel, fields={b'weights': (fields.UniCapList(fieldOrSchema=_weightSchema, deserializedValidators=[
              validate.Length(minValue=1), validate.ValidateIterable([validate.IterableOfUnique(b'name')])]))})
