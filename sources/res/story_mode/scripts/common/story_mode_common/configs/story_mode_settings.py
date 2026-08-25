import typing
from game_params_common.base_manager import GameParamsSchema
from dict2model import models, fields, validate, schemas
from game_params_common.scope import GameParamsScopeFlags
if typing.TYPE_CHECKING:
    import datetime

class EntryPointSettingsModel(models.Model):
    __slots__ = (b'eventStartAt', b'eventEndAt')

    def __init__(self, eventStartAt, eventEndAt):
        super(EntryPointSettingsModel, self).__init__()
        self.eventStartAt = eventStartAt
        self.eventEndAt = eventEndAt
        return


class SettingsModel(models.Model):
    __slots__ = (b'enabled', b'waitTimeQueue', b'hideGameLoadingTimeout', b'joinToQueueFromLogin', b'afk', b'entryPoint', b'modeSelectorCardColumn', b'modeSelectorCardPriority', b'newbieBannerEnabled', b'newbieAdvertisingEnabled', b'parallaxEnabled', b'eventName')

    def __init__(self, enabled, waitTimeQueue, hideGameLoadingTimeout, joinToQueueFromLogin, afk, entryPoint, modeSelectorCardColumn, modeSelectorCardPriority, newbieBannerEnabled, newbieAdvertisingEnabled, parallaxEnabled, eventName):
        super(SettingsModel, self).__init__()
        self.enabled = enabled
        self.waitTimeQueue = waitTimeQueue
        self.hideGameLoadingTimeout = hideGameLoadingTimeout
        self.joinToQueueFromLogin = joinToQueueFromLogin
        self.afk = afk
        self.entryPoint = entryPoint
        self.modeSelectorCardColumn = modeSelectorCardColumn
        self.modeSelectorCardPriority = modeSelectorCardPriority
        self.newbieBannerEnabled = newbieBannerEnabled
        self.newbieAdvertisingEnabled = newbieAdvertisingEnabled
        self.parallaxEnabled = parallaxEnabled
        self.eventName = eventName
        return


class AfkModel(models.Model):
    __slots__ = (b'maxPlayerInactiveTime', b'arenaWaitPlayerTime')

    def __init__(self, maxPlayerInactiveTime, arenaWaitPlayerTime):
        super(AfkModel, self).__init__()
        self.maxPlayerInactiveTime = maxPlayerInactiveTime
        self.arenaWaitPlayerTime = arenaWaitPlayerTime
        return


class AfkModesModel(models.Model):
    __slots__ = (b'onboarding', b'regular')

    def __init__(self, onboarding, regular):
        super(AfkModesModel, self).__init__()
        self.onboarding = onboarding
        self.regular = regular
        return


_bannerSettingsSchema = schemas.Schema(fields={b'eventStartAt': (fields.DateTime()), 
   b'eventEndAt': (fields.DateTime())}, modelClass=EntryPointSettingsModel)
afkSchema = schemas.Schema(fields={b'maxPlayerInactiveTime': (fields.Integer(required=True, deserializedValidators=validate.Range(minValue=1))), 
   b'arenaWaitPlayerTime': (fields.Integer(required=True, deserializedValidators=validate.Range(minValue=1)))}, modelClass=AfkModel, checkUnknown=True)
afkModesSchema = schemas.Schema(fields={b'onboarding': (fields.Nested(schema=afkSchema, required=True)), 
   b'regular': (fields.Nested(schema=afkSchema, required=True))}, modelClass=AfkModesModel, checkUnknown=True)
settingsSchema = GameParamsSchema[SettingsModel](gameParamsKey=b'story_mode_settings', fields={b'enabled': (fields.Boolean(required=True)), 
   b'waitTimeQueue': (fields.Integer(required=True, deserializedValidators=validate.Range(minValue=1))), 
   b'hideGameLoadingTimeout': (fields.Integer(required=True, deserializedValidators=validate.Range(minValue=1))), 
   b'joinToQueueFromLogin': (fields.Boolean(required=True, filterParams=GameParamsScopeFlags.BASE)), 
   b'modeSelectorCardColumn': (fields.Integer(required=True, deserializedValidators=validate.Range(minValue=1, maxValue=3))), 
   b'modeSelectorCardPriority': (fields.Integer(required=True)), 
   b'afk': (fields.Nested(schema=afkModesSchema, required=True, filterParams=GameParamsScopeFlags.BASE)), 
   b'entryPoint': (fields.Nested(schema=_bannerSettingsSchema)), 
   b'newbieBannerEnabled': (fields.Boolean(required=True)), 
   b'newbieAdvertisingEnabled': (fields.Boolean(required=True)), 
   b'parallaxEnabled': (fields.Boolean(required=True)), 
   b'eventName': (fields.NonEmptyString(required=True))}, modelClass=SettingsModel, checkUnknown=True, usedInReplay=True)
