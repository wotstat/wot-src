from __future__ import absolute_import
import typing
from constants import MAX_VEHICLE_LEVEL, MIN_VEHICLE_LEVEL, VEHICLE_CLASS
from dict2model import models, schemas, fields, validate
from fort_rush_common.fort_rush_constants import EXT_GAME_PARAMS_KEY
from game_params_common.schema import GameParamsSchema
from game_params_common.scope import GameParamsScopeFlags
_VEHICLE_CLASSES = (
 VEHICLE_CLASS.LIGHT_TANK, VEHICLE_CLASS.MEDIUM_TANK, VEHICLE_CLASS.HEAVY_TANK, VEHICLE_CLASS.SPG,
 VEHICLE_CLASS.AT_SPG)
if typing.TYPE_CHECKING:
    from typing import List
    from Arena import Arena
_DEFAULT_MODE_SELECTOR_COLUMN = 1
_DEFAULT_MODE_SELECTOR_PRIORITY = 40

class StageModel(models.Model):
    __slots__ = (b'quest', b'level')

    def __init__(self, quest, level):
        super(StageModel, self).__init__()
        self.quest = quest
        self.level = level
        return


class ProgressionModel(models.Model):
    __slots__ = (b'stage',)

    def __init__(self, stage):
        super(ProgressionModel, self).__init__()
        self.stage = stage
        return


class DailyMissionsConfigModel(models.Model):
    __slots__ = (b'dailyMissionQuestPrefix', b'hardDailyMissionQuestPrefix', b'dailyMissionTokenPrefix', b'dailyMissionTokenPostfix', b'dailyMissionTokenTtl', b'tokenLimit', b'dailyGroupsCount', b'dailyQuestMaxDays')

    def __init__(self, dailyMissionQuestPrefix, hardDailyMissionQuestPrefix, dailyMissionTokenPrefix, dailyMissionTokenPostfix, dailyMissionTokenTtl, tokenLimit, dailyGroupsCount, dailyQuestMaxDays):
        super(DailyMissionsConfigModel, self).__init__()
        self.dailyMissionQuestPrefix = dailyMissionQuestPrefix
        self.hardDailyMissionQuestPrefix = hardDailyMissionQuestPrefix
        self.dailyMissionTokenPrefix = dailyMissionTokenPrefix
        self.dailyMissionTokenPostfix = dailyMissionTokenPostfix
        self.dailyMissionTokenTtl = dailyMissionTokenTtl
        self.tokenLimit = tokenLimit
        self.dailyGroupsCount = dailyGroupsCount
        self.dailyQuestMaxDays = dailyQuestMaxDays
        return


class _AwardsByPlace(models.Model):
    __slots__ = (b'win', b'loss', b'draw')

    def __init__(self, win, loss, draw):
        super(_AwardsByPlace, self).__init__()
        self.win = win
        self.loss = loss
        self.draw = draw
        return

    def getAwardForWin(self, place):
        return self._getPointsByPlace(place, self.win)

    def getAwardForLoss(self, place):
        return self._getPointsByPlace(place, self.loss)

    def getAwardForDraw(self, place):
        return self._getPointsByPlace(place, self.draw)

    @classmethod
    def _getPointsByPlace(cls, place, pointsList):
        if 0 <= place < len(pointsList):
            return pointsList[place]
        return 0


class _BattleEconomyModel(models.Model):
    __slots__ = (b'creditsByPlace', b'progressionPointsByPlace')

    def __init__(self, creditsByPlace, progressionPointsByPlace):
        super(_BattleEconomyModel, self).__init__()
        self.creditsByPlace = creditsByPlace
        self.progressionPointsByPlace = progressionPointsByPlace
        return


class ControllableZonesModel(models.Model):
    __slots__ = (b'autoSpotDelaySeconds', b'owned2NeutralTime', b'neutral2OwnedTime', b'progressResetFactor', b'maxHealthHealPercentage')

    def __init__(self, owned2NeutralTime, neutral2OwnedTime, progressResetFactor, maxHealthHealPercentage, autoSpotDelaySeconds):
        super(ControllableZonesModel, self).__init__()
        self.owned2NeutralTime = owned2NeutralTime
        self.neutral2OwnedTime = neutral2OwnedTime
        self.progressResetFactor = progressResetFactor
        self.maxHealthHealPercentage = maxHealthHealPercentage
        self.autoSpotDelaySeconds = autoSpotDelaySeconds
        return


class BattleModel(models.Model):
    __slots__ = (b'controllableZones',)

    def __init__(self, controllableZones):
        super(BattleModel, self).__init__()
        self.controllableZones = controllableZones
        return


class SquadTagRestrictionModel(models.Model):
    __slots__ = (b'maxCount', b'levels')

    def __init__(self, maxCount, levels):
        super(SquadTagRestrictionModel, self).__init__()
        self.maxCount = maxCount
        self.levels = levels
        return


class SquadRestrictionsModel(models.Model):
    __slots__ = (b'tags',)

    def __init__(self, tags):
        super(SquadRestrictionsModel, self).__init__()
        self.tags = tags
        return

    def toPlatoonRestrictionsDict(self):
        return {b'tags': {tag: [restriction.toDict()] for tag, restriction in self.tags.items()}}


class FortRushBattlesConfigModel(models.Model):
    __slots__ = (b'modeSelectorCardColumn', b'modeSelectorCardPriority', b'isEnabled', b'technicalPause', b'startDatetime', b'endDatetime', b'isInfoPageEnabled', b'baseProgressionToken', b'completedProgressionToken', b'progressionQuestPrefix', b'maxRewardsAmountPerStage', b'progression', b'dailyMissionsConfig', b'battleEconomy', b'eligibleVehicleTiers', b'forbiddenVehClasses', b'squadRestrictions', b'battle')

    def __init__(self, modeSelectorCardColumn, modeSelectorCardPriority, isEnabled, technicalPause, startDatetime, endDatetime, isInfoPageEnabled, baseProgressionToken, completedProgressionToken, progressionQuestPrefix, maxRewardsAmountPerStage, progression, dailyMissionsConfig, battleEconomy, eligibleVehicleTiers, forbiddenVehClasses, squadRestrictions, battle):
        super(FortRushBattlesConfigModel, self).__init__()
        self.modeSelectorCardColumn = modeSelectorCardColumn
        self.modeSelectorCardPriority = modeSelectorCardPriority
        self.isEnabled = isEnabled
        self.technicalPause = technicalPause
        self.startDatetime = startDatetime
        self.endDatetime = endDatetime
        self.isInfoPageEnabled = isInfoPageEnabled
        self.baseProgressionToken = baseProgressionToken.strip()
        self.completedProgressionToken = completedProgressionToken.strip()
        self.progressionQuestPrefix = progressionQuestPrefix
        self.maxRewardsAmountPerStage = maxRewardsAmountPerStage
        self.progression = progression
        self.dailyMissionsConfig = dailyMissionsConfig
        self.battleEconomy = battleEconomy
        self.eligibleVehicleTiers = eligibleVehicleTiers
        self.forbiddenVehClasses = forbiddenVehClasses
        self.squadRestrictions = squadRestrictions
        self.battle = battle
        return


_stageSchema = schemas.Schema(fields={b'quest': (fields.NonEmptyString(required=True)), 
   b'level': (fields.Integer(required=True, deserializedValidators=validate.Range(minValue=1)))}, modelClass=StageModel, checkUnknown=True)
_progressionSchema = schemas.Schema(fields={b'stage': (fields.UniCapList(fieldOrSchema=_stageSchema, required=True, deserializedValidators=validate.Length(minValue=1)))}, modelClass=ProgressionModel, checkUnknown=True)
_dailyMissionsConfigSchema = schemas.Schema(fields={b'dailyMissionQuestPrefix': (fields.NonEmptyString(required=True)), 
   b'hardDailyMissionQuestPrefix': (fields.NonEmptyString(required=True)), 
   b'dailyMissionTokenPrefix': (fields.NonEmptyString(required=True)), 
   b'dailyMissionTokenPostfix': (fields.NonEmptyString(required=True)), 
   b'dailyMissionTokenTtl': (fields.Integer(required=True, deserializedValidators=validate.Range(minValue=1))), 
   b'tokenLimit': (fields.Integer(required=True, deserializedValidators=validate.Range(minValue=1))), 
   b'dailyGroupsCount': (fields.Integer(required=True)), 
   b'dailyQuestMaxDays': (fields.Integer(required=True))}, modelClass=DailyMissionsConfigModel, checkUnknown=True)

def _createAwardsForPlaceList():
    return fields.ListFromString(field=fields.Integer(deserializedValidators=validate.Range(minValue=0)))


_awardsByPlaceSchema = schemas.Schema(fields={b'win': (_createAwardsForPlaceList()), 
   b'loss': (_createAwardsForPlaceList()), 
   b'draw': (_createAwardsForPlaceList())}, modelClass=_AwardsByPlace, checkUnknown=True)
_battleEconomySchema = schemas.Schema(fields={b'creditsByPlace': (fields.Nested(schema=_awardsByPlaceSchema, required=True)), 
   b'progressionPointsByPlace': (fields.Nested(schema=_awardsByPlaceSchema, required=True))}, modelClass=_BattleEconomyModel, checkUnknown=True)
_controllableZonesSchema = schemas.Schema[ControllableZonesModel](fields={b'autoSpotDelaySeconds': (fields.Float(required=False, default=2, filterParams=GameParamsScopeFlags.CELL_ARENA)), 
   b'owned2NeutralTime': (fields.Integer(required=True, filterParams=GameParamsScopeFlags.CELL_ARENA)), 
   b'neutral2OwnedTime': (fields.Integer(required=True, filterParams=GameParamsScopeFlags.CELL_ARENA)), 
   b'progressResetFactor': (fields.Float(required=True, filterParams=GameParamsScopeFlags.CELL_ARENA)), 
   b'maxHealthHealPercentage': (fields.Float(required=True, filterParams=GameParamsScopeFlags.CELL_ARENA, deserializedValidators=validate.Range(minValue=0, maxValue=1)))}, modelClass=ControllableZonesModel, checkUnknown=False)
_squadTagRestrictionSchema = schemas.Schema[SquadTagRestrictionModel](fields={b'maxCount': (fields.Integer(required=True, deserializedValidators=validate.Range(minValue=1))), 
   b'levels': (fields.ListFromString(field=fields.Integer(deserializedValidators=validate.Range(minValue=MIN_VEHICLE_LEVEL, maxValue=MAX_VEHICLE_LEVEL)), required=True))}, modelClass=SquadTagRestrictionModel, checkUnknown=True)
_squadRestrictionsSchema = schemas.Schema[SquadRestrictionsModel](fields={b'tags': (fields.Dict(keyFieldOrSchema=fields.NonEmptyString(), valueFieldOrSchema=fields.Nested(schema=_squadTagRestrictionSchema), required=False))}, modelClass=SquadRestrictionsModel, checkUnknown=False)
_battleSchema = schemas.Schema[BattleModel](fields={b'controllableZones': (fields.Nested(schema=_controllableZonesSchema, required=False, filterParams=GameParamsScopeFlags.CELL_ARENA))}, modelClass=BattleModel, checkUnknown=False)
fortRushBattlesConfigGameParamsSchema = GameParamsSchema[FortRushBattlesConfigModel](gameParamsKey=EXT_GAME_PARAMS_KEY, fields={b'modeSelectorCardColumn': (fields.Integer(required=False, default=_DEFAULT_MODE_SELECTOR_COLUMN, deserializedValidators=validate.Range(minValue=0, maxValue=3))), 
   b'modeSelectorCardPriority': (fields.Integer(required=False, default=_DEFAULT_MODE_SELECTOR_PRIORITY)), 
   b'isEnabled': (fields.Boolean(required=True)), 
   b'technicalPause': (fields.Boolean(required=True)), 
   b'startDatetime': (fields.DateTime(required=True)), 
   b'endDatetime': (fields.DateTime(required=True)), 
   b'isInfoPageEnabled': (fields.Boolean(required=True)), 
   b'baseProgressionToken': (fields.String(required=True)), 
   b'completedProgressionToken': (fields.String(required=True)), 
   b'progressionQuestPrefix': (fields.NonEmptyString(required=True)), 
   b'maxRewardsAmountPerStage': (fields.Integer(required=True, deserializedValidators=validate.Range(minValue=1))), 
   b'progression': (fields.Nested(schema=_progressionSchema, required=True)), 
   b'dailyMissionsConfig': (fields.Nested(schema=_dailyMissionsConfigSchema, required=True)), 
   b'battleEconomy': (fields.Nested(schema=_battleEconomySchema, required=True)), 
   b'eligibleVehicleTiers': (fields.ListFromString(field=fields.Integer(deserializedValidators=validate.Range(minValue=MIN_VEHICLE_LEVEL, maxValue=MAX_VEHICLE_LEVEL)), required=True)), 
   b'forbiddenVehClasses': (fields.ListFromString(field=fields.String(deserializedValidators=validate.OneOf(_VEHICLE_CLASSES)), required=False, default=list)), 
   b'squadRestrictions': (fields.Nested(schema=_squadRestrictionsSchema, required=False, filterParams=GameParamsScopeFlags.CLIENT)), 
   b'battle': (fields.Nested(schema=_battleSchema, required=False, filterParams=GameParamsScopeFlags.CELL_ARENA))}, modelClass=FortRushBattlesConfigModel, checkUnknown=False, usedInReplay=True)

def getControllableZonesConfig(arena):
    config = fortRushBattlesConfigGameParamsSchema.getModel(arena=arena)
    if config is None or config.battle is None:
        return
    return config.battle.controllableZones
