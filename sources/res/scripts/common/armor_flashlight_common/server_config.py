from __future__ import absolute_import
from game_params_common.schema import GameParamsSchema
from dict2model import models, fields

class ServerConfigModel(models.Model):
    __slots__ = (b'enabled',)

    def __init__(self, enabled):
        super(ServerConfigModel, self).__init__()
        self.enabled = enabled
        return

    def _reprArgs(self):
        return (b'enabled={}').format(self.enabled)


serverConfigSchema = GameParamsSchema[ServerConfigModel](gameParamsKey=b'armor_flashlight_config', fields={b'enabled': (fields.Boolean(required=True))}, modelClass=ServerConfigModel)
