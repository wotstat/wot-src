import ResMgr, section2dict, typing
from dict2model import models, schemas, fields, validate
_LORE_SETTINGS_PATH = b'story_mode/gui/lore.xml'

class MissionLoreModel(models.Model):
    __slots__ = (b'id', b'music', b'vo', b'battleMusic')

    def __init__(self, id, music, vo, battleMusic):
        super(MissionLoreModel, self).__init__()
        self.id = id
        self.music = music
        self.vo = vo
        self.battleMusic = battleMusic
        return


class EpilogueLoreModel(models.Model):
    __slots__ = (b'music', b'vo')

    def __init__(self, music, vo):
        super(EpilogueLoreModel, self).__init__()
        self.music = music
        self.vo = vo
        return


class LoreSettingsModel(models.Model):
    __slots__ = (b'mission', b'epilogue')

    def __init__(self, mission, epilogue):
        super(LoreSettingsModel, self).__init__()
        self.mission = mission
        self.epilogue = epilogue
        return


missionLoreSchema = schemas.Schema(fields={b'id': (fields.Integer(required=True, serializedValidators=validate.Range(minValue=1), deserializedValidators=validate.Range(minValue=1))), 
   b'music': (fields.String(required=True)), 
   b'vo': (fields.String(required=True)), 
   b'battleMusic': (fields.String(required=True))}, modelClass=MissionLoreModel, checkUnknown=True)
epilogueLoreSchema = schemas.Schema(fields={b'music': (fields.String(required=True)), 
   b'vo': (fields.String(required=True))}, modelClass=EpilogueLoreModel, checkUnknown=True)
loreSchema = schemas.Schema(fields={b'mission': (fields.UniCapList(fieldOrSchema=missionLoreSchema, required=True, deserializedValidators=validate.Length(minValue=1))), 
   b'epilogue': (fields.Nested(schema=epilogueLoreSchema, required=True, public=False))}, modelClass=LoreSettingsModel, checkUnknown=True)
__loreSchema = None

def getLoreSettings():
    global __loreSchema
    if __loreSchema:
        return __loreSchema
    root = ResMgr.openSection(_LORE_SETTINGS_PATH)
    rawData = section2dict.parse(root)
    __loreSchema = loreSchema.deserialize(rawData)
    return __loreSchema
