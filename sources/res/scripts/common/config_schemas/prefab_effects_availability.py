from __future__ import absolute_import
from game_params_common.schema import GameParamsSchema
from dict2model import fields, models

class PrefabEffectsAvailabilityModel(models.Model):
    __slots__ = (b'enabled', b'switchEnabled')

    def __init__(self, enabled, switchEnabled):
        super(PrefabEffectsAvailabilityModel, self).__init__()
        self.enabled = enabled
        self.switchEnabled = switchEnabled
        return


prefabEffectsAvailabilitySchema = GameParamsSchema[PrefabEffectsAvailabilityModel](gameParamsKey=b'prefab_effects_availability_config', modelClass=PrefabEffectsAvailabilityModel, fields={b'enabled': (fields.Boolean(required=False, default=True)), 
   b'switchEnabled': (fields.Boolean(required=False, default=False))}, usedInReplay=True)
