from __future__ import absolute_import
from dict2model import models, fields
from game_params_common.schema import GameParamsSchema

class NewbieBattleHintsConfigModel(models.Model):
    __slots__ = (b'enabled',)

    def __init__(self, enabled):
        super(NewbieBattleHintsConfigModel, self).__init__()
        self.enabled = enabled
        return

    def _reprArgs(self):
        return (b'enabled={}').format(self.enabled)


configSchema = GameParamsSchema[NewbieBattleHintsConfigModel](gameParamsKey=b'newbie_battle_hints_config', fields={b'enabled': (fields.Boolean(required=True))}, modelClass=NewbieBattleHintsConfigModel)
