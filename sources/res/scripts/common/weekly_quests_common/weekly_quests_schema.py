from __future__ import absolute_import
from game_params_common.schema import GameParamsSchema
from constants import Configs
from dict2model import fields, models, validate

class WeeklyQuestsConfigModel(models.Model):
    __slots__ = (b'enabled', b'rerollTimeout')

    def __init__(self, enabled, rerollTimeout):
        super(WeeklyQuestsConfigModel, self).__init__()
        self.enabled = enabled
        self.rerollTimeout = rerollTimeout
        return

    def _reprArgs(self):
        return (b'enabled={}, rerollTimeout={}').format(self.enabled, self.rerollTimeout)


weeklyQuestsSchema = GameParamsSchema[WeeklyQuestsConfigModel](gameParamsKey=Configs.WEEKLY_QUESTS_CONFIG.value, fields={b'enabled': (fields.Boolean(required=True)), 
   b'rerollTimeout': (fields.Integer(required=True, deserializedValidators=validate.Range(minValue=1)))}, modelClass=WeeklyQuestsConfigModel, checkUnknown=True)
