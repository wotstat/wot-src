import ResMgr, section2dict, typing
from dict2model import models, schemas, fields, validate
from story_mode_common.configs.sounds_schema import SoundModel, SoundSchema
INTRO_VIDEO_SETTINGS_PATH = b'story_mode/gui/intro_video.xml'
OUTRO_VIDEO_SETTINGS_PATH = b'story_mode/gui/outro_video.xml'

class SoundEventsModel(SoundModel):
    __slots__ = (b'pause', b'resume')

    def __init__(self, start, pause, resume, stop, group, state):
        super(SoundEventsModel, self).__init__(start, stop, group, state)
        self.pause = pause
        self.resume = resume
        return


class SoundEventsSchema(SoundSchema[SoundEventsModel]):

    def __init__(self):
        super(SoundEventsSchema, self).__init__(fields={b'pause': (fields.String(required=True, default=b'')), 
           b'resume': (fields.String(required=True, default=b''))}, checkUnknown=True, modelClass=SoundEventsModel)
        return


soundEventsSchema = SoundEventsSchema()

class VideoModel(models.Model):
    __slots__ = (b'id', b'videoPath', b'music', b'playSoundOnClose', b'vo')

    def __init__(self, id, videoPath, music, playSoundOnClose, vo):
        super(VideoModel, self).__init__()
        self.id = id
        self.videoPath = videoPath
        self.music = music
        self.playSoundOnClose = playSoundOnClose
        self.vo = vo
        return


class VideoSettingsModel(models.Model):
    __slots__ = (b'missions',)

    def __init__(self, missions):
        super(VideoSettingsModel, self).__init__()
        self.missions = missions
        return


videoSchema = schemas.Schema(fields={b'id': (fields.Integer(required=True, deserializedValidators=validate.Range(minValue=1))), 
   b'videoPath': (fields.String(required=True)), 
   b'music': (fields.Nested(soundEventsSchema, required=True)), 
   b'playSoundOnClose': (fields.String(required=False)), 
   b'vo': (fields.String(required=True))}, modelClass=VideoModel, checkUnknown=True)
introVideoSchema = schemas.Schema(fields={b'missions': (fields.UniCapList(fieldOrSchema=videoSchema, required=True, deserializedValidators=validate.Length(minValue=1)))}, modelClass=VideoSettingsModel, checkUnknown=True)
__introVideoSchema = None
__outroVideoSchema = None

def getIntroVideoSettings():
    global __introVideoSchema
    if __introVideoSchema:
        return __introVideoSchema
    root = ResMgr.openSection(INTRO_VIDEO_SETTINGS_PATH)
    rawData = section2dict.parse(root)
    __introVideoSchema = introVideoSchema.deserialize(rawData)
    return __introVideoSchema


def getOutroVideoSettings():
    global __outroVideoSchema
    if __outroVideoSchema:
        return __outroVideoSchema
    root = ResMgr.openSection(OUTRO_VIDEO_SETTINGS_PATH)
    rawData = section2dict.parse(root)
    __outroVideoSchema = introVideoSchema.deserialize(rawData)
    return __outroVideoSchema
