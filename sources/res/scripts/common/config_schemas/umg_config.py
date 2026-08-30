from __future__ import absolute_import
from game_params_common.schema import GameParamsSchema
from dict2model import fields, models

class ConfigModel(models.Model):
    __slots__ = (b'enableAllDaily', b'enableAllWeekly', b'enableDailyWeeklyUI', b'enablePM3Banner')

    def __init__(self, enableAllDaily, enableAllWeekly, enableDailyWeeklyUI, enablePM3Banner):
        super(ConfigModel, self).__init__()
        self.enableAllDaily = enableAllDaily
        self.enableAllWeekly = enableAllWeekly
        self.enableDailyWeeklyUI = enableDailyWeeklyUI
        self.enablePM3Banner = enablePM3Banner
        return

    def _reprArgs(self):
        return b'enableAllDaily=%s, enableAllWeekly=%s, enableDailyWeeklyUI=%s, enablePM3Banner=%s' % (
         self.enableAllDaily, self.enableAllWeekly, self.enableDailyWeeklyUI, self.enablePM3Banner)


umgConfigSchema = GameParamsSchema[ConfigModel](gameParamsKey=b'umgConfig', modelClass=ConfigModel, fields={b'enableAllDaily': (fields.Integer()), 
   b'enableAllWeekly': (fields.Integer()), 
   b'enableDailyWeeklyUI': (fields.Integer()), 
   b'enablePM3Banner': (fields.Integer())})
