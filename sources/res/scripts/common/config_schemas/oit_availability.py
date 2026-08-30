from __future__ import absolute_import
from game_params_common.schema import GameParamsSchema
from dict2model import fields, models

class OitAvailabilityModel(models.Model):
    __slots__ = (b'min', b'low', b'medium', b'high', b'ultra')

    def __init__(self, min, low, medium, high, ultra):
        super(OitAvailabilityModel, self).__init__()
        self.min = min
        self.low = low
        self.medium = medium
        self.high = high
        self.ultra = ultra
        return


oitAvailabilitySchema = GameParamsSchema[OitAvailabilityModel](gameParamsKey=b'oit_availability_config', modelClass=OitAvailabilityModel, fields={b'min': (fields.Boolean(required=False, default=False)), 
   b'low': (fields.Boolean(required=False, default=False)), 
   b'medium': (fields.Boolean(required=False, default=False)), 
   b'high': (fields.Boolean(required=False, default=False)), 
   b'ultra': (fields.Boolean(required=False, default=False))})
