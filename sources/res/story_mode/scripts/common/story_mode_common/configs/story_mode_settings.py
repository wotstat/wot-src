from base_schema_manager import GameParamsSchema
from dict2model import models, fields, validate, schemas

class SettingsModel(models.Model):
    __slots__ = (b'enabled', b'waitTimeQueue', b'hideGameLoadingTimeout', b'joinToQueueFromLogin', b'quotums', b'afk')

    def __init__(self, enabled, waitTimeQueue, hideGameLoadingTimeout, joinToQueueFromLogin, quotums, afk):
        super(SettingsModel, self).__init__()
        self.enabled = enabled
        self.waitTimeQueue = waitTimeQueue
        self.hideGameLoadingTimeout = hideGameLoadingTimeout
        self.joinToQueueFromLogin = joinToQueueFromLogin
        self.quotums = quotums
        self.afk = afk
        return

    def __repr__(self):
        return (b'<SettingsModel(enabled={}, waitTimeQueue={}, hideGameLoadingTimeout={}, joinToQueueFromLogin={}, quotums={}), afk={}>').format(self.enabled, self.waitTimeQueue, self.hideGameLoadingTimeout, self.joinToQueueFromLogin, self.quotums, self.afk)


class AfkModel(models.Model):
    __slots__ = (b'maxPlayerInactiveTime', b'arenaWaitPlayerTime')

    def __init__(self, maxPlayerInactiveTime, arenaWaitPlayerTime):
        super(AfkModel, self).__init__()
        self.maxPlayerInactiveTime = maxPlayerInactiveTime
        self.arenaWaitPlayerTime = arenaWaitPlayerTime
        return

    def __repr__(self):
        return (b'<AfkModel(maxPlayerInactiveTime={}, arenaWaitPlayerTime={})>').format(self.maxPlayerInactiveTime, self.arenaWaitPlayerTime)


afkSchema = schemas.Schema(fields={b'maxPlayerInactiveTime': (fields.Integer(public=False, required=True, serializedValidators=validate.Range(minValue=1), deserializedValidators=validate.Range(minValue=1))), 
   b'arenaWaitPlayerTime': (fields.Integer(public=False, required=True, serializedValidators=validate.Range(minValue=1), deserializedValidators=validate.Range(minValue=1)))}, modelClass=AfkModel, checkUnknown=True)
settingsSchema = GameParamsSchema(gameParamsKey=b'story_mode_settings', fields={b'enabled': (fields.Boolean(required=True)), 
   b'waitTimeQueue': (fields.Integer(required=True, serializedValidators=validate.Range(minValue=1), deserializedValidators=validate.Range(minValue=1))), 
   b'hideGameLoadingTimeout': (fields.Integer(required=True, serializedValidators=validate.Range(minValue=1), deserializedValidators=validate.Range(minValue=1))), 
   b'joinToQueueFromLogin': (fields.Boolean(required=True)), 
   b'quotums': (fields.List(fieldOrSchema=fields.Integer(serializedValidators=validate.Range(minValue=1), deserializedValidators=validate.Range(minValue=1)), required=True, serializedValidators=validate.Length(minValue=3), deserializedValidators=validate.Length(minValue=3))), 
   b'afk': (fields.Nested(schema=afkSchema, required=True, public=False))}, modelClass=SettingsModel, checkUnknown=True)
