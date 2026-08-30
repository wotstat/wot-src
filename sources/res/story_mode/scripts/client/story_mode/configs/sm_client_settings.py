import os, typing, ResMgr, section2dict
from dict2model import models, schemas, fields, validate, exceptions
from soft_exception import SoftException
from story_mode_common.story_mode_constants import EventMissionSelector, MissionsDifficulty, EXTENSION_NAME
_CLIENT_SETTINGS_PATH = os.path.join(EXTENSION_NAME, b'gui/sm_client_settings.xml')

class BattlesCountSelectorModel(models.Model):
    __slots__ = (b'normal', b'hard')

    def __init__(self, normal=0, hard=0):
        super(BattlesCountSelectorModel, self).__init__()
        self.normal = normal
        self.hard = hard
        return

    def getDifficulty(self, playerBattles):
        currentDifficulty, currentDifficultyBattles = MissionsDifficulty.UNDEFINED, -1
        for difficulty in MissionsDifficulty:
            difficultyBattles = getattr(self, difficulty, None)
            if difficultyBattles is not None and playerBattles >= difficultyBattles > currentDifficultyBattles:
                currentDifficultyBattles = difficultyBattles
                currentDifficulty = difficulty

        return currentDifficulty


battlesCountSelectorSchema = schemas.Schema[BattlesCountSelectorModel](fields={(MissionsDifficulty.NORMAL.value): (fields.Integer(required=False, deserializedValidators=validate.Range(minValue=0))), 
   (MissionsDifficulty.HARD.value): (fields.Integer(required=False, deserializedValidators=validate.Range(minValue=0)))}, modelClass=BattlesCountSelectorModel)

class MissionSelectorsModel(models.Model):
    __slots__ = (b'active', b'default', b'withUnlockMission', b'battlesCount')

    def __init__(self, active=EventMissionSelector.DEFAULT, default=None, withUnlockMission=None, battlesCount=None):
        super(MissionSelectorsModel, self).__init__()
        self.active = active
        self.default = default
        self.withUnlockMission = withUnlockMission
        self.battlesCount = battlesCount or BattlesCountSelectorModel()
        return


def _validateMissionSelectors(selectorsModel):
    if not hasattr(selectorsModel, selectorsModel.active.value):
        exceptions.ValidationError((b'Active mission selector "{}" is not defined.').format(selectorsModel.active))
    return


missionSelectorsSchema = schemas.Schema[MissionSelectorsModel](fields={b'active': (fields.StrEnum(enumClass=EventMissionSelector)), 
   (EventMissionSelector.DEFAULT.value): (fields.Field()), 
   (EventMissionSelector.WITH_UNLOCK_MISSION.value): (fields.Field()), 
   (EventMissionSelector.BATTLES_COUNT.value): (fields.Nested(schema=battlesCountSelectorSchema))}, modelClass=MissionSelectorsModel, deserializedValidators=[
 _validateMissionSelectors])

class EventModel(models.Model):
    __slots__ = (b'missionSelectors',)

    def __init__(self, missionSelectors=None):
        super(EventModel, self).__init__()
        self.missionSelectors = missionSelectors or MissionSelectorsModel()
        return


eventSchema = schemas.Schema[EventModel](fields={b'missionSelectors': (fields.Nested(schema=missionSelectorsSchema))}, modelClass=EventModel)

class ClientSettingsModel(models.Model):
    __slots__ = (b'event',)

    def __init__(self, event=None):
        super(ClientSettingsModel, self).__init__()
        self.event = event or EventModel()
        return


clientSettingsSchema = schemas.Schema[ClientSettingsModel](fields={b'event': (fields.Nested(schema=eventSchema))}, modelClass=ClientSettingsModel)
_g_clientSettings = None

def initialize():
    global _g_clientSettings
    root = ResMgr.openSection(_CLIENT_SETTINGS_PATH)
    rawData = section2dict.parse(root)
    _g_clientSettings = clientSettingsSchema.deserialize(rawData, silent=True) or ClientSettingsModel()
    return


def getClientSettings():
    if _g_clientSettings is None:
        raise SoftException(b'Story mode client settings must be initialized before use.')
    return _g_clientSettings
