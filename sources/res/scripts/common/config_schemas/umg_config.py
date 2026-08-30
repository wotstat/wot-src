from __future__ import absolute_import
import typing
from game_params_common.schema import GameParamsSchema
from dict2model import fields, models, schemas

class ConfigModel(models.Model):
    __slots__ = (b'enableAllDaily', b'enableAllWeekly', b'enableDailyWeeklyUI', b'enablePM3Banner', b'slides')

    def __init__(self, enableAllDaily, enableAllWeekly, enableDailyWeeklyUI, enablePM3Banner, slides):
        super(ConfigModel, self).__init__()
        self.enableAllDaily = enableAllDaily
        self.enableAllWeekly = enableAllWeekly
        self.enableDailyWeeklyUI = enableDailyWeeklyUI
        self.enablePM3Banner = enablePM3Banner
        self.slides = list(slides)
        return

    def _reprArgs(self):
        return b'enableAllDaily=%s, enableAllWeekly=%s, enableDailyWeeklyUI=%s, enablePM3Banner=%s, slides=%s' % (
         self.enableAllDaily, self.enableAllWeekly, self.enableDailyWeeklyUI, self.enablePM3Banner, self.slides)


class SlideModel(models.Model):
    __slots__ = (b'name', b'priority', b'enabled')

    def __init__(self, name, priority, enabled):
        super(SlideModel, self).__init__()
        self.name = name
        self.priority = priority
        self.enabled = enabled
        return

    def _reprArgs(self):
        return b'name=%s, priority=%s, enabled=%s' % (self.name, self.priority, self.enabled)


slideSchema = schemas.Schema(modelClass=SlideModel, fields={b'name': (fields.String(required=True)), 
   b'priority': (fields.Integer(required=True)), 
   b'enabled': (fields.Boolean(required=True))})
umgConfigSchema = GameParamsSchema[ConfigModel](gameParamsKey=b'umgConfig', modelClass=ConfigModel, fields={b'enableAllDaily': (fields.Integer(required=True)), 
   b'enableAllWeekly': (fields.Integer(required=True)), 
   b'enableDailyWeeklyUI': (fields.Integer(required=True)), 
   b'enablePM3Banner': (fields.Integer(required=True)), 
   b'slides': (fields.UniCapList(fieldOrSchema=slideSchema, required=True))})
